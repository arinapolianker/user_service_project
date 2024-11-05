from typing import Optional

from model.user import User
from repository import user_repository


async def get_user_by_id(user_id: int) -> Optional[User]:
    return await user_repository.get_user_by_id(user_id)


async def create_user(user: User) -> int:
    return await user_repository.create_user(user)


async def update_user(user_id: int, user: User):
    return await user_repository.update_user(user_id, user)


async def delete_user(user_id):
    await user_repository.delete_user(user_id)

