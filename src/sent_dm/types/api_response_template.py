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
    """The response data (null if error)"""

    error: Optional[APIError] = None
    """Error details (null if successful)"""

    meta: Optional[APIMeta] = None
    """Metadata about the request and response"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
