# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "MessageRetrieveActivitiesResponse",
    "Data",
    "DataActivity",
    "DataPagination",
    "DataPaginationCursors",
    "Error",
    "Meta",
]


class DataActivity(BaseModel):
    """A single message activity event for v3 API"""

    active_contact_price: Optional[str] = None
    """
    Active contact markup applied on top of the channel cost, formatted to 4 decimal
    places.
    """

    description: Optional[str] = None
    """Human-readable description of the activity"""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """
    Sender phone number for this activity (the customer's sending number for
    outbound, the external sender for inbound). Null when not reported by the
    provider.
    """

    price: Optional[str] = None
    """
    Channel cost for this activity (e.g., SMS/WhatsApp provider cost), formatted to
    4 decimal places.
    """

    status: Optional[str] = None
    """Activity status.

    Outbound: QUEUED, PROCESSED, ROUTED, SENT, DELIVERED, READ, FAILED. Inbound
    (from contact): RECEIVED (terminal).
    """

    timestamp: Optional[datetime] = None
    """When this activity occurred"""


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
    """Response for GET /messages/{id}/activities"""

    activities: Optional[List[DataActivity]] = None
    """List of activity events ordered by most recent first"""

    message_id: Optional[str] = None
    """The message ID these activities belong to"""

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


class MessageRetrieveActivitiesResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """Response for GET /messages/{id}/activities"""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
