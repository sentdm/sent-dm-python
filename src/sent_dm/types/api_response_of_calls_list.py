# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .calls_list import CallsList
from .error_detail import ErrorDetail

__all__ = ["APIResponseOfCallsList"]


class APIResponseOfCallsList(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[CallsList] = None
    """Paginated list of calls"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
