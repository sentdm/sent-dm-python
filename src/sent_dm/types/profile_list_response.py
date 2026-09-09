# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail
from .profile_detail import ProfileDetail
from .pagination_meta import PaginationMeta

__all__ = ["ProfileListResponse", "Data"]


class Data(BaseModel):
    """The profiles in the organization."""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""

    profiles: Optional[List[ProfileDetail]] = None
    """The profiles on this page."""


class ProfileListResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The profiles in the organization."""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
