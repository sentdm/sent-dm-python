# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ProfileUpdateParams",
    "BillingContact",
    "Brand",
    "BrandCompliance",
    "BrandComplianceDestinationCountry",
    "BrandContact",
    "BrandBusiness",
    "PaymentDetails",
]


class ProfileUpdateParams(TypedDict, total=False):
    allow_contact_sharing: Optional[bool]
    """Whether contacts are shared across profiles (optional)"""

    allow_number_change_during_onboarding: Optional[bool]
    """Whether number changes are allowed during onboarding (optional)"""

    allow_template_sharing: Optional[bool]
    """Whether templates are shared across profiles (optional)"""

    billing_contact: Optional[BillingContact]
    """
    Billing contact information for a profile. Required when billing_model is
    "profile" or "profile_and_organization".
    """

    billing_model: Optional[str]
    """Billing model: profile, organization, or profile_and_organization (optional).

    - "organization": the organization's billing details are used; no profile-level
      billing info needed.
    - "profile": the profile is billed independently; billing_contact is required.
    - "profile_and_organization": the profile is billed first with the organization
      as fallback; billing_contact is required.
    """

    brand: Optional[Brand]
    """Brand and KYC data grouped into contact, business, and compliance sections"""

    description: Optional[str]
    """Profile description (optional)"""

    icon: Optional[str]
    """Profile icon URL (optional)"""

    inherit_contacts: Optional[bool]
    """Whether this profile inherits contacts from organization (optional)"""

    inherit_tcr_brand: Optional[bool]
    """Whether this profile inherits TCR brand from organization (optional)"""

    inherit_tcr_campaign: Optional[bool]
    """Whether this profile inherits TCR campaign from organization (optional)"""

    inherit_templates: Optional[bool]
    """Whether this profile inherits templates from organization (optional)"""

    name: Optional[str]
    """Profile name (optional)"""

    payment_details: Optional[PaymentDetails]
    """
    Payment card details for a profile. Accepted when billing_model is "profile" or
    "profile_and_organization". These details are not stored on our servers and will
    be forwarded to the payment processor.
    """

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    sending_phone_number: Optional[str]
    """Direct phone number for SMS sending (optional)"""

    sending_phone_number_profile_id: Optional[str]
    """Reference to another profile to use for SMS/Telnyx configuration (optional)"""

    sending_whatsapp_number_profile_id: Optional[str]
    """Reference to another profile to use for WhatsApp configuration (optional)"""

    short_name: Optional[str]
    """Profile short name/abbreviation (optional).

    Must be 3–11 characters, contain only letters, numbers, and spaces, and include
    at least one letter. Example: "SALES", "Mkt 2", "Support1".
    """

    whatsapp_phone_number: Optional[str]
    """Direct phone number for WhatsApp sending (optional)"""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]


class BillingContact(TypedDict, total=False):
    """
    Billing contact information for a profile.
    Required when billing_model is "profile" or "profile_and_organization".
    """

    email: Required[str]
    """Email address where invoices will be sent (required)"""

    name: Required[str]
    """Full name of the billing contact or company (required)"""

    address: Optional[str]
    """Billing address (optional).

    Free-form text including street, city, state, postal code, and country.
    """

    phone: Optional[str]
    """Phone number for the billing contact (optional)"""


class BrandComplianceDestinationCountry(TypedDict, total=False):
    id: str

    is_main: Annotated[bool, PropertyInfo(alias="isMain")]


