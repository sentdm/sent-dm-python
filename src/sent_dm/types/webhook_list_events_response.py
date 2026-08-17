# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail
from .message_event import MessageEvent
from .template_event import TemplateEvent
from .pagination_meta import PaginationMeta
from .inbound_message_event import InboundMessageEvent

__all__ = ["WebhookListEventsResponse", "Data", "DataEvent", "DataEventEventData"]

DataEventEventData: TypeAlias = Union[MessageEvent, InboundMessageEvent, TemplateEvent]


class DataEvent(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    delivery_attempts: Optional[int] = None

    delivery_status: Optional[str] = None

    error_message: Optional[str] = None

    event_data: Optional[DataEventEventData] = None
    """The exact event body that was delivered, or attempted, for this record.

    One of the three webhook envelopes: a message status change, an inbound message,
    or a template status change. Read field and event to tell which, the same way
    your endpoint does.
    """

    event_type: Optional[str] = None

    http_status_code: Optional[int] = None

    processing_completed_at: Optional[datetime] = None

    processing_started_at: Optional[datetime] = None

    response_body: Optional[str] = None


class Data(BaseModel):
    """The response data (null if error)"""

    events: Optional[List[DataEvent]] = None

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""


class WebhookListEventsResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The response data (null if error)"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
