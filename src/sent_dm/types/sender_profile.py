# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .channels_state import ChannelsState
from .sender_profile_billing import SenderProfileBilling

__all__ = ["SenderProfile", "Compliance", "ComplianceDocument"]


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


class SenderProfile(BaseModel):
    """
    A sender profile as the API reports it — the same document the create call accepts, plus the read-only
    facts it cannot: each market's status and what it still owes.

    No status at the profile, brand or campaign level. Brand and campaign are identity, and
    identity has no lifecycle. What has one is the registration of a sender in a market, and the approval of
    a channel — so status lives there, where it says which specific thing is blocked rather than flattening
    several answers into one.
    """

    id: Optional[str] = None

    api_key: Optional[str] = None
    """The API key for this profile.

    Returned by create and by nothing else. It is shown once; a read that repeated
    it would turn every profile list into a credential dump and put the key into any
    log or cache that keeps a response body.

    Omitted rather than null on a read. A key field that is always present and
    always empty suggests it could be populated, which is an invitation to populate
    it; absent says there is nothing to look for. Doing it with a serializer
    condition rather than a second response type keeps create and read on one shape,
    which is what stops them drifting.
    """

    billing: Optional[SenderProfileBilling] = None
    """Who pays for a sender profile's traffic, as a read reports it.

    Its own type, field for field the same as BillingRequest. Same reason as the
    brand: a response is not a request, whatever it carries.
    """

    channels: Optional[ChannelsState] = None
    """The channels a profile sends on.

    SMS is a list because a profile can send in several markets; WhatsApp and RCS
    are single, because a profile has one business account and one agent.
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

    created_at: Optional[datetime] = None

    description: Optional[str] = None

    name: Optional[str] = None

    notifications: Optional[str] = None
    """
    Who is notified about this profile's events: ORGANIZATION, SENDER_PROFILE, or
    ORGANIZATION_AND_SENDER_PROFILE. Always present — a profile that never chose
    reports as ORGANIZATION, the value a create would send to get the default
    behaviour.
    """

    organization_id: Optional[str] = None

    short_name: Optional[str] = None
