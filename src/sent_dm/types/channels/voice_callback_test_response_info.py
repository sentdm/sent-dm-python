# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["VoiceCallbackTestResponseInfo"]


class VoiceCallbackTestResponseInfo(BaseModel):
    """What your endpoint answered"""

    body: Optional[str] = None
    """The start of the raw response body, capped at 2048 characters"""

    status_code: Optional[int] = None
    """The HTTP status your endpoint returned"""
