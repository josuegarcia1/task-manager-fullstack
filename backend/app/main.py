from fastapi import FastAPI
from app.api.routes.tasks import router as tasks_router

app = FastAPI(
    title= "Task Manager API",
)
app.include_router(tasks_router)

@app.get("/")
async def root():
    return {"message": "Task Manager API"}