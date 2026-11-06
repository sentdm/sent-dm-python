# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .channels_state import ChannelsState
from .sender_profile_billing import SenderProfileBilling
from .channels.supplied_compliance import SuppliedCompliance

__all__ = ["SenderProfile"]


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

    compliance: Optional[SuppliedCompliance] = None
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
