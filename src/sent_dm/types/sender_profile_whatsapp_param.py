# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SenderProfileWhatsappParam"]


class SenderProfileWhatsappParam(TypedDict, total=False):
    """
    The profile's own WhatsApp Business Account, named by the two identifiers the organization cannot answer
    for you.

    No mode: a profile's WABA is its own or it has none. Sharing the organization's would mean
    sharing its inbox and its throughput, which makes the two indistinguishable to a recipient — so
    inheriting is not offered rather than refused.

    Everything derivable is derived. Whenever this block is present, the solution the account
    arrived through, the client business portfolio that owns it, the access token and that token's expiry are
    all resolved from the organization by
    IPartnerSolutionService.ResolveAccountCredentialsAsync — the first two off the org's shared-account
    listing, the token minted against the org's own solution. They were previously asked for and are no
    longer accepted: solution_id and owner_business_id are Meta's answer about provenance, so
    taking them from the caller let a request assert a partnership Meta disagreed with, and the listing has to
    be consulted regardless because it is what proves the account is one this organization may reach.

    No access token, and there never was one here: it is minted per client business portfolio and
    rotates roughly every sixty days, so a pasted value would be stale before it was useful. Asking a
    customer to mint a System User token in Meta Business Manager is skilled work in a console they were
    never meant to see, and it would say nothing about which solution the account came from or when it is
    revoked.
    """

    phone_number_id: Optional[str]
    """The Meta phone-number id this profile sends from.

    Must already be registered under WabaId.

    Optional. Omit it to attach the account now and settle the number later: the
    channel reads as ACTION_NEEDED with CHANNEL_007, and the profile's WhatsApp
    messages fail until a number is named. They do not fall back to the
    organization's account. Nothing picks one on your behalf.
    """

    waba_id: Optional[str]
    """WhatsApp Business Account id — one of the accounts shared into your
    organization.

    Required: the organization holds one per client, and nothing but the caller says
    which belongs to this profile.
    """
