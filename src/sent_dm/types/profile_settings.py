# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ProfileSettings"]


class ProfileSettings(BaseModel):
    """Profile configuration settings"""

    allow_contact_sharing: Optional[bool] = None
    """Whether contacts are shared across profiles in the organization"""

    allow_template_sharing: Optional[bool] = None
    """Whether templates are shared across profiles in the organization"""

    billing_model: Optional[str] = None
    """Billing model: profile, organization, or profile_and_organization"""

    inherit_contacts: Optional[bool] = None
    """Whether this profile inherits contacts from the organization"""

    inherit_tcr_brand: Optional[bool] = None
    """Whether this profile inherits TCR brand from the organization"""

    inherit_tcr_campaign: Optional[bool] = None
    """Whether this profile inherits TCR campaign from the organization"""

    inherit_templates: Optional[bool] = None
    """Whether this profile inherits templates from the organization"""
