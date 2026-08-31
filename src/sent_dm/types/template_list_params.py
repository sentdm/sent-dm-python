# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TemplateListParams"]


class TemplateListParams(TypedDict, total=False):
    page: Required[int]
    """Page number (1-indexed)"""

    page_size: Required[int]
    """Number of items per page"""

    category: Optional[str]
    """Optional category filter: MARKETING, UTILITY, AUTHENTICATION"""

    is_welcome_playground: Optional[bool]
    """Accepted and ignored.

    It used to filter on the welcome-playground marker inside a template's LOB
    details; that filter is gone and nothing reads this value, so sending it neither
    narrows nor widens the result. Retained only so a client still passing
    is_welcome_playground keeps binding instead of the request shape changing under
    it.
    """

    search: Optional[str]
    """Optional search term for filtering templates"""

    status: Optional[str]
    """Optional status filter: APPROVED, PENDING, REJECTED"""

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
