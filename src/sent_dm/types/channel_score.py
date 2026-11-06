# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ChannelScore"]


class ChannelScore(BaseModel):
    channel: Optional[str] = None

    fail_score: Optional[int] = None
    """Percentage (0-100) of messages on this channel that ended in FAILED."""

    success_score: Optional[int] = None
    """
    Percentage (0-100) of messages on this channel that reached a successful
    terminal state: SENT/DELIVERED/READ for outbound, RECEIVED for inbound.
    """
