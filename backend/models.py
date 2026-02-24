from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

    tasks = relationship("Task", back_populates="goal")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    goal_id = Column(Integer, ForeignKey("goals.id"))
    title = Column(String)
    status = Column(String, default="pending")
    time_spent = Column(Integer, default=0)
    problems = Column(Text, nullable=True)
    insights = Column(Text, nullable=True)

    # Add relationship to children
    subtasks = relationship(
        "SubTask", back_populates="task", cascade="all, delete-orphan"
    )
    # --- MISSING LINE BELOW ---
    # You must add this so Goal can find 'goal' here:
    goal = relationship("Goal", back_populates="tasks")


class SubTask(Base):
    __tablename__ = "subtasks"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    title = Column(String)
    is_completed = Column(Boolean, default=False)  # Simple boolean is enough here

    task = relationship("Task", back_populates="subtasks")
