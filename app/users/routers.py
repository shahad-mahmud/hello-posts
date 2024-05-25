from fastapi import APIRouter, status

from app.users.schemas import (
    AllUserDetailsResponse,
    CreateUserRequest,
    UserDetailsResponse,
)
from app.users.services import create_user_service, get_user_details_service

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=AllUserDetailsResponse)
def get_users():
    data = get_user_details_service()
    if not data:
        return {"message": "no users found", "data": []}

    return {"message": "got all users", "data": data}


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=UserDetailsResponse)
def get_user(id: int):
    data = get_user_details_service(id)

    if not data:
        return {"message": f"no user found with id {id}", "data": None}

    return {"message": "got user", "data": data}


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUserRequest):
    create_user_service(user)
    return {"message": "user created"}
