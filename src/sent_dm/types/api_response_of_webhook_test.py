# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail
from .webhook_test import WebhookTest

__all__ = ["APIResponseOfWebhookTest"]


class APIResponseOfWebhookTest(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[WebhookTest] = None
    """The response data (null if error)"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
