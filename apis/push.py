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
    return pushService.send_push(message)
