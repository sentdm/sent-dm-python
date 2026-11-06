# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail
from .channels_state import ChannelsState

__all__ = ["APIResponseOfChannelsState"]


class APIResponseOfChannelsState(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[ChannelsState] = None
    """The channels a profile sends on.

    SMS is a list because a profile can send in several markets; WhatsApp and RCS
    are single, because a profile has one business account and one agent.
    """

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
