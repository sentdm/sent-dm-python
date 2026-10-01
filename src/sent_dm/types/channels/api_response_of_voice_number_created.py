# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..api_meta import APIMeta
from ..error_detail import ErrorDetail
from .voice_number_created import VoiceNumberCreated

__all__ = ["APIResponseOfVoiceNumberCreated"]


class APIResponseOfVoiceNumberCreated(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[VoiceNumberCreated] = None
    """The response data (null if error)"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
