# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "TemplateCreateParams",
    "Definition",
    "DefinitionBody",
    "DefinitionBodyMultiChannel",
    "DefinitionBodyMultiChannelVariable",
    "DefinitionBodyMultiChannelVariableProps",
    "DefinitionBodyRcs",
    "DefinitionBodyRcsVariable",
    "DefinitionBodyRcsVariableProps",
    "DefinitionBodySMS",
    "DefinitionBodySMSVariable",
    "DefinitionBodySMSVariableProps",
    "DefinitionBodyWhatsapp",
    "DefinitionBodyWhatsappVariable",
    "DefinitionBodyWhatsappVariableProps",
    "DefinitionAuthenticationConfig",
    "DefinitionButton",
    "DefinitionButtonProps",
    "DefinitionFooter",
    "DefinitionFooterVariable",
    "DefinitionFooterVariableProps",
    "DefinitionHeader",
    "DefinitionHeaderVariable",
    "DefinitionHeaderVariableProps",
]


class TemplateCreateParams(TypedDict, total=False):
    category: Optional[str]
    """
    Template category: MARKETING, UTILITY, AUTHENTICATION (optional, auto-detected
    if not provided)
    """

    creation_source: Optional[str]
    """Source of template creation (default: from-api)"""

    definition: Definition
    """
    Complete definition of a message template including header, body, footer, and
    buttons
    """

    language: Optional[str]
    """Template language code (e.g., en_US) (optional, auto-detected if not provided)"""

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    submit_for_review: bool
    """Whether to submit the template for review after creation (default: false)"""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]


class DefinitionBodyMultiChannelVariableProps(TypedDict, total=False):
    media_type: Required[Annotated[str, PropertyInfo(alias="mediaType")]]

    sample: Required[str]

    url: Required[str]

    variable_type: Required[Annotated[str, PropertyInfo(alias="variableType")]]

    alt: Optional[str]

    regex: Optional[str]

    short_url: Annotated[Optional[str], PropertyInfo(alias="shortUrl")]


class DefinitionBodyMultiChannelVariable(TypedDict, total=False):
    name: Required[str]

    props: Required[DefinitionBodyMultiChannelVariableProps]

    type: Required[str]

    id: int


class DefinitionBodyMultiChannel(TypedDict, total=False):
    """
    Content that will be used for all channels (SMS and WhatsApp) unless channel-specific content is provided
    """

    template: Required[str]

    type: Optional[str]

    variables: Optional[Iterable[DefinitionBodyMultiChannelVariable]]


class DefinitionBodyRcsVariableProps(TypedDict, total=False):
    media_type: Required[Annotated[str, PropertyInfo(alias="mediaType")]]

    sample: Required[str]

    url: Required[str]

    variable_type: Required[Annotated[str, PropertyInfo(alias="variableType")]]

    alt: Optional[str]

    regex: Optional[str]

    short_url: Annotated[Optional[str], PropertyInfo(alias="shortUrl")]


class DefinitionBodyRcsVariable(TypedDict, total=False):
    name: Required[str]

    props: Required[DefinitionBodyRcsVariableProps]

    type: Required[str]

    id: int


class DefinitionBodyRcs(TypedDict, total=False):
    """RCS-specific content that overrides multi-channel content for RCS messages"""

    template: Required[str]

    type: Optional[str]

    variables: Optional[Iterable[DefinitionBodyRcsVariable]]


class DefinitionBodySMSVariableProps(TypedDict, total=False):
    media_type: Required[Annotated[str, PropertyInfo(alias="mediaType")]]

    sample: Required[str]

    url: Required[str]

    variable_type: Required[Annotated[str, PropertyInfo(alias="variableType")]]

    alt: Optional[str]

    regex: Optional[str]

    short_url: Annotated[Optional[str], PropertyInfo(alias="shortUrl")]


class DefinitionBodySMSVariable(TypedDict, total=False):
    name: Required[str]

    props: Required[DefinitionBodySMSVariableProps]

    type: Required[str]

    id: int


class DefinitionBodySMS(TypedDict, total=False):
    """SMS-specific content that overrides multi-channel content for SMS messages"""

    template: Required[str]

    type: Optional[str]

    variables: Optional[Iterable[DefinitionBodySMSVariable]]


class DefinitionBodyWhatsappVariableProps(TypedDict, total=False):
    media_type: Required[Annotated[str, PropertyInfo(alias="mediaType")]]

    sample: Required[str]

    url: Required[str]

    variable_type: Required[Annotated[str, PropertyInfo(alias="variableType")]]

    alt: Optional[str]

    regex: Optional[str]

    short_url: Annotated[Optional[str], PropertyInfo(alias="shortUrl")]


class DefinitionBodyWhatsappVariable(TypedDict, total=False):
    name: Required[str]

    props: Required[DefinitionBodyWhatsappVariableProps]

    type: Required[str]

    id: int


