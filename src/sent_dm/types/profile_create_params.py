# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProfileCreateParams"]


class ProfileCreateParams(TypedDict, total=False):
    allow_contact_sharing: bool
    """Whether contacts are shared across profiles (default: false)"""

    allow_template_sharing: bool
    """Whether templates are shared across profiles (default: false)"""

    billing_model: Optional[str]
    """
    Billing model: profile, organization, or profile_and_organization (default:
    profile)
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

    short_name: Optional[str]
    """Profile short name/abbreviation (optional)"""

    test_mode: bool
    """
    Test mode flag - when true, the operation is simulated without side effects
    Useful for testing integrations without actual execution
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
