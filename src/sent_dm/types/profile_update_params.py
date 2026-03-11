# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .payment_details_param import PaymentDetailsParam
from .brands_brand_data_param import BrandsBrandDataParam
from .billing_contact_info_param import BillingContactInfoParam

__all__ = ["ProfileUpdateParams"]


class ProfileUpdateParams(TypedDict, total=False):
    allow_contact_sharing: Optional[bool]
    """Whether contacts are shared across profiles (optional)"""

    allow_number_change_during_onboarding: Optional[bool]
    """Whether number changes are allowed during onboarding (optional)"""

    allow_template_sharing: Optional[bool]
    """Whether templates are shared across profiles (optional)"""

    billing_contact: Optional[BillingContactInfoParam]
    """Billing contact for this profile.

    Required when billing_model is "profile" or "profile_and_organization" and no
    billing contact has been configured yet. Identifies who receives invoices and
    who is responsible for payment.
    """

    billing_model: Optional[str]
    """Billing model: profile, organization, or profile_and_organization (optional).

    - "organization": the organization's billing details are used; no profile-level
      billing info needed.
    - "profile": the profile is billed independently; billing_contact is required.
    - "profile_and_organization": the profile is billed first with the organization
      as fallback; billing_contact is required.
    """

    brand: Optional[BrandsBrandDataParam]
    """
    Brand and KYC information for this profile (optional). When provided, creates or
    updates the brand associated with this profile. Cannot be set when
    inherit_tcr_brand is true. Once a brand has been submitted to TCR it cannot be
    modified.
    """

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

    payment_details: Optional[PaymentDetailsParam]
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
