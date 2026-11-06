# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .user_response import UserResponse
from .pagination_meta import PaginationMeta

__all__ = ["UsersList"]


class UsersList(BaseModel):
    """The users in the organization."""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""

    users: Optional[List[UserResponse]] = None
    """The users on this page."""
