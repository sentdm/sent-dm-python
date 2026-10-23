# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tokens import (
    TokensResource,
    AsyncTokensResource,
    TokensResourceWithRawResponse,
    AsyncTokensResourceWithRawResponse,
    TokensResourceWithStreamingResponse,
    AsyncTokensResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .calls.calls import (
    CallsResource,
    AsyncCallsResource,
    CallsResourceWithRawResponse,
    AsyncCallsResourceWithRawResponse,
    CallsResourceWithStreamingResponse,
    AsyncCallsResourceWithStreamingResponse,
)

__all__ = ["VoiceResource", "AsyncVoiceResource"]


class VoiceResource(SyncAPIResource):
    @cached_property
    def calls(self) -> CallsResource:
        """Phone calls from the numbers you hold, driven by your own callback URL.

        `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

        Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
        """
        return CallsResource(self._client)

    @cached_property
    def tokens(self) -> TokensResource:
        """Phone calls from the numbers you hold, driven by your own callback URL.

        `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

        Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
        """
        return TokensResource(self._client)

    @cached_property
    def with_raw_response(self) -> VoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return VoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return VoiceResourceWithStreamingResponse(self)


class AsyncVoiceResource(AsyncAPIResource):
    @cached_property
    def calls(self) -> AsyncCallsResource:
        """Phone calls from the numbers you hold, driven by your own callback URL.

        `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

        Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
        """
        return AsyncCallsResource(self._client)

    @cached_property
    def tokens(self) -> AsyncTokensResource:
        """Phone calls from the numbers you hold, driven by your own callback URL.

        `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

        Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
        """
        return AsyncTokensResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncVoiceResourceWithStreamingResponse(self)


class VoiceResourceWithRawResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

    @cached_property
    def calls(self) -> CallsResourceWithRawResponse:
        """Phone calls from the numbers you hold, driven by your own callback URL.

        `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

        Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
        """
        return CallsResourceWithRawResponse(self._voice.calls)

    @cached_property
    def tokens(self) -> TokensResourceWithRawResponse:
        """Phone calls from the numbers you hold, driven by your own callback URL.

        `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

        Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
        """
        return TokensResourceWithRawResponse(self._voice.tokens)


class AsyncVoiceResourceWithRawResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

    @cached_property
    def calls(self) -> AsyncCallsResourceWithRawResponse:
        """Phone calls from the numbers you hold, driven by your own callback URL.

        `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

        Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
        """
        return AsyncCallsResourceWithRawResponse(self._voice.calls)

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithRawResponse:
        """Phone calls from the numbers you hold, driven by your own callback URL.

        `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

        Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
        """
        return AsyncTokensResourceWithRawResponse(self._voice.tokens)


class VoiceResourceWithStreamingResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

    @cached_property
    def calls(self) -> CallsResourceWithStreamingResponse:
        """Phone calls from the numbers you hold, driven by your own callback URL.

        `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

        Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
        """
        return CallsResourceWithStreamingResponse(self._voice.calls)

    @cached_property
    def tokens(self) -> TokensResourceWithStreamingResponse:
        """Phone calls from the numbers you hold, driven by your own callback URL.

        `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

        Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
        """
        return TokensResourceWithStreamingResponse(self._voice.tokens)


class AsyncVoiceResourceWithStreamingResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

    @cached_property
    def calls(self) -> AsyncCallsResourceWithStreamingResponse:
        """Phone calls from the numbers you hold, driven by your own callback URL.

        `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

        Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
        """
        return AsyncCallsResourceWithStreamingResponse(self._voice.calls)

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithStreamingResponse:
        """Phone calls from the numbers you hold, driven by your own callback URL.

        `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

        Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
        """
        return AsyncTokensResourceWithStreamingResponse(self._voice.tokens)
