# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail

__all__ = ["MessageSendResponse", "Data", "DataRecipient"]


class DataRecipient(BaseModel):
    """Per-recipient result in the send message response"""

    body: Optional[str] = None
    """
    Resolved template body text for this recipient's channel, or null for
    auto-detect
    """

    channel: Optional[str] = None
    """Channel this message will be sent on (e.g.

    "sms", "whatsapp"), or null for auto-detect
    """

    message_id: Optional[str] = None
    """Unique message identifier for tracking this recipient's message"""

    to: Optional[str] = None
    """Phone number in E.164 format"""


class Data(BaseModel):
    """Response for the multi-recipient send message endpoint"""

    recipients: Optional[List[DataRecipient]] = None
    """Per-recipient message results"""

    status: Optional[str] = None
    """
    Overall request status: "QUEUED" when the batch has been accepted and published
    to Kafka.
    """

    template_id: Optional[str] = None
    """Template ID that was used"""

    template_name: Optional[str] = None
    """Template display name"""


class MessageSendResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """Response for the multi-recipient send message endpoint"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
