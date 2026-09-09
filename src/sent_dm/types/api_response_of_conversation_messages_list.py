# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail
from .conversation_messages_list import ConversationMessagesList

__all__ = ["APIResponseOfConversationMessagesList"]


class APIResponseOfConversationMessagesList(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[ConversationMessagesList] = None
    """A paginated list of messages — used by both conversation read endpoints."""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
