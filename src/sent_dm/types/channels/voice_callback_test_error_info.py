# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["VoiceCallbackTestErrorInfo"]


class VoiceCallbackTestErrorInfo(BaseModel):
    """Why the test did not end with ok"""

    message: Optional[str] = None
    """What to fix"""

    path: Optional[str] = None
    """
    Dotted path of the answer field at fault, such as action.action, when one field
    is to blame
    """

    reason: Optional[str] = None
    """
    Machine-readable reason, such as timeout, http_error, malformed_json,
    missing_action or unknown_action
    """
