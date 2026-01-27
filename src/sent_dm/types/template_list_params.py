# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TemplateListParams"]


class TemplateListParams(TypedDict, total=False):
    page: Required[int]
    """The page number (zero-indexed). Default is 0."""

    page_size: Required[Annotated[int, PropertyInfo(alias="pageSize")]]
    """The number of items per page (1-1000). Default is 100."""

    category: Optional[str]
    """Optional filter by template category (e.g., MARKETING, UTILITY, AUTHENTICATION)"""

    search: Optional[str]
    """Optional search term to filter templates by name or content"""

    status: Optional[str]
    """Optional filter by template status (e.g., APPROVED, PENDING, REJECTED, DRAFT)"""
