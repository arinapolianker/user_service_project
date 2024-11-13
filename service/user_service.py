from typing import Optional, List

from fastapi import HTTPException

from model.user import User
from repository import user_repository


async def get_user_by_id(user_id: int) -> Optional[User]:
    return await user_repository.get_user_by_id(user_id)


async def get_all_users() -> List[User]:
    return await user_repository.get_all_users()


async def create_user(user: User) -> int:
    return await user_repository.create_user(user)


async def update_user_by_id(user_id: int, user: User):
    return await user_repository.update_user_by_id(user_id, user)


async def register_user_by_id(user_id: int):
    user_exists = await user_repository.get_user_by_id(user_id)
    if not user_exists.registered:
        return await user_repository.register_user_by_id(user_id, True)
    else:
        raise HTTPException(status_code=404, detail=f"User with id:{user_id} is already registered")


async def delete_user_by_id(user_id):
    await user_repository.delete_user_by_id(user_id)

