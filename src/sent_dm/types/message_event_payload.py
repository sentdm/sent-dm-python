# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MessageEventPayload"]


class MessageEventPayload(BaseModel):
    """Body of an outbound message lifecycle event.

    Delivered once per status change, so a single
    message produces several of these as it moves toward a terminal status.
    """

    message_status: str
    """The status the message just reached, for example SENT, DELIVERED, or FAILED.

    Sent means dispatched and delivered means confirmed, so treat them as distinct
    outcomes.
    """

    account_id: Optional[str] = None
    """The account the message belongs to."""

    agent_id: Optional[str] = None
    """The agent attributed to the send, when the send was attributed to one."""

    channel: Optional[str] = None
    """The channel the message went out on, for example sms or whatsapp.

    A message that falls back to another channel reports the channel actually used.
    """

    message_id: Optional[str] = None
    """The message this event describes.

    Stable across every event in the message's lifecycle, so use it to correlate
    them.
    """

    outbound_number: Optional[str] = None
    """The recipient's number in E.164 format."""

    template_id: Optional[str] = None
    """The template the message was sent from, when it was sent from one."""

    template_name: Optional[str] = None
    """Name of the template the message was sent from.

    Omitted when the message wasn't template-based.
    """

    updated_at: Optional[str] = None
    """When the message reached MessageStatus, in UTC (yyyy-MM-ddTHH:mm:ssZ)."""
