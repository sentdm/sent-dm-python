# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .message_activity import MessageActivity

__all__ = ["MessageActivities"]


class MessageActivities(BaseModel):
    """Response for GET /messages/{id}/activities"""

    activities: Optional[List[MessageActivity]] = None
    """List of activity events ordered by most recent first"""

    message_id: Optional[str] = None
    """The message ID these activities belong to"""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""
