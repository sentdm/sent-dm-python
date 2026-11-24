# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..api_meta import APIMeta
from ..error_detail import ErrorDetail
from .market_numbers import MarketNumbers

__all__ = ["APIResponseOfMarketNumbers"]


class APIResponseOfMarketNumbers(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[MarketNumbers] = None
    """
    The numbers a customer holds in one market: GET
    /v3/channels/{channel}/{country}/{type}/numbers.
    """

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
