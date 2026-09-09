# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail
from .user_response import UserResponse
from .pagination_meta import PaginationMeta

__all__ = ["UserListResponse", "Data"]


class Data(BaseModel):
    """The users in the organization."""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""

    users: Optional[List[UserResponse]] = None
    """The users on this page."""


class UserListResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The users in the organization."""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
