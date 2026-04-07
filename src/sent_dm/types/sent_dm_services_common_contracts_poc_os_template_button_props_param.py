# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SentDmServicesCommonContractsPocOsTemplateButtonPropsParam"]


class SentDmServicesCommonContractsPocOsTemplateButtonPropsParam(TypedDict, total=False):
    active_for: Required[Annotated[int, PropertyInfo(alias="activeFor")]]

    country_code: Required[Annotated[str, PropertyInfo(alias="countryCode")]]

    offer_code: Required[Annotated[str, PropertyInfo(alias="offerCode")]]

    phone_number: Required[Annotated[str, PropertyInfo(alias="phoneNumber")]]

    quick_reply_type: Required[Annotated[str, PropertyInfo(alias="quickReplyType")]]

    text: Required[str]

    url: Required[str]

    url_type: Required[Annotated[str, PropertyInfo(alias="urlType")]]

    autofill_text: Annotated[Optional[str], PropertyInfo(alias="autofillText")]

    otp_type: Annotated[Optional[str], PropertyInfo(alias="otpType")]

    package_name: Annotated[Optional[str], PropertyInfo(alias="packageName")]

    signature_hash: Annotated[Optional[str], PropertyInfo(alias="signatureHash")]
