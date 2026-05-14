# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = [
    "MeRetrieveResponse",
    "Data",
    "DataChannels",
    "DataChannelsRcs",
    "DataChannelsSMS",
    "DataChannelsWhatsapp",
    "DataProfile",
    "DataProfileSettings",
    "DataSettings",
    "Error",
    "Meta",
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


class DataProfileSettings(BaseModel):
    """Profile configuration settings"""

    allow_contact_sharing: Optional[bool] = None
    """Whether contacts are shared across profiles in the organization"""

    allow_template_sharing: Optional[bool] = None
    """Whether templates are shared across profiles in the organization"""

    billing_model: Optional[str] = None
    """Billing model: profile, organization, or profile_and_organization"""

    inherit_contacts: Optional[bool] = None
    """Whether this profile inherits contacts from the organization"""

    inherit_tcr_brand: Optional[bool] = None
    """Whether this profile inherits TCR brand from the organization"""

    inherit_tcr_campaign: Optional[bool] = None
    """Whether this profile inherits TCR campaign from the organization"""

    inherit_templates: Optional[bool] = None
    """Whether this profile inherits templates from the organization"""


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

    settings: Optional[DataProfileSettings] = None
    """Profile configuration settings"""

    short_name: Optional[str] = None
    """Profile short name (abbreviation)"""

    status: Optional[str] = None
    """Profile setup status: incomplete, pending_review, approved, rejected"""


class DataSettings(BaseModel):
    """Profile configuration settings"""

    allow_contact_sharing: Optional[bool] = None
    """Whether contacts are shared across profiles in the organization"""

    allow_template_sharing: Optional[bool] = None
    """Whether templates are shared across profiles in the organization"""

    billing_model: Optional[str] = None
    """Billing model: profile, organization, or profile_and_organization"""

    inherit_contacts: Optional[bool] = None
    """Whether this profile inherits contacts from the organization"""

    inherit_tcr_brand: Optional[bool] = None
    """Whether this profile inherits TCR brand from the organization"""

    inherit_tcr_campaign: Optional[bool] = None
    """Whether this profile inherits TCR campaign from the organization"""

    inherit_templates: Optional[bool] = None
    """Whether this profile inherits templates from the organization"""


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

    settings: Optional[DataSettings] = None
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


class MeRetrieveResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """
    Account response for GET /v3/me endpoint. Returns organization (with profiles),
    user (standalone), or profile (child of an organization) data depending on the
    API key type. Always includes messaging channel configuration.
    """

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
