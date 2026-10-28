# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .voice_agent_audio import VoiceAgentAudio
from .voice_agent_party import VoiceAgentParty
from .voice_agent_limits import VoiceAgentLimits
from .voice_agent_speech import VoiceAgentSpeech
from .voice_agent_transcripts import VoiceAgentTranscripts

__all__ = ["VoiceAgent"]


class VoiceAgent(BaseModel):
    """
    A voice agent as stored: what was written with every default filled in, plus the signing secret the one
    time it is shown (on create, and on rotate). The one shape every read of an agent answers with, on
    /v3/voice/agents and on the admin API the dashboard uses, so the two cannot drift.
    """

    id: Optional[str] = None
    """The agent's id, agent\\__ and a UUID.

    It is also what the agent connects to the gateway as.
    """

    audio: Optional[VoiceAgentAudio] = None
    """Audio sessions: the sample rate in use."""

    created_at: Optional[datetime] = None

    fallback: Optional[VoiceAgentParty] = None

    greeting: Optional[str] = None

    limits: Optional[VoiceAgentLimits] = None

    name: Optional[str] = None

    session_type: Optional[str] = None
    """text or audio."""

    signing_secret: Optional[str] = None
    """The whsec\\__ secret the gateway signs its handshake to websocket_url with.

    Present on create and after a rotate-secret; absent on every other read. Store
    it now.
    """

    speech: Optional[VoiceAgentSpeech] = None
    """Text sessions: the speech setting, voice and language in use."""

    tools: Optional[List[str]] = None

    transcripts: Optional[VoiceAgentTranscripts] = None

    transfer_targets: Optional[List[VoiceAgentParty]] = None

    updated_at: Optional[datetime] = None

    websocket_url: Optional[str] = None
    """
    Where the gateway dials the agent; null when the agent dials in with your API
    key.
    """
