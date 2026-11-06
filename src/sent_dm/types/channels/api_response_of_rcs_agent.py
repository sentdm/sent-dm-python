# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..api_meta import APIMeta
from .rcs_agent import RcsAgent
from ..error_detail import ErrorDetail

__all__ = ["APIResponseOfRcsAgent"]


class APIResponseOfRcsAgent(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[RcsAgent] = None
    """
    An RCS agent as its owner sees it: the order form back, plus where the
    submission stands.

    Not RcsSenderResponse. That one is the admin projection and carries the pipeline
    we track about a customer's request — internalStatus, statusReason, isLaunched —
    and the S3 keys behind the assets. None of that is the customer's to read: an
    internal status is a note to ourselves, and an S3 key is a storage detail that
    would become a contract the moment it was published.

    What is here is what the caller sent, in the names it sent them under, plus the
    three things only we can answer: the record's id, its status, and the number it
    sends from. So a read after a write shows the form as stored rather than as
    echoed.
    """

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
