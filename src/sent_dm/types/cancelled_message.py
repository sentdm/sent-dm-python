# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .message import Message

__all__ = ["CancelledMessage"]


class CancelledMessage(Message):
    """
    Message response for v3 API — same shape as v2 with snake_case JSON conventions.

    The shape of a message that was sent immediately: it never has a scheduled_at key. A message that is
    or was held for a later instant is a ScheduledMessageResponse, and the endpoint decides which of
    the two to answer with. From
    always returns this type.
    """

    scheduled_at: Optional[datetime] = None
    """
    The send time that was called off, in UTC — the scheduled_at the message was
    being held for, whether you set it or the recipient's quiet hours moved it
    there. Omitted only for a held message that carried no recorded instant.
    """
