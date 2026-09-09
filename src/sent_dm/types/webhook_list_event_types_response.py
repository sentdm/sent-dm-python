# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail
from .pagination_meta import PaginationMeta

__all__ = ["WebhookListEventTypesResponse", "Data"]


class Data(BaseModel):
    """The webhook event types a customer can subscribe to."""

    event_types: Optional[List["WebhookEventType"]] = None
    """The event_types on this page."""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""


class WebhookListEventTypesResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The webhook event types a customer can subscribe to."""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""


from .webhook_event_type import WebhookEventType
