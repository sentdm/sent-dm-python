# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MessageEventPayload"]


class MessageEventPayload(BaseModel):
    """Body of an outbound message lifecycle event.

    Delivered once per status change, so a single
    message produces several of these as it moves toward a terminal status.
    """

    message_status: str
    """The status the message just reached, for example SENT, DELIVERED, or FAILED.

    Sent means dispatched and delivered means confirmed, so treat them as distinct
    outcomes.
    """

    account_id: Optional[str] = None
    """The account the message belongs to."""

    agent_id: Optional[str] = None
    """The agent attributed to the send, when the send was attributed to one."""

    body: Optional[str] = None
    """The rendered message body, as plain text.

    Sent as null when we aren't asserting a body for this event. The field is always
    present, so read it and check for null rather than checking whether the key
    exists. Truncated to 3072 characters.
    """

    channel: Optional[str] = None
    """The channel the message went out on, for example sms or whatsapp.

    A message that falls back to another channel reports the channel actually used.
    """

    message_id: Optional[str] = None
    """The message this event describes.

    Stable across every event in the message's lifecycle, so use it to correlate
    them.
    """

    outbound_number: Optional[str] = None
    """The recipient's number in E.164 format."""

    reason: Optional[str] = None
    """
    A human-readable sentence for ReasonCode, for example "The recipient is not
    registered on this channel". Omitted whenever reason_code is.
    """

    reason_code: Optional[str] = None
    """
    Why the message reached this status, as a stable platform code such as
    DELIVERY_007 or BUSINESS_003. Present on message.failed, message.filtered and
    message.blocked; omitted on every status that needs no explanation. Switch on
    this rather than on Reason: the code is stable, the wording may be improved. It
    is the platform's classification of the outcome and never a carrier or vendor
    code.
    """

    schedule_reason: Optional[str] = None
    """
    message.scheduled only: why the message is held, either because you scheduled it
    or because the recipient is inside a protected quiet-hours window. Omitted on
    every other event, including message.cancelled — that is a property of the hold,
    not of the cancellation, and repeating it there would read as "why was this
    cancelled", which it does not answer.
    """

    scheduled_at: Optional[str] = None
    """
    message.scheduled and message.cancelled only, in UTC (yyyy-MM-ddTHH:mm:ssZ): on
    message.scheduled it is when the held message will be released for delivery, on
    message.cancelled the release instant that was called off — the same instant,
    before and after. A consumer that recorded a future send from the first event
    has what it needs to un-record it from the second. Omitted on every other event.
    """

    template_id: Optional[str] = None
    """The template the message was sent from, when it was sent from one."""

    template_name: Optional[str] = None
    """Name of the template the message was sent from.

    Omitted when the message wasn't template-based.
    """

    updated_at: Optional[str] = None
    """When the message reached MessageStatus, in UTC (yyyy-MM-ddTHH:mm:ssZ)."""
