# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail

__all__ = [
    "MessageRetrieveStatusResponse",
    "Data",
    "DataEvent",
    "DataMessageBody",
    "DataMessageBodyButton",
    "DataMessageBodyHeaderMedia",
    "DataMessageBodyMedia",
]


class DataEvent(BaseModel):
    """Represents a status change event in a message's lifecycle (v3)"""

    status: str

    timestamp: datetime

    description: Optional[str] = None


class DataMessageBodyButton(BaseModel):
    postback_data: Optional[str] = FieldInfo(alias="postbackData", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    value: Optional[str] = None


class DataMessageBodyHeaderMedia(BaseModel):
    """The media asset that rode a message's header, recorded as sent."""

    type: Optional[str] = None
    """\"image", "video" or "document" — taken from the header's media variable."""

    url: Optional[str] = None
    """The https URL the caller supplied for this send.

    Never the template's stored props.sample, which is Meta's expiring header_handle
    rather than what was delivered.
    """


class DataMessageBodyMedia(BaseModel):
    """
    One attachment on a message: a customer-supplied public URL handed to the carrier as-is.

                 A URL and nothing else. sent.dm never takes custody of MMS media — the customer hosts it and we
                 pass the link through at send time — so there is no storage key, size or expiry to record. If we ever
                 do host attachments, that belongs with the change that introduces the hosting, not here.
    """

    media_type: Optional[str] = FieldInfo(alias="mediaType", default=None)
    """One of Constants.MmsMediaTypes when known.

    Advisory — the carrier reads the fetched object's Content-Type, not this.
    """

    url: Optional[str] = None


class DataMessageBody(BaseModel):
    """
    Structured message body format for database storage.
    Preserves channel-specific components (header, header media, body, footer, buttons, MMS subject
    and media).

    Persisted as the messageBody jsonb column on Messages. Every write path goes
    through MessageUtils.MessageBodyJsonOptions, which writes nulls, so the envelope shape is
    stable regardless of channel or status. Anything that rebuilds this object field by field — the
    four IMessageBodyStrategy implementations and MessageUtils.BuildSegmentBody — has to
    carry every member, or that member is silently dropped on whichever path forgot it.
    """

    buttons: Optional[List[DataMessageBodyButton]] = None

    content: Optional[str] = None

    footer: Optional[str] = None

    header: Optional[str] = None

    header_media: Optional[DataMessageBodyHeaderMedia] = FieldInfo(alias="headerMedia", default=None)
    """The media asset that rode a message's header, recorded as sent."""

    media: Optional[List[DataMessageBodyMedia]] = None
    """MMS attachments, as the publicly fetchable URLs handed to the carrier.

    Null on every other channel.

    Persisted rather than derived because a resend and a curfew release rebuild the
    send from the stored row — MessageReplayCommandBuilder reads templateId and
    templateVariables and nothing else — so media that lives only on the original
    request would silently turn a replayed MMS into a text message.
    """

    subject: Optional[str] = None
    """MMS subject line. Null on every other channel."""


class Data(BaseModel):
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

    events: Optional[List[DataEvent]] = None

    message_body: Optional[DataMessageBody] = None
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

    region_code: Optional[str] = None

    status: Optional[str] = None

    template_category: Optional[str] = None

    template_id: Optional[str] = None

    template_name: Optional[str] = None


class MessageRetrieveStatusResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """Message response for v3 API — same shape as v2 with snake_case JSON conventions.

    The shape of a message that was sent immediately: it never has a scheduled_at
    key. A message that is or was held for a later instant is a
    ScheduledMessageResponse, and the endpoint decides which of the two to answer
    with. From always returns this type.
    """

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
