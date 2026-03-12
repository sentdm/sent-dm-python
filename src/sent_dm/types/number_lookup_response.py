# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .api_error import APIError

__all__ = ["NumberLookupResponse", "Data"]


class Data(BaseModel):
    """The response data (null if error)"""

    carrier_name: Optional[str] = None

    country_code: Optional[str] = None

    is_ported: Optional[bool] = None

    is_valid: Optional[bool] = None

    is_voip: Optional[bool] = None

    line_type: Optional[str] = None

    mobile_country_code: Optional[str] = None

    mobile_network_code: Optional[str] = None

    phone_number: Optional[str] = None


class NumberLookupResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The response data (null if error)"""

    error: Optional[APIError] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
