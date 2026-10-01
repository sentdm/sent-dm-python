# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CallListParams"]


class CallListParams(TypedDict, total=False):
    direction: Optional[str]
    """
    Optional direction filter: outbound for calls placed from your app, inbound for
    calls to one of your numbers
    """

    from_: Annotated[Union[str, datetime, None], PropertyInfo(alias="from", format="iso8601")]
    """Only calls started at or after this time (ISO 8601)"""

    number: Optional[str]
    """
    Optional filter on the number that owns the call, one of your voice-enabled
    numbers in E.164 format
    """

    page: int
    """Page number (1-indexed)"""

    page_size: int
    """Number of items per page"""

    status: Optional[str]
    """
    Optional status filter: initiated, ringing, answered, completed, failed,
    no_answer or rejected
    """

    to: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Only calls started at or before this time (ISO 8601)"""

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
