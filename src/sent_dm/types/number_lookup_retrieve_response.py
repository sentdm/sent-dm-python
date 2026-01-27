# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["NumberLookupRetrieveResponse"]


class NumberLookupRetrieveResponse(BaseModel):
    """Response containing phone number lookup data"""

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)
    """The country calling code (e.g., 1 for US/Canada)"""

    format_e164: Optional[str] = FieldInfo(alias="formatE164", default=None)
    """The phone number formatted in E.164 standard (e.g., +1234567890)"""

    format_international: Optional[str] = FieldInfo(alias="formatInternational", default=None)
    """The phone number formatted for international dialing (e.g., +1 234-567-890)"""

    format_national: Optional[str] = FieldInfo(alias="formatNational", default=None)
    """The phone number formatted for national dialing (e.g., (234) 567-890)"""

    format_rfc: Optional[str] = FieldInfo(alias="formatRfc", default=None)
    """The phone number formatted according to RFC 3966 (e.g., tel:+1-234-567-890)"""

    number_type: Optional[str] = FieldInfo(alias="numberType", default=None)
    """The type of phone number (e.g., mobile, fixed_line, voip)"""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """The phone number in its original format"""

    phone_timezones: Optional[str] = FieldInfo(alias="phoneTimezones", default=None)
    """The timezones associated with the phone number"""

    region_code: Optional[str] = FieldInfo(alias="regionCode", default=None)
    """The ISO 3166-1 alpha-2 country code (e.g., US, CA, GB)"""
