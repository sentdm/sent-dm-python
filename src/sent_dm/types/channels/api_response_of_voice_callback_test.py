# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..api_meta import APIMeta
from ..error_detail import ErrorDetail
from .voice_callback_test import VoiceCallbackTest

__all__ = ["APIResponseOfVoiceCallbackTest"]


class APIResponseOfVoiceCallbackTest(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[VoiceCallbackTest] = None
    """The verdict of a test question sent to your callback URL"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
