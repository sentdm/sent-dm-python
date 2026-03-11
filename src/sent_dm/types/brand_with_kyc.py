# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .tcr_vertical import TcrVertical
from .destination_country import DestinationCountry
from .tcr_brand_relationship import TcrBrandRelationship

__all__ = ["BrandWithKYC", "Business", "Compliance", "Contact"]


class Business(BaseModel):
    """Business details and address information"""

    city: Optional[str] = None
    """City"""

    country: Optional[str] = None
    """Country code (e.g., US, CA)"""

    country_of_registration: Optional[str] = None
    """Country where the business is registered"""

    entity_type: Optional[str] = None
    """Business entity type"""

    legal_name: Optional[str] = None
    """Legal business name"""

    postal_code: Optional[str] = None
    """Postal/ZIP code"""

    state: Optional[str] = None
    """State/province code"""

    street: Optional[str] = None
    """Street address"""

    tax_id: Optional[str] = None
    """Tax ID/EIN number"""

    tax_id_type: Optional[str] = None
    """Type of tax ID (e.g., us_ein, ca_bn)"""

    url: Optional[str] = None
    """Business website URL"""


class Compliance(BaseModel):
    """Compliance and TCR-related information"""

    brand_relationship: Optional[TcrBrandRelationship] = None
    """Brand relationship level with TCR"""

    destination_countries: Optional[List[DestinationCountry]] = None
    """List of destination countries for messaging"""

    expected_messaging_volume: Optional[str] = None
    """Expected daily messaging volume"""

    is_tcr_application: Optional[bool] = None
    """Whether this is a TCR (Campaign Registry) application"""

    notes: Optional[str] = None
    """Additional notes about the business or use case"""

    phone_number_prefix: Optional[str] = None
    """Phone number prefix for messaging (e.g., "+1")"""

    primary_use_case: Optional[str] = None
    """Primary messaging use case description"""

    vertical: Optional[TcrVertical] = None
    """Business vertical/industry category"""


class Contact(BaseModel):
    """Contact information for the brand"""

    business_name: Optional[str] = None
    """Business/brand name"""

    email: Optional[str] = None
    """Contact email address"""

    name: Optional[str] = None
    """Primary contact name"""

    phone: Optional[str] = None
    """Contact phone number in E.164 format"""

    phone_country_code: Optional[str] = None
    """Contact phone country code (e.g., "1" for US)"""

    role: Optional[str] = None
    """Contact's role in the business"""


class BrandWithKYC(BaseModel):
    """
    Brand response with nested contact, business, and compliance sections — mirrors the request structure.
    """

    id: Optional[str] = None
    """Unique identifier for the brand"""

    business: Optional[Business] = None
    """Business details and address information"""

    compliance: Optional[Compliance] = None
    """Compliance and TCR-related information"""

    contact: Optional[Contact] = None
    """Contact information for the brand"""

    created_at: Optional[datetime] = None
    """When the brand was created"""

    csp_id: Optional[str] = None
    """CSP (Campaign Service Provider) ID"""

    identity_status: Optional[Literal["SELF_DECLARED", "UNVERIFIED", "VERIFIED", "VETTED_VERIFIED"]] = None
    """TCR brand identity verification status"""

    is_inherited: Optional[bool] = None
    """Whether this brand is inherited from the parent organization"""

    status: Optional[Literal["ACTIVE", "INACTIVE", "SUSPENDED"]] = None
    """TCR brand status"""

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