class BrandCompliance(TypedDict, total=False):
    """Compliance and TCR information for brand registration"""

    brand_relationship: Required[
        Annotated[
            Literal["BASIC_ACCOUNT", "MEDIUM_ACCOUNT", "LARGE_ACCOUNT", "SMALL_ACCOUNT", "KEY_ACCOUNT"],
            PropertyInfo(alias="brandRelationship"),
        ]
    ]

    vertical: Required[
        Literal[
            "PROFESSIONAL",
            "REAL_ESTATE",
            "HEALTHCARE",
            "HUMAN_RESOURCES",
            "ENERGY",
            "ENTERTAINMENT",
            "RETAIL",
            "TRANSPORTATION",
            "AGRICULTURE",
            "INSURANCE",
            "POSTAL",
            "EDUCATION",
            "HOSPITALITY",
            "FINANCIAL",
            "POLITICAL",
            "GAMBLING",
            "LEGAL",
            "CONSTRUCTION",
            "NGO",
            "MANUFACTURING",
            "GOVERNMENT",
            "TECHNOLOGY",
            "COMMUNICATION",
        ]
    ]

    destination_countries: Annotated[
        Optional[Iterable[BrandComplianceDestinationCountry]], PropertyInfo(alias="destinationCountries")
    ]
    """List of destination countries for messaging"""

    expected_messaging_volume: Annotated[Optional[str], PropertyInfo(alias="expectedMessagingVolume")]
    """Expected daily messaging volume"""

    is_tcr_application: Annotated[Optional[bool], PropertyInfo(alias="isTcrApplication")]
    """Whether this is a TCR (Campaign Registry) application"""

    notes: Optional[str]
    """Additional notes about the business or use case"""

    phone_number_prefix: Annotated[Optional[str], PropertyInfo(alias="phoneNumberPrefix")]
    """Phone number prefix for messaging (e.g., "+1")"""

    primary_use_case: Annotated[Optional[str], PropertyInfo(alias="primaryUseCase")]
    """Primary messaging use case description"""


class BrandContact(TypedDict, total=False):
    """Contact information for brand KYC"""

    name: Required[str]
    """Primary contact name (required)"""

    business_name: Annotated[Optional[str], PropertyInfo(alias="businessName")]
    """Business/brand name"""

    email: Optional[str]
    """Contact email address"""

    phone: Optional[str]
    """Contact phone number in E.164 format"""

    phone_country_code: Annotated[Optional[str], PropertyInfo(alias="phoneCountryCode")]
    """Contact phone country code (e.g., "1" for US)"""

    role: Optional[str]
    """Contact's role in the business"""


class BrandBusiness(TypedDict, total=False):
    """Business details and address for brand KYC"""

    city: Optional[str]
    """City"""

    country: Optional[str]
    """Country code (e.g., US, CA)"""

    country_of_registration: Annotated[Optional[str], PropertyInfo(alias="countryOfRegistration")]
    """Country where the business is registered"""

    entity_type: Annotated[
        Optional[Literal["PRIVATE_PROFIT", "PUBLIC_PROFIT", "NON_PROFIT", "SOLE_PROPRIETOR", "GOVERNMENT"]],
        PropertyInfo(alias="entityType"),
    ]

    legal_name: Annotated[Optional[str], PropertyInfo(alias="legalName")]
    """Legal business name"""

    postal_code: Annotated[Optional[str], PropertyInfo(alias="postalCode")]
    """Postal/ZIP code"""

    state: Optional[str]
    """State/province code"""

    street: Optional[str]
    """Street address"""

    tax_id: Annotated[Optional[str], PropertyInfo(alias="taxId")]
    """Tax ID/EIN number"""

    tax_id_type: Annotated[Optional[str], PropertyInfo(alias="taxIdType")]
    """Type of tax ID (e.g., us_ein, ca_bn)"""

    url: Optional[str]
    """Business website URL"""


class Brand(TypedDict, total=False):
    """Brand and KYC data grouped into contact, business, and compliance sections"""

    compliance: Required[BrandCompliance]
    """Compliance and TCR information for brand registration"""

    contact: Required[BrandContact]
    """Contact information for brand KYC"""

    business: Optional[BrandBusiness]
    """Business details and address for brand KYC"""


class PaymentDetails(TypedDict, total=False):
    """
    Payment card details for a profile.
    Accepted when billing_model is "profile" or "profile_and_organization".
    These details are not stored on our servers and will be forwarded to the payment processor.
    """

    card_number: Required[str]
    """Card number (digits only, 13–19 characters)"""

    cvc: Required[str]
    """Card security code (3–4 digits)"""

    expiry: Required[str]
    """Card expiry date in MM/YY format (e.g. "09/27")"""

    zip_code: Required[str]
    """Billing ZIP / postal code associated with the card"""
