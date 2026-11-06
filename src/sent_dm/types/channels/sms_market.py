# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .sms_number import SMSNumber

__all__ = ["SMSMarket", "Compliance", "ComplianceDocument"]


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


class SMSMarket(BaseModel):
    """
    One SMS market the profile sends in — its sender, where that sender stands, and what the market wants.

    A profile may send in several: it is a tenant, not a market. Each carries its own status, because
    a profile can be live in one country and mid-registration in another — and each carries what it still owes,
    rather than that being reported in a separate array a caller has to join on.
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

    country: Optional[str] = None

    number_type: Optional[str] = None

    numbers: Optional[List[SMSNumber]] = None
    """
    Every number this market holds or is still owed, each with its area code and its
    own status (ACTIVE once it can send, PROVISIONING while it is still to be
    assigned, INACTIVE once it could send and no longer can). One entry for a market
    holding one number. US 10DLC numbers are assigned when the campaign is approved,
    so they read as owed until then. Read-only.
    """

    reason: Optional[str] = None
    """
    A sentence for reason_code: this market's own explanation, naming what is
    outstanding where that is you. Omitted while ACTIVE.
    """

    reason_code: Optional[str] = None
    """
    Why the market is not ACTIVE, as a stable code: an ErrorCodes CHANNEL_xxx value
    such as CHANNEL_001 (something you owe) or CHANNEL_009 (under review). Switch on
    this rather than on reason. Omitted while ACTIVE. Read-only; when nothing more
    specific is known it is the generic reason for the status.
    """

    sender_value: Optional[str] = None
    """The sender itself.

    Null until a carrier-assigned number is procured. For a market holding several
    numbers, the first active one (the first assigned while none is active) — every
    number is in numbers.
    """

    status: Optional[Literal["PROVISIONING", "ACTION_NEEDED", "PENDING_REVIEW", "ACTIVE", "INACTIVE"]] = None
    """
    Where this market's sender stands, in terms of who is holding it up —
    PROVISIONING, ACTION_NEEDED, PENDING_REVIEW or ACTIVE. Read-only.

    Resolved rather than reported raw: a live sender reads ACTIVE whatever it still
    owes, a market with outstanding requirements or an open resubmission request
    reads ACTION_NEEDED, and a market that registers with a regime reads
    PENDING_REVIEW once its brand exists — filing to The Campaign Registry is ours
    to do and need not have happened yet, so a dedicated brand created through this
    API reads PENDING_REVIEW from the moment it is stored.

    Describes whether the market can send, not each number: a market holding several
    numbers reads ACTIVE as soon as one of them is, whatever the others are doing.
    Each number's own status is in numbers.
    """
