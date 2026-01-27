# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .template_variable import TemplateVariable
from .template_body_content import TemplateBodyContent

__all__ = ["TemplateDefinition", "Body", "AuthenticationConfig", "Button", "ButtonProps", "Footer", "Header"]


class Body(BaseModel):
    """
    Required template body with content for different channels (multi-channel, SMS-specific, or WhatsApp-specific)
    """

    multi_channel: Optional[TemplateBodyContent] = FieldInfo(alias="multiChannel", default=None)
    """
    Content that will be used for all channels (SMS and WhatsApp) unless
    channel-specific content is provided
    """

    sms: Optional[TemplateBodyContent] = None
    """SMS-specific content that overrides multi-channel content for SMS messages"""

    whatsapp: Optional[TemplateBodyContent] = None
    """
    WhatsApp-specific content that overrides multi-channel content for WhatsApp
    messages
    """


class AuthenticationConfig(BaseModel):
    """Configuration specific to AUTHENTICATION category templates (optional)"""

    add_security_recommendation: Optional[bool] = FieldInfo(alias="addSecurityRecommendation", default=None)
    """
    Whether to add the security recommendation text: "For your security, do not
    share this code."
    """

    code_expiration_minutes: Optional[int] = FieldInfo(alias="codeExpirationMinutes", default=None)
    """Code expiration time in minutes (1-90).

    If set, adds footer: "This code expires in X minutes."
    """


class ButtonProps(BaseModel):
    """Properties specific to the button type"""

    active_for: Optional[int] = FieldInfo(alias="activeFor", default=None)

    autofill_text: Optional[str] = FieldInfo(alias="autofillText", default=None)

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    offer_code: Optional[str] = FieldInfo(alias="offerCode", default=None)

    otp_type: Optional[str] = FieldInfo(alias="otpType", default=None)

    package_name: Optional[str] = FieldInfo(alias="packageName", default=None)

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    quick_reply_type: Optional[str] = FieldInfo(alias="quickReplyType", default=None)

    signature_hash: Optional[str] = FieldInfo(alias="signatureHash", default=None)

    text: Optional[str] = None

    url: Optional[str] = None

    url_type: Optional[str] = FieldInfo(alias="urlType", default=None)


class Button(BaseModel):
    """Interactive button in a message template"""

    id: Optional[int] = None
    """The unique identifier of the button (1-based index)"""

    props: Optional[ButtonProps] = None
    """Properties specific to the button type"""

    type: Optional[str] = None
    """
    The type of button (e.g., QUICK_REPLY, URL, PHONE_NUMBER, VOICE_CALL, COPY_CODE)
    """


class Footer(BaseModel):
    """Optional template footer with optional variables"""

    template: Optional[str] = None
    """The footer template text with optional variable placeholders"""

    type: Optional[str] = None
    """The type of footer (typically "text")"""

    variables: Optional[List[TemplateVariable]] = None
    """List of variables used in the footer template"""


class Header(BaseModel):
    """Optional template header with optional variables"""

    template: Optional[str] = None
    """
    The header template text with optional variable placeholders (e.g., "Welcome to
    {{0:variable}}")
    """

    type: Optional[str] = None
    """The type of header (e.g., "text", "image", "video", "document")"""

    variables: Optional[List[TemplateVariable]] = None
    """List of variables used in the header template"""


class TemplateDefinition(BaseModel):
    """
    Complete definition of a message template including header, body, footer, and buttons
    """

    body: Body
    """
    Required template body with content for different channels (multi-channel,
    SMS-specific, or WhatsApp-specific)
    """

    authentication_config: Optional[AuthenticationConfig] = FieldInfo(alias="authenticationConfig", default=None)
    """Configuration specific to AUTHENTICATION category templates (optional)"""

    buttons: Optional[List[Button]] = None
    """Optional list of interactive buttons (e.g., quick replies, URLs, phone numbers)"""

    definition_version: Optional[str] = FieldInfo(alias="definitionVersion", default=None)
    """The version of the template definition format"""

    footer: Optional[Footer] = None
    """Optional template footer with optional variables"""

    header: Optional[Header] = None
    """Optional template header with optional variables"""
