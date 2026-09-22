from fastapi import APIRouter, status
from app.schemas.auth import LoginRequest, LoginResponse

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post(
    "/login",
    response_model=LoginResponse,
    status_code=status.HTTP_200_OK,
)
async def login(data: LoginRequest):
    return LoginResponse(
        message=f"Login received for {data.email}"
    )