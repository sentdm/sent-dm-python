# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .api_error import APIError
from .profile_detail import ProfileDetail

__all__ = ["ProfileListResponse", "Data"]


class Data(BaseModel):
    """List of profiles response"""

    profiles: Optional[List[ProfileDetail]] = None
    """List of profiles in the organization"""


class ProfileListResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """List of profiles response"""

    error: Optional[APIError] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
