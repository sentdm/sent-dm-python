# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..api_meta import APIMeta
from .sms_market import SMSMarket
from ..error_detail import ErrorDetail

__all__ = ["APIResponseOfListOfSMSMarket"]


class APIResponseOfListOfSMSMarket(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[List[SMSMarket]] = None
    """The response data (null if error)"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
