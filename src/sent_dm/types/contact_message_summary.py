# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .channel_score import ChannelScore

__all__ = ["ContactMessageSummary"]


class ContactMessageSummary(BaseModel):
    channel_scores: Optional[List[ChannelScore]] = None

    channels_used: Optional[List[str]] = None

    contact_id: Optional[str] = None

    first_message_at: Optional[datetime] = None

    last_message_at: Optional[datetime] = None

    message_count: Optional[int] = None
