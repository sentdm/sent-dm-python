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
from ...types.channels import voice_test_params, voice_create_params, voice_update_params, voice_rotate_secret_params
from ...types.channels.api_response_of_voice_number import APIResponseOfVoiceNumber
from ...types.channels.api_response_of_voice_secret import APIResponseOfVoiceSecret
from ...types.channels.api_response_of_voice_callback_test import APIResponseOfVoiceCallbackTest
from ...types.channels.api_response_of_list_of_voice_number import APIResponseOfListOfVoiceNumber
from ...types.channels.api_response_of_voice_number_created import APIResponseOfVoiceNumberCreated

__all__ = ["VoiceResource", "AsyncVoiceResource"]


class VoiceResource(SyncAPIResource):
    """The senders you send from, one per channel.

    **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

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
        agent_id: Optional[str] | Omit = omit,
        area_code: Optional[str] | Omit = omit,
        callback_url: Optional[str] | Omit = omit,
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

        Send `agent_id` instead of `callback_url`, or with it, to have one of your voice
        agents (`GET /v3/voice/agents`) answer calls to the number. The agent wins over
        the callback URL for calls to the number; calls your app places from it still
        follow your app. `routes_to` in the response says which answers, and reads
        `agent_pending` while the number is still being moved to the agent. Calls follow
        the move within about an hour, as the provider applies it on its own clock.
        While numbers cannot be bound to agents, a request with `agent_id` is refused
        with `502` before any number is obtained or anything is written; send
        `callback_url` instead.

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
          agent_id: One of your voice agents (GET /v3/voice/agents), such as
              agent_9f2ab000-0000-4000-8000-000000000001, to answer calls to this number. It
              wins over callback_url for calls to the number, and both may be sent; calls your
              app places from the number still follow your app. Send it instead of
              callback_url for a number only an agent answers.

          area_code: The US area code a new number should be in, as 212. Only for a request that
              leaves number out — sending both says two different things about which number to
              use, and is refused. Omit it too and the number comes from anywhere in the
              country.

          callback_url: Where Sent asks what to do with each call on this number: an absolute HTTP or
              HTTPS URL on a public host. A signed question is POSTed here when a call arrives
              or a caller presses a key, and the answer decides the call. Every question is
              signed with the callback_secret the response returns, the same way your webhooks
              are signed. Turning the number on again with a different URL replaces it and
              keeps the secret. Required unless agent_id is sent.

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
                    "agent_id": agent_id,
                    "area_code": area_code,
                    "callback_url": callback_url,
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
        agent_id: Optional[str] | Omit = omit,
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

        | Body                                          | Effect                                                                                                                                                                                                                                                                                                                                                                                                     |
        | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | `"status": "ACTIVE"`                          | turns calls on again for a number you turned off; the callback URL and the secret it had are kept                                                                                                                                                                                                                                                                                                          |
        | `"status": "INACTIVE"`                        | turns calls off; the callback URL and the secret stay on the number                                                                                                                                                                                                                                                                                                                                        |
        | `"default_for_app_calls": true`               | makes this the line app-originated calls are placed from when a voice token names no number                                                                                                                                                                                                                                                                                                                |
        | `"callback_url": "https://example.com/voice"` | replaces where Sent asks what to do with each call on the number; the signing secret and the status are kept                                                                                                                                                                                                                                                                                               |
        | `"agent_id": "agent_…"`                       | one of your voice agents answers calls to the number, within about an hour of the change (the provider applies the move on its own clock, and `routes_to` reads `agent` as soon as it has recorded it); it wins over `callback_url` for calls to the number, and calls your app places from it still follow your app. `routes_to` reads `agent_pending` while the number is still being moved to the agent |
        | `"agent_id": null`                            | unbinds the agent, so `callback_url` answers calls to the number again                                                                                                                                                                                                                                                                                                                                     |
        | key omitted                                   | left exactly as it is                                                                                                                                                                                                                                                                                                                                                                                      |

        `status` is matched ignoring case. Any combination is accepted:
        `status: "ACTIVE"` with `default_for_app_calls: true` turns a number on as the
        new default, and a `callback_url` sent with either status is written too.
        `agent_id` is applied first, so a refusal to move the number to or from the
        agent leaves everything as it was, and the `409` and `400` refusals below are
        decided before anything is written, so they leave everything as it was too. A
        body that names none of them is refused.

        A number can be on without a callback URL: calls placed from your app then
        connect straight to the number or user they dial, and calls to the number are
        declined.

        ## What it will refuse

        **`default_for_app_calls: false` is `400`.** An account with active voice
        numbers always has exactly one default, so the default moves by giving it to
        another number.

        **Turning the default line off is `409`** while other active voice numbers
        remain. Move the default to another number first. Turning off your last voice
        number is allowed; that turns phone calls off.

        **Making an inactive number the default is `400`.** Send `status: "ACTIVE"` in
        the same call.

        **A number you never turned voice on for is `404`**, and so is an `agent_id`
        that is not one of your agents. Add the number with `POST /v3/channels/voice`.

        **`502` means the number could not be moved to or from the agent**, or an
        `agent_id` was sent while numbers cannot be bound to agents; nothing was
        written.

        The number is the E.164 value in the path with the plus sign URL-encoded
        (`%2B`).

        With `sandbox: true` nothing is written: the request is validated against the
        stored number and the number is reported with `200` as it would read after the
        change.

        Args:
          agent_id: One of your voice agents, such as agent_9f2ab000-0000-4000-8000-000000000001, to
              answer calls to the number, or null to unbind it so the callback URL answers
              them again. The agent wins over callback_url for calls to the number; calls your
              app places from it still follow your app.

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
                    "agent_id": agent_id,
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

    **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

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
        agent_id: Optional[str] | Omit = omit,
        area_code: Optional[str] | Omit = omit,
        callback_url: Optional[str] | Omit = omit,
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

        Send `agent_id` instead of `callback_url`, or with it, to have one of your voice
        agents (`GET /v3/voice/agents`) answer calls to the number. The agent wins over
        the callback URL for calls to the number; calls your app places from it still
        follow your app. `routes_to` in the response says which answers, and reads
        `agent_pending` while the number is still being moved to the agent. Calls follow
        the move within about an hour, as the provider applies it on its own clock.
        While numbers cannot be bound to agents, a request with `agent_id` is refused
        with `502` before any number is obtained or anything is written; send
        `callback_url` instead.

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
          agent_id: One of your voice agents (GET /v3/voice/agents), such as
              agent_9f2ab000-0000-4000-8000-000000000001, to answer calls to this number. It
              wins over callback_url for calls to the number, and both may be sent; calls your
              app places from the number still follow your app. Send it instead of
              callback_url for a number only an agent answers.

          area_code: The US area code a new number should be in, as 212. Only for a request that
              leaves number out — sending both says two different things about which number to
              use, and is refused. Omit it too and the number comes from anywhere in the
              country.

          callback_url: Where Sent asks what to do with each call on this number: an absolute HTTP or
              HTTPS URL on a public host. A signed question is POSTed here when a call arrives
              or a caller presses a key, and the answer decides the call. Every question is
              signed with the callback_secret the response returns, the same way your webhooks
              are signed. Turning the number on again with a different URL replaces it and
              keeps the secret. Required unless agent_id is sent.

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
                    "agent_id": agent_id,
                    "area_code": area_code,
                    "callback_url": callback_url,
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
        agent_id: Optional[str] | Omit = omit,
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

        | Body                                          | Effect                                                                                                                                                                                                                                                                                                                                                                                                     |
        | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | `"status": "ACTIVE"`                          | turns calls on again for a number you turned off; the callback URL and the secret it had are kept                                                                                                                                                                                                                                                                                                          |
        | `"status": "INACTIVE"`                        | turns calls off; the callback URL and the secret stay on the number                                                                                                                                                                                                                                                                                                                                        |
        | `"default_for_app_calls": true`               | makes this the line app-originated calls are placed from when a voice token names no number                                                                                                                                                                                                                                                                                                                |
        | `"callback_url": "https://example.com/voice"` | replaces where Sent asks what to do with each call on the number; the signing secret and the status are kept                                                                                                                                                                                                                                                                                               |
        | `"agent_id": "agent_…"`                       | one of your voice agents answers calls to the number, within about an hour of the change (the provider applies the move on its own clock, and `routes_to` reads `agent` as soon as it has recorded it); it wins over `callback_url` for calls to the number, and calls your app places from it still follow your app. `routes_to` reads `agent_pending` while the number is still being moved to the agent |
        | `"agent_id": null`                            | unbinds the agent, so `callback_url` answers calls to the number again                                                                                                                                                                                                                                                                                                                                     |
        | key omitted                                   | left exactly as it is                                                                                                                                                                                                                                                                                                                                                                                      |

        `status` is matched ignoring case. Any combination is accepted:
        `status: "ACTIVE"` with `default_for_app_calls: true` turns a number on as the
        new default, and a `callback_url` sent with either status is written too.
        `agent_id` is applied first, so a refusal to move the number to or from the
        agent leaves everything as it was, and the `409` and `400` refusals below are
        decided before anything is written, so they leave everything as it was too. A
        body that names none of them is refused.

        A number can be on without a callback URL: calls placed from your app then
        connect straight to the number or user they dial, and calls to the number are
        declined.

        ## What it will refuse

        **`default_for_app_calls: false` is `400`.** An account with active voice
        numbers always has exactly one default, so the default moves by giving it to
        another number.

        **Turning the default line off is `409`** while other active voice numbers
        remain. Move the default to another number first. Turning off your last voice
        number is allowed; that turns phone calls off.

        **Making an inactive number the default is `400`.** Send `status: "ACTIVE"` in
        the same call.

        **A number you never turned voice on for is `404`**, and so is an `agent_id`
        that is not one of your agents. Add the number with `POST /v3/channels/voice`.

        **`502` means the number could not be moved to or from the agent**, or an
        `agent_id` was sent while numbers cannot be bound to agents; nothing was
        written.

        The number is the E.164 value in the path with the plus sign URL-encoded
        (`%2B`).

        With `sandbox: true` nothing is written: the request is validated against the
        stored number and the number is reported with `200` as it would read after the
        change.

        Args:
          agent_id: One of your voice agents, such as agent_9f2ab000-0000-4000-8000-000000000001, to
              answer calls to the number, or null to unbind it so the callback URL answers
              them again. The agent wins over callback_url for calls to the number; calls your
              app places from it still follow your app.

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
                    "agent_id": agent_id,
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
        self.rotate_secret = async_to_streamed_response_wrapper(
            voice.rotate_secret,
        )
        self.test = async_to_streamed_response_wrapper(
            voice.test,
        )
