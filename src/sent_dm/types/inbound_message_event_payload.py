# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

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
    """The channel the message arrived on, for example sms or whatsapp."""

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
