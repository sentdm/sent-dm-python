# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ContactUpdateResponse", "Data", "Error", "Meta"]


class Data(BaseModel):
    """
    Contact response for v3 API
    Uses snake_case for JSON property names
    """

    id: Optional[str] = None
    """Unique identifier for the contact"""

    available_channels: Optional[str] = None
    """Comma-separated list of available messaging channels (e.g., "sms,whatsapp")"""

    country_code: Optional[str] = None
    """Country calling code (e.g., 1 for US/Canada)"""

    created_at: Optional[datetime] = None
    """When the contact was created"""

    default_channel: Optional[str] = None
    """Default messaging channel to use (e.g., "sms" or "whatsapp")"""

    format_e164: Optional[str] = None
    """Phone number in E.164 format (e.g., +1234567890)"""

    format_international: Optional[str] = None
    """Phone number in international format (e.g., +1 234-567-890)"""

    format_national: Optional[str] = None
    """Phone number in national format (e.g., (234) 567-890)"""

    format_rfc: Optional[str] = None
    """Phone number in RFC 3966 format (e.g., tel:+1-234-567-890)"""

    is_inherited: Optional[bool] = None
    """Whether this is an inherited contact (read-only)"""

    opt_out: Optional[bool] = None
    """Whether the contact has opted out of messaging.

    Single source of truth — opt-out is per-contact, not per-channel.
    """

    phone_number: Optional[str] = None
    """Phone number in original format"""

    region_code: Optional[str] = None
    """ISO 3166-1 alpha-2 country code (e.g., US, CA, GB)"""

    updated_at: Optional[datetime] = None
    """When the contact was last updated"""


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


class ContactUpdateResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """Contact response for v3 API Uses snake_case for JSON property names"""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
