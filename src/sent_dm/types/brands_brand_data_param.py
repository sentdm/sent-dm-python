# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .brand_contact_info_param import BrandContactInfoParam
from .brand_business_info_param import BrandBusinessInfoParam
from .brand_compliance_info_param import BrandComplianceInfoParam

__all__ = ["BrandsBrandDataParam"]


class BrandsBrandDataParam(TypedDict, total=False):
    """Brand and KYC data grouped into contact, business, and compliance sections"""

    compliance: Required[BrandComplianceInfoParam]
    """Compliance and TCR information for brand registration"""

    contact: Required[BrandContactInfoParam]
    """Contact information for brand KYC"""

    business: Optional[BrandBusinessInfoParam]
    """Business details and address for brand KYC"""
