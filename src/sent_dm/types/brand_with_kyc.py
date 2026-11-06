# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .brand_contact import BrandContact
from .brand_business import BrandBusiness
from .brand_compliance import BrandCompliance
from .tcr_brand_status import TcrBrandStatus
from .tcr_brand_identity_status import TcrBrandIdentityStatus

__all__ = ["BrandWithKYC"]


class BrandWithKYC(BaseModel):
    """
    Brand response with nested contact, business, and compliance sections — mirrors the request structure.
    """

    id: Optional[str] = None
    """Unique identifier for the brand"""

    business: Optional[BrandBusiness] = None
    """Business details and address information"""

    compliance: Optional[BrandCompliance] = None
    """Compliance and TCR-related information"""

    contact: Optional[BrandContact] = None
    """Contact information for the brand"""

    created_at: Optional[datetime] = None
    """When the brand was created"""

    csp_id: Optional[str] = None
    """Deprecated and scheduled for removal.

    Identifies the Campaign Service Provider that registered the brand, which is
    Sent, so the value is the same for every brand and every account. Nothing on
    your side can act on it and there is no replacement. Stop reading it.
    """

    identity_status: Optional[TcrBrandIdentityStatus] = None

    is_inherited: Optional[bool] = None
    """Whether this brand is inherited from the parent organization"""

    status: Optional[TcrBrandStatus] = None

    submitted_at: Optional[datetime] = None
    """When the brand was submitted to TCR"""

    submitted_to_tcr: Optional[bool] = None
    """Whether this brand has been submitted to TCR"""

    tcr_brand_id: Optional[str] = None
    """TCR brand ID (populated after TCR submission)"""

    universal_ein: Optional[str] = None
    """Universal EIN from TCR"""

    updated_at: Optional[datetime] = None
    """When the brand was last updated"""
