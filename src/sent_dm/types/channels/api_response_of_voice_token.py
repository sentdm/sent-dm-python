# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..api_meta import APIMeta
from .voice_token import VoiceToken
from ..error_detail import ErrorDetail

__all__ = ["APIResponseOfVoiceToken"]


class APIResponseOfVoiceToken(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[VoiceToken] = None
    """A short-lived token your app passes to the voice client SDK to register"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
