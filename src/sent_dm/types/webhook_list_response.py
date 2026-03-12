# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .api_error import APIError
from .pagination_meta import PaginationMeta
from .webhook_response import WebhookResponse

__all__ = ["WebhookListResponse", "Data"]


class Data(BaseModel):
    """The response data (null if error)"""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""

    webhooks: Optional[List[WebhookResponse]] = None


class WebhookListResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The response data (null if error)"""

    error: Optional[APIError] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
