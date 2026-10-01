# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .call_party import CallParty
from .call_timeline_entry import CallTimelineEntry

__all__ = ["Call"]


class Call(BaseModel):
    """A call record"""

    id: Optional[str] = None
    """
    The call id, the same one carried by the call.request question and every call
    webhook
    """

    answered_at: Optional[datetime] = None
    """When the call was answered (UTC).

    Null until then, and always null for a call between two of your app users
    """

    direction: Optional[str] = None
    """
    outbound for a call placed from your app, inbound for a call to one of your
    numbers
    """

    duration_seconds: Optional[int] = None
    """Billable duration in seconds. Null while the call is live"""

    ended_at: Optional[datetime] = None
    """When the call ended (UTC). Null while the call is live"""

    failure_reason: Optional[str] = None
    """
    Why the call did not complete: callback_timeout, invalid_answer,
    insufficient_balance, destination_blocked, rejected or no_answer. Null while the
    call is live, when it completed, and when it failed without a recorded reason
    """

    from_: Optional[CallParty] = FieldInfo(alias="from", default=None)
    """One end of a call"""

    number: Optional[str] = None
    """
    Your number that owns the call, in E.164 format: the dialed number for an
    inbound call, the caller's bound number for a call placed from your app
    """

    price: Optional[float] = None
    """What the call cost. Null until it has been priced"""

    recording_available: Optional[bool] = None
    """True once a recording of the call is available"""

    started_at: Optional[datetime] = None
    """When the call was placed (UTC)"""

    status: Optional[str] = None
    """initiated, ringing, answered, completed, failed, no_answer or rejected"""

    timeline: Optional[List[CallTimelineEntry]] = None
    """When the call entered each status, oldest first.

    Only returned when reading one call
    """

    to: Optional[CallParty] = None
    """One end of a call"""
