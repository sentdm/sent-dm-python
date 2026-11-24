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

__all__ = [
    "WebhookDelivery",
    "EventData",
    "EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfAgentWebhookPayload",
    "EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfAgentWebhookPayloadPayload",
]


class EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfAgentWebhookPayloadPayload(BaseModel):
    """Body of an agent.* webhook (Sent Agents).

    The event is the agent service's own record,
    forwarded without renaming: EventId is its id, so a subscriber can dedupe a redelivery.
    """

    event_id: str
    """The agent service's event id. The same event is never delivered under two ids."""

    occurred_at: str
    """When the agent service recorded it, UTC, to the millisecond."""

    account_id: Optional[str] = None
    """The sender profile the agent runs on."""

    actor: Optional[str] = None
    """Who caused it: system, the agent service's customer, or an approver."""

    agent_id: Optional[str] = None
    """The agent."""

    agent_name: Optional[str] = None
    """The agent's name, as it is listed.

    Absent for an agent services no longer holds.
    """

    agent_version: Optional[int] = None
    """
    The version of the agent the event is of: the one its conversation runs, or the
    active one for an event of the agent itself. Absent when the agent service does
    not say it.
    """

    contact_id: Optional[str] = None
    """The contact of that conversation; absent on agent-level events."""

    contact_phone_number: Optional[str] = None
    """
    The contact's phone number, in E.164, so a receiver knows who the event is about
    without asking for the contact. Read from the account's contacts as the webhook
    is built: the agent service's own record names a contact by id only. Absent on
    agent-level events, and for a contact the account no longer holds.
    """

    data: Optional[object] = None
    """
    The event's own fields (outcome, reason, ...), exactly as the agent service
    recorded them.
    """

    instance_id: Optional[str] = None
    """
    The conversation (agent × contact) the event belongs to; absent on agent-level
    events.
    """

    sequence: Optional[int] = None
    """
    Where the event stands among the agent's events: a number that grows with each,
    so two events of the same second are put in order by it. Not a count: there are
    gaps between an agent's own. Absent from an agent service that does not say it.
    """


class EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfAgentWebhookPayload(BaseModel):
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

    payload: Optional[
        EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfAgentWebhookPayloadPayload
    ] = None
    """Body of an agent.\\** webhook (Sent Agents).

    The event is the agent service's own record, forwarded without renaming: EventId
    is its id, so a subscriber can dedupe a redelivery.
    """

    request_id: Optional[str] = None
    """The event-specific body."""

    timestamp: Optional[str] = None
    """When Sent emitted the event, in UTC (yyyy-MM-ddTHH:mm:ssZ).

    This is the emission time, not the time the underlying change happened. Use the
    timestamp inside the payload for the latter.
    """


EventData: TypeAlias = Union[
    MessageEvent,
    InboundMessageEvent,
    TemplateEvent,
    ChannelEvent,
    ContactEvent,
    LinkEvent,
    CallEvent,
    EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfAgentWebhookPayload,
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
