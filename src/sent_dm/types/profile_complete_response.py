# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail

__all__ = ["ProfileCompleteResponse", "Data"]


class Data(BaseModel):
    """
    Response when a profile is already in the completed state and no further action is taken.
    """

    message: Optional[str] = None
    """Human-readable message describing the result."""

    status: Optional[str] = None
    """
    Current process status of the profile (e.g., "completed", "submitted",
    "in_progress").
    """


class ProfileCompleteResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
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
