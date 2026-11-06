# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .message import Message
from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail

__all__ = ["APIResponseOfMessage"]


class APIResponseOfMessage(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Message] = None
    """Message response for v3 API — same shape as v2 with snake_case JSON conventions.

    The shape of a message that was sent immediately: it never has a scheduled_at
    key. A message that is or was held for a later instant is a
    ScheduledMessageResponse, and the endpoint decides which of the two to answer
    with. From always returns this type.
    """

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
