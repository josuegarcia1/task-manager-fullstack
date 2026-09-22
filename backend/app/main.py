from fastapi import FastAPI
from app.api.routes.tasks import router as tasks_router
from app.api.routes.auth import router as auth_router

app = FastAPI(
    title= "Task Manager API",
)
app.include_router(tasks_router)
app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "Task Manager API"}