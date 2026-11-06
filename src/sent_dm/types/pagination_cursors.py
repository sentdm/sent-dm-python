# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PaginationCursors"]


class PaginationCursors(BaseModel):
    """Cursor-based pagination. Never populated — see Cursors."""

    after: Optional[str] = None
    """Cursor to fetch the next page."""

    before: Optional[str] = None
    """Cursor to fetch the previous page."""
