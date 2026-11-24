# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .template_body_content import TemplateBodyContent
from .template_mms_body_content import TemplateMmsBodyContent

__all__ = ["TemplateBody"]


class TemplateBody(BaseModel):
    """
    Body section of a message template.

    A body picks one of two authoring strategies, and mixing them is refused
    (TemplateDefinitionValidator.HaveValidChannelConfiguration):
    a shared multiChannel body on its own, or
    an explicit sms + whatsapp pair, both present.

    multiChannel together with sms or whatsapp is rejected, and so is
    sms or whatsapp on its own — every template is expected to be deliverable on every
    channel. rcs is the one true override: it may accompany either strategy to vary the copy,
    but cannot stand alone.
    """

    mms: Optional[TemplateMmsBodyContent] = None
    """MMS-specific content — subject, text and attachments.

    Like Rcs, an override that cannot stand on its own: a template still needs a
    MultiChannel body or the Sms + Whatsapp pair to be deliverable at all. Without
    this slot MMS renders the shared or SMS body, so it is only needed for
    MMS-specific copy, a subject or attachments. When present it replaces that body
    on MMS rather than adding to it.
    """

    multi_channel: Optional[TemplateBodyContent] = FieldInfo(alias="multiChannel", default=None)
    """The shared body, used for every channel.

    One half of the choice described above.
    """

    rcs: Optional[TemplateBodyContent] = None
    """RCS-specific copy that overrides the chosen strategy for RCS only.

    The one true override: optional on top of either strategy, but it cannot be the
    only body present. Its length cap is the higher one described on Template.
    """

    sms: Optional[TemplateBodyContent] = None
    """The SMS body. It does not override multiChannel, it replaces it."""

    whatsapp: Optional[TemplateBodyContent] = None
    """The WhatsApp body. It does not override multiChannel, it replaces it."""
