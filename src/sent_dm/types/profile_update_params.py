# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProfileUpdateParams"]


class ProfileUpdateParams(TypedDict, total=False):
    allow_contact_sharing: Optional[bool]
    """Whether contacts are shared across profiles (optional)"""

    allow_number_change_during_onboarding: Optional[bool]
    """Whether number changes are allowed during onboarding (optional)"""

    allow_template_sharing: Optional[bool]
    """Whether templates are shared across profiles (optional)"""

    billing_model: Optional[str]
    """Billing model: profile, organization, or profile_and_organization (optional)"""

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

    body_profile_id: Annotated[str, PropertyInfo(alias="profile_id")]
    """Profile ID from route parameter"""

    sending_phone_number: Optional[str]
    """Direct phone number for SMS sending (optional)"""

    sending_phone_number_profile_id: Optional[str]
    """Reference to another profile to use for SMS/Telnyx configuration (optional)"""

    sending_whatsapp_number_profile_id: Optional[str]
    """Reference to another profile to use for WhatsApp configuration (optional)"""

    short_name: Optional[str]
    """Profile short name/abbreviation (optional)"""

    test_mode: bool
    """
    Test mode flag - when true, the operation is simulated without side effects
    Useful for testing integrations without actual execution
    """

    whatsapp_phone_number: Optional[str]
    """Direct phone number for WhatsApp sending (optional)"""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
