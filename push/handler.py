from .apn_handler import APNsClient, Payload, TokenCredentials
from .config import PushConfig


class PushHandler:
    """
    A wrapper class for sending push notifications using the Apple Push Notification service (APNs).

    Attributes:
        token_credentials (TokenCredentials): A dictionary containing the token credentials required to connect to APNs.
        connection (APNsClient): An instance of the APNsClient class used to establish a connection to APNs.

    Methods:
        send_push(to_device_token: str, body: str, sound: str = "default", badge: int = 1) -> None:
            Sends a push notification to a single device token.
        send_multiple_push(to_device_tokens: list[str], body: str, sound: str = "default", badge: int = 1) -> None:
            Sends a push notification to multiple device tokens.
    """

    def __init__(self):
        self.token_credentials: TokenCredentials = PushConfig.get_token_credentials()
        self.connection: APNsClient = APNsClient(
            credentials=self.token_credentials, use_sandbox=False
        )

    def send_push(
        self, to_device_token: str, body: str, sound: str = "default", badge: int = 1
    ) -> None:
        """
        Sends a push notification to a single device token.

        Args:
            to_device_token (str): The device token of the device to send the push notification to.
            body (str): The message body of the push notification.
            sound (str, optional): The name of the sound to play when the push notification is received. Defaults to "default".
            badge (int, optional): The number to display as the badge of the app icon. Defaults to 1.
        """
        payload: Payload = Payload(alert=body, sound=sound, badge=badge)
        self.connection.send_notification(
            to_device_token, payload, topic=PushConfig.get_apns_app_bundle_id()
        )

    def send_multiple_push(
        self,
        to_device_tokens: list[str],
        body: str,
        sound: str = "default",
        badge: int = 1,
    ) -> None:
        """
        Sends a push notification to multiple device tokens.

        Args:
            to_device_tokens (list[str]): A list of device tokens to send the push notification to.
            body (str): The message body of the push notification.
            sound (str, optional): The name of the sound to play when the push notification is received. Defaults to "default".
            badge (int, optional): The number to display as the badge of the app icon. Defaults to 1.
        """
        [
            self.send_push(
                to_device_token=to_device_token, body=body, sound=sound, badge=badge
            )
            for to_device_token in to_device_tokens
        ]
