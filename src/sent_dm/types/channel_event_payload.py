# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["ChannelEventPayload", "Compliance", "ComplianceDocument"]


class ComplianceDocument(BaseModel):
    """A document a market asked for and has been given."""

    document_id: Optional[str] = None
    """Identifier of the upload, for fetching it back through the documents endpoints."""

    file_name: Optional[str] = None

    key: Optional[str] = None
    """The catalog's name for this document, matching the requirement it satisfies."""


class Compliance(BaseModel):
    """
    What a market has been given: the identity it registers under, its programme, and any documents attached.

    What it does not carry is what the market asks for. That is the subject of
    GET /v3/compliance/requirements, and it is the same answer for every caller — a description of what
    a compliance regime wants, not a record of one customer's progress through it. It was reported here as
    well for a while, which put the same array in six response shapes and left a caller deciding which of two
    sources to believe.

    Present on a list read for markets that register (carrying brand and campaign), but with
    documents absent — documents are not fetched for a list, because a catalog lookup and a document
    read per market would multiply across a page. Absent documents is distinct from an empty list:
    absent says they were not fetched; empty says the market has been given none. The parent object is null
    only when the market registers with nobody and compliance was not computed — nothing to show at all.
    """

    brand: Optional[Dict[str, object]] = None
    """The identity this market registers under, with inherit saying whose it is.

    Reported here rather than on the profile because it belongs to the registration
    this market files, and only one market files one. It was a top-level block for a
    while, which put a per-registration value beside a list of markets and left a
    caller to work out which market it belonged to.

    Absent for a market that registers with nobody — such a market asks for no
    identity, so there is none to report. Absent and null mean different things:
    absent says this market does not ask, null would say it asks and nothing was
    supplied.

    Untyped, like the request side, because its members are declared by the market's
    own schema rather than by a C# class. A typed pair here would be a second
    definition of what a market wants, free to drift from the one that validates.
    """

    campaign: Optional[Dict[str, object]] = None
    """The programme this market registers, with inherit saying whose it is.

    One, not a list. TcrCampaigns permits several and an account built on the admin
    side may hold them, but this surface offers one — which is what lets the
    market's PATCH be an upsert rather than a collection with an addressable create
    behind it. An account holding several is reported as its first and refused on
    write, rather than half-edited.

    Carries no id. Nothing addresses a campaign, and an undeclared key would be
    refused if the caller sent this object back — which it is meant to be able to
    do.
    """

    documents: Optional[List[ComplianceDocument]] = None
    """What has been supplied for this market.

    Files, not values — the declared halves above carry the values. A document
    cannot be a JSON value, so it is sent as multipart on the channel call and
    reported here as a reference.

    Absent on a list read, which fetches identity but does not compute compliance
    documents per market. Absent and empty mean different things: absent says the
    documents were not fetched; empty says the market has been given none.
    """


class ChannelEventPayload(BaseModel):
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
    one of its profiles. Matches customer_id on GET /v3/channels and the sender
    profile's id. Together with channel, country, and number_type, it identifies the
    market.
    """

    channel: Optional[str] = None
    """The channel this market belongs to: sms, whatsapp, or rcs.

    Never sent — that value belongs to message events, where it names the
    smart-routing brand rather than a channel that can be provisioned.
    """

    compliance: Optional[Compliance] = None
    """
    What a market has been given: the identity it registers under, its programme,
    and any documents attached.

    What it does not carry is what the market asks for. That is the subject of GET
    /v3/compliance/requirements, and it is the same answer for every caller — a
    description of what a compliance regime wants, not a record of one customer's
    progress through it. It was reported here as well for a while, which put the
    same array in six response shapes and left a caller deciding which of two
    sources to believe.

    Present on a list read for markets that register (carrying brand and campaign),
    but with documents absent — documents are not fetched for a list, because a
    catalog lookup and a document read per market would multiply across a page.
    Absent documents is distinct from an empty list: absent says they were not
    fetched; empty says the market has been given none. The parent object is null
    only when the market registers with nobody and compliance was not computed —
    nothing to show at all.
    """

    number_type: Optional[str] = None
    """The kind of sender the market uses, for example TEN_DLC, LOCAL, or ALPHANUMERIC.

    Omitted when the subject has no sender type of its own.
    """

    reason: Optional[str] = None
    """
    Why the market reached this state, as a sentence to show a person: the specific
    explanation when one was given (a correction explained, a campaign lapse),
    otherwise what reason_code means for this market. Not a value to branch on.
    """

    reason_code: Optional[str] = None
    """
    Why the market is not ACTIVE, as a stable code: an ErrorCodes CHANNEL_xxx value
    such as CHANNEL_001 (something you owe) or CHANNEL_002 (a correction was
    requested). The same code the channels resource reports for the market. Switch
    on this rather than on reason. Omitted while ACTIVE.
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
