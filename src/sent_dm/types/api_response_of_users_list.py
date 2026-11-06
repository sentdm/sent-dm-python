# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .users_list import UsersList
from .error_detail import ErrorDetail

__all__ = ["APIResponseOfUsersList"]


class APIResponseOfUsersList(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[UsersList] = None
    """The users in the organization."""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
