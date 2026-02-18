# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .api_meta import APIMeta
from .api_error import APIError

__all__ = ["LookupRetrievePhoneInfoResponse", "Data"]


class Data(BaseModel):
    """The response data (null if error)"""

    carrier_name: Optional[str] = FieldInfo(alias="carrierName", default=None)

    is_ported: Optional[bool] = FieldInfo(alias="isPorted", default=None)

    is_valid: Optional[bool] = FieldInfo(alias="isValid", default=None)

    is_voip: Optional[bool] = FieldInfo(alias="isVoip", default=None)

    line_type: Optional[str] = FieldInfo(alias="lineType", default=None)

    mobile_country_code: Optional[str] = FieldInfo(alias="mobileCountryCode", default=None)

    mobile_network_code: Optional[str] = FieldInfo(alias="mobileNetworkCode", default=None)

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    provider: Optional[str] = None


class LookupRetrievePhoneInfoResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The response data (null if error)"""

    error: Optional[APIError] = None
    """Error details (null if successful)"""

    meta: Optional[APIMeta] = None
    """Metadata about the request and response"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
