# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ContactMessageSummary", "ChannelScore"]


class ChannelScore(BaseModel):
    channel: Optional[str] = None

    fail_score: Optional[int] = None
    """Percentage (0-100) of messages on this channel that ended in FAILED."""

    success_score: Optional[int] = None
    """
    Percentage (0-100) of messages on this channel that reached a successful
    terminal state: SENT/DELIVERED/READ for outbound, RECEIVED for inbound.
    """


class ContactMessageSummary(BaseModel):
    channel_scores: Optional[List[ChannelScore]] = None

    channels_used: Optional[List[str]] = None

    contact_id: Optional[str] = None

    first_message_at: Optional[datetime] = None

    last_message_at: Optional[datetime] = None

    message_count: Optional[int] = None
