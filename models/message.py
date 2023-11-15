from pydantic import BaseModel

class Message(BaseModel):
    recipients: list[str] # List of recipient tokens
    body: str # Message to send