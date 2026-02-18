# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TemplateListParams"]


class TemplateListParams(TypedDict, total=False):
    page: Required[int]
    """Page number (1-indexed)"""

    page_size: Required[Annotated[int, PropertyInfo(alias="pageSize")]]

    category: Optional[str]
    """Optional category filter: MARKETING, UTILITY, AUTHENTICATION"""

    search: Optional[str]
    """Optional search term for filtering templates"""

    status: Optional[str]
    """Optional status filter: APPROVED, PENDING, REJECTED"""
