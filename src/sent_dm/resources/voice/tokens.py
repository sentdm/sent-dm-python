# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.voice import token_create_params
from ..._base_client import make_request_options
from ...types.voice.api_response_of_voice_token import APIResponseOfVoiceToken

__all__ = ["TokensResource", "AsyncTokensResource"]


class TokensResource(SyncAPIResource):
    """Phone calls from the numbers you hold, driven by your own callback URL.

    `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

    Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
    """

    @cached_property
    def with_raw_response(self) -> TokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return TokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return TokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        identity: str | Omit = omit,
        number: Optional[str] | Omit = omit,
        sandbox: bool | Omit = omit,
        ttl: Optional[int] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceToken:
        """Mints a short-lived token for one of your app users.

        Call this from your backend
        and return the token to your app, which passes it to the voice client SDK to
        register. The identity is bound to the given number, or to your default app-call
        number when omitted, and calls placed by that identity are routed through the
        bound number. Minting again re-binds the identity, so an identity can move
        between numbers.

        Args:
          identity: Your identifier for the app user, such as an agent or account id. Letters,
              digits, hyphens and underscores only, up to 200 characters.

          number: One of your voice-enabled phone numbers in E.164 format. Calls placed by this
              identity are routed through that number. Omit to use your default app-call
              number.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          ttl: Token lifetime in seconds. Defaults to 600 and cannot exceed 3600.

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
            "/v3/voice/tokens",
            body=maybe_transform(
                {
                    "identity": identity,
                    "number": number,
                    "sandbox": sandbox,
                    "ttl": ttl,
                },
                token_create_params.TokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceToken,
        )


class AsyncTokensResource(AsyncAPIResource):
    """Phone calls from the numbers you hold, driven by your own callback URL.

    `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

    Every call is a record under `/v3/voice/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        identity: str | Omit = omit,
        number: Optional[str] | Omit = omit,
        sandbox: bool | Omit = omit,
        ttl: Optional[int] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceToken:
        """Mints a short-lived token for one of your app users.

        Call this from your backend
        and return the token to your app, which passes it to the voice client SDK to
        register. The identity is bound to the given number, or to your default app-call
        number when omitted, and calls placed by that identity are routed through the
        bound number. Minting again re-binds the identity, so an identity can move
        between numbers.

        Args:
          identity: Your identifier for the app user, such as an agent or account id. Letters,
              digits, hyphens and underscores only, up to 200 characters.

          number: One of your voice-enabled phone numbers in E.164 format. Calls placed by this
              identity are routed through that number. Omit to use your default app-call
              number.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          ttl: Token lifetime in seconds. Defaults to 600 and cannot exceed 3600.

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
            "/v3/voice/tokens",
            body=await async_maybe_transform(
                {
                    "identity": identity,
                    "number": number,
                    "sandbox": sandbox,
                    "ttl": ttl,
                },
                token_create_params.TokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceToken,
        )


class TokensResourceWithRawResponse:
    def __init__(self, tokens: TokensResource) -> None:
        self._tokens = tokens

        self.create = to_raw_response_wrapper(
            tokens.create,
        )


class AsyncTokensResourceWithRawResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
        self._tokens = tokens

        self.create = async_to_raw_response_wrapper(
            tokens.create,
        )


class TokensResourceWithStreamingResponse:
    def __init__(self, tokens: TokensResource) -> None:
        self._tokens = tokens

        self.create = to_streamed_response_wrapper(
            tokens.create,
        )


class AsyncTokensResourceWithStreamingResponse:
    def __init__(self, tokens: AsyncTokensResource) -> None:
        self._tokens = tokens

        self.create = async_to_streamed_response_wrapper(
            tokens.create,
        )
