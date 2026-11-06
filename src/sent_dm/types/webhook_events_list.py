# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .webhook_delivery import WebhookDelivery

__all__ = ["WebhookEventsList"]


class WebhookEventsList(BaseModel):
    """A paginated list of webhook delivery records."""

    events: Optional[List[WebhookDelivery]] = None
    """The events on this page."""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""
