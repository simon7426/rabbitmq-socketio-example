from fastapi import APIRouter

from project.utils import publish_message

router = APIRouter()


@router.get("/publish/{user}")
async def publish(user: str):
    body: dict = {"user": int(user)}
    print(body)
    await publish_message(body)
    return {"message": "published to queue"}
