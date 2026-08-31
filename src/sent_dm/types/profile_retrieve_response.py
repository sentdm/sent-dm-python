# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .tcr_vertical import TcrVertical
from .destination_country import DestinationCountry
from .tcr_brand_relationship import TcrBrandRelationship

__all__ = [
    "ProfileRetrieveResponse",
    "Data",
    "DataBillingContact",
    "DataBrand",
    "DataBrandBusiness",
    "DataBrandCompliance",
    "DataBrandContact",
    "Error",
    "Meta",
]


class DataBillingContact(BaseModel):
    """Billing contact info returned in profile responses"""

    address: Optional[str] = None

    email: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[str] = None


class DataBrandBusiness(BaseModel):
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


class DataBrandCompliance(BaseModel):
    """Compliance and TCR-related information"""

    brand_relationship: Optional[TcrBrandRelationship] = None

    destination_countries: Optional[List[DestinationCountry]] = None
    """List of destination countries for messaging"""

    is_tcr_application: Optional[bool] = None
    """Whether this is a TCR (Campaign Registry) application"""

    notes: Optional[str] = None
    """Additional notes about the business or use case"""

    phone_number_prefix: Optional[str] = None
    """Phone number prefix for messaging (e.g., "+1")"""

    primary_use_case: Optional[str] = None
    """Always null.

    The brand's free-text primary use case is no longer stored: it reached neither
    TCR nor any decision, and its column is dropped with no backfill, because the
    values were prose and the typed equivalent is the campaign's MessagingUseCaseUS.

    Retained so existing v3 clients reading primary_use_case keep deserializing.
    Unlike the profile sharing flags, which can answer false truthfully, there is no
    value to report here — the field is present and empty rather than present and
    wrong.
    """

    vertical: Optional[TcrVertical] = None


class DataBrandContact(BaseModel):
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


class DataBrand(BaseModel):
    """
    Brand response with nested contact, business, and compliance sections — mirrors the request structure.
    """

    id: Optional[str] = None
    """Unique identifier for the brand"""

    business: Optional[DataBrandBusiness] = None
    """Business details and address information"""

    compliance: Optional[DataBrandCompliance] = None
    """Compliance and TCR-related information"""

    contact: Optional[DataBrandContact] = None
    """Contact information for the brand"""

    created_at: Optional[datetime] = None
    """When the brand was created"""

    csp_id: Optional[str] = None
    """Deprecated and scheduled for removal.

    Identifies the Campaign Service Provider that registered the brand, which is
    Sent, so the value is the same for every brand and every account. Nothing on
    your side can act on it and there is no replacement. Stop reading it.
    """

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


class Data(BaseModel):
    """Detailed profile response for v3 API"""

    id: Optional[str] = None
    """Profile unique identifier"""

    allow_contact_sharing: Optional[bool] = None
    """Always false.

    A profile no longer shares contacts with sibling profiles — it sees only what it
    owns. Retained so existing v3 clients reading allow_contact_sharing keep
    deserializing; it carries no information.
    """

    allow_number_change_during_onboarding: Optional[bool] = None
    """Whether number changes are allowed during onboarding"""

    allow_template_sharing: Optional[bool] = None
    """Always false.

    A profile no longer shares templates with sibling profiles. Retained so existing
    v3 clients reading allow_template_sharing keep deserializing; it carries no
    information.
    """

    billing_contact: Optional[DataBillingContact] = None
    """Billing contact info returned in profile responses"""

    billing_model: Optional[str] = None
    """Billing model: profile, organization, or profile_and_organization"""

    brand: Optional[DataBrand] = None
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
    """Always false.

    A profile no longer inherits its organization's contacts. Retained so existing
    v3 clients reading inherit_contacts keep deserializing; it carries no
    information.
    """

    inherit_tcr_brand: Optional[bool] = None
    """Whether this profile inherits TCR brand from the organization"""

    inherit_tcr_campaign: Optional[bool] = None
    """Whether this profile inherits TCR campaign from the organization"""

    inherit_templates: Optional[bool] = None
    """Always false.

    A profile no longer inherits its organization's templates. Retained so existing
    v3 clients reading inherit_templates keep deserializing; it carries no
    information.
    """

    name: Optional[str] = None
    """Profile name"""

    organization_id: Optional[str] = None
    """Parent organization ID"""

    sending_phone_number: Optional[str] = None
    """Direct SMS phone number"""

    sending_phone_number_profile_id: Optional[str] = None
    """Deprecated.

    Always null. Sender borrowing is gone: a profile no longer points at another
    profile for its SMS sender, and every profile owns the sender it sends from.

    Kept on the wire, and never populated, because those are two different promises.
    Removing the key changes the response's shape — a generated client loses the
    property and stops compiling on the next regenerate, for a value that is now
    null for every profile in existence. Keeping it null costs a key and breaks
    nobody, and null is the honest answer rather than a placeholder: there is no
    borrowing left to report.

    Nothing could populate it. Migration 260813161500 dropped the column and copied
    each borrower its own channel-provider row; its Down() says outright that the
    borrower-to-lender pairing is not recoverable. The only surviving trace is a
    notes string on the copied row.
    """

    sending_whatsapp_number_profile_id: Optional[str] = None

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


class ProfileRetrieveResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """Detailed profile response for v3 API"""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
