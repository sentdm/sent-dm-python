# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .call_party import CallParty
from .call_timeline_entry import CallTimelineEntry

__all__ = ["Call", "Leg"]


class Leg(BaseModel):
    """One leg of a call the price covers"""

    billed_minutes: Optional[int] = None
    """The whole minutes the leg was billed for"""

    cost: Optional[float] = None
    """What the leg cost, in the same unit as the call's price"""

    currency: Optional[str] = None
    """The currency of the cost: USD"""

    direction: Optional[str] = None
    """
    inbound for the caller's leg to your number, outbound for a leg placed on your
    behalf
    """

    number: Optional[str] = None
    """
    The phone number the leg reached, in E.164 format: your number for the inbound
    leg, the number dialed for an outbound one. Null for a leg to one of your app
    users or a room
    """


class Call(BaseModel):
    """A call record"""

    id: Optional[str] = None
    """
    The call id, the same one carried by the call.request question and every call
    webhook
    """

    agent_id: Optional[str] = None
    """
    The voice agent that answered the call, such as
    agent_9f2ab000-0000-4000-8000-000000000001. Null for an inapp call
    """

    answered_at: Optional[datetime] = None
    """When the call was answered (UTC).

    Null until then, and always null for a call between two of your app users
    """

    caller_id_used: Optional[str] = None
    """
    The caller id shown on the phone leg, in E.164 format: the one your answer
    chose, or the owning number when it chose none. Null for a call with no phone
    leg
    """

    connected_number: Optional[str] = None
    """
    The phone number the call was connected to, in E.164 format: the number your
    answer dialed, or the fallback number a call to one of your voice agents
    reached. Null when the call was not connected to a phone number
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
    insufficient_balance, destination_blocked, callback_not_configured, rejected,
    no_answer, or for an agent call agent_busy or agent_unreachable. Null while the
    call is live, when it completed, and when it failed without a recorded reason
    """

    from_: Optional[CallParty] = FieldInfo(alias="from", default=None)
    """One end of a call"""

    legs: Optional[List[Leg]] = None
    """
    The legs the price covers, one entry per billed leg, each with its own cost: a
    call your answer connected to a phone number ran the caller's leg to your number
    and the leg to the connected number at once, and both are billed. Null until the
    call has been priced
    """

    mode: Optional[str] = None
    """
    The calling mode: inapp for a call between people in your app and phone numbers,
    routed by your number's callback URL; agent for a call one of your voice agents
    answered
    """

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
    """INITIATED, RINGING, ANSWERED, COMPLETED, FAILED, NO_ANSWER or REJECTED"""

    timeline: Optional[List[CallTimelineEntry]] = None
    """When the call entered each status, oldest first.

    Only returned when reading one call
    """

    to: Optional[CallParty] = None
    """One end of a call"""
