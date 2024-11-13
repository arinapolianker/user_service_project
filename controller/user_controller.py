from typing import List

from fastapi import APIRouter, HTTPException

from model.user import User
from service import user_service

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


@router.get("/{user_id}", response_model=User)
async def get_user_by_id(user_id: int):
    user = await user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id:{user_id} not found...")
    else:
        return user


@router.get("/", response_model=List[User])
async def get_all_users():
    return await user_service.get_all_users()


@router.post("/", response_model=User)
async def create_user(user: User):
    user_id = await user_service.create_user(user)
    return await user_service.get_user_by_id(user_id)


@router.put("/{user_id}", response_model=User)
async def update_user_by_id(user_id: int, user: User):
    user_exists = await user_service.get_user_by_id(user_id)
    if not user_exists:
        raise HTTPException(status_code=404, detail=f"Can't update user with id:{user_id}, user not found...")
    await user_service.update_user_by_id(user_id, user)
    return await user_service.get_user_by_id(user_id)


@router.put("/register/{user_id}", response_model=User)
async def register_user_by_id(user_id: int):
    user_exists = await user_service.get_user_by_id(user_id)
    if not user_exists:
        raise HTTPException(status_code=404, detail=f"Can't register user with id:{user_id}, user not found...")
    await user_service.register_user_by_id(user_id)
    return await user_service.get_user_by_id(user_id)


@router.delete("/{user_id}")
async def delete_user_by_id(user_id: int):
    user_exists = await user_service.get_user_by_id(user_id)
    if not user_exists:
        raise HTTPException(status_code=404, detail=f"Can't delete user with id:{user_id}, user not found...")
    await user_service.delete_user_by_id(user_id)


