# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail
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
    """RCS channel configuration. When configured, includes the RCS phone number."""

    configured: Optional[bool] = None
    """Whether RCS is configured for this account"""

    phone_number: Optional[str] = None
    """RCS-enabled phone number in E.164 format"""


class DataChannelsSMS(BaseModel):
    """SMS channel configuration. When configured, includes the sending phone number."""

    configured: Optional[bool] = None
    """Whether SMS is configured for this account"""

    phone_number: Optional[str] = None
    """Sending phone number in E.164 format"""


class DataChannelsWhatsapp(BaseModel):
    """WhatsApp Business channel configuration.

    When configured, includes the WhatsApp phone number
    and business name.
    """

    business_name: Optional[str] = None
    """WhatsApp Business display name"""

    configured: Optional[bool] = None
    """Whether WhatsApp is configured for this account"""

    phone_number: Optional[str] = None
    """WhatsApp phone number in E.164 format"""


class DataChannels(BaseModel):
    """Messaging channel configuration.

    All three channels are always present.
    Each channel has a "configured" flag; configured channels expose additional details.
    """

    rcs: Optional[DataChannelsRcs] = None
    """RCS channel configuration. When configured, includes the RCS phone number."""

    sms: Optional[DataChannelsSMS] = None
    """SMS channel configuration. When configured, includes the sending phone number."""

    whatsapp: Optional[DataChannelsWhatsapp] = None
    """WhatsApp Business channel configuration.

    When configured, includes the WhatsApp phone number and business name.
    """


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
    """
    Account response for GET /v3/me endpoint.
    Returns organization (with profiles), user (standalone), or profile (child of an organization)
    data depending on the API key type. Always includes messaging channel configuration.
    """

    id: Optional[str] = None
    """Customer ID (organization, account, or profile)"""

    channels: Optional[DataChannels] = None
    """Messaging channel configuration.

    All three channels are always present. Each channel has a "configured" flag;
    configured channels expose additional details.
    """

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

    sending_phone_number: Optional[str] = None
    """The SMS sender this account sends from in the United States, in E.164 form.

    Null when the account has no US SMS sender.

    The same value as channels.sms.phone_number, published under both names on
    purpose: sending_phone_number is what this value is already called on GET
    /v3/profiles, so the same key answers the same question whichever of the two
    endpoints you ask. Neither name is preferred over the other and neither is
    deprecated.

    The same value, not the same presence: this key is always written, including as
    null, whereas channels.sms.phone_number is left out entirely when there is no
    sender.
    """

    sending_phone_number_profile_id: Optional[str] = None
    """
    The account that holds sending_phone_number in number inventory: normally this
    account itself, and a different account when the number is held elsewhere. Null
    when there is no US sender, or when the sender is not a number drawn from
    inventory — an alphanumeric sender ID or a short code.
    """

    settings: Optional[ProfileSettings] = None
    """Profile configuration settings"""

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
    """
    Account response for GET /v3/me endpoint. Returns organization (with profiles),
    user (standalone), or profile (child of an organization) data depending on the
    API key type. Always includes messaging channel configuration.
    """

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
