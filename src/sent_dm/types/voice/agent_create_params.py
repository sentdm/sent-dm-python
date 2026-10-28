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

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    audio: Optional[VoiceAgentAudioSpecParam]
    """Audio sessions only: the sound format."""

    fallback: Optional[VoiceAgentPartySpecParam]
    """Who takes the call when the agent cannot: a phone number (kind: number).

    Omit it and such a call hangs up.
    """

    greeting: Optional[str]
    """
    Text sessions only: what the caller hears as soon as the call is answered,
    before the agent's first turn. 1 to 4,096 characters. Omit it and the agent
    speaks first.
    """

    limits: Optional[VoiceAgentLimitsSpecParam]

    name: Optional[str]
    """A name for your own reference, 1 to 100 characters."""

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    session_type: Optional[str]
    """
    text: Sent turns the caller's speech into text and the agent's text into speech,
    so the agent exchanges text frames. audio: the agent receives and sends the
    sound itself.
    """

    speech: Optional[VoiceAgentSpeechSpecParam]
    """Text sessions only: how the caller is spoken to and listened to."""

    tools: Optional[SequenceNotStr[str]]
    """What the agent may do to the call: any of transfer, hangup, send_dtmf and hold.

    Default ["hangup"]. transfer needs at least one transfer_targets entry.
    """

    transcripts: Optional[VoiceAgentTranscriptsSpecParam]

    transfer_targets: Optional[Iterable[VoiceAgentPartySpecParam]]
    """
    Where the agent may transfer a call to, up to 20 parties: a phone number (kind:
    number, E.164), one of your app users (kind: user, the identity) or another of
    your agents (kind: agent, its id). The agent can only transfer to a party listed
    here.
    """

    websocket_url: Optional[str]
    """
    Where the gateway connects to the agent for each call: an absolute wss:// URL on
    a public host, at most 2,048 characters. The handshake is signed with the
    agent's signing_secret. Leave it out and the agent dials in instead, connecting
    to the gateway with your API key.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
