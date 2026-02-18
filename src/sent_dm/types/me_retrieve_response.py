# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .api_meta import APIMeta
from .api_error import APIError
from .profile_settings import ProfileSettings

__all__ = ["MeRetrieveResponse", "Data", "DataProfile"]


class DataProfile(BaseModel):
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


class Data(BaseModel):
    """The response data (null if error)"""

    id: Optional[str] = None
    """Customer ID (organization or profile)"""

    created_at: Optional[datetime] = None
    """When the account was created"""

    description: Optional[str] = None
    """Account description"""

    icon: Optional[str] = None
    """Account icon URL"""

    name: Optional[str] = None
    """Account name"""

    profiles: Optional[List[DataProfile]] = None
    """List of profiles (only for organization type)"""

    settings: Optional[ProfileSettings] = None
    """Profile settings (only for profile type)"""

    status: Optional[str] = None
    """
    Profile status (only for profile type): incomplete, pending_review, approved,
    etc.
    """


class MeRetrieveResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The response data (null if error)"""

    error: Optional[APIError] = None
    """Error details (null if successful)"""

    meta: Optional[APIMeta] = None
    """Metadata about the request and response"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
