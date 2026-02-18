# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .tcr_vertical import TcrVertical
from .tcr_brand_relationship import TcrBrandRelationship
from .destination_country_param import DestinationCountryParam

__all__ = ["BrandDataParam"]


class BrandDataParam(TypedDict, total=False):
    """Brand and KYC data"""

    brand_relationship: Required[Annotated[TcrBrandRelationship, PropertyInfo(alias="brandRelationship")]]
    """Brand relationship level with TCR (required for TCR)"""

    contact_name: Required[Annotated[str, PropertyInfo(alias="contactName")]]
    """Primary contact name (required)"""

    vertical: Required[TcrVertical]
    """Business vertical/industry category (required for TCR)"""

    brand_name: Annotated[Optional[str], PropertyInfo(alias="brandName")]
    """Brand name for KYC submission"""

    business_legal_name: Annotated[Optional[str], PropertyInfo(alias="businessLegalName")]
    """Legal business name"""

    business_name: Annotated[Optional[str], PropertyInfo(alias="businessName")]
    """Business/brand name"""

    business_role: Annotated[Optional[str], PropertyInfo(alias="businessRole")]
    """Contact's role in the business"""

    business_url: Annotated[Optional[str], PropertyInfo(alias="businessUrl")]
    """Business website URL"""

    city: Optional[str]
    """City"""

    contact_email: Annotated[Optional[str], PropertyInfo(alias="contactEmail")]
    """Contact email address"""

    contact_phone: Annotated[Optional[str], PropertyInfo(alias="contactPhone")]
    """Contact phone number in E.164 format"""

    contact_phone_country_code: Annotated[Optional[str], PropertyInfo(alias="contactPhoneCountryCode")]
    """Contact phone country code (e.g., "1" for US)"""

    country: Optional[str]
    """Country code (e.g., US, CA)"""

    country_of_registration: Annotated[Optional[str], PropertyInfo(alias="countryOfRegistration")]
    """Country where the business is registered"""

    destination_countries: Annotated[
        Optional[Iterable[DestinationCountryParam]], PropertyInfo(alias="destinationCountries")
    ]
    """List of destination countries for messaging"""

    entity_type: Annotated[
        Optional[Literal["PRIVATE_PROFIT", "PUBLIC_PROFIT", "NON_PROFIT", "SOLE_PROPRIETOR", "GOVERNMENT"]],
        PropertyInfo(alias="entityType"),
    ]
    """Business entity type"""

    expected_messaging_volume: Annotated[Optional[str], PropertyInfo(alias="expectedMessagingVolume")]
    """Expected daily messaging volume"""

    is_tcr_application: Annotated[Optional[bool], PropertyInfo(alias="isTcrApplication")]
    """Whether this is a TCR (Campaign Registry) application"""

    notes: Optional[str]
    """Additional notes about the business or use case"""

    phone_number_prefix: Annotated[Optional[str], PropertyInfo(alias="phoneNumberPrefix")]
    """Phone number prefix for messaging (e.g., "+1")"""

    postal_code: Annotated[Optional[str], PropertyInfo(alias="postalCode")]
    """Postal/ZIP code"""

    primary_use_case: Annotated[Optional[str], PropertyInfo(alias="primaryUseCase")]
    """Primary messaging use case description"""

    state: Optional[str]
    """State/province code"""

    street: Optional[str]
    """Street address"""

    tax_id: Annotated[Optional[str], PropertyInfo(alias="taxId")]
    """Tax ID/EIN number"""

    tax_id_type: Annotated[Optional[str], PropertyInfo(alias="taxIdType")]
    """Type of tax ID (e.g., us_ein, ca_bn)"""
