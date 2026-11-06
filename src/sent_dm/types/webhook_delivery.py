# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .call_event import CallEvent
from .link_event import LinkEvent
from .channel_event import ChannelEvent
from .contact_event import ContactEvent
from .message_event import MessageEvent
from .template_event import TemplateEvent
from .inbound_message_event import InboundMessageEvent

__all__ = ["WebhookDelivery", "EventData"]

EventData: TypeAlias = Union[
    MessageEvent, InboundMessageEvent, TemplateEvent, ChannelEvent, ContactEvent, LinkEvent, CallEvent
]


class WebhookDelivery(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    delivery_attempts: Optional[int] = None

    delivery_status: Optional[str] = None

    error_message: Optional[str] = None

    event_data: Optional[EventData] = None
    """The exact event body that was delivered, or attempted, for this record.

    One of the six webhook envelopes:

    message — an outbound message changed status. message with event:
    message.received — someone replied to you. templates — a template was approved,
    rejected, paused or similar. channel — one of your markets moved in provisioning
    or compliance. contact — a consent signal: opt-in, opt-out or help. link — a
    tracked short link was clicked or a hosted file downloaded, or one expired or
    was revoked.

    Read field and event to tell which, the same way your endpoint does. The two
    message envelopes are the reason that is two fields and not one: they share a
    field and differ by event.

    Treat the list as open. It has grown twice — channel and then link — and a
    handler that rejects an envelope it does not recognise will break on the next
    addition rather than ignore it.
    """

    event_type: Optional[str] = None

    http_status_code: Optional[int] = None

    processing_completed_at: Optional[datetime] = None

    processing_started_at: Optional[datetime] = None

    response_body: Optional[str] = None
