# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = [
    "ConversationMessagesList",
    "Message",
    "MessageEvent",
    "MessageMessageBody",
    "MessageMessageBodyButton",
    "MessageMessageBodyHeaderMedia",
]


class MessageEvent(BaseModel):
    """Represents a status change event in a message's lifecycle (v3)"""

    status: str

    timestamp: datetime

    description: Optional[str] = None


class MessageMessageBodyButton(BaseModel):
    postback_data: Optional[str] = FieldInfo(alias="postbackData", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    value: Optional[str] = None


class MessageMessageBodyHeaderMedia(BaseModel):
    """The media asset that rode a message's header, recorded as sent."""

    type: Optional[str] = None
    """\"image", "video" or "document" — taken from the header's media variable."""

    url: Optional[str] = None
    """The https URL the caller supplied for this send.

    Never the template's stored props.sample, which is Meta's expiring header_handle
    rather than what was delivered.
    """


class MessageMessageBody(BaseModel):
    """
    Structured message body format for database storage.
    Preserves channel-specific components (header, body, footer, buttons).
    """

    buttons: Optional[List[MessageMessageBodyButton]] = None

    content: Optional[str] = None

    footer: Optional[str] = None

    header: Optional[str] = None

    header_media: Optional[MessageMessageBodyHeaderMedia] = FieldInfo(alias="headerMedia", default=None)
    """The media asset that rode a message's header, recorded as sent."""


class Message(BaseModel):
    """Message response for v3 API — same shape as v2 with snake_case JSON conventions"""

    id: Optional[str] = None

    active_contact_price: Optional[float] = None

    channel: Optional[str] = None

    contact_id: Optional[str] = None

    created_at: Optional[datetime] = None

    customer_id: Optional[str] = None

    direction: Optional[str] = None

    events: Optional[List[MessageEvent]] = None

    message_body: Optional[MessageMessageBody] = None
    """
    Structured message body format for database storage. Preserves channel-specific
    components (header, body, footer, buttons).
    """

    phone: Optional[str] = None

    phone_international: Optional[str] = None

    price: Optional[float] = None

    region_code: Optional[str] = None

    status: Optional[str] = None

    template_category: Optional[str] = None

    template_id: Optional[str] = None

    template_name: Optional[str] = None


class ConversationMessagesList(BaseModel):
    """A paginated list of messages — used by both conversation read endpoints."""

    messages: Optional[List[Message]] = None
    """The messages on this page."""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""
