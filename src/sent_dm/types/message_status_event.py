# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["MessageStatusEvent"]


class MessageStatusEvent(BaseModel):
    """Represents a status change event in a message's lifecycle (v3)"""

    status: str

    timestamp: datetime

    description: Optional[str] = None

    reason: Optional[str] = None
    """A human-readable sentence for reason_code. Omitted whenever reason_code is."""

    reason_code: Optional[str] = None
    """
    Why the message reached this status, as a stable platform code such as
    DELIVERY_007. Present on FAILED, FILTERED and BLOCKED events; omitted on every
    status that needs no explanation. Same wire name and vocabulary as on the
    activities list and the webhook.
    """
