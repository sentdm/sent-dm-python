# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .supplied_campaign import SuppliedCampaign
from .supplied_document import SuppliedDocument

__all__ = ["SuppliedCompliance"]


class SuppliedCompliance(BaseModel):
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

    campaigns: Optional[List[SuppliedCampaign]] = None
    """
    Every campaign this market registers, each with inherit saying whose it is —
    oldest first.

    A list, because a market can now be on more than one. POST
    /v3/channels/sms/compliances/US/TEN_DLC/campaigns adds a campaign of the
    customer's own beside the one it has, and a profile running on its
    organization's campaign keeps that one when it adds its own. Campaign can only
    show one of them, so it stays as it was, for callers that read it, and this is
    where the rest are.

    The organization's campaign reads "inherit": true and the customer's own read
    "inherit": false. Each entry is the shape of Campaign plus id, the campaign's
    own id, so several can be told apart. Campaign carries no id, because it is sent
    back to PATCH, which refuses a key it does not declare; this list is read-only.

    Absent for a market that registers with nobody; empty for one that registers and
    has no campaign yet.
    """

    documents: Optional[List[SuppliedDocument]] = None
    """What has been supplied for this market.

    Files, not values — the declared halves above carry the values. A document
    cannot be a JSON value, so it is sent as multipart on the channel call and
    reported here as a reference.

    Absent on a list read, which fetches identity but does not compute compliance
    documents per market. Absent and empty mean different things: absent says the
    documents were not fetched; empty says the market has been given none.
    """
