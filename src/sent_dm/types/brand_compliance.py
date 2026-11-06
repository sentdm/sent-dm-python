# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .tcr_vertical import TcrVertical
from .destination_country import DestinationCountry
from .tcr_brand_relationship import TcrBrandRelationship

__all__ = ["BrandCompliance"]


class BrandCompliance(BaseModel):
    brand_relationship: Optional[TcrBrandRelationship] = None

    destination_countries: Optional[List[DestinationCountry]] = None
    """List of destination countries for messaging"""

    is_tcr_application: Optional[bool] = None
    """Whether this is a TCR (Campaign Registry) application"""

    notes: Optional[str] = None
    """Additional notes about the business or use case"""

    phone_number_prefix: Optional[str] = None
    """Phone number prefix for messaging (e.g., "+1")"""

    primary_use_case: Optional[str] = None
    """Always null.

    The brand's free-text primary use case is no longer stored: it reached neither
    TCR nor any decision, and its column is dropped with no backfill, because the
    values were prose and the typed equivalent is the campaign's MessagingUseCaseUS.

    Retained so existing v3 clients reading primary_use_case keep deserializing.
    Unlike the profile sharing flags, which can answer false truthfully, there is no
    value to report here — the field is present and empty rather than present and
    wrong.
    """

    vertical: Optional[TcrVertical] = None
