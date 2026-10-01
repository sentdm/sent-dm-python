# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .call import Call
from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail

__all__ = ["APIResponseOfCall"]


class APIResponseOfCall(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Call] = None
    """A call record"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
