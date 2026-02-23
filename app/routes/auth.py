from fastapi import APIRouter
from app.models import User

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.get("/mock-user")
def get_current_user():
    return User(id=1, username="mock_user", email="mock@example.com")
