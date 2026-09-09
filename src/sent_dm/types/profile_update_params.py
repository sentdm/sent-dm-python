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
    """Deprecated.

    Accepted and ignored. Contact and template sharing between sender profiles is
    gone — a profile sees only what it owns, and the organization still sees all of
    its profiles' contacts and templates through read-time widening. The four
    columns behind these flags were dropped by M260720120000.

    Retired the same way as SendingPhoneNumberProfileId, and for the same reason:
    the properties stay bound so an SDK that assigns them keeps compiling, and a 400
    would break a working integration over a capability that is gone regardless.
    Every profile reports all four as false, so a caller that checks its own write
    can see it did not take.
    """

    allow_number_change_during_onboarding: Optional[bool]
    """Whether number changes are allowed during onboarding (optional)"""

    allow_template_sharing: Optional[bool]

    billing_contact: Optional[BillingContactInfoParam]
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

    brand: Optional[BrandsBrandDataParam]
    """Brand and KYC data grouped into contact, business, and compliance sections"""

    description: Optional[str]
    """Profile description (optional)"""

    icon: Optional[str]
    """Profile icon URL (optional)"""

    inherit_contacts: Optional[bool]

    inherit_tcr_brand: Optional[bool]
    """Whether this profile inherits TCR brand from organization (optional)"""

    inherit_tcr_campaign: Optional[bool]
    """Whether this profile inherits TCR campaign from organization (optional)"""

    inherit_templates: Optional[bool]

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
    """Deprecated.

    Accepted and ignored. Sender borrowing is gone: a profile cannot send from
    another profile's SMS number. Supplying this changes nothing and the request
    still succeeds.

    Bound rather than dropped so the property survives on the wire and in a
    generated client — an SDK that assigns it keeps compiling, which is the
    compatibility this exists for. It is deliberately not refused: a 400 here would
    break an integration that is otherwise working, and the capability it asks for
    is gone either way.

    The trade-off, stated plainly. A caller asking for borrowing is told it
    succeeded when nothing happened. What makes that survivable is the read:
    sending_phone_number_profile_id comes back null on every profile, so a caller
    that checks its own write can see it did not take. Every request that carries
    one is logged, so we can tell when nobody is sending it any more and the field
    can go for real.

    Give the profile a sender of its own instead: POST /v3/channels/sms with the
    x-profile-id header naming it.
    """

    sending_whatsapp_number_profile_id: Optional[str]

    short_name: Optional[str]
    """Profile short name/abbreviation (optional).

    Must be 3–11 characters, contain only letters, numbers, and spaces, and include
    at least one letter. Example: "SALES", "Mkt 2", "Support1".
    """

    whatsapp_phone_number: Optional[str]
    """Direct phone number for WhatsApp sending (optional)"""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
