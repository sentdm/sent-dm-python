# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .call import Call
from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["CallsList"]


class CallsList(BaseModel):
    """Paginated list of calls"""

    calls: Optional[List[Call]] = None
    """The calls on this page, most recent first"""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""
