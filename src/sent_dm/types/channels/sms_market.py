# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .sms_number import SMSNumber
from .supplied_compliance import SuppliedCompliance

__all__ = ["SMSMarket"]


class SMSMarket(BaseModel):
    """
    One SMS market the profile sends in — its sender, where that sender stands, and what the market wants.

    A profile may send in several: it is a tenant, not a market. Each carries its own status, because
    a profile can be live in one country and mid-registration in another — and each carries what it still owes,
    rather than that being reported in a separate array a caller has to join on.
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
