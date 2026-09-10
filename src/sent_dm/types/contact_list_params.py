# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactListParams"]


class ContactListParams(TypedDict, total=False):
    channel: Optional[str]
    """Optional channel filter (sms, whatsapp)"""

    page: int
    """Page number (1-indexed)"""

    page_size: int
    """Number of items per page"""

    phone: Optional[str]
    """Optional phone number filter (alternative to list view)"""

    search: Optional[str]
    """Optional search term for filtering contacts"""

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
