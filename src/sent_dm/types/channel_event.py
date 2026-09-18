# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .channel_event_payload import ChannelEventPayload

__all__ = ["ChannelEvent"]


class ChannelEvent(BaseModel):
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

    payload: Optional[ChannelEventPayload] = None
    """
    Body of a channel event: where one of the customer's channels stands in
    provisioning and compliance. Delivered when a milestone moves — a registration
    filed, a verdict returned, a resubmission asked for, a sender gone live — so a
    customer's own onboarding UI does not have to poll GET /v3/channels.

    The subject is one item, never the account. A customer's "SMS channel" has no
    status; a market does. Country, NumberType and SenderValue name which one, so a
    customer terminating only to Kosovo never receives an event about US 10DLC.

    Status is the stable half of the contract. It is the same four-value set GET
    /v3/channels publishes, computed through the same code, so an event and a read
    of the same market cannot disagree. A subscriber that reads nothing but the
    status and the subject fields is a correct subscriber. The sub-type on the
    envelope names the specific milestone and is additive — that vocabulary comes
    from registries and carriers, which are parties Sent does not control.

    Status means provisioning and compliance are complete, not that a send will
    succeed right now. An account can be suspended, or a destination blocked by a
    routing rule, without either showing up here. Those are separate surfaces and
    deliberately not modelled on this payload.
    """

    request_id: Optional[str] = None
    """The event-specific body."""

    timestamp: Optional[str] = None
    """When Sent emitted the event, in UTC (yyyy-MM-ddTHH:mm:ssZ).

    This is the emission time, not the time the underlying change happened. Use the
    timestamp inside the payload for the latter.
    """
