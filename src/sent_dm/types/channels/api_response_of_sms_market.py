# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..api_meta import APIMeta
from .sms_market import SMSMarket
from ..error_detail import ErrorDetail

__all__ = ["APIResponseOfSMSMarket"]


class APIResponseOfSMSMarket(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[SMSMarket] = None
    """
    One SMS market the profile sends in — its sender, where that sender stands, and
    what the market wants.

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
