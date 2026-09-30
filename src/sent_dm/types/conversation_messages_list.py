# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = [
    "ConversationMessagesList",
    "Message",
    "MessageEvent",
    "MessageMessageBody",
    "MessageMessageBodyButton",
    "MessageMessageBodyHeaderMedia",
    "MessageMessageBodyMedia",
]


class MessageEvent(BaseModel):
    """Represents a status change event in a message's lifecycle (v3)"""

    status: str

    timestamp: datetime

    description: Optional[str] = None

    reason: Optional[str] = None
    """A human-readable sentence for reason_code. Omitted whenever reason_code is."""

    reason_code: Optional[str] = None
    """
    Why the message reached this status, as a stable platform code such as
    DELIVERY_007. Present on FAILED, FILTERED and BLOCKED events; omitted on every
    status that needs no explanation. Same wire name and vocabulary as on the
    activities list and the webhook.
    """


class MessageMessageBodyButton(BaseModel):
    postback_data: Optional[str] = FieldInfo(alias="postbackData", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    value: Optional[str] = None


class MessageMessageBodyHeaderMedia(BaseModel):
    """The media asset that rode a message's header, recorded as sent."""

    type: Optional[str] = None
    """\"image", "video" or "document" — taken from the header's media variable."""

    url: Optional[str] = None
    """The https URL the caller supplied for this send.

    Never the template's stored props.sample, which is Meta's expiring header_handle
    rather than what was delivered.
    """


class MessageMessageBodyMedia(BaseModel):
    """
    One attachment on a message, in either direction — and in both, a URL somebody else hosts.

    Outbound: the customer supplied a public URL and we handed it to the carrier.
    Inbound: the carrier hosts the file and we record where. sent.dm never holds the bytes, so
    there is no key, no expiry bookkeeping and nothing minted per read — what is stored is what is
    served.

    An inbound link expires on the carrier's own schedule and is unauthenticated. That is the
    customer's to manage, and it is documented where they will see it rather than only here — a
    recipient who needs an attachment to outlive that window copies it on receipt.

    Storing a presigned URL is the specific mistake this shape still avoids:
    M260826130000 and M260826140000 exist because RCS assets were stored as signed URLs
    and went stale. Nothing here is signed.
    """

    media_type: Optional[str] = FieldInfo(alias="mediaType", default=None)
    """One of MmsMediaTypes when the content type is known.

    Advisory — a reader should trust the fetched object's own Content-Type.
    """

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)
    """Content type as the provider declared it. Null when it declared none."""

    size_bytes: Optional[int] = FieldInfo(alias="sizeBytes", default=None)
    """Size as the provider declared it.

    Never measured here — nothing downloads the file.
    """

    source_hash_sha256: Optional[str] = FieldInfo(alias="sourceHashSha256", default=None)
    """
    Inbound only: the SHA-256 the provider declared alongside the attachment, when
    it declared one. Relayed to the customer so they can verify what they fetch
    matches what the carrier said it sent. It is the only integrity signal available
    on an attachment nobody here has read.
    """

    url: Optional[str] = None
    """Where the file lives.

    Outbound: the URL the customer gave us and the carrier fetched. Inbound: the URL
    the carrier hosts it at, relayed unchanged.
    """


class MessageMessageBody(BaseModel):
    """
    Structured message body format for database storage.
    Preserves channel-specific components (header, header media, body, footer, buttons, MMS subject
    and media).

    Persisted as the messageBody jsonb column on Messages. Every write path goes
    through MessageUtils.MessageBodyJsonOptions, which writes nulls, so the envelope shape is
    stable regardless of channel or status. Anything that rebuilds this object field by field — the
    four IMessageBodyStrategy implementations and MessageUtils.BuildSegmentBody — has to
    carry every member, or that member is silently dropped on whichever path forgot it.
    """

    buttons: Optional[List[MessageMessageBodyButton]] = None

    content: Optional[str] = None

    footer: Optional[str] = None

    header: Optional[str] = None

    header_media: Optional[MessageMessageBodyHeaderMedia] = FieldInfo(alias="headerMedia", default=None)
    """The media asset that rode a message's header, recorded as sent."""

    media: Optional[List[MessageMessageBodyMedia]] = None
    """MMS attachments, as the publicly fetchable URLs handed to the carrier.

    Null on every other channel.

    Persisted rather than derived because a resend and a curfew release rebuild the
    send from the stored row — MessageReplayCommandBuilder reads templateId and
    templateVariables and nothing else — so media that lives only on the original
    request would silently turn a replayed MMS into a text message.
    """

    subject: Optional[str] = None
    """MMS subject line. Null on every other channel."""


class Message(BaseModel):
    """
    Message response for v3 API — same shape as v2 with snake_case JSON conventions.

    The shape of a message that was sent immediately: it never has a scheduled_at key. A message that is
    or was held for a later instant is a ScheduledMessageResponse, and the endpoint decides which of
    the two to answer with. From
    always returns this type.
    """

    id: Optional[str] = None

    active_contact_price: Optional[float] = None

    channel: Optional[str] = None

    contact_id: Optional[str] = None

    created_at: Optional[datetime] = None

    customer_id: Optional[str] = None

    direction: Optional[str] = None

    events: Optional[List[MessageEvent]] = None

    message_body: Optional[MessageMessageBody] = None
    """
    Structured message body format for database storage. Preserves channel-specific
    components (header, header media, body, footer, buttons, MMS subject and media).

    Persisted as the messageBody jsonb column on Messages. Every write path goes
    through MessageUtils.MessageBodyJsonOptions, which writes nulls, so the envelope
    shape is stable regardless of channel or status. Anything that rebuilds this
    object field by field — the four IMessageBodyStrategy implementations and
    MessageUtils.BuildSegmentBody — has to carry every member, or that member is
    silently dropped on whichever path forgot it.
    """

    phone: Optional[str] = None

    phone_international: Optional[str] = None

    price: Optional[float] = None

    reason: Optional[str] = None
    """A human-readable sentence for reason_code, for example "Insufficient balance".

    Omitted whenever reason_code is.
    """

    reason_code: Optional[str] = None
    """
    Why the message is at its current status, as a stable platform code such as
    DELIVERY_007, BUSINESS_003 or DELIVERY_003. Present when the current status is
    FAILED, FILTERED or BLOCKED and the lifecycle was loaded; omitted otherwise.
    Switch on this rather than on reason: the code is stable, the wording may be
    improved. It is the platform's classification of the outcome, never a carrier or
    vendor code.
    """

    region_code: Optional[str] = None

    status: Optional[str] = None

    template_category: Optional[str] = None

    template_id: Optional[str] = None

    template_name: Optional[str] = None


class ConversationMessagesList(BaseModel):
    """A paginated list of messages — used by both conversation read endpoints."""

    messages: Optional[List[Message]] = None
    """The messages on this page."""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""
