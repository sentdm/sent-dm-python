# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ProfileSettings"]


class ProfileSettings(BaseModel):
    """Profile configuration settings"""

    allow_contact_sharing: Optional[bool] = None
    """Always false.

    A profile no longer shares contacts with sibling profiles — it sees only what it
    owns. Retained so existing v3 clients reading allow_contact_sharing keep
    deserializing; it carries no information.
    """

    allow_template_sharing: Optional[bool] = None
    """Always false.

    A profile no longer shares templates with sibling profiles. Retained so existing
    v3 clients reading allow_template_sharing keep deserializing; it carries no
    information.
    """

    billing_model: Optional[str] = None
    """Billing model: profile, organization, or profile_and_organization"""

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
