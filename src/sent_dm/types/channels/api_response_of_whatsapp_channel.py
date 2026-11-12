# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..api_meta import APIMeta
from ..error_detail import ErrorDetail
from .whatsapp_channel import WhatsappChannel

__all__ = ["APIResponseOfWhatsappChannel"]


class APIResponseOfWhatsappChannel(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[WhatsappChannel] = None
    """The profile's WhatsApp account. Its status is Meta's verification state."""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
