# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail
from .sender_profile import SenderProfile

__all__ = ["APIResponseOfSenderProfile"]


class APIResponseOfSenderProfile(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[SenderProfile] = None
    """
    A sender profile as the API reports it — the same document the create call
    accepts, plus the read-only facts it cannot: each market's status and what it
    still owes.

    No status at the profile, brand or campaign level. Brand and campaign are
    identity, and identity has no lifecycle. What has one is the registration of a
    sender in a market, and the approval of a channel — so status lives there, where
    it says which specific thing is blocked rather than flattening several answers
    into one.
    """

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
