# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConversationListMessagesParams"]


class ConversationListMessagesParams(TypedDict, total=False):
    page: int

    page_size: int

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
