# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .api_error import APIError

__all__ = ["MessageSendResponse", "Data", "DataRecipient"]


class DataRecipient(BaseModel):
    """Per-recipient result in the send message response"""

    channel: Optional[str] = None
    """Channel this message will be sent on (e.g.

    "sms", "whatsapp"), or null for auto-detect
    """

    message_id: Optional[str] = None
    """Unique message identifier for tracking this recipient's message"""

    to: Optional[str] = None
    """Phone number in E.164 format"""


class Data(BaseModel):
    """The response data (null if error)"""

    body: Optional[str] = None
    """Resolved template body text"""

    recipients: Optional[List[DataRecipient]] = None
    """Per-recipient message results"""

    status: Optional[str] = None
    """Overall request status (e.g. "accepted")"""

    template_id: Optional[str] = None
    """Template ID that was used"""

    template_name: Optional[str] = None
    """Template display name"""


class MessageSendResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The response data (null if error)"""

    error: Optional[APIError] = None
    """Error details (null if successful)"""

    meta: Optional[APIMeta] = None
    """Metadata about the request and response"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
