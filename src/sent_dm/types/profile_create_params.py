# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .brand_data_param import BrandDataParam

__all__ = ["ProfileCreateParams", "BillingContact", "PaymentDetails", "WhatsappBusinessAccount"]


class ProfileCreateParams(TypedDict, total=False):
    allow_contact_sharing: bool
    """Whether contacts are shared across profiles (default: false)"""

    allow_template_sharing: bool
    """Whether templates are shared across profiles (default: false)"""

    billing_contact: Optional[BillingContact]
    """Billing contact for this profile.

    Required when billing_model is "profile" or "profile_and_organization".
    Identifies who receives invoices and who is responsible for payment.
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

    brand: Optional[BrandDataParam]
    """
    Brand and KYC information for this profile (optional). When provided, creates
    the brand associated with this profile. Cannot be set when inherit_tcr_brand is
    true.
    """

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

    payment_details: Optional[PaymentDetails]
    """
    Payment card details for this profile (optional). Accepted when billing_model is
    "profile" or "profile_and_organization". Not persisted on our servers —
    forwarded to the payment processor.
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
    Direct WhatsApp Business Account credentials for this profile. When provided,
    the profile uses its own WhatsApp Business Account instead of inheriting from
    the organization. When omitted, the profile inherits the organization's WhatsApp
    Business Account (requires the organization to have completed WhatsApp Embedded
    Signup).
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]


class BillingContact(TypedDict, total=False):
    """Billing contact for this profile.

    Required when billing_model is "profile" or "profile_and_organization".
    Identifies who receives invoices and who is responsible for payment.
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


class PaymentDetails(TypedDict, total=False):
    """
    Payment card details for this profile (optional).
    Accepted when billing_model is "profile" or "profile_and_organization".
    Not persisted on our servers — forwarded to the payment processor.
    """

    card_number: Required[str]
    """Card number (digits only, 13–19 characters)"""

    cvc: Required[str]
    """Card security code (3–4 digits)"""

    expiry: Required[str]
    """Card expiry date in MM/YY format (e.g. "09/27")"""

    zip_code: Required[str]
    """Billing ZIP / postal code associated with the card"""


class WhatsappBusinessAccount(TypedDict, total=False):
    """
    Direct WhatsApp Business Account credentials for this profile.
    When provided, the profile uses its own WhatsApp Business Account instead of inheriting from the organization.
    When omitted, the profile inherits the organization's WhatsApp Business Account (requires the organization
    to have completed WhatsApp Embedded Signup).
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
