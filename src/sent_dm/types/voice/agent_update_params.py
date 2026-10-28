# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .voice_agent_audio_spec_param import VoiceAgentAudioSpecParam
from .voice_agent_party_spec_param import VoiceAgentPartySpecParam
from .voice_agent_limits_spec_param import VoiceAgentLimitsSpecParam
from .voice_agent_speech_spec_param import VoiceAgentSpeechSpecParam
from .voice_agent_transcripts_spec_param import VoiceAgentTranscriptsSpecParam

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    audio: Optional[VoiceAgentAudioSpecParam]
    """Audio sessions: { sample_rate }; null restores the default."""

    fallback: Optional[VoiceAgentPartySpecParam]
    """A new fallback party, or null for none."""

    greeting: Optional[str]
    """A new greeting, or null for none."""

    limits: Optional[VoiceAgentLimitsSpecParam]
    """The whole limits object; null restores the defaults."""

    name: str
    """A new name, 1 to 100 characters."""

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    session_type: str
    """text or audio.

    Changing it drops the settings the other type cannot have (speech, audio,
    greeting) unless the body sends them.
    """

    speech: Optional[VoiceAgentSpeechSpecParam]
    """
    Text sessions: { setting, voice, language }, replaced whole; null restores the
    defaults.
    """

    tools: Optional[SequenceNotStr[str]]
    """The whole list of tools; null restores the default."""

    transcripts: Optional[VoiceAgentTranscriptsSpecParam]
    """The whole transcripts object; null restores the defaults."""

    transfer_targets: Optional[Iterable[VoiceAgentPartySpecParam]]
    """The whole list of parties; null clears it."""

    websocket_url: Optional[str]
    """A new wss:// URL, or null for an agent that dials in."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
