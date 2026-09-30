# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["InboundMessageEventPayload", "Media"]


class Media(BaseModel):
    """One attachment on an inbound message."""

    hash_sha256: Optional[str] = None
    """SHA-256 of the file as the carrier declared it, when it declares one.

    Verify what you download against this — sent.dm never reads the bytes, so it is
    the only integrity signal available.
    """

    mime_type: Optional[str] = None
    """Content type as the carrier reported it, for example image/jpeg."""

    size_bytes: Optional[int] = None
    """Size in bytes as the carrier declared it. Absent when it declared none."""

    url: Optional[str] = None
    """Where the carrier hosts the attachment.

    This link expires and is not authenticated. sent.dm relays it rather than
    copying the file, so how long it stays fetchable is the carrier's decision and
    differs between them — assume days, not months. Anyone holding the URL can fetch
    it until it lapses. Copy the file on receipt if you need it to outlive that
    window; do not store this URL as a permanent reference.
    """


class InboundMessageEventPayload(BaseModel):
    """Body of a message.received event.

    Delivered when a contact messages one of your numbers.
    """

    inbound_number: str
    """The contact's number in E.164 format, meaning the number the message came from."""

    received_at: str
    """When the message was received, in UTC (yyyy-MM-ddTHH:mm:ssZ)."""

    account_id: Optional[str] = None
    """The account the message belongs to."""

    channel: Optional[str] = None
    """The channel the message arrived on, for example sms or mms."""

    media: Optional[List[Media]] = None
    """
    Attachments the contact sent, present only on channels that carry them (mms
    today) and omitted entirely otherwise.

    Each url points at the carrier's own copy of the file — sent.dm records where
    the attachment is, not the attachment itself. The link is unauthenticated and
    expires on the carrier's schedule, which differs between them: assume days, not
    months. Download what you need on receipt; re-reading the message through GET
    /v3/messages/{id} returns the same stored link, not a fresh one, so once it
    lapses the entry remains with whatever the carrier declared about the file but
    the file is no longer reachable.
    """

    message_id: Optional[str] = None
    """The inbound message."""

    outbound_number: Optional[str] = None
    """Your number in E.164 format, meaning the number the message was addressed to."""

    text: Optional[str] = None
    """The message body.

    Sent as null when the inbound message carried no text, for example a media-only
    message. The field is always present, so read it and check for null rather than
    checking whether the key exists.
    """

    updated_at: Optional[str] = None
    """When the message was received, in UTC (yyyy-MM-ddTHH:mm:ssZ).

    Same value as ReceivedAt, kept for envelope consistency with outbound events.
    """
