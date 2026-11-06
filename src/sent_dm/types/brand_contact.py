# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BrandContact"]


class BrandContact(BaseModel):
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
