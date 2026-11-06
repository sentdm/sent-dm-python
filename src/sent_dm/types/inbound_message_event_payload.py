# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .inbound_media import InboundMedia

__all__ = ["InboundMessageEventPayload"]


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

    media: Optional[List[InboundMedia]] = None
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

    referral: Optional[object] = None
    """
    The ad the contact tapped to start the conversation, present only on whatsapp
    messages sent from a Click to WhatsApp ad and omitted entirely otherwise.

    This is Meta's referral object passed through unchanged, with Meta's field names
    and nesting: source_url, source_id, source_type, headline, body, media_type,
    image_url (image ads), video_url and thumbnail_url (video ads), ctwa_clid and
    welcome_message.text. Which fields appear is Meta's decision: ctwa_clid in
    particular is not sent for ads shown in WhatsApp Status, so treat every field as
    optional.
    """

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
