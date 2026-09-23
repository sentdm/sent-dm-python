# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .template_body_content_param import TemplateBodyContentParam

__all__ = ["TemplateBodyParam", "Mms", "MmsMedia"]


class MmsMedia(TypedDict, total=False):
    """One attachment on an MMS template body."""

    media_type: Annotated[Optional[str], PropertyInfo(alias="mediaType")]
    """One of MmsMediaTypes.

    Advisory: the carrier reads the Content-Type off the fetched object, not this
    field. It exists so an authoring UI can render the right preview and so a
    reviewer can see what was intended.
    """

    url: str
    """Publicly fetchable https URL.

    The carrier's MMSC fetches this at send time, so it has to stay reachable and
    unauthenticated for the life of the send — including retries and a DLQ replay —
    which is why a presigned URL is not a valid value here.
    """


class Mms(TemplateBodyContentParam, total=False):
    """
    MMS-specific content — subject, text and attachments.

    Like Rcs, an override that cannot stand on its own: a template still needs a
    MultiChannel body or the Sms + Whatsapp pair to be
    deliverable at all. Unlike Rcs, it has no fallback at send time — MMS with no
    media is a more expensive SMS, so a template without this slot is deliberately not MMS-capable
    and never produces an MMS route candidate.
    """

    media: Optional[Iterable[MmsMedia]]
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

    mms: Optional[Mms]
    """MMS-specific content — subject, text and attachments.

    Like Rcs, an override that cannot stand on its own: a template still needs a
    MultiChannel body or the Sms + Whatsapp pair to be deliverable at all. Unlike
    Rcs, it has no fallback at send time — MMS with no media is a more expensive
    SMS, so a template without this slot is deliberately not MMS-capable and never
    produces an MMS route candidate.
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
