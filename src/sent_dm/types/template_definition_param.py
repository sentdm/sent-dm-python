# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .template_variable_param import TemplateVariableParam
from .template_body_content_param import TemplateBodyContentParam

__all__ = ["TemplateDefinitionParam", "Body", "AuthenticationConfig", "Button", "ButtonProps", "Footer", "Header"]


class Body(TypedDict, total=False):
    """
    Required template body with content for different channels (multi-channel, SMS-specific, or WhatsApp-specific)
    """

    multi_channel: Annotated[Optional[TemplateBodyContentParam], PropertyInfo(alias="multiChannel")]
    """
    Content that will be used for all channels (SMS and WhatsApp) unless
    channel-specific content is provided
    """

    sms: Optional[TemplateBodyContentParam]
    """SMS-specific content that overrides multi-channel content for SMS messages"""

    whatsapp: Optional[TemplateBodyContentParam]
    """
    WhatsApp-specific content that overrides multi-channel content for WhatsApp
    messages
    """


class AuthenticationConfig(TypedDict, total=False):
    """Configuration specific to AUTHENTICATION category templates (optional)"""

    add_security_recommendation: Annotated[bool, PropertyInfo(alias="addSecurityRecommendation")]
    """
    Whether to add the security recommendation text: "For your security, do not
    share this code."
    """

    code_expiration_minutes: Annotated[Optional[int], PropertyInfo(alias="codeExpirationMinutes")]
    """Code expiration time in minutes (1-90).

    If set, adds footer: "This code expires in X minutes."
    """


class ButtonProps(TypedDict, total=False):
    """Properties specific to the button type"""

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


class Button(TypedDict, total=False):
    """Interactive button in a message template"""

    id: int
    """The unique identifier of the button (1-based index)"""

    props: ButtonProps
    """Properties specific to the button type"""

    type: str
    """
    The type of button (e.g., QUICK_REPLY, URL, PHONE_NUMBER, VOICE_CALL, COPY_CODE)
    """


class Footer(TypedDict, total=False):
    """Optional template footer with optional variables"""

    template: str
    """The footer template text with optional variable placeholders"""

    type: Optional[str]
    """The type of footer (typically "text")"""

    variables: Optional[Iterable[TemplateVariableParam]]
    """List of variables used in the footer template"""


class Header(TypedDict, total=False):
    """Optional template header with optional variables"""

    template: str
    """
    The header template text with optional variable placeholders (e.g., "Welcome to
    {{0:variable}}")
    """

    type: Optional[str]
    """The type of header (e.g., "text", "image", "video", "document")"""

    variables: Optional[Iterable[TemplateVariableParam]]
    """List of variables used in the header template"""


class TemplateDefinitionParam(TypedDict, total=False):
    """
    Complete definition of a message template including header, body, footer, and buttons
    """

    body: Required[Body]
    """
    Required template body with content for different channels (multi-channel,
    SMS-specific, or WhatsApp-specific)
    """

    authentication_config: Annotated[Optional[AuthenticationConfig], PropertyInfo(alias="authenticationConfig")]
    """Configuration specific to AUTHENTICATION category templates (optional)"""

    buttons: Optional[Iterable[Button]]
    """Optional list of interactive buttons (e.g., quick replies, URLs, phone numbers)"""

    definition_version: Annotated[Optional[str], PropertyInfo(alias="definitionVersion")]
    """The version of the template definition format"""

    footer: Optional[Footer]
    """Optional template footer with optional variables"""

    header: Optional[Header]
    """Optional template header with optional variables"""
