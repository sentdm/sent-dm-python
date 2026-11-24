# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..api_meta import APIMeta
from ..error_detail import ErrorDetail
from .channel_market import ChannelMarket

__all__ = ["APIResponseOfListOfChannelMarket"]


class APIResponseOfListOfChannelMarket(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[List[ChannelMarket]] = None
    """The response data (null if error)"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
