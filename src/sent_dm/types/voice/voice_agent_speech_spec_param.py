# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["VoiceAgentSpeechSpecParam"]


class VoiceAgentSpeechSpecParam(TypedDict, total=False):
    language: Optional[str]
    """The language spoken and listened for, a BCP 47 tag from GET /v3/voice/voices.

    Default en-US.
    """

    setting: Optional[str]
    """standard, Sent's speech. Other settings are not available yet."""

    voice: Optional[str]
    """A voice name from GET /v3/voice/voices. Default: the catalogue's default voice."""
