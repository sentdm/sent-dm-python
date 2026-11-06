# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .sender_profile_channels_param import SenderProfileChannelsParam
from .channels.market_compliance_param import MarketComplianceParam
from .sender_profile_billing_request_param import SenderProfileBillingRequestParam

__all__ = ["SenderProfileCreateParams"]


class SenderProfileCreateParams(TypedDict, total=False):
    billing: Optional[SenderProfileBillingRequestParam]
    """Who pays for what a sender profile sends.

    Ownership reads the same way as BrandRequest and CampaignRequest: inherit: true
    is the organization paying; inherit: false (or an empty block) is the profile
    paying for itself.

    An absent block is the one place billing differs from brand and campaign: a
    profile still has to be paid for, so omitting billing stores
    ProfileAndOrganizationBilling — the profile pays first and its organization
    covers what the profile's balance cannot (see ResolveStored). { "name": "..." }
    stays a complete request.

    Billing carries no fields of its own yet, so a profile paying for itself is {
    "inherit": false } — or an empty block, which means the same. That is thinner
    than brand and campaign, where supplying data is the act of owning; it becomes
    ordinary the moment billing gains a contact or a payment method to carry.
    """

    channels: Optional[SenderProfileChannelsParam]
    """The channels the profile sends on.

    Each is independently the profile's own or absent — none can be inherited, so
    none carries a mode and presence is the whole of the request.

    A profile can send SMS in several markets, but create takes one — the market it
    starts in. Further markets are added through POST /v3/channels/sms with
    x-profile-id, and a read returns them all as a list. Create stays singular
    permanently rather than being a list that accepts one entry: the constraint is
    in the type, and there is no later widening to break the contract.
    """

    compliance: MarketComplianceParam
    """The compliance values a market registers with.

    `brand` and `campaign` apply to US `TEN_DLC`; other markets fill this map with
    the document keys their own requirements name.
    """

    description: Optional[str]

    name: str
    """Display name for the profile. Required."""

    notifications: Optional[str]
    """
    Who is notified about this profile's events: ORGANIZATION, SENDER_PROFILE, or
    ORGANIZATION_AND_SENDER_PROFILE. Omitting it leaves the profile on the
    Organization default.
    """

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    short_name: str
    """Short name, which is also the SMS sender id — required.

    3–11 characters of letters, numbers and spaces, with at least one letter.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
