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
from ..._base_client import make_request_options
from ...types.channels import whatsapp_create_params
from ...types.channels.api_response_of_whatsapp_channel import APIResponseOfWhatsappChannel

__all__ = ["WhatsappResource", "AsyncWhatsappResource"]


class WhatsappResource(SyncAPIResource):
    """The senders you send from, one per channel.

    **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

    ## Compliance lives on the market

    Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

    `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

    Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
    """

    @cached_property
    def with_raw_response(self) -> WhatsappResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return WhatsappResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WhatsappResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return WhatsappResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        phone_number_id: Optional[str] | Omit = omit,
        sandbox: bool | Omit = omit,
        waba_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfWhatsappChannel:
        """
        Connects a WhatsApp Business Account shared with us through a Multi-Partner
        Solution to the calling sender profile. Send `x-profile-id` for the profile the
        account belongs to.

        **Two fields, because everything else is derived.** `waba_id` says which of your
        organization's shared accounts this is — you hold one per client, and nothing
        else can say which. `phone_number_id` names the account's number, which is what
        assigns it to the profile as the number it sends from.

        The solution the account arrived through, the client business portfolio that
        owns it, the access token and its expiry are all resolved from your
        organization. They are not accepted here: the first two are Meta's answer about
        provenance, and the token is minted per client business and rotates roughly
        every sixty days, so a value you sent would be stale before it was useful.

        `phone_number_id` is optional. Omit it to connect the account now and settle the
        number later — the channel reads as `ACTION_NEEDED` with `reason_code`
        `CHANNEL_007`, and the profile's WhatsApp messages fail until a number is named.
        They do not fall back to your organization's account. Call this endpoint again
        with `phone_number_id` to name one.

        The same resolution runs behind `channels.whatsapp` on
        `POST /v3/sender-profiles`, so connecting at create and connecting afterwards
        fill the same fields.

        Returns **the account**, not every channel you have — adding one cannot change a
        market or an RCS agent, and `GET /v3/channels` is the whole picture. Giving an
        account up is not self-service: ask support, because deregistering a number
        lands in your own Meta business.

        Args:
          phone_number_id: The Meta phone-number id of the number on WabaId, which assigns it to this
              profile as the number it sends from. It is not checked against the account here,
              so name the account's number; it is refused if another profile already uses it.

              Optional: omit it to connect the account and settle the number later. Nothing
              picks one on your behalf.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          waba_id: WhatsApp Business Account id — one of the accounts shared into your
              organization. Required: the organization holds one per client, and nothing but
              the caller says which is meant here.

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
            "/v3/channels/whatsapp",
            body=maybe_transform(
                {
                    "phone_number_id": phone_number_id,
                    "sandbox": sandbox,
                    "waba_id": waba_id,
                },
                whatsapp_create_params.WhatsappCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfWhatsappChannel,
        )


class AsyncWhatsappResource(AsyncAPIResource):
    """The senders you send from, one per channel.

    **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

    ## Compliance lives on the market

    Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

    `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

    Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
    """

    @cached_property
    def with_raw_response(self) -> AsyncWhatsappResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWhatsappResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWhatsappResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncWhatsappResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        phone_number_id: Optional[str] | Omit = omit,
        sandbox: bool | Omit = omit,
        waba_id: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfWhatsappChannel:
        """
        Connects a WhatsApp Business Account shared with us through a Multi-Partner
        Solution to the calling sender profile. Send `x-profile-id` for the profile the
        account belongs to.

        **Two fields, because everything else is derived.** `waba_id` says which of your
        organization's shared accounts this is — you hold one per client, and nothing
        else can say which. `phone_number_id` names the account's number, which is what
        assigns it to the profile as the number it sends from.

        The solution the account arrived through, the client business portfolio that
        owns it, the access token and its expiry are all resolved from your
        organization. They are not accepted here: the first two are Meta's answer about
        provenance, and the token is minted per client business and rotates roughly
        every sixty days, so a value you sent would be stale before it was useful.

        `phone_number_id` is optional. Omit it to connect the account now and settle the
        number later — the channel reads as `ACTION_NEEDED` with `reason_code`
        `CHANNEL_007`, and the profile's WhatsApp messages fail until a number is named.
        They do not fall back to your organization's account. Call this endpoint again
        with `phone_number_id` to name one.

        The same resolution runs behind `channels.whatsapp` on
        `POST /v3/sender-profiles`, so connecting at create and connecting afterwards
        fill the same fields.

        Returns **the account**, not every channel you have — adding one cannot change a
        market or an RCS agent, and `GET /v3/channels` is the whole picture. Giving an
        account up is not self-service: ask support, because deregistering a number
        lands in your own Meta business.

        Args:
          phone_number_id: The Meta phone-number id of the number on WabaId, which assigns it to this
              profile as the number it sends from. It is not checked against the account here,
              so name the account's number; it is refused if another profile already uses it.

              Optional: omit it to connect the account and settle the number later. Nothing
              picks one on your behalf.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          waba_id: WhatsApp Business Account id — one of the accounts shared into your
              organization. Required: the organization holds one per client, and nothing but
              the caller says which is meant here.

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
            "/v3/channels/whatsapp",
            body=await async_maybe_transform(
                {
                    "phone_number_id": phone_number_id,
                    "sandbox": sandbox,
                    "waba_id": waba_id,
                },
                whatsapp_create_params.WhatsappCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfWhatsappChannel,
        )


class WhatsappResourceWithRawResponse:
    def __init__(self, whatsapp: WhatsappResource) -> None:
        self._whatsapp = whatsapp

        self.create = to_raw_response_wrapper(
            whatsapp.create,
        )


class AsyncWhatsappResourceWithRawResponse:
    def __init__(self, whatsapp: AsyncWhatsappResource) -> None:
        self._whatsapp = whatsapp

        self.create = async_to_raw_response_wrapper(
            whatsapp.create,
        )


class WhatsappResourceWithStreamingResponse:
    def __init__(self, whatsapp: WhatsappResource) -> None:
        self._whatsapp = whatsapp

        self.create = to_streamed_response_wrapper(
            whatsapp.create,
        )


class AsyncWhatsappResourceWithStreamingResponse:
    def __init__(self, whatsapp: AsyncWhatsappResource) -> None:
        self._whatsapp = whatsapp

        self.create = async_to_streamed_response_wrapper(
            whatsapp.create,
        )
