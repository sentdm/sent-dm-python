# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookListEventsParams"]


class WebhookListEventsParams(TypedDict, total=False):
    page: Required[int]

    page_size: Required[int]

    search: Optional[str]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
