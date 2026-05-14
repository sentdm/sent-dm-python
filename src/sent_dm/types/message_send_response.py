# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["MessageSendResponse", "Data", "DataRecipient", "Error", "Meta"]


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


class Error(BaseModel):
    """Error information"""

    code: Optional[str] = None
    """Machine-readable error code (e.g., "RESOURCE_001")"""

    details: Optional[Dict[str, List[str]]] = None
    """Additional validation error details (field-level errors)"""

    doc_url: Optional[str] = None
    """URL to documentation about this error"""

    message: Optional[str] = None
    """Human-readable error message"""


class Meta(BaseModel):
    """Request and response metadata"""

    request_id: Optional[str] = None
    """Unique identifier for this request (for tracing and support)"""

    timestamp: Optional[datetime] = None
    """Server timestamp when the response was generated"""

    version: Optional[str] = None
    """API version used for this request"""


class MessageSendResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """Response for the multi-recipient send message endpoint"""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
