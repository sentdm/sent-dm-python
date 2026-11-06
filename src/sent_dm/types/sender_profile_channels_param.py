# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .sender_profile_rcs_param import SenderProfileRcsParam
from .sender_profile_sms_param import SenderProfileSMSParam
from .sender_profile_whatsapp_param import SenderProfileWhatsappParam

__all__ = ["SenderProfileChannelsParam"]


class SenderProfileChannelsParam(TypedDict, total=False):
    """The channels the profile sends on.

    Each is independently the profile's own or absent — none can be
    inherited, so none carries a mode and presence is the whole of the request.

    A profile can send SMS in several markets, but create takes one — the market it starts in.
    Further markets are added through POST /v3/channels/sms with x-profile-id, and a read returns
    them all as a list. Create stays singular permanently rather than being a list that accepts one entry:
    the constraint is in the type, and there is no later widening to break the contract.
    """

    rcs: Optional[SenderProfileRcsParam]
    """
    Asks for an RCS agent of the profile's own, optionally with the full order form
    inline.

    Two modes, distinguished by whether any field is populated: "rcs": {} — intent
    only. Records that the profile wants its own agent; the order form is submitted
    separately through POST /v3/channels/rcs once the fields are ready. "rcs": {
    ...fields... } — full form. All required fields must be present; the agent is
    created alongside the profile in one call. Omitting opt_in_screenshot_url is
    allowed.
    """

    sms: Optional[SenderProfileSMSParam]
    """One SMS market a profile sends in — a country and a sender type.

    A profile may have several. It is a tenant, not a market: a business sending to
    two countries is one customer of yours, and forcing it into two profiles would
    give it two API keys, two inboxes and two contact lists for one business. The
    platform already assumes many — CustomerChannelProviders is unique on (customer,
    channel, iso, number).

    No mode: a sender is the profile's own or it has none. Listing a market is the
    request for one.

    Also the discriminator for everything else: the compliance catalog is keyed on
    (country, number type), and that pair decides which fields brand accepts and
    what compliance is asked for.
    """

    whatsapp: Optional[SenderProfileWhatsappParam]
    """
    The profile's own WhatsApp Business Account, named by the two identifiers the
    organization cannot answer for you.

    No mode: a profile's WABA is its own or it has none. Sharing the organization's
    would mean sharing its inbox and its throughput, which makes the two
    indistinguishable to a recipient — so inheriting is not offered rather than
    refused.

    Everything derivable is derived. Whenever this block is present, the solution
    the account arrived through, the client business portfolio that owns it, the
    access token and that token's expiry are all resolved from the organization by
    IPartnerSolutionService.ResolveAccountCredentialsAsync — the first two off the
    org's shared-account listing, the token minted against the org's own solution.
    They were previously asked for and are no longer accepted: solution_id and
    owner_business_id are Meta's answer about provenance, so taking them from the
    caller let a request assert a partnership Meta disagreed with, and the listing
    has to be consulted regardless because it is what proves the account is one this
    organization may reach.

    No access token, and there never was one here: it is minted per client business
    portfolio and rotates roughly every sixty days, so a pasted value would be stale
    before it was useful. Asking a customer to mint a System User token in Meta
    Business Manager is skilled work in a console they were never meant to see, and
    it would say nothing about which solution the account came from or when it is
    revoked.
    """
