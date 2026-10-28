# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["VoiceAgentLimitsSpecParam"]


class VoiceAgentLimitsSpecParam(TypedDict, total=False):
    allowed_countries: Optional[SequenceNotStr[str]]
    """ISO 3166-1 alpha-2 codes of the countries the agent may call or transfer to.

    Omit it to allow every country. Stored now, applied when the agent places calls.
    """

    max_call_seconds: Optional[int]
    """The longest a call may last, 60 to 14,400 seconds. Default 3,600."""

    max_concurrent_calls: Optional[int]
    """How many calls the agent may have going at once, from 1. Default 10."""
