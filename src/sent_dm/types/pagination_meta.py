# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PaginationMeta", "Cursors"]


class Cursors(BaseModel):
    """Cursor-based pagination (optional)"""

    after: Optional[str] = None
    """Cursor to fetch the next page"""

    before: Optional[str] = None
    """Cursor to fetch the previous page"""


class PaginationMeta(BaseModel):
    """Pagination metadata for list responses"""

    cursors: Optional[Cursors] = None
    """Cursor-based pagination (optional)"""

    has_more: Optional[bool] = None
    """Whether there are more pages after this one"""

    page: Optional[int] = None
    """Current page number (1-indexed)"""

    page_size: Optional[int] = None
    """Number of items per page"""

    total_count: Optional[int] = None
    """Total number of items across all pages"""

    total_pages: Optional[int] = None
    """Total number of pages"""
