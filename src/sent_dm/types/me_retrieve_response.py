# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .api_meta import APIMeta
from .api_error import APIError
from .profile_settings import ProfileSettings

__all__ = [
    "MeRetrieveResponse",
    "Data",
    "DataChannels",
    "DataChannelsRcs",
    "DataChannelsSMS",
    "DataChannelsWhatsapp",
    "DataProfile",
]


class DataChannelsRcs(BaseModel):
    """RCS channel (provider: vibes)"""

    configured: Optional[bool] = None
    """Whether RCS is configured for this account"""

    phone_number: Optional[str] = None
    """RCS-enabled phone number in E.164 format"""


class DataChannelsSMS(BaseModel):
    """SMS channel (providers: telnyx, sinch)"""

    configured: Optional[bool] = None
    """Whether SMS is configured for this account"""

    phone_number: Optional[str] = None
    """Sending phone number in E.164 format"""


class DataChannelsWhatsapp(BaseModel):
    """WhatsApp Business channel (provider: meta)"""

    business_name: Optional[str] = None
    """WhatsApp Business display name"""

    configured: Optional[bool] = None
    """Whether WhatsApp is configured for this account"""

    phone_number: Optional[str] = None
    """WhatsApp phone number in E.164 format"""


class DataChannels(BaseModel):
    """Messaging channel configuration"""

    rcs: Optional[DataChannelsRcs] = None
    """RCS channel (provider: vibes)"""

    sms: Optional[DataChannelsSMS] = None
    """SMS channel (providers: telnyx, sinch)"""

    whatsapp: Optional[DataChannelsWhatsapp] = None
    """WhatsApp Business channel (provider: meta)"""


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
    """Customer ID (organization, account, or profile)"""

    channels: Optional[DataChannels] = None
    """Messaging channel configuration"""

    created_at: Optional[datetime] = None
    """When the account was created"""

    description: Optional[str] = None
    """Account description"""

    email: Optional[str] = None
    """Contact email address"""

    icon: Optional[str] = None
    """Account icon URL"""

    name: Optional[str] = None
    """Account name"""

    organization_id: Optional[str] = None
    """Organization ID (only for profile type — the parent organization)"""

    profiles: Optional[List[DataProfile]] = None
    """
    List of profiles (populated for organization type, empty for user and profile
    types)
    """

    settings: Optional[ProfileSettings] = None
    """Profile settings (only for profile type)"""

    short_name: Optional[str] = None
    """Short name / abbreviation (only for profile type)"""

    status: Optional[str] = None
    """
    Profile status (only for profile type): incomplete, pending_review, approved,
    etc.
    """

    type: Optional[str] = None
    """
    Account type: "organization" (has profiles), "user" (no profiles), or "profile"
    (child of an organization)
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
