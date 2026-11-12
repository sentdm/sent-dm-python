# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .message_body import MessageBody
from .message_status_event import MessageStatusEvent

__all__ = ["Message"]


class Message(BaseModel):
    """
    Message response for v3 API — same shape as v2 with snake_case JSON conventions.

    The shape of a message that was sent immediately: it never has a scheduled_at key. A message that is
    or was held for a later instant is a ScheduledMessageResponse, and the endpoint decides which of
    the two to answer with. From
    always returns this type.
    """

    id: Optional[str] = None

    active_contact_price: Optional[float] = None

    channel: Optional[str] = None

    contact_id: Optional[str] = None

    created_at: Optional[datetime] = None

    customer_id: Optional[str] = None

    direction: Optional[str] = None

    events: Optional[List[MessageStatusEvent]] = None

    message_body: Optional[MessageBody] = None
    """
    Structured message body format for database storage. Preserves channel-specific
    components (header, header media, body, footer, buttons, MMS subject and media).

    Persisted as the messageBody jsonb column on Messages. Every write path goes
    through MessageUtils.MessageBodyJsonOptions, which writes nulls, so the envelope
    shape is stable regardless of channel or status. Anything that rebuilds this
    object field by field — the four IMessageBodyStrategy implementations and
    MessageUtils.BuildSegmentBody — has to carry every member, or that member is
    silently dropped on whichever path forgot it.
    """

    phone: Optional[str] = None

    phone_international: Optional[str] = None

    price: Optional[float] = None

    reason: Optional[str] = None
    """A human-readable sentence for reason_code, for example "Insufficient balance".

    Omitted whenever reason_code is.
    """

    reason_code: Optional[str] = None
    """
    Why the message is at its current status, as a stable platform code such as
    DELIVERY_007, BUSINESS_003 or DELIVERY_003. Present when the current status is
    FAILED, FILTERED or BLOCKED and the lifecycle was loaded; omitted otherwise.
    Switch on this rather than on reason: the code is stable, the wording may be
    improved. It is the platform's classification of the outcome, never a carrier or
    vendor code.
    """

    region_code: Optional[str] = None

    status: Optional[str] = None

    template_category: Optional[str] = None

    template_id: Optional[str] = None

    template_name: Optional[str] = None
