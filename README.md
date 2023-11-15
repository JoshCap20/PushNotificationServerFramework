# PushNotificationServerFramework

## Introduction
`PushNotificationServerFramework` is an open-source project designed to offer a template for creating remote push notification servers. It simplifies the process of registering devices with the server and provides services for storing, fetching, and clearing device information.

### Features
- **Device Endpoints**: Facilitates registering and fetching devices with the server.
- **Push Endpoints**: Provides endpoints for sending push notifications to devices.
- **Data Persistence**: Utilizes SQLAlchemy ORM for managing database operations.
- **Pydantic Models**: Ensures validation and serialization of device and message entities.
- **Modified APNS2**: Includes a modified version of the Python `apns2` package, updated for Python 3.11 compatibility.
- **FastAPI Framework**: Leverages the FastAPI framework for efficient and easy server development.

## Prerequisites
Before installing `PushNotificationServerFramework`, ensure you have the following:
- Python 3.11
- Pip package manager

## Installation
To install `PushNotificationServerFramework`, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/JoshCap20/PushNotificationServerFramework.git
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
Configure the application by editing `config.py`. Set the necessary parameters like database URI, server host, and port.

## Running the Server
To start the server, run the following command:
```bash
python main.py
```

# Endpoints
## Devices API
Use the provided endpoints to register devices with the server.

#### Register a Device
- **Endpoint**: `/devices/register`
- **Method**: `POST`
- **Body**:
  ```json
  {
    "token": "unique_device_id",
    "other_info": "additional_information"
  }
  ```

#### Retrieve Devices Information
- **Endpoint**: `/devices/all`
- **Method**: `GET`

#### Clear Devices Information
- **Endpoint**: `/devices/clear`
- **Method**: `GET`

## Push API


## Contributing
Contributions to `PushNotificationServerFramework` are welcome. Please follow the standard GitHub pull request process to propose changes.

## License
This project is licensed under the [MIT License](LICENSE.md).

## Acknowledgements
- Pydantic for data validation and serialization.
- SQLAlchemy ORM for database management.
- FastAPI for the server framework.
- Modified Python `apns2` package for handling Apple Push Notification services.
