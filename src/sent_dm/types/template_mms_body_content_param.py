# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

from .template_media_item_param import TemplateMediaItemParam
from .template_body_content_param import TemplateBodyContentParam

__all__ = ["TemplateMmsBodyContentParam"]


class TemplateMmsBodyContentParam(TemplateBodyContentParam, total=False):
    """
    MMS-specific body content.

    Why MMS needs its own type when the other channels share one: it is the only channel
    with a subject line and the only one with attachments. Every other channel's body is text and
    variables, which is exactly what TemplateBodyContent already is. Putting
    Subject and Media on the shared type instead would give sms, whatsapp and rcs two
    members none of them can ever use.

    Derives from TemplateBodyContent so that every existing consumer of a body slot —
    MessageUtils.ConvertVariableToReadable, TemplateDefinition.GetRequiredVariables,
    TemplateDefinitionValidator.ApplyBodyContentRules — reads it with no change. The two extra
    members are what the MMS strategy and the provider request need on top.
    """

    media: Optional[Iterable[TemplateMediaItemParam]]
    """Attachments carried by every send on this template, in order.

    A per-send media_urls on the request replaces this list rather than adding to
    it, so a template can hold a default creative and a caller can still send
    something recipient-specific.
    """

    subject: Optional[str]
    """MMS subject line.

    Optional — most handsets render it above the body, some ignore it entirely.
    Deliberately its own field rather than riding TemplateHeader: the header is
    authored once and shared across every channel, and carries Meta's 60-character
    cap plus its no-newline, no-emoji text rules, none of which describe an MMS
    subject.
    """
