# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .voice_agent import VoiceAgent
from ..pagination_meta import PaginationMeta

__all__ = ["VoiceAgentsList"]


class VoiceAgentsList(BaseModel):
    """A page of the account's agents.

    The agent itself is VoiceAgentResponse, shared with the admin API.
    """

    agents: Optional[List[VoiceAgent]] = None

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""
