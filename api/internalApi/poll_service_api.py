import httpx

from repository.database import config


async def delete_answers_by_user_id(user_id: int) -> bool:
    url = f"{config.POLL_SERVICE_BASE_URL}/answer/user_id/{user_id}"
    async with httpx.AsyncClient(follow_redirects=True) as client:
        try:
            response = await client.delete(url)
            response.raise_for_status()
            return True
        except httpx.HTTPStatusError as exception:
            print(f"Error in deleting answers for user_id {user_id}. error: {exception.response}")
            return False
