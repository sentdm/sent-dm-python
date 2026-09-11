# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebhookListParams"]


class WebhookListParams(TypedDict, total=False):
    is_active: Optional[bool]

    page: int

    page_size: int

    search: Optional[str]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
