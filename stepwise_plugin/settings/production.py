"""
Common Pluggable Django App settings
"""


def plugin_settings(settings):
    """
    Injects local settings into django settings
    """

    # MemberPress REST API client
    # -------------------------------------------------------------------------
    settings.MEMBERPRESS_API_KEY = "set-me-please"  # noqa: F841
    settings.MEMBERPRESS_API_BASE_URL = "https://stepwisemath.ai"  # noqa: F841
    settings.MEMBERPRESS_CACHE_EXPIRATION = 60 * 60 * 24  # noqa: F841
    settings.MEMBERPRESS_API_KEY_NAME = "MEMBERPRESS-API-KEY"  # noqa: F841
    settings.MEMBERPRESS_SENSITIVE_KEYS = [
        "password",
        "token",
        "client_id",
        "client_secret",
        "Authorization",
        "secret",
    ]  # noqa: F841
