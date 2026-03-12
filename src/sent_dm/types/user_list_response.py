# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .api_error import APIError
from .user_response import UserResponse

__all__ = ["UserListResponse", "Data"]


class Data(BaseModel):
    """List of users response"""

    users: Optional[List[UserResponse]] = None
    """List of users in the organization"""


class UserListResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """List of users response"""

    error: Optional[APIError] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