class DefinitionBodyWhatsapp(TypedDict, total=False):
    """
    WhatsApp-specific content that overrides multi-channel content for WhatsApp messages
    """

    template: Required[str]

    type: Optional[str]

    variables: Optional[Iterable[DefinitionBodyWhatsappVariable]]


class DefinitionBody(TypedDict, total=False):
    """Body section of a message template with channel-specific content"""

    multi_channel: Annotated[Optional[DefinitionBodyMultiChannel], PropertyInfo(alias="multiChannel")]
    """
    Content that will be used for all channels (SMS and WhatsApp) unless
    channel-specific content is provided
    """

    rcs: Optional[DefinitionBodyRcs]
    """RCS-specific content that overrides multi-channel content for RCS messages"""

    sms: Optional[DefinitionBodySMS]
    """SMS-specific content that overrides multi-channel content for SMS messages"""

    whatsapp: Optional[DefinitionBodyWhatsapp]
    """
    WhatsApp-specific content that overrides multi-channel content for WhatsApp
    messages
    """


class DefinitionAuthenticationConfig(TypedDict, total=False):
    """Configuration for AUTHENTICATION category templates"""

    add_security_recommendation: Annotated[bool, PropertyInfo(alias="addSecurityRecommendation")]
    """
    Whether to add the security recommendation text: "For your security, do not
    share this code."
    """

    code_expiration_minutes: Annotated[Optional[int], PropertyInfo(alias="codeExpirationMinutes")]
    """Code expiration time in minutes (1-90).

    If set, adds footer: "This code expires in X minutes."
    """


class DefinitionButtonProps(TypedDict, total=False):
    """Properties specific to the button type"""

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


class DefinitionButton(TypedDict, total=False):
    """Interactive button in a message template"""

    props: Required[DefinitionButtonProps]
    """Properties specific to the button type"""

    type: Required[str]
    """
    The type of button (e.g., QUICK_REPLY, URL, PHONE_NUMBER, VOICE_CALL, COPY_CODE)
    """

    id: int
    """The unique identifier of the button (1-based index)"""


class DefinitionFooterVariableProps(TypedDict, total=False):
    media_type: Required[Annotated[str, PropertyInfo(alias="mediaType")]]

    sample: Required[str]

    url: Required[str]

    variable_type: Required[Annotated[str, PropertyInfo(alias="variableType")]]

    alt: Optional[str]

    regex: Optional[str]

    short_url: Annotated[Optional[str], PropertyInfo(alias="shortUrl")]


class DefinitionFooterVariable(TypedDict, total=False):
    name: Required[str]

    props: Required[DefinitionFooterVariableProps]

    type: Required[str]

    id: int


class DefinitionFooter(TypedDict, total=False):
    """Footer section of a message template"""

    template: Required[str]
    """The footer template text with optional variable placeholders"""

    type: Optional[str]
    """The type of footer (typically "text")"""

    variables: Optional[Iterable[DefinitionFooterVariable]]
    """List of variables used in the footer template"""


class DefinitionHeaderVariableProps(TypedDict, total=False):
    media_type: Required[Annotated[str, PropertyInfo(alias="mediaType")]]

    sample: Required[str]

    url: Required[str]

    variable_type: Required[Annotated[str, PropertyInfo(alias="variableType")]]

    alt: Optional[str]

    regex: Optional[str]

    short_url: Annotated[Optional[str], PropertyInfo(alias="shortUrl")]


class DefinitionHeaderVariable(TypedDict, total=False):
    name: Required[str]

    props: Required[DefinitionHeaderVariableProps]

    type: Required[str]

    id: int


class DefinitionHeader(TypedDict, total=False):
    """Header section of a message template"""

    template: Required[str]
    """
    The header template text with optional variable placeholders (e.g., "Welcome to
    {{0:variable}}")
    """

    type: Optional[str]
    """The type of header (e.g., "text", "image", "video", "document")"""

    variables: Optional[Iterable[DefinitionHeaderVariable]]
    """List of variables used in the header template"""


class Definition(TypedDict, total=False):
    """
    Complete definition of a message template including header, body, footer, and buttons
    """

    body: Required[DefinitionBody]
    """Body section of a message template with channel-specific content"""

    authentication_config: Annotated[
        Optional[DefinitionAuthenticationConfig], PropertyInfo(alias="authenticationConfig")
    ]
    """Configuration for AUTHENTICATION category templates"""

    buttons: Optional[Iterable[DefinitionButton]]
    """Optional list of interactive buttons (e.g., quick replies, URLs, phone numbers)"""

    definition_version: Annotated[Optional[str], PropertyInfo(alias="definitionVersion")]
    """The version of the template definition format"""

    footer: Optional[DefinitionFooter]
    """Footer section of a message template"""

    header: Optional[DefinitionHeader]
    """Header section of a message template"""
