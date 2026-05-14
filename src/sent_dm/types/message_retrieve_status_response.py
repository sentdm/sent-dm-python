# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "MessageRetrieveStatusResponse",
    "Data",
    "DataEvent",
    "DataMessageBody",
    "DataMessageBodyButton",
    "Error",
    "Meta",
]


class DataEvent(BaseModel):
    """Represents a status change event in a message's lifecycle (v3)"""

    description: Optional[str] = None

    status: Optional[str] = None

    timestamp: Optional[datetime] = None


class DataMessageBodyButton(BaseModel):
    postback_data: Optional[str] = FieldInfo(alias="postbackData", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    value: Optional[str] = None


class DataMessageBody(BaseModel):
    """
    Structured message body format for database storage.
    Preserves channel-specific components (header, body, footer, buttons).
    """

    buttons: Optional[List[DataMessageBodyButton]] = None

    content: Optional[str] = None

    footer: Optional[str] = None

    header: Optional[str] = None


class Data(BaseModel):
    """Message response for v3 API — same shape as v2 with snake_case JSON conventions"""

    id: Optional[str] = None

    active_contact_price: Optional[float] = None

    channel: Optional[str] = None

    contact_id: Optional[str] = None

    created_at: Optional[datetime] = None

    customer_id: Optional[str] = None

    direction: Optional[str] = None

    events: Optional[List[DataEvent]] = None

    message_body: Optional[DataMessageBody] = None
    """
    Structured message body format for database storage. Preserves channel-specific
    components (header, body, footer, buttons).
    """

    phone: Optional[str] = None

    phone_international: Optional[str] = None

    price: Optional[float] = None

    region_code: Optional[str] = None

    status: Optional[str] = None

    template_category: Optional[str] = None

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


class MessageRetrieveStatusResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """Message response for v3 API — same shape as v2 with snake_case JSON conventions"""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
