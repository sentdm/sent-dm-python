# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageRetrieveResponse", "Event", "MessageBody", "MessageBodyButton"]


class Event(BaseModel):
    """
    Represents a status change event in a message's lifecycle
    Follows industry standards (Twilio, SendGrid, Mailgun pattern)
    """

    description: Optional[str] = None
    """
    Optional human-readable description of the event Useful for error messages or
    additional context
    """

    status: Optional[str] = None
    """
    The status of the message at this point in time Examples: "queued", "sent",
    "delivered", "read", "failed"
    """

    timestamp: Optional[datetime] = None
    """When this status change occurred (ISO 8601 format)"""


class MessageBodyButton(BaseModel):
    type: Optional[str] = None

    value: Optional[str] = None


class MessageBody(BaseModel):
    """The message body content with variables substituted"""

    buttons: Optional[List[MessageBodyButton]] = None

    content: Optional[str] = None

    footer: Optional[str] = None

    header: Optional[str] = None


class MessageRetrieveResponse(BaseModel):
    """
    Represents a sent message with comprehensive delivery and template information (v2)
    """

    id: Optional[str] = None
    """The unique identifier of the message"""

    channel: Optional[str] = None
    """The messaging channel used (e.g., SMS, WhatsApp)"""

    contact_id: Optional[str] = FieldInfo(alias="contactId", default=None)
    """The unique identifier of the contact who received the message"""

    corrected_price: Optional[float] = FieldInfo(alias="correctedPrice", default=None)
    """The final price charged for sending this message"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time when the message was created"""

    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)
    """The unique identifier of the customer who sent the message"""

    events: Optional[List[Event]] = None
    """
    A chronological list of status change events for this message. Each event
    includes a status and timestamp, following industry standards (Twilio, SendGrid,
    Mailgun). Events are ordered chronologically from oldest to newest.
    """

    message_body: Optional[MessageBody] = FieldInfo(alias="messageBody", default=None)
    """The message body content with variables substituted"""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """The phone number of the recipient (E.164 format)"""

    phone_number_international: Optional[str] = FieldInfo(alias="phoneNumberInternational", default=None)
    """The phone number in international format"""

    region_code: Optional[str] = FieldInfo(alias="regionCode", default=None)
    """The region code of the phone number (e.g., US, GB, DE)"""

    status: Optional[str] = None
    """The delivery status of the message (e.g., sent, delivered, failed, read)"""

    template_category: Optional[str] = FieldInfo(alias="templateCategory", default=None)
    """The category of the template (e.g., MARKETING, UTILITY, AUTHENTICATION)"""

    template_id: Optional[str] = FieldInfo(alias="templateId", default=None)
    """
    The unique identifier of the template used for this message (null if no template
    was used)
    """

    template_name: Optional[str] = FieldInfo(alias="templateName", default=None)
    """The display name of the template"""
