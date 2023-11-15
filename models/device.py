from pydantic import BaseModel
from datetime import datetime


class Device(BaseModel):
    id: int | None = None
    token: str
    name: str
    systemName: str
    systemVersion: str
    model: str
    localizedModel: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
