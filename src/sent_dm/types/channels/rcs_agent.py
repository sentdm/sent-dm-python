# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .rcs_address import RcsAddress

__all__ = ["RcsAgent"]


class RcsAgent(BaseModel):
    """
    An RCS agent as its owner sees it: the order form back, plus where the submission stands.

    Not RcsSenderResponse. That one is the admin projection and carries the pipeline we
    track about a customer's request — internalStatus, statusReason,
    isLaunched — and the S3 keys behind the assets. None of that is the customer's to read: an internal
    status is a note to ourselves, and an S3 key is a storage detail that would become a contract the moment
    it was published.

    What is here is what the caller sent, in the names it sent them under, plus the three things only we
    can answer: the record's id, its status, and the number it sends from. So a read after a
    write shows the form as stored rather than as echoed.
    """

    id: Optional[str] = None
    """The agent record.

    Stable across the whole approval, and what support will ask for.

    Nullable and omitted when absent: a sender profile with RCS intent records the
    channel but has no agent until the order form is submitted, so no id exists to
    report. A zero GUID is not a valid id and is worse than the field being absent.
    """

    agent_use_case: Optional[str] = None

    brand_color: Optional[str] = None

    brand_email: Optional[str] = None

    brand_name: Optional[str] = None

    brand_phone_number: Optional[str] = None

    brief_company_description: Optional[str] = None

    company_ein: Optional[str] = None

    contact_name_and_title: Optional[str] = None

    created_at: Optional[datetime] = None
    """
    Omitted when no real agent record exists — the intent-only path has no creation
    timestamp.
    """

    customer_support_email: Optional[str] = None

    customer_support_phone_number: Optional[str] = None

    description: Optional[str] = None

    display_name: Optional[str] = None

    entity_type: Optional[str] = None

    help_message: Optional[str] = None

    official_address: Optional[RcsAddress] = None
    """The registered address of the company behind the agent."""

    opt_in_process_description: Optional[str] = None

    phone_number: Optional[str] = None
    """The number the agent sends from, derived from brand_phone_number."""

    privacy_policy_url: Optional[str] = None

    reason: Optional[str] = None
    """A sentence for reason_code, saying what to do where it is yours.

    Omitted while ACTIVE.
    """

    reason_code: Optional[str] = None
    """
    Why the agent is not ACTIVE, as a stable code: an ErrorCodes CHANNEL_xxx value
    such as CHANNEL_001 (something you owe) or CHANNEL_009 (under review). Switch on
    this rather than on reason. Omitted while ACTIVE. Read-only; when nothing more
    specific is known it is the generic reason for the status.
    """

    sample_messages: Optional[List[str]] = None

    start_message: Optional[str] = None

    status: Optional[Literal["PROVISIONING", "ACTION_NEEDED", "PENDING_REVIEW", "ACTIVE", "INACTIVE"]] = None
    """
    Where the agent stands, in terms of who is holding it up — PROVISIONING,
    ACTION_NEEDED, PENDING_REVIEW or ACTIVE.

    Resolved from both of the provider's axes rather than reported raw: an agent
    whose resubmission we have asked for reads ACTION_NEEDED however its carrier
    status still reads, and an agent not yet handed over reads PROVISIONING rather
    than pending a review nobody has started.
    """

    stop_message: Optional[str] = None

    terms_and_conditions_url: Optional[str] = None

    website_url: Optional[str] = None
