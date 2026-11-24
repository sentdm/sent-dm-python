# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..api_meta import APIMeta
from ..error_detail import ErrorDetail
from .channel_market import ChannelMarket

__all__ = ["APIResponseOfChannelMarket"]


class APIResponseOfChannelMarket(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[ChannelMarket] = None
    """
    One market the profile sends in on a channel — its sender, where that sender
    stands, and what the market wants. Named for no one channel, as the routes it
    answers are not (/v3/channels/{channel}/{country}/{type}); SMS is the channel
    with markets today.

    A profile may send in several: it is a tenant, not a market. Each carries its
    own status, because a profile can be live in one country and mid-registration in
    another — and each carries what it still owes, rather than that being reported
    in a separate array a caller has to join on.
    """

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
