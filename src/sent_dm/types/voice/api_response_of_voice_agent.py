# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..api_meta import APIMeta
from .voice_agent import VoiceAgent
from ..error_detail import ErrorDetail

__all__ = ["APIResponseOfVoiceAgent"]


class APIResponseOfVoiceAgent(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[VoiceAgent] = None
    """
    A voice agent as stored: what was written with every default filled in, plus the
    signing secret the one time it is shown (on create, and on rotate). The one
    shape every read of an agent answers with, on /v3/voice/agents and on the admin
    API the dashboard uses, so the two cannot drift.
    """

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
