from fastapi import Depends
from models import Message
from push import PushHandler


class PushService:
    """
    A service for sending push notifications.

    Attributes:
        handler (PushHandler): The handler used to send push notifications. Injected by FastAPI.
    """

    def __init__(self, handler: PushHandler = Depends()):
        """Initialize the Service."""
        self.handler = handler

    def send_push(self, message: Message) -> None:
        """Send a push notification."""
        self.handler.send_multiple_push(
            to_device_tokens=message.recipients, body=message.body
        )
