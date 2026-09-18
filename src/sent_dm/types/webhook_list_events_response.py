# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .message_event import MessageEvent
from .template_event import TemplateEvent
from .inbound_message_event import InboundMessageEvent

__all__ = [
    "WebhookListEventsResponse",
    "EventData",
    "EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfChannelWebhookPayload",
    "EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfChannelWebhookPayloadPayload",
    "EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfContactWebhookPayload",
    "EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfContactWebhookPayloadPayload",
]


class EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfChannelWebhookPayloadPayload(BaseModel):
    """
    Body of a channel event: where one of the customer's channels stands in provisioning and
    compliance. Delivered when a milestone moves — a registration filed, a verdict returned, a
    resubmission asked for, a sender gone live — so a customer's own onboarding UI does not have to
    poll GET /v3/channels.

    The subject is one item, never the account. A customer's "SMS channel" has no
    status; a market does. Country, NumberType and
    SenderValue name which one, so a customer terminating only to Kosovo never
    receives an event about US 10DLC.

    Status is the stable half of the contract. It is the same four-value
    set GET /v3/channels publishes, computed through the same code, so an event and a read of
    the same market cannot disagree. A subscriber that reads nothing but the status and the subject
    fields is a correct subscriber. The sub-type on the envelope names the specific milestone and is
    additive — that vocabulary comes from registries and carriers, which are parties Sent does not
    control.

    Status means provisioning and compliance are complete, not that a send
    will succeed right now. An account can be suspended, or a destination blocked by a routing
    rule, without either showing up here. Those are separate surfaces and deliberately not modelled
    on this payload.
    """

    country: str
    """The market's destination country as an ISO 3166-1 alpha-2 code, for example XK.

    Always present, and the property that identifies this payload among the
    delivered envelopes — see DeliveredWebhookEvents. Every event in this family
    reports one market, and a market has a country.
    """

    account_id: Optional[str] = None
    """The account whose market this is, named as on every other family.

    When an organization receives an event for one of its sender profiles this is
    the profile, so a reseller compares it with its own id and anything different is
    one of its profiles.
    """

    channel: Optional[str] = None
    """The channel this market belongs to: sms, whatsapp, or rcs.

    Never sent — that value belongs to message events, where it names the
    smart-routing brand rather than a channel that can be provisioned.
    """

    number_type: Optional[str] = None
    """The kind of sender the market uses, for example TEN_DLC, LOCAL, or ALPHANUMERIC.

    Omitted when the subject has no sender type of its own.
    """

    reason: Optional[str] = None
    """
    Why the market reached this state, when a reason was given — a correction
    explained, or a campaign lapse. Free text, passed through from the registry or
    carrier that wrote it, so treat it as a message to show a human rather than a
    value to branch on.
    """

    sender_value: Optional[str] = None
    """The sender itself — a number in E.164, or an alphanumeric sender ID.

    Always present, and null until a sender exists. The key is on every delivery so
    a subscriber reads one shape rather than branching on whether the field arrived
    — the same choice template_id makes on the message payload.

    It can carry a value at any point in the lifecycle, not only once the market is
    live: a number ordered and not yet active at the carrier is already known during
    PROVISIONING, and an alphanumeric sender the customer chose themselves is known
    before anything is filed. It is null while the market is still waiting on a
    number, which for a US 10DLC registration is every event up to
    channel.activated.
    """

    status: Optional[str] = None
    """
    Where the market stands: PENDING_REVIEW, ACTION_NEEDED, PROVISIONING, ACTIVE or
    INACTIVE. PENDING_REVIEW means a registry or a carrier holds it and the wait is
    theirs; ACTION_NEEDED means it is yours; PROVISIONING means the verdict is in
    and Sent is acquiring the sender; INACTIVE means it had a working sender and no
    longer does.

    Each event name is the transition into one of these, but the two are separate
    fields and may legitimately differ. A resubmission filed against a market whose
    sender is already live is channel.submitted carrying ACTIVE: a correction is
    with the registry and the sender keeps working. Read both.
    """

    updated_at: Optional[str] = None
    """When the transition happened, in UTC (yyyy-MM-ddTHH:mm:ssZ)."""


class EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfChannelWebhookPayload(BaseModel):
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
        EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfChannelWebhookPayloadPayload
    ] = None
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


class EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfContactWebhookPayloadPayload(BaseModel):
    """Body of a contact.opt_in, contact.opt_out or contact.help event.

    Delivered
    when a contact signals a consent change or asks for help.

    These events state the signal outright, so you do not have to recognise keywords in the
    text of a message.received event. They also cover cases that produce no inbound message
    at all, such as a network handling an opt-out on your behalf.

    Fields are ordered identity → resulting state → provenance → join key. Nothing here
    restates the envelope: which of the three signals occurred is the envelope's event, and
    when it was emitted is its timestamp. Retries carry the same X-Webhook-Event-ID
    header, which is what to deduplicate on.
    """

    opt_out: bool
    """
    Whether the contact is opted out after this signal — the state to write to your
    own record. Same meaning as opt_out on the contact resource. On contact.help
    this reports the contact's existing state, which help does not change.

    Two signals from the same contact can arrive out of order, because each one is
    queued on its own rather than against the contact. Compare the envelope's
    timestamp before you overwrite a newer state with an older one. That timestamp
    is second-precision, so treat two signals stamped in the same second as
    unordered and read the contact resource to settle them.
    """

    source: str
    """How the signal reached us.

    INBOUND_KEYWORD means the contact sent a message whose text matched one of the
    keywords; PROVIDER_SIGNAL means the network reported it. A provider signal
    usually carries no message_id or text, so read both for null rather than
    inferring them from this field.
    """

    account_id: Optional[str] = None
    """The account the contact belongs to.

    Present so one endpoint can serve several accounts.
    """

    channel: Optional[str] = None
    """The channel the signal arrived on, for example sms or whatsapp."""

    contact_id: Optional[str] = None
    """The contact who raised the signal.

    Always populated, including for contact.help from a number you have not messaged
    before — the contact is created if it does not exist yet, so this identifier is
    always resolvable against the contacts API.
    """

    message_id: Optional[str] = None
    """
    The inbound message that carried the signal, matching message_id on the
    corresponding message.received event so the two can be joined.

    Sent as null when the signal did not arrive as a message — for example when a
    network processed an opt-out on your behalf — and also when the message belongs
    to a different account than this event, which can happen on a shared WhatsApp
    number. The field is always present, so read it and check for null rather than
    checking whether the key exists.
    """

    phone_number: Optional[str] = None
    """The contact's number in E.164 format.

    Same value as phone_number on the contact resource.
    """

    text: Optional[str] = None
    """The text the contact sent, for example STOP or UNSUBSCRIBE.

    Sent as null when the signal did not arrive as text. The field is always
    present, so read it and check for null rather than checking whether the key
    exists.
    """


class EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfContactWebhookPayload(BaseModel):
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
        EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfContactWebhookPayloadPayload
    ] = None
    """Body of a contact.opt_in, contact.opt_out or contact.help event.

    Delivered when a contact signals a consent change or asks for help.

    These events state the signal outright, so you do not have to recognise keywords
    in the text of a message.received event. They also cover cases that produce no
    inbound message at all, such as a network handling an opt-out on your behalf.

    Fields are ordered identity → resulting state → provenance → join key. Nothing
    here restates the envelope: which of the three signals occurred is the
    envelope's event, and when it was emitted is its timestamp. Retries carry the
    same X-Webhook-Event-ID header, which is what to deduplicate on.
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
    EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfChannelWebhookPayload,
    EventDataSentDmServicesCommonServicesWebhooksContractsWebhookEventOfContactWebhookPayload,
]


class WebhookListEventsResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    delivery_attempts: Optional[int] = None

    delivery_status: Optional[str] = None

    error_message: Optional[str] = None

    event_data: Optional[EventData] = None
    """The exact event body that was delivered, or attempted, for this record.

    One of the four webhook envelopes: a message status change, an inbound message,
    a template status change, or a contact consent signal. Read field and event to
    tell which, the same way your endpoint does.
    """

    event_type: Optional[str] = None

    http_status_code: Optional[int] = None

    processing_completed_at: Optional[datetime] = None

    processing_started_at: Optional[datetime] = None

    response_body: Optional[str] = None
