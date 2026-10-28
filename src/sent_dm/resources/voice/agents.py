# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncVoiceAgentsPage, AsyncVoiceAgentsPage
from ...types.voice import (
    agent_list_params,
    agent_create_params,
    agent_delete_params,
    agent_update_params,
    agent_rotate_secret_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.voice.voice_agent import VoiceAgent
from ...types.voice.api_response_of_voice_agent import APIResponseOfVoiceAgent
from ...types.voice.voice_agent_audio_spec_param import VoiceAgentAudioSpecParam
from ...types.voice.voice_agent_party_spec_param import VoiceAgentPartySpecParam
from ...types.voice.voice_agent_limits_spec_param import VoiceAgentLimitsSpecParam
from ...types.voice.voice_agent_speech_spec_param import VoiceAgentSpeechSpecParam
from ...types.voice.api_response_of_voice_agent_secret import APIResponseOfVoiceAgentSecret
from ...types.voice.voice_agent_transcripts_spec_param import VoiceAgentTranscriptsSpecParam

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    """Phone calls from the numbers you hold, driven by your own callback URL.

    `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

    Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.

    **Voice agents.** `POST /v3/voice/agents` creates an agent that answers calls through the Sent Voice Gateway: `session_type` says whether Sent carries the call as text (speech recognised and spoken for the agent) or as audio, `websocket_url` is where the gateway dials the agent for each call (leave it out and the agent dials in with your API key), and `tools`, `transfer_targets`, `fallback` and `limits` say what it may do on a call. The agent's `signing_secret` is shown on create and on `POST /v3/voice/agents/{id}/rotate-secret` only. Voices and languages for text sessions come from `GET /v3/voice/voices`. A number takes calls to an agent once it is bound to it on `/v3/channels/voice`.
    """

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        audio: Optional[VoiceAgentAudioSpecParam] | Omit = omit,
        fallback: Optional[VoiceAgentPartySpecParam] | Omit = omit,
        greeting: Optional[str] | Omit = omit,
        limits: Optional[VoiceAgentLimitsSpecParam] | Omit = omit,
        name: Optional[str] | Omit = omit,
        sandbox: bool | Omit = omit,
        session_type: Optional[str] | Omit = omit,
        speech: Optional[VoiceAgentSpeechSpecParam] | Omit = omit,
        tools: Optional[SequenceNotStr[str]] | Omit = omit,
        transcripts: Optional[VoiceAgentTranscriptsSpecParam] | Omit = omit,
        transfer_targets: Optional[Iterable[VoiceAgentPartySpecParam]] | Omit = omit,
        websocket_url: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceAgent:
        """
        Creates an agent that answers phone calls through the Sent Voice Gateway.
        `session_type` says whether Sent carries the call as text (the caller's speech
        recognised for the agent, the agent's text spoken) or as audio. With
        `websocket_url` the gateway dials your agent for each call and signs the
        handshake with the `signing_secret` this response returns; without it, your
        agent dials in with your API key and this agent's `id`.

        `tools`, `transfer_targets`, `fallback` and `limits` say what the agent may do
        on a call. Voices and languages for text sessions come from
        `GET /v3/voice/voices`. Calls reach the agent once a number is bound to it on
        `/v3/channels/voice`.

        `signing_secret` is shown here and on `POST /v3/voice/agents/{id}/rotate-secret`
        only; store it now. With `sandbox: true` the request is validated and the agent
        reported with `202`; nothing is written.

        Args:
          audio: Audio sessions only: the sound format.

          fallback: Who takes the call when the agent cannot: a phone number (kind: number). Omit it
              and such a call hangs up.

          greeting: Text sessions only: what the caller hears as soon as the call is answered,
              before the agent's first turn. 1 to 4,096 characters. Omit it and the agent
              speaks first.

          name: A name for your own reference, 1 to 100 characters.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          session_type: text: Sent turns the caller's speech into text and the agent's text into speech,
              so the agent exchanges text frames. audio: the agent receives and sends the
              sound itself.

          speech: Text sessions only: how the caller is spoken to and listened to.

          tools: What the agent may do to the call: any of transfer, hangup, send_dtmf and hold.
              Default ["hangup"]. transfer needs at least one transfer_targets entry.

          transfer_targets:
              Where the agent may transfer a call to, up to 20 parties: a phone number (kind:
              number, E.164), one of your app users (kind: user, the identity) or another of
              your agents (kind: agent, its id). The agent can only transfer to a party listed
              here.

          websocket_url: Where the gateway connects to the agent for each call: an absolute wss:// URL on
              a public host, at most 2,048 characters. The handshake is signed with the
              agent's signing_secret. Leave it out and the agent dials in instead, connecting
              to the gateway with your API key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-profile-id": x_profile_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/v3/voice/agents",
            body=maybe_transform(
                {
                    "audio": audio,
                    "fallback": fallback,
                    "greeting": greeting,
                    "limits": limits,
                    "name": name,
                    "sandbox": sandbox,
                    "session_type": session_type,
                    "speech": speech,
                    "tools": tools,
                    "transcripts": transcripts,
                    "transfer_targets": transfer_targets,
                    "websocket_url": websocket_url,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceAgent,
        )

    def retrieve(
        self,
        id: str,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceAgent:
        """
        The agent as stored, without its signing secret.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v3/voice/agents/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceAgent,
        )

    def update(
        self,
        id: str,
        *,
        audio: Optional[VoiceAgentAudioSpecParam] | Omit = omit,
        fallback: Optional[VoiceAgentPartySpecParam] | Omit = omit,
        greeting: Optional[str] | Omit = omit,
        limits: Optional[VoiceAgentLimitsSpecParam] | Omit = omit,
        name: str | Omit = omit,
        sandbox: bool | Omit = omit,
        session_type: str | Omit = omit,
        speech: Optional[VoiceAgentSpeechSpecParam] | Omit = omit,
        tools: Optional[SequenceNotStr[str]] | Omit = omit,
        transcripts: Optional[VoiceAgentTranscriptsSpecParam] | Omit = omit,
        transfer_targets: Optional[Iterable[VoiceAgentPartySpecParam]] | Omit = omit,
        websocket_url: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceAgent:
        """
        Changes the fields you name and answers with the agent as stored, the same shape
        `GET` returns.

        A key left out is left alone. A key sent as `null` clears an optional field
        (`websocket_url` makes the agent dial in, `greeting` and `fallback` go,
        `speech`, `audio`, `tools`, `limits` and `transcripts` return to their
        defaults). A key sent with a value replaces that field whole: send the whole
        `limits` object, not one of its keys. Changing `session_type` drops `speech`,
        `audio` and `greeting` unless the body sends them, since the other type cannot
        carry them. The result is checked like a new agent, and a body that changes
        nothing is `400`.

        With `sandbox: true` nothing is written: the request is validated against the
        stored agent and the agent is reported with `200` as it would read after the
        change.

        Args:
          audio: Audio sessions: { sample_rate }; null restores the default.

          fallback: A new fallback party, or null for none.

          greeting: A new greeting, or null for none.

          limits: The whole limits object; null restores the defaults.

          name: A new name, 1 to 100 characters.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          session_type: text or audio. Changing it drops the settings the other type cannot have
              (speech, audio, greeting) unless the body sends them.

          speech: Text sessions: { setting, voice, language }, replaced whole; null restores the
              defaults.

          tools: The whole list of tools; null restores the default.

          transcripts: The whole transcripts object; null restores the defaults.

          transfer_targets: The whole list of parties; null clears it.

          websocket_url: A new wss:// URL, or null for an agent that dials in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-profile-id": x_profile_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template("/v3/voice/agents/{id}", id=id),
            body=maybe_transform(
                {
                    "audio": audio,
                    "fallback": fallback,
                    "greeting": greeting,
                    "limits": limits,
                    "name": name,
                    "sandbox": sandbox,
                    "session_type": session_type,
                    "speech": speech,
                    "tools": tools,
                    "transcripts": transcripts,
                    "transfer_targets": transfer_targets,
                    "websocket_url": websocket_url,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceAgent,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncVoiceAgentsPage[VoiceAgent]:
        """Your voice agents, newest first.

        `page` and `page_size` (1 to 100, default 20)
        page the list. Signing secrets are never listed.

        Args:
          page: Page number, from 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get_api_list(
            "/v3/voice/agents",
            page=SyncVoiceAgentsPage[VoiceAgent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            model=VoiceAgent,
        )

    def delete(
        self,
        id: str,
        *,
        sandbox: bool | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes the agent.

        Calls it already took keep their `agent_id`.

        An agent that one of your voice numbers routes to, or that another of your
        agents lists in `transfer_targets`, is not deleted: the answer is `409` with a
        message naming those numbers and agents. Unbind the numbers
        (`PATCH /v3/channels/voice/{number}` with `"agent_id": null`), take the agent
        out of the others' `transfer_targets` or delete them, and try again.

        With `sandbox: true` nothing is written: the agent is looked up and the answer
        is the one a real delete would give.

        Args:
          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._delete(
            path_template("/v3/voice/agents/{id}", id=id),
            body=maybe_transform({"sandbox": sandbox}, agent_delete_params.AgentDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def rotate_secret(
        self,
        id: str,
        *,
        sandbox: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceAgentSecret:
        """Generates a new `signing_secret` for the agent and returns it.

        The previous
        secret stops signing immediately, so update your agent before the next call
        reaches it.

        With `sandbox: true` a secret is generated and returned with `202`, and nothing
        is written.

        Args:
          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-profile-id": x_profile_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/v3/voice/agents/{id}/rotate-secret", id=id),
            body=maybe_transform({"sandbox": sandbox}, agent_rotate_secret_params.AgentRotateSecretParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceAgentSecret,
        )


class AsyncAgentsResource(AsyncAPIResource):
    """Phone calls from the numbers you hold, driven by your own callback URL.

    `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

    Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.

    **Voice agents.** `POST /v3/voice/agents` creates an agent that answers calls through the Sent Voice Gateway: `session_type` says whether Sent carries the call as text (speech recognised and spoken for the agent) or as audio, `websocket_url` is where the gateway dials the agent for each call (leave it out and the agent dials in with your API key), and `tools`, `transfer_targets`, `fallback` and `limits` say what it may do on a call. The agent's `signing_secret` is shown on create and on `POST /v3/voice/agents/{id}/rotate-secret` only. Voices and languages for text sessions come from `GET /v3/voice/voices`. A number takes calls to an agent once it is bound to it on `/v3/channels/voice`.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        audio: Optional[VoiceAgentAudioSpecParam] | Omit = omit,
        fallback: Optional[VoiceAgentPartySpecParam] | Omit = omit,
        greeting: Optional[str] | Omit = omit,
        limits: Optional[VoiceAgentLimitsSpecParam] | Omit = omit,
        name: Optional[str] | Omit = omit,
        sandbox: bool | Omit = omit,
        session_type: Optional[str] | Omit = omit,
        speech: Optional[VoiceAgentSpeechSpecParam] | Omit = omit,
        tools: Optional[SequenceNotStr[str]] | Omit = omit,
        transcripts: Optional[VoiceAgentTranscriptsSpecParam] | Omit = omit,
        transfer_targets: Optional[Iterable[VoiceAgentPartySpecParam]] | Omit = omit,
        websocket_url: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceAgent:
        """
        Creates an agent that answers phone calls through the Sent Voice Gateway.
        `session_type` says whether Sent carries the call as text (the caller's speech
        recognised for the agent, the agent's text spoken) or as audio. With
        `websocket_url` the gateway dials your agent for each call and signs the
        handshake with the `signing_secret` this response returns; without it, your
        agent dials in with your API key and this agent's `id`.

        `tools`, `transfer_targets`, `fallback` and `limits` say what the agent may do
        on a call. Voices and languages for text sessions come from
        `GET /v3/voice/voices`. Calls reach the agent once a number is bound to it on
        `/v3/channels/voice`.

        `signing_secret` is shown here and on `POST /v3/voice/agents/{id}/rotate-secret`
        only; store it now. With `sandbox: true` the request is validated and the agent
        reported with `202`; nothing is written.

        Args:
          audio: Audio sessions only: the sound format.

          fallback: Who takes the call when the agent cannot: a phone number (kind: number). Omit it
              and such a call hangs up.

          greeting: Text sessions only: what the caller hears as soon as the call is answered,
              before the agent's first turn. 1 to 4,096 characters. Omit it and the agent
              speaks first.

          name: A name for your own reference, 1 to 100 characters.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          session_type: text: Sent turns the caller's speech into text and the agent's text into speech,
              so the agent exchanges text frames. audio: the agent receives and sends the
              sound itself.

          speech: Text sessions only: how the caller is spoken to and listened to.

          tools: What the agent may do to the call: any of transfer, hangup, send_dtmf and hold.
              Default ["hangup"]. transfer needs at least one transfer_targets entry.

          transfer_targets:
              Where the agent may transfer a call to, up to 20 parties: a phone number (kind:
              number, E.164), one of your app users (kind: user, the identity) or another of
              your agents (kind: agent, its id). The agent can only transfer to a party listed
              here.

          websocket_url: Where the gateway connects to the agent for each call: an absolute wss:// URL on
              a public host, at most 2,048 characters. The handshake is signed with the
              agent's signing_secret. Leave it out and the agent dials in instead, connecting
              to the gateway with your API key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-profile-id": x_profile_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/v3/voice/agents",
            body=await async_maybe_transform(
                {
                    "audio": audio,
                    "fallback": fallback,
                    "greeting": greeting,
                    "limits": limits,
                    "name": name,
                    "sandbox": sandbox,
                    "session_type": session_type,
                    "speech": speech,
                    "tools": tools,
                    "transcripts": transcripts,
                    "transfer_targets": transfer_targets,
                    "websocket_url": websocket_url,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceAgent,
        )

    async def retrieve(
        self,
        id: str,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceAgent:
        """
        The agent as stored, without its signing secret.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v3/voice/agents/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceAgent,
        )

    async def update(
        self,
        id: str,
        *,
        audio: Optional[VoiceAgentAudioSpecParam] | Omit = omit,
        fallback: Optional[VoiceAgentPartySpecParam] | Omit = omit,
        greeting: Optional[str] | Omit = omit,
        limits: Optional[VoiceAgentLimitsSpecParam] | Omit = omit,
        name: str | Omit = omit,
        sandbox: bool | Omit = omit,
        session_type: str | Omit = omit,
        speech: Optional[VoiceAgentSpeechSpecParam] | Omit = omit,
        tools: Optional[SequenceNotStr[str]] | Omit = omit,
        transcripts: Optional[VoiceAgentTranscriptsSpecParam] | Omit = omit,
        transfer_targets: Optional[Iterable[VoiceAgentPartySpecParam]] | Omit = omit,
        websocket_url: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceAgent:
        """
        Changes the fields you name and answers with the agent as stored, the same shape
        `GET` returns.

        A key left out is left alone. A key sent as `null` clears an optional field
        (`websocket_url` makes the agent dial in, `greeting` and `fallback` go,
        `speech`, `audio`, `tools`, `limits` and `transcripts` return to their
        defaults). A key sent with a value replaces that field whole: send the whole
        `limits` object, not one of its keys. Changing `session_type` drops `speech`,
        `audio` and `greeting` unless the body sends them, since the other type cannot
        carry them. The result is checked like a new agent, and a body that changes
        nothing is `400`.

        With `sandbox: true` nothing is written: the request is validated against the
        stored agent and the agent is reported with `200` as it would read after the
        change.

        Args:
          audio: Audio sessions: { sample_rate }; null restores the default.

          fallback: A new fallback party, or null for none.

          greeting: A new greeting, or null for none.

          limits: The whole limits object; null restores the defaults.

          name: A new name, 1 to 100 characters.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          session_type: text or audio. Changing it drops the settings the other type cannot have
              (speech, audio, greeting) unless the body sends them.

          speech: Text sessions: { setting, voice, language }, replaced whole; null restores the
              defaults.

          tools: The whole list of tools; null restores the default.

          transcripts: The whole transcripts object; null restores the defaults.

          transfer_targets: The whole list of parties; null clears it.

          websocket_url: A new wss:// URL, or null for an agent that dials in.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-profile-id": x_profile_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template("/v3/voice/agents/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "audio": audio,
                    "fallback": fallback,
                    "greeting": greeting,
                    "limits": limits,
                    "name": name,
                    "sandbox": sandbox,
                    "session_type": session_type,
                    "speech": speech,
                    "tools": tools,
                    "transcripts": transcripts,
                    "transfer_targets": transfer_targets,
                    "websocket_url": websocket_url,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceAgent,
        )

    def list(
        self,
        *,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[VoiceAgent, AsyncVoiceAgentsPage[VoiceAgent]]:
        """Your voice agents, newest first.

        `page` and `page_size` (1 to 100, default 20)
        page the list. Signing secrets are never listed.

        Args:
          page: Page number, from 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get_api_list(
            "/v3/voice/agents",
            page=AsyncVoiceAgentsPage[VoiceAgent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            model=VoiceAgent,
        )

    async def delete(
        self,
        id: str,
        *,
        sandbox: bool | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Removes the agent.

        Calls it already took keep their `agent_id`.

        An agent that one of your voice numbers routes to, or that another of your
        agents lists in `transfer_targets`, is not deleted: the answer is `409` with a
        message naming those numbers and agents. Unbind the numbers
        (`PATCH /v3/channels/voice/{number}` with `"agent_id": null`), take the agent
        out of the others' `transfer_targets` or delete them, and try again.

        With `sandbox: true` nothing is written: the agent is looked up and the answer
        is the one a real delete would give.

        Args:
          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/voice/agents/{id}", id=id),
            body=await async_maybe_transform({"sandbox": sandbox}, agent_delete_params.AgentDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def rotate_secret(
        self,
        id: str,
        *,
        sandbox: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceAgentSecret:
        """Generates a new `signing_secret` for the agent and returns it.

        The previous
        secret stops signing immediately, so update your agent before the next call
        reaches it.

        With `sandbox: true` a secret is generated and returned with `202`, and nothing
        is written.

        Args:
          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-profile-id": x_profile_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/v3/voice/agents/{id}/rotate-secret", id=id),
            body=await async_maybe_transform({"sandbox": sandbox}, agent_rotate_secret_params.AgentRotateSecretParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceAgentSecret,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )
        self.rotate_secret = to_raw_response_wrapper(
            agents.rotate_secret,
        )


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )
        self.rotate_secret = async_to_raw_response_wrapper(
            agents.rotate_secret,
        )


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )
        self.rotate_secret = to_streamed_response_wrapper(
            agents.rotate_secret,
        )


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
        self.rotate_secret = async_to_streamed_response_wrapper(
            agents.rotate_secret,
        )
