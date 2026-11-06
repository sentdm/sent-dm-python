# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .profile_detail import ProfileDetail
from .pagination_meta import PaginationMeta

__all__ = ["ProfilesList"]


class ProfilesList(BaseModel):
    """The profiles in the organization."""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""

    profiles: Optional[List[ProfileDetail]] = None
    """The profiles on this page."""
