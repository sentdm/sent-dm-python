# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ConversationListMessagesResponse",
    "Data",
    "DataMessage",
    "DataMessageEvent",
    "DataMessageMessageBody",
    "DataMessageMessageBodyButton",
    "DataPagination",
    "DataPaginationCursors",
    "Error",
    "Meta",
]


class DataMessageEvent(BaseModel):
    """Represents a status change event in a message's lifecycle (v3)"""

    status: str

    timestamp: datetime

    description: Optional[str] = None


class DataMessageMessageBodyButton(BaseModel):
    postback_data: Optional[str] = FieldInfo(alias="postbackData", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    value: Optional[str] = None


class DataMessageMessageBody(BaseModel):
    """
    Structured message body format for database storage.
    Preserves channel-specific components (header, body, footer, buttons).
    """

    buttons: Optional[List[DataMessageMessageBodyButton]] = None

    content: Optional[str] = None

    footer: Optional[str] = None

    header: Optional[str] = None


class DataMessage(BaseModel):
    """Message response for v3 API — same shape as v2 with snake_case JSON conventions"""

    id: Optional[str] = None

    active_contact_price: Optional[float] = None

    channel: Optional[str] = None

    contact_id: Optional[str] = None

    created_at: Optional[datetime] = None

    customer_id: Optional[str] = None

    direction: Optional[str] = None

    events: Optional[List[DataMessageEvent]] = None

    message_body: Optional[DataMessageMessageBody] = None
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


class DataPaginationCursors(BaseModel):
    """Cursor-based pagination. Never populated — see Cursors."""

    after: Optional[str] = None
    """Cursor to fetch the next page."""

    before: Optional[str] = None
    """Cursor to fetch the previous page."""


class DataPagination(BaseModel):
    """Pagination metadata for list responses"""

    cursors: Optional[DataPaginationCursors] = None
    """Cursor-based pagination. Never populated — see Cursors."""

    has_more: Optional[bool] = None
    """Whether there are more pages after this one"""

    page: Optional[int] = None
    """Current page number (1-indexed)"""

    page_size: Optional[int] = None
    """Number of items per page"""

    total_count: Optional[int] = None
    """Total number of items across all pages"""

    total_pages: Optional[int] = None
    """Total number of pages"""


class Data(BaseModel):
    """A paginated list of messages — used by both conversation read endpoints."""

    messages: Optional[List[DataMessage]] = None
    """The messages on this page."""

    pagination: Optional[DataPagination] = None
    """Pagination metadata for list responses"""


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


class ConversationListMessagesResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """A paginated list of messages — used by both conversation read endpoints."""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
