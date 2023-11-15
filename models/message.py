from pydantic import BaseModel


class Message(BaseModel):
    """
    Represents a message to be sent to one or more recipients.

    Attributes:
        recipients (list[str]): List of recipient tokens.
        body (str): Message to send.
    """

    recipients: list[str]
    body: str
