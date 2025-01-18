from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Task(BaseModel):
    id: int
    text: str
    complete: bool

tasks = []

@app.post("/tasks")
async def create_task(task: Task):
    tasks.append({
        "id": len(tasks) + 1,
        "text": task.text,
        "complete": task.complete,
    })
    return {"Задача успешно выполнена": True}

@app.get