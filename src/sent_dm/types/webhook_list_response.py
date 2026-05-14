# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WebhookListResponse", "Data", "DataPagination", "DataPaginationCursors", "DataWebhook", "Error", "Meta"]


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


class DataWebhook(BaseModel):
    id: Optional[str] = None

    consecutive_failures: Optional[int] = None

    created_at: Optional[datetime] = None

    display_name: Optional[str] = None

    endpoint_url: Optional[str] = None

    event_filters: Optional[Dict[str, List[str]]] = None

    event_types: Optional[List[str]] = None

    is_active: Optional[bool] = None

    last_delivery_attempt_at: Optional[datetime] = None

    last_successful_delivery_at: Optional[datetime] = None

    retry_count: Optional[int] = None

    signing_secret: Optional[str] = None

    timeout_seconds: Optional[int] = None

    updated_at: Optional[datetime] = None


class Data(BaseModel):
    """The response data (null if error)"""

    pagination: Optional[DataPagination] = None
    """Pagination metadata for list responses"""

    webhooks: Optional[List[DataWebhook]] = None


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


class WebhookListResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The response data (null if error)"""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
