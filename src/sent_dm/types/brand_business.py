# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BrandBusiness"]


class BrandBusiness(BaseModel):
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
