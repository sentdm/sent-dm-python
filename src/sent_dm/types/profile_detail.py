# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ProfileDetail", "Settings"]


class Settings(BaseModel):
    """Profile configuration settings"""

    allow_contact_sharing: Optional[bool] = None
    """Whether contacts are shared across profiles in the organization"""

    allow_number_change_during_onboarding: Optional[bool] = None
    """Whether number changes are allowed during onboarding"""

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

    sending_phone_number: Optional[str] = None
    """Direct SMS phone number"""

    sending_phone_number_profile_id: Optional[str] = None
    """Reference to another profile for SMS/Telnyx configuration"""

    sending_whatsapp_number_profile_id: Optional[str] = None
    """Reference to another profile for WhatsApp configuration"""

    whatsapp_phone_number: Optional[str] = None
    """Direct WhatsApp phone number"""


class ProfileDetail(BaseModel):
    """Detailed profile response for v3 API"""

    id: Optional[str] = None
    """Profile unique identifier"""

    created_at: Optional[datetime] = None
    """When the profile was created"""

    description: Optional[str] = None
    """Profile description"""

    email: Optional[str] = None
    """Profile email (inherited from organization)"""

    icon: Optional[str] = None
    """Profile icon URL"""

    name: Optional[str] = None
    """Profile name"""

    organization_id: Optional[str] = None
    """Parent organization ID"""

    settings: Optional[Settings] = None
    """Profile configuration settings"""

    short_name: Optional[str] = None
    """Profile short name (abbreviation)"""

    status: Optional[str] = None
    """Profile setup status: incomplete, pending_review, approved, rejected"""

    updated_at: Optional[datetime] = None
    """When the profile was last updated"""
