from .apn_handler import TokenCredentials
from utils import getenv


class PushConfig:
    """
    A class representing the configuration for push notifications.
    """
    AUTH_KEY_PATH: str | None = None
    AUTH_KEY_ID: str | None = None
    TEAM_ID: str | None = None
    APNS_APP_BUNDLE_ID: str | None = None

    @classmethod
    def get_auth_key_path(cls) -> str:
        """
        Returns the path to the authentication key for APNS.
        """
        if not cls.AUTH_KEY_PATH:
            cls.AUTH_KEY_PATH = getenv("APNS_AUTH_KEY_PATH")
        return cls.AUTH_KEY_PATH

    @classmethod
    def get_auth_key_id(cls) -> str:
        """
        Returns the ID of the authentication key for APNS.
        """
        if not cls.AUTH_KEY_ID:
            cls.AUTH_KEY_ID = getenv("APNS_KEY_ID")
        return cls.AUTH_KEY_ID

    @classmethod
    def get_team_id(cls) -> str:
        """
        Returns the team ID for APNS.
        """
        if not cls.TEAM_ID:
            cls.TEAM_ID = getenv("APNS_TEAM_ID")
        return cls.TEAM_ID

    @classmethod
    def get_apns_app_bundle_id(cls) -> str:
        """
        Returns the bundle ID for the APNS app.
        """
        if not cls.APNS_APP_BUNDLE_ID:
            cls.APNS_APP_BUNDLE_ID = getenv("APNS_APP_BUNDLE_ID")
        return cls.APNS_APP_BUNDLE_ID

    @classmethod
    def get_token_credentials(cls) -> TokenCredentials:
        """
        Returns the token credentials for APNS.
        """
        return TokenCredentials(
            auth_key_path=cls.get_auth_key_path(),
            auth_key_id=cls.get_auth_key_id(),
            team_id=cls.get_team_id(),
        )
