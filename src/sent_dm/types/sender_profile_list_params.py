# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SenderProfileListParams"]


class SenderProfileListParams(TypedDict, total=False):
    page: int
    """Page number, 1-indexed."""

    page_size: int
    """Profiles per page. Between 1 and 100."""
