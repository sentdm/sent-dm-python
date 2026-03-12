# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .tcr_vertical import TcrVertical
from .tcr_brand_relationship import TcrBrandRelationship
from .destination_country_param import DestinationCountryParam

__all__ = ["SentDmServicesEndpointsCustomerApIv3ContractsRequestsBrandsBrandComplianceInfoParam"]


class SentDmServicesEndpointsCustomerApIv3ContractsRequestsBrandsBrandComplianceInfoParam(TypedDict, total=False):
    """Compliance and TCR information for brand registration"""

    brand_relationship: Required[Annotated[TcrBrandRelationship, PropertyInfo(alias="brandRelationship")]]

    vertical: Required[TcrVertical]

    destination_countries: Annotated[
        Optional[Iterable[DestinationCountryParam]], PropertyInfo(alias="destinationCountries")
    ]
    """List of destination countries for messaging"""

    expected_messaging_volume: Annotated[Optional[str], PropertyInfo(alias="expectedMessagingVolume")]
    """Expected daily messaging volume"""

    is_tcr_application: Annotated[Optional[bool], PropertyInfo(alias="isTcrApplication")]
    """Whether this is a TCR (Campaign Registry) application"""

    notes: Optional[str]
    """Additional notes about the business or use case"""

    phone_number_prefix: Annotated[Optional[str], PropertyInfo(alias="phoneNumberPrefix")]
    """Phone number prefix for messaging (e.g., "+1")"""

    primary_use_case: Annotated[Optional[str], PropertyInfo(alias="primaryUseCase")]
    """Primary messaging use case description"""
