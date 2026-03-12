# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .api_error import APIError
from .user_response import UserResponse

__all__ = ["APIResponseOfUser"]


class APIResponseOfUser(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[UserResponse] = None
    """User response for v3 API"""

    error: Optional[APIError] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
