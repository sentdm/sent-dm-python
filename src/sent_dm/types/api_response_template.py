# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .template import Template
from .api_error import APIError

__all__ = ["APIResponseTemplate"]


class APIResponseTemplate(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Template] = None
    """Template response for v3 API"""

    error: Optional[APIError] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
