# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .template_event_payload import TemplateEventPayload

__all__ = ["TemplateEvent"]


class TemplateEvent(BaseModel):
    """The envelope Sent POSTs to a subscribed webhook endpoint.

    Every event shares this shape and
    varies only in Payload.
    """

    event: Optional[str] = None
    """
    The specific event within the family, for example message.delivered or
    message.received. Absent on events that have no subtype, so treat it as
    optional.
    """

    field: Optional[str] = None
    """The event family, for example message or templates.

    Route on this first, then on event for the specific change.
    """

    payload: Optional[TemplateEventPayload] = None
    """Body of a template status event.

    Delivered when a template's review outcome changes, so you can react without
    polling.
    """

    timestamp: Optional[str] = None
    """When Sent emitted the event, in UTC (yyyy-MM-ddTHH:mm:ssZ).

    This is the emission time, not the time the underlying change happened. Use the
    timestamp inside the payload for the latter.
    """
