from fastapi import APIRouter, Depends
from models import Device
from services import DeviceService

router = APIRouter(
    prefix="/devices",
    tags=["devices"],
    responses={404: {"description": "Not found"}},
)


@router.post("/register", response_model=Device)
def register_device(
    device: Device, deviceService: DeviceService = Depends()
):
    return deviceService.register_device(device)


@router.get("/all", response_model=list[Device])
def get_registered_devices(
    deviceService: DeviceService = Depends(),
):
    return deviceService.get_registered_devices()


# FOR TESTING PURPOSES ONLY
@router.get("/clear", response_model=None)
def clear_registered_devices(
    deviceService: DeviceService = Depends(),
):
    return deviceService.clear_registered_devices()
