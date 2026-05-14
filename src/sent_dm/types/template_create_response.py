# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["TemplateCreateResponse", "Data", "Error", "Meta"]


class Data(BaseModel):
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


class TemplateCreateResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """Template response for v3 API"""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
