# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .template_body_param import TemplateBodyParam
from .template_button_param import TemplateButtonParam
from .template_footer_param import TemplateFooterParam
from .template_header_param import TemplateHeaderParam
from .authentication_config_param import AuthenticationConfigParam

__all__ = ["TemplateDefinitionParam"]


class TemplateDefinitionParam(TypedDict, total=False):
    """
    Complete definition of a message template including header, body, footer, and buttons
    """

    body: Required[TemplateBodyParam]
    """Body section of a message template.

    A body picks one of two authoring strategies, and mixing them is refused
    (TemplateDefinitionValidator.HaveValidChannelConfiguration): a shared
    multiChannel body on its own, or an explicit sms + whatsapp pair, both present.

    multiChannel together with sms or whatsapp is rejected, and so is sms or
    whatsapp on its own — every template is expected to be deliverable on every
    channel. rcs is the one true override: it may accompany either strategy to vary
    the copy, but cannot stand alone.
    """

    authentication_config: Annotated[Optional[AuthenticationConfigParam], PropertyInfo(alias="authenticationConfig")]
    """Configuration for AUTHENTICATION category templates"""

    buttons: Optional[Iterable[TemplateButtonParam]]
    """Optional list of interactive buttons (e.g., quick replies, URLs, phone numbers)"""

    definition_version: Annotated[Optional[str], PropertyInfo(alias="definitionVersion")]
    """The version of the template definition format"""

    footer: Optional[TemplateFooterParam]
    """Footer section of a message template"""

    header: Optional[TemplateHeaderParam]
    """Header section of a message template"""
