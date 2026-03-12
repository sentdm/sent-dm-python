# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail

__all__ = ["WebhookListEventTypesResponse", "Data", "DataEventType"]


class DataEventType(BaseModel):
    description: Optional[str] = None

    display_name: Optional[str] = None

    is_active: Optional[bool] = None

    name: Optional[str] = None


class Data(BaseModel):
    """The response data (null if error)"""

    event_types: Optional[List[DataEventType]] = None


class WebhookListEventTypesResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The response data (null if error)"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
