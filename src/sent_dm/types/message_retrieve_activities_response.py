# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageRetrieveActivitiesResponse", "Data", "DataActivity", "Error", "Meta"]


class DataActivity(BaseModel):
    """A single message activity event for v3 API"""

    active_contact_price: Optional[str] = None
    """
    Active contact markup applied on top of the channel cost, formatted to 4 decimal
    places.
    """

    description: Optional[str] = None
    """Human-readable description of the activity"""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """
    Sender phone number for this activity (the customer's sending number for
    outbound, the external sender for inbound). Null when not reported by the
    provider.
    """

    price: Optional[str] = None
    """
    Channel cost for this activity (e.g., SMS/WhatsApp provider cost), formatted to
    4 decimal places.
    """

    status: Optional[str] = None
    """Activity status (e.g., QUEUED, PROCESSED, ROUTED, SENT, DELIVERED, FAILED)"""

    timestamp: Optional[datetime] = None
    """When this activity occurred"""


class Data(BaseModel):
    """Response for GET /messages/{id}/activities"""

    activities: Optional[List[DataActivity]] = None
    """List of activity events ordered by most recent first"""

    message_id: Optional[str] = None
    """The message ID these activities belong to"""


class Error(BaseModel):
    """Error information"""

    code: Optional[str] = None
    """Machine-readable error code (e.g., "RESOURCE_001")"""

    details: Optional[Dict[str, List[str]]] = None
    """Additional validation error details (field-level errors)"""

    doc_url: Optional[str] = None
    """URL to documentation about this error"""

    message: Optional[str] = None
    """Human-readable error message"""


class Meta(BaseModel):
    """Request and response metadata"""

    request_id: Optional[str] = None
    """Unique identifier for this request (for tracing and support)"""

    timestamp: Optional[datetime] = None
    """Server timestamp when the response was generated"""

    version: Optional[str] = None
    """API version used for this request"""


class MessageRetrieveActivitiesResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """Response for GET /messages/{id}/activities"""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
