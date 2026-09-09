# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail
from .contact_response import ContactResponse

__all__ = ["APIResponseOfContact"]


class APIResponseOfContact(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[ContactResponse] = None
    """Contact response for v3 API Uses snake_case for JSON property names"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
