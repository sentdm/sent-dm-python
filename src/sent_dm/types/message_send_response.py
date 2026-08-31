# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["MessageSendResponse", "Data", "DataRecipient", "Error", "Meta"]


class DataRecipient(BaseModel):
    """What one recipient of a send got, as the API reports it."""

    body: Optional[str] = None
    """
    Resolved template body for this recipient's channel, or null when the channel is
    auto-detected.
    """

    channel: Optional[str] = None
    """Channel this message will be sent on — sms, whatsapp — or null to auto-detect."""

    message_id: Optional[str] = None
    """Identifier for tracking this recipient's message."""

    to: Optional[str] = None
    """Phone number in E.164 format."""


class Data(BaseModel):
    """
    The result of a multi-recipient send.

    Declared here rather than in the service layer. POST /v3/messages used to publish
    MessageSendResult — a type in Common.Services.Messaging.Contracts — so the public contract was
    whatever the send service happened to return, and changing that service for an internal reason changed the
    API. The service keeps its result; this is what a caller sees, and the mapping between them is a decision the
    endpoint makes.

    The wire is unchanged by the move: same names, same values.
    """

    recipients: Optional[List[DataRecipient]] = None

    status: Optional[str] = None
    """Overall status — QUEUED once the batch is accepted for delivery."""

    template_id: Optional[str] = None

    template_name: Optional[str] = None


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
    """The result of a multi-recipient send.

    Declared here rather than in the service layer. POST /v3/messages used to
    publish MessageSendResult — a type in Common.Services.Messaging.Contracts — so
    the public contract was whatever the send service happened to return, and
    changing that service for an internal reason changed the API. The service keeps
    its result; this is what a caller sees, and the mapping between them is a
    decision the endpoint makes.

    The wire is unchanged by the move: same names, same values.
    """

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
