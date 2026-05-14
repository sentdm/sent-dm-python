# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SentDmServicesEndpointsCustomerApIv3ContractsRequestsBrandsBrandContactInfoParam"]


class SentDmServicesEndpointsCustomerApIv3ContractsRequestsBrandsBrandContactInfoParam(TypedDict, total=False):
    """Contact information for brand KYC"""

    name: Required[str]
    """Primary contact name (required)"""

    business_name: Annotated[Optional[str], PropertyInfo(alias="businessName")]
    """Business/brand name"""

    email: Optional[str]
    """Contact email address"""

    phone: Optional[str]
    """Contact phone number in E.164 format"""

    phone_country_code: Annotated[Optional[str], PropertyInfo(alias="phoneCountryCode")]
    """Contact phone country code (e.g., "1" for US)"""

    role: Optional[str]
    """Contact's role in the business"""
