# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["VoiceAgentAudioSpecParam"]


class VoiceAgentAudioSpecParam(TypedDict, total=False):
    sample_rate: Optional[int]
    """Samples per second of the audio exchanged: 8000, 16000 or 24000. Default 16000."""
