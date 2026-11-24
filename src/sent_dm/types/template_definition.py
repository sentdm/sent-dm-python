# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .template_body import TemplateBody
from .template_button import TemplateButton
from .template_footer import TemplateFooter
from .template_header import TemplateHeader
from .authentication_config import AuthenticationConfig

__all__ = ["TemplateDefinition"]


class TemplateDefinition(BaseModel):
    """
    Complete definition of a message template including header, body, footer, and buttons
    """

    body: TemplateBody
    """Body section of a message template.

    A body picks one of two authoring strategies, and mixing them is refused
    (TemplateDefinitionValidator.HaveValidChannelConfiguration): a shared
    multiChannel body on its own, or an explicit sms + whatsapp pair, both present.

    multiChannel together with sms or whatsapp is rejected, and so is sms or
    whatsapp on its own — every template is expected to be deliverable on every
    channel. rcs is the one true override: it may accompany either strategy to vary
    the copy, but cannot stand alone.
    """

    authentication_config: Optional[AuthenticationConfig] = FieldInfo(alias="authenticationConfig", default=None)
    """Configuration for AUTHENTICATION category templates"""

    buttons: Optional[List[TemplateButton]] = None
    """Optional list of interactive buttons (e.g., quick replies, URLs, phone numbers)"""

    definition_version: Optional[str] = FieldInfo(alias="definitionVersion", default=None)
    """The version of the template definition format"""

    footer: Optional[TemplateFooter] = None
    """Footer section of a message template"""

    header: Optional[TemplateHeader] = None
    """Header section of a message template"""
