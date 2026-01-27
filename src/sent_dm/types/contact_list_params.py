# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactListParams"]


class ContactListParams(TypedDict, total=False):
    page: Required[int]
    """The page number (zero-indexed). Default is 0."""

    page_size: Required[Annotated[int, PropertyInfo(alias="pageSize")]]
    """The number of items per page. Default is 20."""
