# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail
from .message_resend_response_data import MessageResendResponseData

__all__ = ["MessageResendResponse"]


class MessageResendResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[MessageResendResponseData] = None
    """The result of a multi-recipient send.

    Declared here rather than in the service layer. POST /v3/messages used to
    publish MessageSendResult — a type in Common.Services.Messaging.Contracts — so
    the public contract was whatever the send service happened to return, and
    changing that service for an internal reason changed the API. The service keeps
    its result; this is what a caller sees, and the mapping between them is a
    decision the endpoint makes.

    The shape of an immediate send: it never has a scheduled_at key. A send that
    carried scheduled_at is a ScheduledSendMessageResponse, and the endpoint decides
    which of the two to answer with. From always returns this type.
    """

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
