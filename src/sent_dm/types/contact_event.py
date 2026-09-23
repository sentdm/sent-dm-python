# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .contact_event_payload import ContactEventPayload

__all__ = ["ContactEvent"]


class ContactEvent(BaseModel):
    """The envelope Sent POSTs to a subscribed webhook endpoint.

    Every event shares this shape and
    varies only in Payload.
    """

    event: Optional[str] = None
    """
    The specific event within the family, for example message.delivered,
    message.received or contact.opt_out. Absent on events that have no subtype, so
    treat it as optional.
    """

    field: Optional[str] = None
    """The event family, for example message, templates or contact.

    Route on this first, then on event for the specific change.
    """

    payload: Optional[ContactEventPayload] = None
    """
    Body of a contact.opt_in, contact.opt_out, contact.help or
    contact.custom_keyword event. Delivered when a contact signals a consent change,
    asks for help, or sends one of your own auto-reply keywords.

    These events state the signal outright, so you do not have to recognise keywords
    in the text of a message.received event. They also cover cases that produce no
    inbound message at all, such as a network handling an opt-out on your behalf.

    Two of the four change consent and two do not: contact.help and
    contact.custom_keyword report the state the contact already had. Read opt_out
    for the state and the envelope's event for what happened, rather than inferring
    one from the other.

    Fields are ordered identity → resulting state → provenance → join keys. The two
    parties are from and to. Note that the message family has not moved to those
    names yet — message.received still calls the same two parties inbound_number and
    outbound_number. Nothing here restates the envelope: which signal occurred is
    the envelope's event, and when it was emitted is its timestamp. Retries carry
    the same X-Webhook-Event-ID header, which is what to deduplicate on.
    """

    request_id: Optional[str] = None
    """The event-specific body."""

    timestamp: Optional[str] = None
    """When Sent emitted the event, in UTC (yyyy-MM-ddTHH:mm:ssZ).

    This is the emission time, not the time the underlying change happened. Use the
    timestamp inside the payload for the latter.
    """
