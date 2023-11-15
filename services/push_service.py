from fastapi import Depends
from models import Message
from push import PushHandler


class PushService:
    """
    A service for sending push notifications.

    Attributes:
        handler (PushHandler): The handler used to send push notifications. Injected by FastAPI.

    Methods:
        send_push(message: Message) -> None: Sends a push notification.
    """

    def __init__(self, handler: PushHandler = Depends()):
        """
        Initialize the PushService.

        Args:
            handler (PushHandler): The push notification handler to use. Injected by FastAPI.
        """
        self.handler = handler

    def send_push(self, message: Message) -> None:
        """
        Send a push notification.

        Args:
            message (Message): The message to send.

        Returns:
            None
        """
        self.handler.send_multiple_push(
            to_device_tokens=message.recipients, body=message.body
        )
