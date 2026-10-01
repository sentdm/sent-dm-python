# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..api_meta import APIMeta
from .voice_secret import VoiceSecret
from ..error_detail import ErrorDetail

__all__ = ["APIResponseOfVoiceSecret"]


class APIResponseOfVoiceSecret(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[VoiceSecret] = None
    """A freshly rotated callback signing secret"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
