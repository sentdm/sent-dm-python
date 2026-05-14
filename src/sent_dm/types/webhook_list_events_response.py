# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WebhookListEventsResponse", "Data", "DataEvent", "DataPagination", "DataPaginationCursors", "Error", "Meta"]


class DataEvent(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    delivery_attempts: Optional[int] = None

    delivery_status: Optional[str] = None

    error_message: Optional[str] = None

    event_data: Optional[object] = None

    event_type: Optional[str] = None

    http_status_code: Optional[int] = None

    processing_completed_at: Optional[datetime] = None

    processing_started_at: Optional[datetime] = None

    response_body: Optional[str] = None


class DataPaginationCursors(BaseModel):
    """Cursor-based pagination pointers"""

    after: Optional[str] = None
    """Cursor to fetch the next page"""

    before: Optional[str] = None
    """Cursor to fetch the previous page"""


class DataPagination(BaseModel):
    """Pagination metadata for list responses"""

    cursors: Optional[DataPaginationCursors] = None
    """Cursor-based pagination pointers"""

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
    """The response data (null if error)"""

    events: Optional[List[DataEvent]] = None

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


class WebhookListEventsResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The response data (null if error)"""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
