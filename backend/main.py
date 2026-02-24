from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas
from llm_service import generate_tasks, generate_subtasks_llm

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Execution Planner API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ... imports ...


@app.post("/tasks/{task_id}/generate_subtasks")
def generate_subtasks_route(task_id: int, db: Session = Depends(get_db)):
    # 1. Get the parent task
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    # 2. Generate steps using LLM
    # (Make sure to import generate_subtasks_llm from llm_service)
    subtasks_data = generate_subtasks_llm(task.title)

    # 3. Save to DB
    for st_data in subtasks_data:
        db_subtask = models.SubTask(task_id=task.id, title=st_data["title"])
        db.add(db_subtask)

    db.commit()
    return {"message": "Subtasks generated"}


@app.put("/subtasks/{subtask_id}")
def toggle_subtask(subtask_id: int, is_completed: bool, db: Session = Depends(get_db)):
    sub = db.query(models.SubTask).filter(models.SubTask.id == subtask_id).first()
    sub.is_completed = is_completed
    db.commit()
    return {"status": "updated"}


@app.post("/goals", response_model=schemas.GoalResponse)
def create_goal(goal: schemas.GoalCreate, db: Session = Depends(get_db)):
    db_goal = models.Goal(title=goal.title)
    db.add(db_goal)
    db.commit()
    db.refresh(db_goal)

    # PASS THE SELECTED MODEL HERE
    tasks = generate_tasks(goal.title, model_name=goal.model_name)

    for task in tasks:
        db_task = models.Task(goal_id=db_goal.id, title=task["title"])
        db.add(db_task)

    db.commit()
    db.refresh(db_goal)
    return db_goal


@app.get("/goals", response_model=list[schemas.GoalResponse])
def get_goals(db: Session = Depends(get_db)):
    return db.query(models.Goal).all()


@app.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    time_spent: int,
    problems: str = "",
    insights: str = "",
    db: Session = Depends(get_db),
):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    task.status = "completed"
    task.time_spent = time_spent
    task.problems = problems
    task.insights = insights
    db.commit()
    return {"message": "Task updated"}


@app.delete("/goals/{goal_id}")
def delete_goal(goal_id: int, db: Session = Depends(get_db)):
    # 1. Find the goal
    goal = db.query(models.Goal).filter(models.Goal.id == goal_id).first()

    if not goal:
        raise HTTPException(status_code=404, detail="Goal not found")

    # 2. Delete associated tasks manually (to prevent foreign key errors)
    db.query(models.Task).filter(models.Task.goal_id == goal_id).delete()

    # 3. Delete the goal
    db.delete(goal)
    db.commit()

    return {"message": "Goal and tasks deleted"}
