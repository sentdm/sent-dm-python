# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta

__all__ = ["WebhookEventTypesList"]


class WebhookEventTypesList(BaseModel):
    """The webhook event types a customer can subscribe to."""

    event_types: Optional[List["WebhookEventType"]] = None
    """The event_types on this page."""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""


from .webhook_event_type import WebhookEventType
