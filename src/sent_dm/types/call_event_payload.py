# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CallEventPayload"]


class CallEventPayload(BaseModel):
    """
    Body of a call.initiated, call.answered, call.completed, call.failed
    or call.recording_ready event. Which of them occurred is the envelope's event.

    Shaped like the message, inbound, template and channel payloads: account_id names the
    account the event is about, channel names the channel, and updated_at is when the change
    happened on the call, in the same yyyy-MM-ddTHH:mm:ssZ form. duration_seconds and
    price are added on call.completed, reason on call.failed and
    recording_id on call.recording_ready; each is omitted rather than sent as null when it
    does not apply.

    Casing is snake_case because these ride the same webhook stream customers already parse
    message_id from; the question/answer contract is a separate surface and stays camelCase.
    Nothing here is provider-shaped: no provider call id, no namespaced identity.
    """

    call_id: str
    """Sent's call id, the same one the customer saw on the first question."""

    account_id: Optional[str] = None
    """
    The account the call belongs to: the key's own customer, or the sender profile
    it acted as.
    """

    channel: Optional[str] = None
    """Always voice."""

    duration_seconds: Optional[int] = None
    """How long the call lasted. Only on call.completed."""

    number: Optional[str] = None
    """The customer number that owns the call, in E.164 format."""

    price: Optional[float] = None
    """What the call was charged.

    Only on call.completed, and omitted there until billing has recorded the charge.
    """

    reason: Optional[str] = None
    """The machine-readable reason the call did not complete.

    Only on call.failed, and omitted when no reason was recorded.
    """

    recording_id: Optional[str] = None
    """
    The recording that became available, the same id GET /v3/calls/{id}/recordings
    lists it under. Only on call.recording_ready, which is sent once per recording.
    """

    updated_at: Optional[str] = None
    """When the change happened on the call, as opposed to when the event was emitted."""
