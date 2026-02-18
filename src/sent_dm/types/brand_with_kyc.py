# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tcr_vertical import TcrVertical
from .destination_country import DestinationCountry
from .tcr_brand_relationship import TcrBrandRelationship

__all__ = ["BrandWithKYC"]


class BrandWithKYC(BaseModel):
    """Flattened brand response with embedded KYC information"""

    id: Optional[str] = None
    """Unique identifier for the brand"""

    brand_relationship: Optional[TcrBrandRelationship] = FieldInfo(alias="brandRelationship", default=None)
    """Brand relationship level with TCR"""

    business_legal_name: Optional[str] = FieldInfo(alias="businessLegalName", default=None)
    """Legal business name"""

    business_name: Optional[str] = FieldInfo(alias="businessName", default=None)
    """Business/brand name"""

    business_role: Optional[str] = FieldInfo(alias="businessRole", default=None)
    """Contact's role in the business"""

    business_url: Optional[str] = FieldInfo(alias="businessUrl", default=None)
    """Business website URL"""

    city: Optional[str] = None
    """City"""

    contact_email: Optional[str] = FieldInfo(alias="contactEmail", default=None)
    """Contact email address"""

    contact_name: Optional[str] = FieldInfo(alias="contactName", default=None)
    """Primary contact name"""

    contact_phone: Optional[str] = FieldInfo(alias="contactPhone", default=None)
    """Contact phone number"""

    contact_phone_country_code: Optional[str] = FieldInfo(alias="contactPhoneCountryCode", default=None)
    """Contact phone country code"""

    country: Optional[str] = None
    """Country code"""

    country_of_registration: Optional[str] = FieldInfo(alias="countryOfRegistration", default=None)
    """Country where the business is registered"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """When the brand was created"""

    csp_id: Optional[str] = FieldInfo(alias="cspId", default=None)
    """CSP (Campaign Service Provider) ID"""

    destination_countries: Optional[List[DestinationCountry]] = FieldInfo(alias="destinationCountries", default=None)
    """List of destination countries for messaging"""

    entity_type: Optional[str] = FieldInfo(alias="entityType", default=None)
    """Business entity type"""

    expected_messaging_volume: Optional[str] = FieldInfo(alias="expectedMessagingVolume", default=None)
    """Expected daily messaging volume"""

    identity_status: Optional[Literal["SELF_DECLARED", "UNVERIFIED", "VERIFIED", "VETTED_VERIFIED"]] = FieldInfo(
        alias="identityStatus", default=None
    )
    """TCR brand identity verification status"""

    is_inherited: Optional[bool] = FieldInfo(alias="isInherited", default=None)
    """Whether this brand is inherited from parent organization"""

    is_tcr_application: Optional[bool] = FieldInfo(alias="isTcrApplication", default=None)
    """Whether this is a TCR application"""

    notes: Optional[str] = None
    """Additional notes"""

    phone_number_prefix: Optional[str] = FieldInfo(alias="phoneNumberPrefix", default=None)
    """Phone number prefix for messaging"""

    postal_code: Optional[str] = FieldInfo(alias="postalCode", default=None)
    """Postal/ZIP code"""

    primary_use_case: Optional[str] = FieldInfo(alias="primaryUseCase", default=None)
    """Primary messaging use case description"""

    state: Optional[str] = None
    """State/province code"""

    status: Optional[Literal["ACTIVE", "INACTIVE", "SUSPENDED"]] = None
    """TCR brand status"""

    street: Optional[str] = None
    """Street address"""

    submitted_at: Optional[datetime] = FieldInfo(alias="submittedAt", default=None)
    """When the brand was submitted to TCR"""

    submitted_to_tcr: Optional[bool] = FieldInfo(alias="submittedToTCR", default=None)
    """Whether this brand was submitted to TCR"""

    tax_id: Optional[str] = FieldInfo(alias="taxId", default=None)
    """Tax ID/EIN number"""

    tax_id_type: Optional[str] = FieldInfo(alias="taxIdType", default=None)
    """Type of tax ID"""

    tcr_brand_id: Optional[str] = FieldInfo(alias="tcrBrandId", default=None)
    """TCR brand ID (populated after TCR submission)"""

    universal_ein: Optional[str] = FieldInfo(alias="universalEin", default=None)
    """Universal EIN from TCR"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When the brand was last updated"""

    vertical: Optional[TcrVertical] = None
    """Business vertical/industry category"""
