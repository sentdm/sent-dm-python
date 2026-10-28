# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["VoiceAgentSpeech"]


class VoiceAgentSpeech(BaseModel):
    language: Optional[str] = None

    setting: Optional[str] = None

    voice: Optional[str] = None
