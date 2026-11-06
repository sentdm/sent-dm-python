# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .account import Account
from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail

__all__ = ["APIResponseOfAccount"]


class APIResponseOfAccount(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Account] = None
    """
    Account response for GET /v3/me endpoint. Returns organization (with profiles),
    user (standalone), or profile (child of an organization) data depending on the
    API key type. Always includes messaging channel configuration.
    """

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
