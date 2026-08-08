# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConversationListMessagesParams"]


class ConversationListMessagesParams(TypedDict, total=False):
    page: Required[int]

    page_size: Required[int]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
