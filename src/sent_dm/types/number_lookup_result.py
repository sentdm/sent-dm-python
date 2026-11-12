# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["NumberLookupResult"]


class NumberLookupResult(BaseModel):
    carrier_name: Optional[str] = None

    country_code: Optional[str] = None

    is_ported: Optional[bool] = None

    is_valid: Optional[bool] = None

    is_voip: Optional[bool] = None

    line_type: Optional[str] = None

    mobile_country_code: Optional[str] = None

    mobile_network_code: Optional[str] = None

    phone_number: Optional[str] = None
