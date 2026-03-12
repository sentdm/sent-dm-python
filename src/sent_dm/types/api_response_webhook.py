# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .api_error import APIError
from .webhook_response import WebhookResponse

__all__ = ["APIResponseWebhook"]


class APIResponseWebhook(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[WebhookResponse] = None
    """The response data (null if error)"""

    error: Optional[APIError] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
