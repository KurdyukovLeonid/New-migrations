from fastapi import FastAPI
from app.routers.task import router as task_router
from app.routers.user import router as user_router
from app.backend.db import engine, Base
from app.models.task import Task
from app.models.user import User

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)