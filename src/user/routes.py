from fastapi import APIRouter, Response
from src.user.model import User
from . import service
router = APIRouter()


# Create a new user
@router.post("/user/register", status_code=201)
async def register_user(user: User, ):
    await service.create_user(user)
    return {
            "registered"
        }