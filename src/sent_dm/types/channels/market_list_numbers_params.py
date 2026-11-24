# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MarketListNumbersParams"]


class MarketListNumbersParams(TypedDict, total=False):
    channel: Required[str]

    country: Required[str]

    campaign_id: Optional[str]
    """
    Only the numbers of this campaign (US TEN_DLC); all of the market's when absent.
    """

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
