from .apn_handler import APNsClient, Payload
from .config import PushConfig


class PushHandler:
    def __init__(self):
        self.token_credentials = PushConfig.get_token_credentials()
        self.connection = APNsClient(
            credentials=self.token_credentials, use_sandbox=False
        )

    def send_push(
        self, to_device_token: str, body: str, sound: str = "default", badge: int = 1
    ) -> None:
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
        [
            self.send_push(
                to_device_token=to_device_token, body=body, sound=sound, badge=badge
            )
            for to_device_token in to_device_tokens
        ]
