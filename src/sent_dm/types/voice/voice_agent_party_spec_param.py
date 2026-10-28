# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["VoiceAgentPartySpecParam"]


class VoiceAgentPartySpecParam(TypedDict, total=False):
    kind: Optional[str]
    """number, user or agent."""

    value: Optional[str]
    """The E.164 number, the app user's identity, or the agent id (agent\\__…)."""
