# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .link_event_payload import LinkEventPayload

__all__ = ["LinkEvent"]


class LinkEvent(BaseModel):
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

    payload: Optional[LinkEventPayload] = None
    """
    Body of a link event: something happened to a tracked link Sent published on the
    customer's behalf. A link points either at a URL the customer supplied or at a
    file Sent hosts for them; LinkKind says which. Delivered when an eligible
    request is served, or when a published link reaches the end of its life.

    A click is a request, not a read receipt. link.clicked means the redirect was
    served; link.downloaded means bytes went out. Neither proves a person saw
    anything — messaging providers and link scanners fetch URLs on their own, which
    is what TrafficClass exists to tell apart. Filter on it before reporting a
    click-through rate; treat likely_human as a hint, never as delivery
    confirmation.

    RecordId identifies the link; the X-Webhook-Event-ID header identifies the
    delivery. One link is hit many times, so those are the two keys a subscriber
    needs: group by the first, deduplicate on the second — exactly as on every other
    family. The payload carries no event identifier of its own, for the same reason
    none of the others do.

    Nothing here identifies the visitor. No IP address and no visitor token crosses
    this boundary. Country, Device and Browser are coarse buckets derived at the
    edge and are absent whenever the request did not supply enough to derive them.
    """

    request_id: Optional[str] = None
    """The event-specific body."""

    timestamp: Optional[str] = None
    """When Sent emitted the event, in UTC (yyyy-MM-ddTHH:mm:ssZ).

    This is the emission time, not the time the underlying change happened. Use the
    timestamp inside the payload for the latter.
    """
