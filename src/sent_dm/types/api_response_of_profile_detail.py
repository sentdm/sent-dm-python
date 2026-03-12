# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail
from .profile_detail import ProfileDetail

__all__ = ["APIResponseOfProfileDetail"]


class APIResponseOfProfileDetail(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[ProfileDetail] = None
    """Detailed profile response for v3 API"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
