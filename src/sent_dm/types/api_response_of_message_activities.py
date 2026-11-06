# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail
from .message_activities import MessageActivities

__all__ = ["APIResponseOfMessageActivities"]


class APIResponseOfMessageActivities(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[MessageActivities] = None
    """Response for GET /messages/{id}/activities"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
