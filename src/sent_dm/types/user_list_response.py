# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["UserListResponse", "Data", "DataPagination", "DataPaginationCursors", "DataUser", "Error", "Meta"]


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


class DataUser(BaseModel):
    """User response for v3 API"""

    id: Optional[str] = None
    """User unique identifier"""

    created_at: Optional[datetime] = None
    """When the user was added to the organization"""

    customer_id: Optional[str] = None
    """Which customer owns this — the key's own, or the profile named in x-profile-id.

    Says whose resource this is, which the resource's own id does not.
    """

    email: Optional[str] = None
    """User email address"""

    invited_at: Optional[datetime] = None
    """When the user was invited"""

    last_login_at: Optional[datetime] = None
    """When the user last logged in"""

    name: Optional[str] = None
    """User full name"""

    role: Optional[str] = None
    """User role in the organization: admin, billing, developer"""

    status: Optional[str] = None
    """User status: active, invited, suspended, rejected"""

    updated_at: Optional[datetime] = None
    """When the user record was last updated"""


class Data(BaseModel):
    """The users in the organization."""

    pagination: Optional[DataPagination] = None
    """Pagination metadata for list responses"""

    users: Optional[List[DataUser]] = None
    """The users on this page."""


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


class UserListResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The users in the organization."""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
