# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .sender_profile import SenderProfile
from .pagination_meta import PaginationMeta

__all__ = ["SenderProfilesList"]


class SenderProfilesList(BaseModel):
    """A paginated list of sender profiles."""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""

    sender_profiles: Optional[List[SenderProfile]] = None
    """The sender_profiles on this page."""
