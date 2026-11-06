# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .profile_settings import ProfileSettings

__all__ = ["AccountProfile"]


class AccountProfile(BaseModel):
    """Profile (sender profile) response for v3 API"""

    id: Optional[str] = None
    """Profile unique identifier"""

    created_at: Optional[datetime] = None
    """When the profile was created"""

    description: Optional[str] = None
    """Profile description"""

    icon: Optional[str] = None
    """Profile icon URL"""

    name: Optional[str] = None
    """Profile name"""

    role: Optional[str] = None
    """
    User's role in this profile: admin, billing, developer (inherited from
    organization if not explicitly set)
    """

    settings: Optional[ProfileSettings] = None
    """Profile configuration settings"""

    short_name: Optional[str] = None
    """Profile short name (abbreviation)"""

    status: Optional[str] = None
    """Profile setup status: incomplete, pending_review, approved, rejected"""
