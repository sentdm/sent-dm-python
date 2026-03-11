# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .sent_dm_services_endpoints_customer_ap_iv3_contracts_requests_brands_brand_contact_info_param import (
    SentDmServicesEndpointsCustomerApIv3ContractsRequestsBrandsBrandContactInfoParam,
)
from .sent_dm_services_endpoints_customer_ap_iv3_contracts_requests_brands_brand_business_info_param import (
    SentDmServicesEndpointsCustomerApIv3ContractsRequestsBrandsBrandBusinessInfoParam,
)
from .sent_dm_services_endpoints_customer_ap_iv3_contracts_requests_brands_brand_compliance_info_param import (
    SentDmServicesEndpointsCustomerApIv3ContractsRequestsBrandsBrandComplianceInfoParam,
)

__all__ = ["BrandsBrandDataParam"]


class BrandsBrandDataParam(TypedDict, total=False):
    """Brand and KYC data grouped into contact, business, and compliance sections"""

    compliance: Required[SentDmServicesEndpointsCustomerApIv3ContractsRequestsBrandsBrandComplianceInfoParam]
    """Compliance and TCR-related information"""

    contact: Required[SentDmServicesEndpointsCustomerApIv3ContractsRequestsBrandsBrandContactInfoParam]
    """Contact information for the brand"""

    business: Optional[SentDmServicesEndpointsCustomerApIv3ContractsRequestsBrandsBrandBusinessInfoParam]
    """Business details and address information"""
