from pydantic import BaseModel
from datetime import datetime


class Device(BaseModel):
    """
    Represents a device that can receive push notifications.

    Attributes:
        id (int | None): The unique identifier for the device.
        token (str): The device token used for push notifications.
        name (str): The name of the device.
        systemName (str): The name of the operating system running on the device.
        systemVersion (str): The version of the operating system running on the device.
        model (str): The model of the device.
        localizedModel (str): The localized model of the device.
        created_at (datetime | None): The date and time the device was created.
        updated_at (datetime | None): The date and time the device was last updated.
    """

    id: int | None = None
    token: str
    name: str
    systemName: str
    systemVersion: str
    model: str
    localizedModel: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
