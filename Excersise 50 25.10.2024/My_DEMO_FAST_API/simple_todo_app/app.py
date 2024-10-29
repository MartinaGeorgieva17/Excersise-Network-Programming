from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from db import SessionLocal, engine
from simple_todo_app.db import get_tasks, add_task, delete_task
from simple_todo_app.models import Task, TaskCreate



app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return {"message": "Hello, FastApi!"}

@app.get("/", response_class=HTMLResponse)
async def read_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/tasks")
async def read_tasks():
    return get_tasks()


@ app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    new_task = add_task(task.dict())
    if not new_task:
        raise HTTPException(status_code=400, detail="Could not add task.")
    return new_task

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    success = delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found.")
    return {"message": "Task deleted successfully"}