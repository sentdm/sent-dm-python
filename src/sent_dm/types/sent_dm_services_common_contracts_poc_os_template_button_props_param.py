# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .template_variable_param import TemplateVariableParam

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

    variables: Required[Iterable[TemplateVariableParam]]
    """
    Variables embedded in a dynamic URL button (only when UrlType = dynamic). Count
    is capped by TemplateContentLimits.MaxUrlButtonVariables; the placeholder must
    appear at the end of Url (validated in TemplateDefinitionValidator).
    """

    autofill_text: Annotated[Optional[str], PropertyInfo(alias="autofillText")]

    otp_type: Annotated[Optional[str], PropertyInfo(alias="otpType")]

    package_name: Annotated[Optional[str], PropertyInfo(alias="packageName")]

    signature_hash: Annotated[Optional[str], PropertyInfo(alias="signatureHash")]
