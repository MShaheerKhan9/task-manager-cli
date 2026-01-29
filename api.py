from typing import List
from fastapi import HTTPException
from core import TaskNotFoundError, TaskDoneAlreadyError, TaskAlreadyExists
from fastapi import FastAPI
from pydantic import BaseModel
from services.task_services import TaskServices
from core import TaskManager

app = FastAPI()

task_manager = TaskManager()
task_manager.run()
task_service = TaskServices(task_manager)


#using pydantic
class TaskCreate(BaseModel):
    name: str

class TaskResponse(BaseModel):
    name: str
    id: int
    status: bool

class TaskListResponse(BaseModel):
    tasks: List[TaskResponse]

class TaskCreated(BaseModel):
    message:str
    task:TaskResponse

class TaskUpdated(BaseModel):
    message:str
    task:TaskResponse

class TaskDeleted(BaseModel):
    message: str
    name : str

class Progress(BaseModel):
    completed: int
    total: int
    percent: float

@app.get("/")
def root():
    return {"message": "API is running!"}


@app.get("/tasks", response_model=TaskListResponse)
def list_tasks():
    return {
        "tasks": task_service.list_tasks()
    }

@app.post("/tasks", response_model=TaskCreated, status_code=201)
def add_task(task: TaskCreate):
    try:
        task = task_service.add_task(task.name)
        return {
            "message" : "Task added successfully!",
            "task" : {
                "id" : task["id"],
                "name" : task["name"],
                "status" : False
            }
        }
    except TaskAlreadyExists:
        raise HTTPException(status_code=400, detail="Task already exists!")

@app.delete("/tasks/{id}", response_model = TaskDeleted,status_code=200)
def delete_task(id: int):

    try:
        task = task_service.remove_task(id)
        return{
            "message" : "Task removed successfully!",
            "name" : task["name"]
        }
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{id}/done", response_model = TaskUpdated,status_code=200)
def mark_task_done(id: int):
    try:
        task = task_service.mark_done(id)
        return{
            "message" : "Task marked successfully!",
            "task" : {
                "id" : id,
                "name" : task["name"],
                "status" : True
            }
        }
    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")
    except TaskDoneAlreadyError:
        raise HTTPException(status_code=400, detail="Task already done")

@app.get("/tasks/{id}", response_model=TaskResponse)
def get_task(id: int):
    try:
        task = task_service.get_task(id)
        return{

                "id" : id,
                "name" : task["name"],
                "status": task["status"]
        }

    except TaskNotFoundError:
        raise HTTPException(status_code=404, detail="Task not found")


@app.get("/progress", response_model = Progress)
def get_progress():
    return task_service.get_progress()


