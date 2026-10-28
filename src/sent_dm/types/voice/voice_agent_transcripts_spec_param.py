# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["VoiceAgentTranscriptsSpecParam"]


class VoiceAgentTranscriptsSpecParam(TypedDict, total=False):
    retention_days: Optional[int]
    """How long a stored transcript is kept, 1 to 365 days. Default 30."""

    store: Optional[bool]
    """Whether Sent keeps the call's transcript.

    Default false. Stored now, applied when transcripts land.
    """
