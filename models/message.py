from pydantic import BaseModel

class Message(BaseModel):
    recipients: list[str] # List of recipient tokens
    message: str # Message to send