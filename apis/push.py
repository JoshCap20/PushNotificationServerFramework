from fastapi import APIRouter, Depends
from models import Message
from services import PushService

router = APIRouter(
    prefix="/push",
    tags=["push"],
    responses={404: {"description": "Not found"}},
)


@router.post("/send")
def send_push(message: Message, pushService: PushService = Depends()):
    """
    Sends a push notification using the specified push service.

    Args:
        message (Message): The message to send.
        pushService (PushService): The push service to use. Injected by FastAPI.

    Returns:
        The result of sending the push notification.
    """
    return pushService.send_push(message)
