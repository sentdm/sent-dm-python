# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["VoiceAgentLimits"]


class VoiceAgentLimits(BaseModel):
    allowed_countries: Optional[List[str]] = None

    max_call_seconds: Optional[int] = None

    max_concurrent_calls: Optional[int] = None
