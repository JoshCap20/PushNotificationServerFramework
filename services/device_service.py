from entities import DeviceEntity
from models import Device
from sqlalchemy import select
from database import db_session
from sqlalchemy.orm import Session
from fastapi import Depends

""" 
Instance Methods:
    register_device(Device) -> Device
    get_registered_devices() -> list[Device]
    clear_registered_devices() -> None
"""


class DeviceService:
    def __init__(self, session: Session = Depends(db_session)):
        """Initialize the Service."""
        self._session = session

    def register_device(self, device: Device) -> Device:
        """Register a device."""
        device_entity = DeviceEntity.from_model(device)
        self._session.add(device_entity)
        self._session.commit()
        return device_entity.to_model()

    def get_registered_devices(self) -> list[Device]:
        """Get all registered devices."""
        devices = self._session.execute(select(DeviceEntity)).scalars().all()
        return [device.to_model() for device in devices]

    def clear_registered_devices(self) -> None:
        """Clear all registered devices."""
        self._session.execute(select(DeviceEntity)).delete()
        self._session.commit()
