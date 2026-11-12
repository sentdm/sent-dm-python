# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .message import Message
from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["ConversationMessagesList"]


class ConversationMessagesList(BaseModel):
    """A paginated list of messages — used by both conversation read endpoints."""

    messages: Optional[List[Message]] = None
    """The messages on this page."""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""
