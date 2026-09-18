# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .template_body_content_param import TemplateBodyContentParam

__all__ = ["TemplateBodyParam"]


class TemplateBodyParam(TypedDict, total=False):
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

    multi_channel: Annotated[Optional[TemplateBodyContentParam], PropertyInfo(alias="multiChannel")]
    """The shared body, used for every channel.

    One half of the choice described above.
    """

    rcs: Optional[TemplateBodyContentParam]
    """RCS-specific copy that overrides the chosen strategy for RCS only.

    The one true override: optional on top of either strategy, but it cannot be the
    only body present. Its length cap is the higher one described on Template.
    """

    sms: Optional[TemplateBodyContentParam]
    """The SMS body. It does not override multiChannel, it replaces it."""

    whatsapp: Optional[TemplateBodyContentParam]
    """The WhatsApp body. It does not override multiChannel, it replaces it."""
