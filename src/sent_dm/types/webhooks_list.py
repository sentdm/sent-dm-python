# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .webhook_response import WebhookResponse

__all__ = ["WebhooksList"]


class WebhooksList(BaseModel):
    """A paginated list of webhooks."""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""

    webhooks: Optional[List[WebhookResponse]] = None
    """The webhooks on this page."""
