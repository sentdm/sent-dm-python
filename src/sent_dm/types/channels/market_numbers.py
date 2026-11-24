# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .market_number import MarketNumber

__all__ = ["MarketNumbers"]


class MarketNumbers(BaseModel):
    """
    The numbers a customer holds in one market: GET /v3/channels/{channel}/{country}/{type}/numbers.
    """

    channel: Optional[str] = None

    country: Optional[str] = None
    """ISO 3166-1 alpha-2, uppercase."""

    numbers: Optional[List[MarketNumber]] = None
    """Empty, never null, when the customer holds nothing there."""
