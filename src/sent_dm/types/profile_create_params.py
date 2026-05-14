# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .payment_details_param import PaymentDetailsParam
from .brands_brand_data_param import BrandsBrandDataParam
from .billing_contact_info_param import BillingContactInfoParam

__all__ = ["ProfileCreateParams", "WhatsappBusinessAccount"]


class ProfileCreateParams(TypedDict, total=False):
    allow_contact_sharing: bool
    """Whether contacts are shared across profiles (default: false)"""

    allow_template_sharing: bool
    """Whether templates are shared across profiles (default: false)"""

    billing_contact: Optional[BillingContactInfoParam]
    """
    Billing contact information for a profile. Required when billing_model is
    "profile" or "profile_and_organization".
    """

    billing_model: Optional[str]
    """
    Billing model: profile, organization, or profile_and_organization (default:
    profile).

    - "organization": the organization's billing details are used; no profile-level
      billing info needed.
    - "profile": the profile is billed independently; billing_contact is required.
    - "profile_and_organization": the profile is billed first with the organization
      as fallback; billing_contact is required.
    """

    brand: Optional[BrandsBrandDataParam]
    """Brand and KYC data grouped into contact, business, and compliance sections"""

    description: Optional[str]
    """Profile description (optional)"""

    icon: Optional[str]
    """Profile icon URL (optional)"""

    inherit_contacts: Optional[bool]
    """Whether this profile inherits contacts from organization (default: true)"""

    inherit_tcr_brand: Optional[bool]
    """Whether this profile inherits TCR brand from organization (default: true)"""

    inherit_tcr_campaign: Optional[bool]
    """Whether this profile inherits TCR campaign from organization (default: true)"""

    inherit_templates: Optional[bool]
    """Whether this profile inherits templates from organization (default: true)"""

    name: str
    """Profile name (required)"""

    payment_details: Optional[PaymentDetailsParam]
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

    short_name: Optional[str]
    """Profile short name/abbreviation (optional).

    Must be 3–11 characters, contain only letters, numbers, and spaces, and include
    at least one letter. Example: "SALES", "Mkt 2", "Support1".
    """

    whatsapp_business_account: Optional[WhatsappBusinessAccount]
    """
    Direct WhatsApp Business Account credentials for a profile. Use this when the
    profile should have its own WhatsApp Business Account instead of inheriting from
    the organization. Credentials must be obtained from Meta Business Manager by
    creating a System User with whatsapp_business_messaging and
    whatsapp_business_management scopes.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]


class WhatsappBusinessAccount(TypedDict, total=False):
    """
    Direct WhatsApp Business Account credentials for a profile.
    Use this when the profile should have its own WhatsApp Business Account instead of inheriting from the organization.
    Credentials must be obtained from Meta Business Manager by creating a System User with
    whatsapp_business_messaging and whatsapp_business_management scopes.
    """

    access_token: Required[str]
    """
    System User access token with whatsapp_business_messaging and
    whatsapp_business_management permissions. This value is stored securely and
    never returned in API responses.
    """

    waba_id: Required[str]
    """WhatsApp Business Account ID from Meta Business Manager"""

    phone_number_id: Optional[str]
    """
    Phone Number ID of an existing number already registered under this WABA in Meta
    Business Manager. Optional — when omitted, a number will be provisioned from our
    pool and registered in the WABA during the onboarding flow. When provided, the
    number must already exist in the WABA.
    """
