# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ...api_meta import APIMeta
from ...error_detail import ErrorDetail
from ..supplied_compliance import SuppliedCompliance

__all__ = ["APIResponseOfSuppliedCompliance"]


class APIResponseOfSuppliedCompliance(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[SuppliedCompliance] = None
    """
    What a market has been given: the identity it registers under, its programme,
    and any documents attached.

    What it does not carry is what the market asks for. That is the subject of GET
    /v3/compliance/requirements, and it is the same answer for every caller — a
    description of what a compliance regime wants, not a record of one customer's
    progress through it. It was reported here as well for a while, which put the
    same array in six response shapes and left a caller deciding which of two
    sources to believe.

    Present on a list read for markets that register (carrying brand and campaign),
    but with documents absent — documents are not fetched for a list, because a
    catalog lookup and a document read per market would multiply across a page.
    Absent documents is distinct from an empty list: absent says they were not
    fetched; empty says the market has been given none. The parent object is null
    only when the market registers with nobody and compliance was not computed —
    nothing to show at all.
    """

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
