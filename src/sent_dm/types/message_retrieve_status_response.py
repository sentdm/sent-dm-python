# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .api_meta import APIMeta
from .api_error import APIError

__all__ = ["MessageRetrieveStatusResponse", "Data", "DataEvent", "DataMessageBody", "DataMessageBodyButton"]


class DataEvent(BaseModel):
    """Represents a status change event in a message's lifecycle (v3)"""

    description: Optional[str] = None

    status: Optional[str] = None

    timestamp: Optional[datetime] = None


class DataMessageBodyButton(BaseModel):
    type: Optional[str] = None

    value: Optional[str] = None


class DataMessageBody(BaseModel):
    """
    Structured message body format for database storage.
    Preserves channel-specific components (header, body, footer, buttons).
    """

    buttons: Optional[List[DataMessageBodyButton]] = None

    content: Optional[str] = None

    footer: Optional[str] = None

    header: Optional[str] = None


class Data(BaseModel):
    """The response data (null if error)"""

    id: Optional[str] = None

    channel: Optional[str] = None

    contact_id: Optional[str] = None

    created_at: Optional[datetime] = None

    customer_id: Optional[str] = None

    events: Optional[List[DataEvent]] = None

    message_body: Optional[DataMessageBody] = None
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


class MessageRetrieveStatusResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The response data (null if error)"""

    error: Optional[APIError] = None
    """Error details (null if successful)"""

    meta: Optional[APIMeta] = None
    """Metadata about the request and response"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
