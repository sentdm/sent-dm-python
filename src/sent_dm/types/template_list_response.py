# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["TemplateListResponse", "Data", "DataPagination", "DataPaginationCursors", "DataTemplate", "Error", "Meta"]


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


class DataTemplate(BaseModel):
    """Template response for v3 API"""

    id: Optional[str] = None
    """Unique template identifier"""

    category: Optional[str] = None
    """Template category: MARKETING, UTILITY, AUTHENTICATION"""

    channels: Optional[List[str]] = None
    """Supported channels: sms, whatsapp"""

    created_at: Optional[datetime] = None
    """When the template was created"""

    is_published: Optional[bool] = None
    """Whether the template is published and active"""

    language: Optional[str] = None
    """Template language code (e.g., en_US)"""

    name: Optional[str] = None
    """Template display name"""

    status: Optional[str] = None
    """Template status: APPROVED, PENDING, REJECTED"""

    updated_at: Optional[datetime] = None
    """When the template was last updated"""

    variables: Optional[List[str]] = None
    """Template variables for personalization"""


class Data(BaseModel):
    """Paginated list of templates"""

    pagination: Optional[DataPagination] = None
    """Pagination metadata for list responses"""

    templates: Optional[List[DataTemplate]] = None
    """List of templates"""


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


class TemplateListResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """Paginated list of templates"""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
