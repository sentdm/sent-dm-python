# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Contact"]


class Contact(BaseModel):
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
    """Whether the contact has opted out of messaging"""

    phone_number: Optional[str] = None
    """Phone number in original format"""

    region_code: Optional[str] = None
    """ISO 3166-1 alpha-2 country code (e.g., US, CA, GB)"""

    updated_at: Optional[datetime] = None
    """When the contact was last updated"""
