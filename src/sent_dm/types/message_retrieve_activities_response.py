# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .api_meta import APIMeta
from .api_error import APIError

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
    """Activity status (e.g., ACCEPTED, PROCESSED, SENT, DELIVERED, FAILED)"""

    timestamp: Optional[datetime] = None
    """When this activity occurred"""


class Data(BaseModel):
    """The response data (null if error)"""

    activities: Optional[List[DataActivity]] = None
    """List of activity events ordered by most recent first"""

    message_id: Optional[str] = None
    """The message ID these activities belong to"""


class MessageRetrieveActivitiesResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The response data (null if error)"""

    error: Optional[APIError] = None
    """Error details (null if successful)"""

    meta: Optional[APIMeta] = None
    """Metadata about the request and response"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
