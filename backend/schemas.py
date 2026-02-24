from pydantic import BaseModel
from typing import List, Optional


class GoalCreate(BaseModel):
    title: str
    # Add this optional field
    model_name: Optional[str] = "gemma-3-12b-it"


class SubTaskResponse(BaseModel):
    id: int
    title: str
    is_completed: bool

    class Config:
        orm_mode = True


class TaskResponse(BaseModel):
    id: int
    title: str
    status: str
    time_spent: int
    # Add subtasks list here
    subtasks: List[SubTaskResponse] = []

    class Config:
        orm_mode = True


class GoalResponse(BaseModel):
    id: int
    title: str
    tasks: List[TaskResponse]

    class Config:
        orm_mode = True
