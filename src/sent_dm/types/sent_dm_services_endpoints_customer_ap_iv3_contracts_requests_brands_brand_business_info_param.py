# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SentDmServicesEndpointsCustomerApIv3ContractsRequestsBrandsBrandBusinessInfoParam"]


class SentDmServicesEndpointsCustomerApIv3ContractsRequestsBrandsBrandBusinessInfoParam(TypedDict, total=False):
    """Business details and address for brand KYC"""

    city: Optional[str]
    """City"""

    country: Optional[str]
    """Country code (e.g., US, CA)"""

    country_of_registration: Annotated[Optional[str], PropertyInfo(alias="countryOfRegistration")]
    """Country where the business is registered"""

    entity_type: Annotated[
        Optional[Literal["PRIVATE_PROFIT", "PUBLIC_PROFIT", "NON_PROFIT", "SOLE_PROPRIETOR", "GOVERNMENT"]],
        PropertyInfo(alias="entityType"),
    ]
    """Business entity type"""

    legal_name: Annotated[Optional[str], PropertyInfo(alias="legalName")]
    """Legal business name"""

    postal_code: Annotated[Optional[str], PropertyInfo(alias="postalCode")]
    """Postal/ZIP code"""

    state: Optional[str]
    """State/province code"""

    street: Optional[str]
    """Street address"""

    tax_id: Annotated[Optional[str], PropertyInfo(alias="taxId")]
    """Tax ID/EIN number"""

    tax_id_type: Annotated[Optional[str], PropertyInfo(alias="taxIdType")]
    """Type of tax ID (e.g., us_ein, ca_bn)"""

    url: Optional[str]
    """Business website URL"""
