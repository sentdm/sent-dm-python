# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SentDmServicesCommonContractsPocOsTemplateButtonPropsParam"]


class SentDmServicesCommonContractsPocOsTemplateButtonPropsParam(TypedDict, total=False):
    active_for: Annotated[Optional[int], PropertyInfo(alias="activeFor")]

    autofill_text: Annotated[Optional[str], PropertyInfo(alias="autofillText")]

    country_code: Annotated[Optional[str], PropertyInfo(alias="countryCode")]

    offer_code: Annotated[Optional[str], PropertyInfo(alias="offerCode")]

    otp_type: Annotated[Optional[str], PropertyInfo(alias="otpType")]

    package_name: Annotated[Optional[str], PropertyInfo(alias="packageName")]

    phone_number: Annotated[Optional[str], PropertyInfo(alias="phoneNumber")]

    quick_reply_type: Annotated[Optional[str], PropertyInfo(alias="quickReplyType")]

    signature_hash: Annotated[Optional[str], PropertyInfo(alias="signatureHash")]

    text: Optional[str]

    url: Optional[str]

    url_type: Annotated[Optional[str], PropertyInfo(alias="urlType")]
