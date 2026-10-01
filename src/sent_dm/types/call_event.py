# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_event_payload import CallEventPayload

__all__ = ["CallEvent"]


class CallEvent(BaseModel):
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

    payload: Optional[CallEventPayload] = None
    """
    Body of a call.initiated, call.answered, call.completed, call.failed or
    call.recording_ready event. Which of them occurred is the envelope's event.

    Shaped like the message, inbound, template and channel payloads: account_id
    names the account the event is about, channel names the channel, and updated_at
    is when the change happened on the call, in the same yyyy-MM-ddTHH:mm:ssZ form.
    duration_seconds and price are added on call.completed, reason on call.failed
    and recording_id on call.recording_ready; each is omitted rather than sent as
    null when it does not apply.

    Casing is snake_case because these ride the same webhook stream customers
    already parse message_id from; the question/answer contract is a separate
    surface and stays camelCase. Nothing here is provider-shaped: no provider call
    id, no namespaced identity.
    """

    request_id: Optional[str] = None
    """The event-specific body."""

    timestamp: Optional[str] = None
    """When Sent emitted the event, in UTC (yyyy-MM-ddTHH:mm:ssZ).

    This is the emission time, not the time the underlying change happened. Use the
    timestamp inside the payload for the latter.
    """
