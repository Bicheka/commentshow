from fastapi import APIRouter
from src.user.model import User
from . import service
router = APIRouter()


# Create a new user
@router.post("/user/register")
async def register_user(user: User, status_code=201):
    await service.create_user(user)
    return {
            "registered"
        }