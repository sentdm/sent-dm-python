# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .brand_with_kyc import BrandWithKYC
from .billing_contact import BillingContact

__all__ = ["ProfileDetail"]


class ProfileDetail(BaseModel):
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

    billing_contact: Optional[BillingContact] = None
    """Billing contact info returned in profile responses"""

    billing_model: Optional[str] = None
    """Billing model: profile, organization, or profile_and_organization"""

    brand: Optional[BrandWithKYC] = None
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
