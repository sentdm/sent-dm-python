# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["UserInviteResponse", "Data", "Error", "Meta"]


class Data(BaseModel):
    """User response for v3 API"""

    id: Optional[str] = None
    """User unique identifier"""

    created_at: Optional[datetime] = None
    """When the user was added to the organization"""

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


class UserInviteResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """User response for v3 API"""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
