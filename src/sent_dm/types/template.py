# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Template"]


class Template(BaseModel):
    """Template response for v3 API"""

    customer_id: str
    """Which customer owns this — the key's own, or the profile named in x-profile-id.

    Says whose resource this is, which the resource's own id does not.
    """

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
