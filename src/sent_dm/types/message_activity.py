# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageActivity"]


class MessageActivity(BaseModel):
    """
    A single message activity event for v3 API.

    The activity list mixes statuses, so unlike a message it is one shape rather than two: a SCHEDULED
    entry carries scheduled_at, and every other entry has no such key.
    """

    active_contact_price: Optional[str] = None
    """
    Active contact markup applied on top of the channel cost, formatted to 4 decimal
    places.
    """

    description: Optional[str] = None
    """Human-readable description of the activity"""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """
    Sender phone number for this activity (the customer's sending number for
    outbound, the external sender for inbound). Null when not reported by the
    provider.
    """

    price: Optional[str] = None
    """
    Channel cost for this activity (e.g., SMS/WhatsApp provider cost), formatted to
    4 decimal places.
    """

    reason: Optional[str] = None
    """
    A human-readable sentence for reason_code, for example "The recipient is not
    registered on this channel" Omitted whenever reason_code is.
    """

    reason_code: Optional[str] = None
    """
    Why the message reached this status, as a stable platform code such as
    DELIVERY_007 or BUSINESS_003. Present on FAILED, FILTERED and BLOCKED
    activities; omitted on every status that needs no explanation. Switch on this
    rather than on reason: the code is stable, the wording may be improved. Same
    wire name and vocabulary as on the message and the webhook.
    """

    scheduled_at: Optional[datetime] = None
    """
    SCHEDULED and CANCELLED activities only, in UTC: on a SCHEDULED entry, when the
    held message will be released for delivery; on a CANCELLED entry, the instant
    that was called off. Same wire name as on the send response, the message and the
    webhook. Omitted on every other activity. A message that quiet hours moved at
    release has two SCHEDULED entries, each carrying the instant as it stood at that
    moment.
    """

    status: Optional[str] = None
    """Activity status.

    Outbound: QUEUED, PROCESSED, ROUTED, SCHEDULED, SENT, DELIVERED, READ, FAILED.
    Inbound (from contact): RECEIVED (terminal).
    """

    timestamp: Optional[datetime] = None
    """When this activity occurred"""
