# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .template_variable import TemplateVariable

__all__ = ["TemplateButtonProps"]


class TemplateButtonProps(BaseModel):
    active_for: int = FieldInfo(alias="activeFor")

    country_code: str = FieldInfo(alias="countryCode")

    offer_code: str = FieldInfo(alias="offerCode")

    phone_number: str = FieldInfo(alias="phoneNumber")

    quick_reply_type: str = FieldInfo(alias="quickReplyType")

    text: str
    """The button's label.

    Required for every button type, and capped at
    TemplateContentLimits.MaxButtonTextLength (25) characters.

    Meta accepts only static text here, so a label is refused when it contains a
    {{...}} variable placeholder, a newline, an emoji, or WhatsApp formatting markup
    (\\**, \\__, ~) — enforced by ApplyButtonLabelContentRules in
    TemplateButtonValidator. Meta reports all four as one error: "Buttons can't have
    any variables, newlines, emojis, or formatting characters."

    AUTHENTICATION OTP buttons are the exception: Meta auto-localizes their label
    from the template language, and the converter drops whatever text was sent.
    """

    url: str

    url_type: str = FieldInfo(alias="urlType")

    variables: List[TemplateVariable]
    """
    Variables embedded in a dynamic URL button (only when UrlType = dynamic). Count
    is capped by TemplateContentLimits.MaxUrlButtonVariables; the placeholder must
    appear at the end of Url (validated in TemplateDefinitionValidator).
    """

    autofill_text: Optional[str] = FieldInfo(alias="autofillText", default=None)

    otp_type: Optional[str] = FieldInfo(alias="otpType", default=None)

    package_name: Optional[str] = FieldInfo(alias="packageName", default=None)

    signature_hash: Optional[str] = FieldInfo(alias="signatureHash", default=None)
