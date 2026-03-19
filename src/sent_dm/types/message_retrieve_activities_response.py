# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail

__all__ = ["MessageRetrieveActivitiesResponse", "Data", "DataActivity"]


class DataActivity(BaseModel):
    """A single message activity event for v3 API"""

    active_contact_price: Optional[str] = None
    """
    Active contact markup applied on top of the channel cost, formatted to 4 decimal
    places.
    """

    description: Optional[str] = None
    """Human-readable description of the activity"""

    price: Optional[str] = None
    """
    Channel cost for this activity (e.g., SMS/WhatsApp provider cost), formatted to
    4 decimal places.
    """

    status: Optional[str] = None
    """Activity status (e.g., QUEUED, PROCESSED, SENT, DELIVERED, FAILED)"""

    timestamp: Optional[datetime] = None
    """When this activity occurred"""


class Data(BaseModel):
    """Response for GET /messages/{id}/activities"""

    activities: Optional[List[DataActivity]] = None
    """List of activity events ordered by most recent first"""

    message_id: Optional[str] = None
    """The message ID these activities belong to"""


class MessageRetrieveActivitiesResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """Response for GET /messages/{id}/activities"""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
