# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .tcr_vertical import TcrVertical
from .destination_country import DestinationCountry
from .tcr_brand_relationship import TcrBrandRelationship

__all__ = ["ProfileDetail", "BillingContact", "Brand", "BrandBusiness", "BrandCompliance", "BrandContact"]


class BillingContact(BaseModel):
    """Billing contact info returned in profile responses"""

    address: Optional[str] = None

    email: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[str] = None


class BrandBusiness(BaseModel):
    """Business details and address information"""

    city: Optional[str] = None
    """City"""

    country: Optional[str] = None
    """Country code (e.g., US, CA)"""

    country_of_registration: Optional[str] = None
    """Country where the business is registered"""

    entity_type: Optional[str] = None
    """Business entity type"""

    legal_name: Optional[str] = None
    """Legal business name"""

    postal_code: Optional[str] = None
    """Postal/ZIP code"""

    state: Optional[str] = None
    """State/province code"""

    street: Optional[str] = None
    """Street address"""

    tax_id: Optional[str] = None
    """Tax ID/EIN number"""

    tax_id_type: Optional[str] = None
    """Type of tax ID (e.g., us_ein, ca_bn)"""

    url: Optional[str] = None
    """Business website URL"""


class BrandCompliance(BaseModel):
    """Compliance and TCR-related information"""

    brand_relationship: Optional[TcrBrandRelationship] = None

    destination_countries: Optional[List[DestinationCountry]] = None
    """List of destination countries for messaging"""

    expected_messaging_volume: Optional[str] = None
    """Expected daily messaging volume"""

    is_tcr_application: Optional[bool] = None
    """Whether this is a TCR (Campaign Registry) application"""

    notes: Optional[str] = None
    """Additional notes about the business or use case"""

    phone_number_prefix: Optional[str] = None
    """Phone number prefix for messaging (e.g., "+1")"""

    primary_use_case: Optional[str] = None
    """Primary messaging use case description"""

    vertical: Optional[TcrVertical] = None


class BrandContact(BaseModel):
    """Contact information for the brand"""

    business_name: Optional[str] = None
    """Business/brand name"""

    email: Optional[str] = None
    """Contact email address"""

    name: Optional[str] = None
    """Primary contact name"""

    phone: Optional[str] = None
    """Contact phone number in E.164 format"""

    phone_country_code: Optional[str] = None
    """Contact phone country code (e.g., "1" for US)"""

    role: Optional[str] = None
    """Contact's role in the business"""


class Brand(BaseModel):
    """
    Brand response with nested contact, business, and compliance sections — mirrors the request structure.
    """

    id: Optional[str] = None
    """Unique identifier for the brand"""

    business: Optional[BrandBusiness] = None
    """Business details and address information"""

    compliance: Optional[BrandCompliance] = None
    """Compliance and TCR-related information"""

    contact: Optional[BrandContact] = None
    """Contact information for the brand"""

    created_at: Optional[datetime] = None
    """When the brand was created"""

    csp_id: Optional[str] = None
    """CSP (Campaign Service Provider) ID"""

    identity_status: Optional[Literal["SELF_DECLARED", "UNVERIFIED", "VERIFIED", "VETTED_VERIFIED"]] = None

    is_inherited: Optional[bool] = None
    """Whether this brand is inherited from the parent organization"""

    status: Optional[Literal["ACTIVE", "INACTIVE", "SUSPENDED"]] = None

    submitted_at: Optional[datetime] = None
    """When the brand was submitted to TCR"""

    submitted_to_tcr: Optional[bool] = None
    """Whether this brand has been submitted to TCR"""

    tcr_brand_id: Optional[str] = None
    """TCR brand ID (populated after TCR submission)"""

    universal_ein: Optional[str] = None
    """Universal EIN from TCR"""

    updated_at: Optional[datetime] = None
    """When the brand was last updated"""


class ProfileDetail(BaseModel):
    """Detailed profile response for v3 API"""

    id: Optional[str] = None
    """Profile unique identifier"""

    allow_contact_sharing: Optional[bool] = None
    """Whether contacts are shared across profiles in the organization"""

    allow_number_change_during_onboarding: Optional[bool] = None
    """Whether number changes are allowed during onboarding"""

    allow_template_sharing: Optional[bool] = None
    """Whether templates are shared across profiles in the organization"""

    billing_contact: Optional[BillingContact] = None
    """Billing contact info returned in profile responses"""

    billing_model: Optional[str] = None
    """Billing model: profile, organization, or profile_and_organization"""

    brand: Optional[Brand] = None
    """
    Brand response with nested contact, business, and compliance sections — mirrors
    the request structure.
    """

    created_at: Optional[datetime] = None
    """When the profile was created"""

    description: Optional[str] = None
    """Profile description"""

    email: Optional[str] = None
    """Profile email (inherited from organization)"""

    icon: Optional[str] = None
    """Profile icon URL"""

    inherit_contacts: Optional[bool] = None
    """Whether this profile inherits contacts from the organization"""

    inherit_tcr_brand: Optional[bool] = None
    """Whether this profile inherits TCR brand from the organization"""

    inherit_tcr_campaign: Optional[bool] = None
    """Whether this profile inherits TCR campaign from the organization"""

    inherit_templates: Optional[bool] = None
    """Whether this profile inherits templates from the organization"""

    name: Optional[str] = None
    """Profile name"""

    organization_id: Optional[str] = None
    """Parent organization ID"""

    sending_phone_number: Optional[str] = None
    """Direct SMS phone number"""

    sending_phone_number_profile_id: Optional[str] = None
    """Reference to another profile for SMS/Telnyx configuration"""

    sending_whatsapp_number_profile_id: Optional[str] = None
    """Reference to another profile for WhatsApp configuration"""

    short_name: Optional[str] = None
    """Profile short name/abbreviation.

    3–11 characters: letters, numbers, and spaces only, with at least one letter.
    """

    status: Optional[str] = None
    """Profile setup status: incomplete, pending_review, approved, rejected"""

    updated_at: Optional[datetime] = None
    """When the profile was last updated"""

    waba_id: Optional[str] = None
    """
    WhatsApp Business Account ID associated with this profile. Present whether the
    WABA is inherited from the organization or configured directly.
    """

    whatsapp_phone_number: Optional[str] = None
    """Direct WhatsApp phone number"""
