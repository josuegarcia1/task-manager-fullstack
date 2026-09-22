from fastapi import APIRouter


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.get("/")
async def get_tasks():
    return []

@router.get("/{task_id}")
async def get_task(task_id: int):
    return {
        "task_id": task_id,
        "title": "Temporary Task",
    }