# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .tcr_vertical import TcrVertical
from .tcr_brand_relationship import TcrBrandRelationship
from .destination_country_param import DestinationCountryParam

__all__ = ["BrandDataParam", "Compliance", "Contact", "Business"]


class Compliance(TypedDict, total=False):
    """Compliance and TCR-related information"""

    brand_relationship: Required[Annotated[TcrBrandRelationship, PropertyInfo(alias="brandRelationship")]]
    """Brand relationship level with TCR (required for TCR)"""

    vertical: Required[TcrVertical]
    """Business vertical/industry category (required for TCR)"""

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


class Contact(TypedDict, total=False):
    """Contact information for the brand"""

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


class Business(TypedDict, total=False):
    """Business details and address information"""

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


class BrandDataParam(TypedDict, total=False):
    """Brand and KYC data grouped into contact, business, and compliance sections"""

    compliance: Required[Compliance]
    """Compliance and TCR-related information"""

    contact: Required[Contact]
    """Contact information for the brand"""

    business: Optional[Business]
    """Business details and address information"""
