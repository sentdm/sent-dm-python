# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .channel_event import ChannelEvent
from .contact_event import ContactEvent
from .message_event import MessageEvent
from .template_event import TemplateEvent
from .inbound_message_event import InboundMessageEvent

__all__ = [
    "WebhookListEventsResponse",
    "EventData",
    "EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfLinkWebhookPayload",
    "EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfLinkWebhookPayloadPayload",
    "EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfCallWebhookPayload",
    "EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfCallWebhookPayloadPayload",
]


class EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfLinkWebhookPayloadPayload(BaseModel):
    """
    Body of a link event: something happened to a tracked link Sent published on the customer's
    behalf. A link points either at a URL the customer supplied or at a file Sent hosts for them;
    LinkKind says which. Delivered when an eligible request is served, or when a
    published link reaches the end of its life.

    A click is a request, not a read receipt. link.clicked means the redirect
    was served; link.downloaded means bytes went out. Neither proves a person saw anything —
    messaging providers and link scanners fetch URLs on their own, which is what
    TrafficClass exists to tell apart. Filter on it before reporting a click-through
    rate; treat likely_human as a hint, never as delivery confirmation.

    RecordId identifies the link; the X-Webhook-Event-ID header
    identifies the delivery. One link is hit many times, so those are the two keys a
    subscriber needs: group by the first, deduplicate on the second — exactly as on every other
    family. The payload carries no event identifier of its own, for the same reason none of the
    others do.

    Nothing here identifies the visitor. No IP address and no visitor token crosses
    this boundary. Country, Device and Browser are coarse
    buckets derived at the edge and are absent whenever the request did not supply enough to derive
    them.
    """

    record_id: str
    """
    The link's public identifier — the eight-character code in the short URL, for
    example A78B2BU0. Unique across both kinds, and never reused, so it is the
    stable key to group one link's events by.
    """

    access_country: Optional[str] = None
    """Where the request appeared to come from, as an ISO 3166-1 alpha-2 code.

    Named separately from the country on a channel event, which is a destination
    market the customer registered for — this one is a property of a single visitor
    and is absent when the edge could not resolve it.
    """

    access_outcome: Optional[str] = None
    """How the request was served, when the edge recorded it.

    Free text describing the outcome — show it to a human rather than branching on
    it.
    """

    browser: Optional[str] = None
    """The requesting browser family, for example chrome or safari, or unknown.

    Derived from the user agent.
    """

    bytes_served: Optional[int] = None
    """How many bytes were served, for a file access.

    A ranged request reports the bytes in that range, not the size of the file, so
    several accesses of one file can each report a part.
    """

    channel: Optional[str] = None
    """The channel the message carrying this link went out on: sms, whatsapp, or rcs."""

    customer_id: Optional[str] = None
    """The organization the link belongs to.

    Always the parent account, never a sender profile — read SenderProfileId for
    that.

    This family publishes the owner as an explicit pair rather than the single
    account_id the other families use. The pair says which organization and which
    profile without the subscriber deriving either, which is the trade: one more key
    against not having to know that account_id silently becomes the profile when one
    exists.
    """

    device: Optional[str] = None
    """The requesting device class: mobile, tablet, desktop or unknown.

    Derived from the user agent.
    """

    link_kind: Optional[str] = None
    """
    What the link points at: url for a destination the customer supplied, file for
    media Sent hosts. Always present, and implied by the event — link.clicked is
    always url and link.downloaded always file — but published as its own field so a
    subscriber can branch on the kind without parsing the event name, the same
    separation the channel family keeps between its event and its status.
    """

    message_id: Optional[str] = None
    """The message the link was published in.

    The event can arrive before the message is readable through GET /v3/messages: a
    provider may fetch a link within milliseconds of the send, and nothing here
    waits for the message row. Retry the read rather than treating an unknown id as
    an error.
    """

    occurred_at: Optional[str] = None
    """
    When the access or lifecycle change actually happened, in UTC
    (yyyy-MM-ddTHH:mm:ssZ). The envelope's timestamp is when Sent emitted the event;
    this is when the thing occurred, and the two differ by the ingest delay.
    """

    reference_key: Optional[str] = None
    """
    The caller-supplied label tying this link back to a position in the message, for
    example body:0 for the first link in the body. Present when the link was created
    with one.
    """

    referrer_host: Optional[str] = None
    """The host of the page that linked here, when the request supplied one.

    The host only — never a full referring URL.
    """

    request_method: Optional[str] = None
    """The HTTP method of the request that was served, for an access event.

    Omitted on link.expired and link.revoked, which describe no request.
    """

    sender_profile_id: Optional[str] = None
    """
    The sender profile that owns the link, or null when the organization owns it
    directly. Always on the wire so a handler reads one shape rather than branching
    on whether the key arrived.

    sender_profile_id, not profile_id: the API already publishes
    messaging_profile_id and sending_phone_number_profile_id for provider-side
    profiles, which are a different thing entirely. The unqualified name would read
    as one of those.
    """

    status_code: Optional[int] = None
    """
    The HTTP status Sent answered the request with: 302 for a link, 200 or 206 for a
    file. Omitted on lifecycle events.
    """

    traffic_class: Optional[str] = None
    """
    A coarse guess at what made the request: likely_human, provider (a messaging
    platform prefetching the link), bot, or unknown. Derived from the user agent, so
    it is a hint for filtering noise rather than a fact to bill or report on.
    """


class EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfLinkWebhookPayload(BaseModel):
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

    payload: Optional[EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfLinkWebhookPayloadPayload] = (
        None
    )
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


class EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfCallWebhookPayloadPayload(BaseModel):
    """
    Body of a call.initiated, call.answered, call.completed, call.failed
    or call.recording_ready event. Which of them occurred is the envelope's event.

    Shaped like the message, inbound, template and channel payloads: account_id names the
    account the event is about, channel names the channel, and updated_at is when the change
    happened on the call, in the same yyyy-MM-ddTHH:mm:ssZ form. duration_seconds and
    price are added on call.completed, reason on call.failed and
    recording_id on call.recording_ready; each is omitted rather than sent as null when it
    does not apply.

    Casing is snake_case because these ride the same webhook stream customers already parse
    message_id from; the question/answer contract is a separate surface and stays camelCase.
    Nothing here is provider-shaped: no provider call id, no namespaced identity.
    """

    call_id: str
    """Sent's call id, the same one the customer saw on the first question."""

    account_id: Optional[str] = None
    """
    The account the call belongs to: the key's own customer, or the sender profile
    it acted as.
    """

    channel: Optional[str] = None
    """Always voice."""

    duration_seconds: Optional[int] = None
    """How long the call lasted. Only on call.completed."""

    number: Optional[str] = None
    """The customer number that owns the call, in E.164 format."""

    price: Optional[float] = None
    """What the call was charged.

    Only on call.completed, and omitted there until billing has recorded the charge.
    """

    reason: Optional[str] = None
    """The machine-readable reason the call did not complete.

    Only on call.failed, and omitted when no reason was recorded.
    """

    recording_id: Optional[str] = None
    """
    The recording that became available, the same id GET /v3/calls/{id}/recordings
    lists it under. Only on call.recording_ready, which is sent once per recording.
    """

    updated_at: Optional[str] = None
    """When the change happened on the call, as opposed to when the event was emitted."""


class EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfCallWebhookPayload(BaseModel):
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

    payload: Optional[EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfCallWebhookPayloadPayload] = (
        None
    )
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


EventData: TypeAlias = Union[
    MessageEvent,
    InboundMessageEvent,
    TemplateEvent,
    ChannelEvent,
    ContactEvent,
    EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfLinkWebhookPayload,
    EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfCallWebhookPayload,
]


class WebhookListEventsResponse(BaseModel):
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
