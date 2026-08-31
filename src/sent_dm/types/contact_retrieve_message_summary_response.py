# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ContactRetrieveMessageSummaryResponse", "Data", "DataChannelScore", "Error", "Meta"]


class DataChannelScore(BaseModel):
    channel: Optional[str] = None

    fail_score: Optional[int] = None
    """Percentage (0-100) of messages on this channel that ended in FAILED."""

    success_score: Optional[int] = None
    """
    Percentage (0-100) of messages on this channel that reached a successful
    terminal state: SENT/DELIVERED/READ for outbound, RECEIVED for inbound.
    """


class Data(BaseModel):
    """The response data (null if error)"""

    channel_scores: Optional[List[DataChannelScore]] = None

    channels_used: Optional[List[str]] = None

    contact_id: Optional[str] = None

    first_message_at: Optional[datetime] = None

    last_message_at: Optional[datetime] = None

    message_count: Optional[int] = None


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


class ContactRetrieveMessageSummaryResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The response data (null if error)"""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
