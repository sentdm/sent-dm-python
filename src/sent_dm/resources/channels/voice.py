# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.channels import (
    voice_test_params,
    voice_create_params,
    voice_update_params,
    voice_create_token_params,
    voice_rotate_secret_params,
)
from ...types.channels.api_response_of_voice_token import APIResponseOfVoiceToken
from ...types.channels.api_response_of_voice_number import APIResponseOfVoiceNumber
from ...types.channels.api_response_of_voice_secret import APIResponseOfVoiceSecret
from ...types.channels.api_response_of_voice_callback_test import APIResponseOfVoiceCallbackTest
from ...types.channels.api_response_of_list_of_voice_number import APIResponseOfListOfVoiceNumber
from ...types.channels.api_response_of_voice_number_created import APIResponseOfVoiceNumberCreated

__all__ = ["VoiceResource", "AsyncVoiceResource"]


class VoiceResource(SyncAPIResource):
    """The senders you send from, one per channel.

    **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted under `POST /v3/channels/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

    ## Compliance lives on the market

    Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

    `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

    Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
    """

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

    def create(
        self,
        *,
        callback_url: str,
        area_code: Optional[str] | Omit = omit,
        default_for_app_calls: Optional[bool] | Omit = omit,
        number: Optional[str] | Omit = omit,
        sandbox: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceNumberCreated:
        """Adds voice to one of the numbers you hold, or gives you a new one.

        Send `number`
        for a number that is already yours (see `GET /v3/channels`); leave it out to be
        given a new US number, optionally in a particular `area_code`. Sending both is
        refused. Nothing registers, so the number can carry calls as soon as this
        returns.

        What happens on a call is decided by your `callback_url`: when a call arrives on
        the number, or a caller presses a key on a menu, Sent POSTs a signed question
        there and follows the answer. The response carries the `callback_secret` the
        questions are signed with, the one time it is shown without rotating; verify a
        question the way you verify a webhook. `POST /v3/channels/voice/{number}/test`
        sends a test question and reports the verdict.

        Your first voice number becomes the line app-originated calls are placed from
        when a voice token names no number; send `default_for_app_calls: true` to give
        that role to another number. A number you turned off earlier is turned back on,
        and the same number with a different `callback_url` has its URL replaced and
        keeps its secret.

        Read the number's settings with `GET /v3/channels/voice` and change them with
        `PATCH /v3/channels/voice/{number}`.

        With `sandbox: true` the request is validated and a simulated number reported
        with `202`; nothing is written and no number is bought.

        Args:
          callback_url: Where Sent asks what to do with each call on this number: an absolute HTTP or
              HTTPS URL on a public host. A signed question is POSTed here when a call arrives
              or a caller presses a key, and the answer decides the call. Every question is
              signed with the callback_secret the response returns, the same way your webhooks
              are signed. Turning the number on again with a different URL replaces it and
              keeps the secret.

          area_code: The US area code a new number should be in, as 212. Only for a request that
              leaves number out — sending both says two different things about which number to
              use, and is refused. Omit it too and the number comes from anywhere in the
              country.

          default_for_app_calls: Make this the line app-originated calls are placed from when a voice token names
              no number. Omit it and your first voice number takes that role; a later one
              leaves it where it is.

          number: One of your phone numbers, in E.164 format. Leave the field out entirely to be
              given a new one instead; sending it empty is a refused request rather than a
              request for a new number.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

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
            "/v3/channels/voice",
            body=maybe_transform(
                {
                    "callback_url": callback_url,
                    "area_code": area_code,
                    "default_for_app_calls": default_for_app_calls,
                    "number": number,
                    "sandbox": sandbox,
                },
                voice_create_params.VoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceNumberCreated,
        )

    def retrieve(
        self,
        number: str,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceNumber:
        """
        Reads one of your voice numbers, active or inactive: its status, whether it is
        the default line for calls placed from your app, and its callback URL. The
        signing secret is not on this read.

        The same shape `GET /v3/channels/voice` lists, and the same shape `PATCH` on
        this path accepts and returns, so what comes back can be sent back.

        The number is the E.164 value in the path with the plus sign URL-encoded
        (`%2B`).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v3/channels/voice/{number}", number=number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceNumber,
        )

    def update(
        self,
        number: str,
        *,
        callback_url: Optional[str] | Omit = omit,
        default_for_app_calls: Optional[bool] | Omit = omit,
        sandbox: bool | Omit = omit,
        status: Optional[Literal["ACTIVE", "INACTIVE"]] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceNumber:
        """
        Changes one of your voice numbers and answers with the number as stored, the
        same shape `GET` on this path returns, so what comes back can be sent back.

        ## What it changes

        | Body                                          | Effect                                                                                                                                                     |
        | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | `"status": "ACTIVE"`                          | turns calls on again for a number you turned off; the callback URL and the secret it had are kept                                                          |
        | `"status": "INACTIVE"`                        | turns calls off; the callback URL and the secret stay on the number                                                                                        |
        | `"default_for_app_calls": true`               | makes this the line app-originated calls are placed from when a voice token names no number                                                                |
        | `"callback_url": "https://example.com/voice"` | replaces where Sent asks what to do with each call on the number; the signing secret is kept, and a number that was waiting for its first URL is turned on |
        | key omitted                                   | left exactly as it is                                                                                                                                      |

        `status` is matched ignoring case. Any combination is accepted:
        `status: "ACTIVE"` with `default_for_app_calls: true` turns a number on as the
        new default, and a `callback_url` sent with either status is written too. A body
        that names none of the three is refused.

        ## What it will refuse

        **`default_for_app_calls: false` is `400`.** An account with active voice
        numbers always has exactly one default, so the default moves by giving it to
        another number.

        **Turning the default line off is `409`** while other active voice numbers
        remain. Move the default to another number first. Turning off your last voice
        number is allowed; that turns phone calls off.

        **Making an inactive number the default is `400`.** Send `status: "ACTIVE"` in
        the same call.

        A number added without a `callback_url` is `INACTIVE` for that one reason, so
        sending it a `callback_url` turns it on by itself, and it becomes your default
        line if you have no other active voice number. A number you turned off while it
        had a URL stays off.

        **A number you never turned voice on for is `404`.** Add it with
        `POST /v3/channels/voice`.

        The number is the E.164 value in the path with the plus sign URL-encoded
        (`%2B`).

        With `sandbox: true` nothing is written: the request is validated against the
        stored number and the number is reported with `200` as it would read after the
        change.

        Args:
          callback_url: A new callback URL for the number, active or not: an absolute HTTP or HTTPS URL
              on a public host, where Sent asks what to do with each call. The signing secret
              is kept.

          default_for_app_calls: true makes this the line app-originated calls are placed from when a voice token
              names no number. false is refused: an account with active voice numbers always
              has exactly one default, so the default moves by giving it to another number.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          status: ACTIVE turns calls on for the number again, INACTIVE turns them off. Matched
              ignoring case. Turning the default line off is refused while other active voice
              numbers remain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
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
            path_template("/v3/channels/voice/{number}", number=number),
            body=maybe_transform(
                {
                    "callback_url": callback_url,
                    "default_for_app_calls": default_for_app_calls,
                    "sandbox": sandbox,
                    "status": status,
                },
                voice_update_params.VoiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceNumber,
        )

    def list(
        self,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfListOfVoiceNumber:
        """
        Every number you turned phone calls on for, active or inactive, oldest first.
        Each entry carries the number's status, whether it is the default line for calls
        placed from your app, and its callback URL. The signing secret is never on a
        read; it is shown when voice is turned on and by
        `POST /v3/channels/voice/{number}/rotate-secret`.

        The same entries `GET /v3/channels` reports under `voice`, and the same shape
        `GET /v3/channels/voice/{number}` returns for one of them. Change a number with
        `PATCH /v3/channels/voice/{number}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            "/v3/channels/voice",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfListOfVoiceNumber,
        )

    def create_token(
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
            "/v3/channels/voice/tokens",
            body=maybe_transform(
                {
                    "identity": identity,
                    "number": number,
                    "sandbox": sandbox,
                    "ttl": ttl,
                },
                voice_create_token_params.VoiceCreateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceToken,
        )

    def rotate_secret(
        self,
        number: str,
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
    ) -> APIResponseOfVoiceSecret:
        """
        Generates a new signing secret for the questions Sent sends to this number's
        callback URL and returns it. The previous secret stops signing immediately, so
        update your backend before the next call reaches it. The number is the E.164
        value in the path with the plus sign URL-encoded (`%2B`).

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
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
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
            path_template("/v3/channels/voice/{number}/rotate-secret", number=number),
            body=maybe_transform({"sandbox": sandbox}, voice_rotate_secret_params.VoiceRotateSecretParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceSecret,
        )

    def test(
        self,
        number: str,
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
    ) -> APIResponseOfVoiceCallbackTest:
        """
        Sends a synthetic call.request question, flagged "test": true, to the number's
        callback URL, signed with that number's real secret, and reports what came back.
        Use it to build and debug your callback endpoint without placing calls: no call
        is placed, nothing is billed, and nothing is stored. One attempt with the same
        deadline as a live call, no retry. The outcome is ok when your endpoint answered
        2xx with a valid answer; otherwise it is timeout, connection_failed, http_error
        or invalid_answer, with the reason and, for an invalid answer, the field at
        fault. The number is the E.164 value in the path with the plus sign URL-encoded
        (`%2B`).

        With `sandbox: true` nothing is sent: the verdict comes back ok with `202` and
        no request or response in it.

        Args:
          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
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
            path_template("/v3/channels/voice/{number}/test", number=number),
            body=maybe_transform({"sandbox": sandbox}, voice_test_params.VoiceTestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceCallbackTest,
        )


class AsyncVoiceResource(AsyncAPIResource):
    """The senders you send from, one per channel.

    **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted under `POST /v3/channels/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

    ## Compliance lives on the market

    Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

    `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

    Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
    """

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

    async def create(
        self,
        *,
        callback_url: str,
        area_code: Optional[str] | Omit = omit,
        default_for_app_calls: Optional[bool] | Omit = omit,
        number: Optional[str] | Omit = omit,
        sandbox: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceNumberCreated:
        """Adds voice to one of the numbers you hold, or gives you a new one.

        Send `number`
        for a number that is already yours (see `GET /v3/channels`); leave it out to be
        given a new US number, optionally in a particular `area_code`. Sending both is
        refused. Nothing registers, so the number can carry calls as soon as this
        returns.

        What happens on a call is decided by your `callback_url`: when a call arrives on
        the number, or a caller presses a key on a menu, Sent POSTs a signed question
        there and follows the answer. The response carries the `callback_secret` the
        questions are signed with, the one time it is shown without rotating; verify a
        question the way you verify a webhook. `POST /v3/channels/voice/{number}/test`
        sends a test question and reports the verdict.

        Your first voice number becomes the line app-originated calls are placed from
        when a voice token names no number; send `default_for_app_calls: true` to give
        that role to another number. A number you turned off earlier is turned back on,
        and the same number with a different `callback_url` has its URL replaced and
        keeps its secret.

        Read the number's settings with `GET /v3/channels/voice` and change them with
        `PATCH /v3/channels/voice/{number}`.

        With `sandbox: true` the request is validated and a simulated number reported
        with `202`; nothing is written and no number is bought.

        Args:
          callback_url: Where Sent asks what to do with each call on this number: an absolute HTTP or
              HTTPS URL on a public host. A signed question is POSTed here when a call arrives
              or a caller presses a key, and the answer decides the call. Every question is
              signed with the callback_secret the response returns, the same way your webhooks
              are signed. Turning the number on again with a different URL replaces it and
              keeps the secret.

          area_code: The US area code a new number should be in, as 212. Only for a request that
              leaves number out — sending both says two different things about which number to
              use, and is refused. Omit it too and the number comes from anywhere in the
              country.

          default_for_app_calls: Make this the line app-originated calls are placed from when a voice token names
              no number. Omit it and your first voice number takes that role; a later one
              leaves it where it is.

          number: One of your phone numbers, in E.164 format. Leave the field out entirely to be
              given a new one instead; sending it empty is a refused request rather than a
              request for a new number.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

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
            "/v3/channels/voice",
            body=await async_maybe_transform(
                {
                    "callback_url": callback_url,
                    "area_code": area_code,
                    "default_for_app_calls": default_for_app_calls,
                    "number": number,
                    "sandbox": sandbox,
                },
                voice_create_params.VoiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceNumberCreated,
        )

    async def retrieve(
        self,
        number: str,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceNumber:
        """
        Reads one of your voice numbers, active or inactive: its status, whether it is
        the default line for calls placed from your app, and its callback URL. The
        signing secret is not on this read.

        The same shape `GET /v3/channels/voice` lists, and the same shape `PATCH` on
        this path accepts and returns, so what comes back can be sent back.

        The number is the E.164 value in the path with the plus sign URL-encoded
        (`%2B`).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v3/channels/voice/{number}", number=number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceNumber,
        )

    async def update(
        self,
        number: str,
        *,
        callback_url: Optional[str] | Omit = omit,
        default_for_app_calls: Optional[bool] | Omit = omit,
        sandbox: bool | Omit = omit,
        status: Optional[Literal["ACTIVE", "INACTIVE"]] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfVoiceNumber:
        """
        Changes one of your voice numbers and answers with the number as stored, the
        same shape `GET` on this path returns, so what comes back can be sent back.

        ## What it changes

        | Body                                          | Effect                                                                                                                                                     |
        | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | `"status": "ACTIVE"`                          | turns calls on again for a number you turned off; the callback URL and the secret it had are kept                                                          |
        | `"status": "INACTIVE"`                        | turns calls off; the callback URL and the secret stay on the number                                                                                        |
        | `"default_for_app_calls": true`               | makes this the line app-originated calls are placed from when a voice token names no number                                                                |
        | `"callback_url": "https://example.com/voice"` | replaces where Sent asks what to do with each call on the number; the signing secret is kept, and a number that was waiting for its first URL is turned on |
        | key omitted                                   | left exactly as it is                                                                                                                                      |

        `status` is matched ignoring case. Any combination is accepted:
        `status: "ACTIVE"` with `default_for_app_calls: true` turns a number on as the
        new default, and a `callback_url` sent with either status is written too. A body
        that names none of the three is refused.

        ## What it will refuse

        **`default_for_app_calls: false` is `400`.** An account with active voice
        numbers always has exactly one default, so the default moves by giving it to
        another number.

        **Turning the default line off is `409`** while other active voice numbers
        remain. Move the default to another number first. Turning off your last voice
        number is allowed; that turns phone calls off.

        **Making an inactive number the default is `400`.** Send `status: "ACTIVE"` in
        the same call.

        A number added without a `callback_url` is `INACTIVE` for that one reason, so
        sending it a `callback_url` turns it on by itself, and it becomes your default
        line if you have no other active voice number. A number you turned off while it
        had a URL stays off.

        **A number you never turned voice on for is `404`.** Add it with
        `POST /v3/channels/voice`.

        The number is the E.164 value in the path with the plus sign URL-encoded
        (`%2B`).

        With `sandbox: true` nothing is written: the request is validated against the
        stored number and the number is reported with `200` as it would read after the
        change.

        Args:
          callback_url: A new callback URL for the number, active or not: an absolute HTTP or HTTPS URL
              on a public host, where Sent asks what to do with each call. The signing secret
              is kept.

          default_for_app_calls: true makes this the line app-originated calls are placed from when a voice token
              names no number. false is refused: an account with active voice numbers always
              has exactly one default, so the default moves by giving it to another number.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          status: ACTIVE turns calls on for the number again, INACTIVE turns them off. Matched
              ignoring case. Turning the default line off is refused while other active voice
              numbers remain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
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
            path_template("/v3/channels/voice/{number}", number=number),
            body=await async_maybe_transform(
                {
                    "callback_url": callback_url,
                    "default_for_app_calls": default_for_app_calls,
                    "sandbox": sandbox,
                    "status": status,
                },
                voice_update_params.VoiceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceNumber,
        )

    async def list(
        self,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfListOfVoiceNumber:
        """
        Every number you turned phone calls on for, active or inactive, oldest first.
        Each entry carries the number's status, whether it is the default line for calls
        placed from your app, and its callback URL. The signing secret is never on a
        read; it is shown when voice is turned on and by
        `POST /v3/channels/voice/{number}/rotate-secret`.

        The same entries `GET /v3/channels` reports under `voice`, and the same shape
        `GET /v3/channels/voice/{number}` returns for one of them. Change a number with
        `PATCH /v3/channels/voice/{number}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            "/v3/channels/voice",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfListOfVoiceNumber,
        )

    async def create_token(
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
            "/v3/channels/voice/tokens",
            body=await async_maybe_transform(
                {
                    "identity": identity,
                    "number": number,
                    "sandbox": sandbox,
                    "ttl": ttl,
                },
                voice_create_token_params.VoiceCreateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceToken,
        )

    async def rotate_secret(
        self,
        number: str,
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
    ) -> APIResponseOfVoiceSecret:
        """
        Generates a new signing secret for the questions Sent sends to this number's
        callback URL and returns it. The previous secret stops signing immediately, so
        update your backend before the next call reaches it. The number is the E.164
        value in the path with the plus sign URL-encoded (`%2B`).

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
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
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
            path_template("/v3/channels/voice/{number}/rotate-secret", number=number),
            body=await async_maybe_transform({"sandbox": sandbox}, voice_rotate_secret_params.VoiceRotateSecretParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceSecret,
        )

    async def test(
        self,
        number: str,
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
    ) -> APIResponseOfVoiceCallbackTest:
        """
        Sends a synthetic call.request question, flagged "test": true, to the number's
        callback URL, signed with that number's real secret, and reports what came back.
        Use it to build and debug your callback endpoint without placing calls: no call
        is placed, nothing is billed, and nothing is stored. One attempt with the same
        deadline as a live call, no retry. The outcome is ok when your endpoint answered
        2xx with a valid answer; otherwise it is timeout, connection_failed, http_error
        or invalid_answer, with the reason and, for an invalid answer, the field at
        fault. The number is the E.164 value in the path with the plus sign URL-encoded
        (`%2B`).

        With `sandbox: true` nothing is sent: the verdict comes back ok with `202` and
        no request or response in it.

        Args:
          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not number:
            raise ValueError(f"Expected a non-empty value for `number` but received {number!r}")
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
            path_template("/v3/channels/voice/{number}/test", number=number),
            body=await async_maybe_transform({"sandbox": sandbox}, voice_test_params.VoiceTestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfVoiceCallbackTest,
        )


class VoiceResourceWithRawResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

        self.create = to_raw_response_wrapper(
            voice.create,
        )
        self.retrieve = to_raw_response_wrapper(
            voice.retrieve,
        )
        self.update = to_raw_response_wrapper(
            voice.update,
        )
        self.list = to_raw_response_wrapper(
            voice.list,
        )
        self.create_token = to_raw_response_wrapper(
            voice.create_token,
        )
        self.rotate_secret = to_raw_response_wrapper(
            voice.rotate_secret,
        )
        self.test = to_raw_response_wrapper(
            voice.test,
        )


class AsyncVoiceResourceWithRawResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

        self.create = async_to_raw_response_wrapper(
            voice.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            voice.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            voice.update,
        )
        self.list = async_to_raw_response_wrapper(
            voice.list,
        )
        self.create_token = async_to_raw_response_wrapper(
            voice.create_token,
        )
        self.rotate_secret = async_to_raw_response_wrapper(
            voice.rotate_secret,
        )
        self.test = async_to_raw_response_wrapper(
            voice.test,
        )


class VoiceResourceWithStreamingResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

        self.create = to_streamed_response_wrapper(
            voice.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            voice.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            voice.update,
        )
        self.list = to_streamed_response_wrapper(
            voice.list,
        )
        self.create_token = to_streamed_response_wrapper(
            voice.create_token,
        )
        self.rotate_secret = to_streamed_response_wrapper(
            voice.rotate_secret,
        )
        self.test = to_streamed_response_wrapper(
            voice.test,
        )


class AsyncVoiceResourceWithStreamingResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

        self.create = async_to_streamed_response_wrapper(
            voice.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            voice.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            voice.update,
        )
        self.list = async_to_streamed_response_wrapper(
            voice.list,
        )
        self.create_token = async_to_streamed_response_wrapper(
            voice.create_token,
        )
        self.rotate_secret = async_to_streamed_response_wrapper(
            voice.rotate_secret,
        )
        self.test = async_to_streamed_response_wrapper(
            voice.test,
        )
