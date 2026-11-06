# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail
from .profile_completion_result import ProfileCompletionResult

__all__ = ["APIResponseOfProfileCompletionResult"]


class APIResponseOfProfileCompletionResult(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[ProfileCompletionResult] = None
    """
    Response when a profile is already in the completed state and no further action
    is taken.
    """

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
