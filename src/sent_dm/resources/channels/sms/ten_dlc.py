# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.channels.sms import ten_dlc_add_campaign_params, ten_dlc_update_campaign_params
from ....types.channels.api_response_of_channel_market import APIResponseOfChannelMarket
from ....types.channels.sms.ten_dlc_campaign_use_case_param import TenDlcCampaignUseCaseParam
from ....types.channels.sms.ten_dlc_list_campaigns_response import TenDlcListCampaignsResponse

__all__ = ["TenDlcResource", "AsyncTenDlcResource"]


class TenDlcResource(SyncAPIResource):
    """The senders you send from, one per channel.

    **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

    ## Compliance lives on the market

    Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

    `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

    Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
    """

    @cached_property
    def with_raw_response(self) -> TenDlcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return TenDlcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TenDlcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return TenDlcResourceWithStreamingResponse(self)

    def add_campaign(
        self,
        *,
        description: str,
        help_keywords: str,
        help_message: str,
        message_flow: str,
        opt_in_keywords: str,
        opt_in_message: str,
        opt_out_keywords: str,
        opt_out_message: str,
        privacy_policy_link: str,
        terms_and_conditions_link: str,
        use_cases: Iterable[TenDlcCampaignUseCaseParam],
        volume: str,
        idempotency_key: str,
        sandbox: bool | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfChannelMarket:
        """
        Registers **a new campaign** on the US `TEN_DLC` market you already hold — the
        one market that registers campaigns. Use it when you want numbers for a
        different use case than the market's existing campaign covers. The campaign is
        filed under the brand the market files under — your organization's when you
        inherit its identity.

        ## What to send

        The new campaign's fields, at the top level of the body: use cases, consent
        narrative, volume, sample messages and keywords, under their keys
        (`description`, `message_flow`, `use_cases`, `volume`, …). It has to be
        complete. A rejected field is keyed by its name (`description`). `id` and
        `inherit` are ignored, so an entry of `campaigns` can be sent as read.

        The identity is the market's and is not sent here. A market whose identity has
        no registration yet, or one not yet submitted for review, is `400`.

        ## What happens

        The campaign is recorded and goes for review; it is not filed with The Campaign
        Registry by this call. **It comes without numbers**: send its `id` from
        `compliance.campaigns` to `POST /v3/channels/sms/{country}/{type}/numbers` to
        give it some. **The campaign you already have, and its numbers, are not
        touched** — including a campaign you run on from your organization.

        **Each call files a new campaign**, which is charged when it is submitted. Send
        an `Idempotency-Key` so a retried request does not file a second one.

        To change a campaign, use
        `PATCH /v3/channels/sms/US/TEN_DLC/campaigns/{campaignId}`;
        `PATCH /v3/channels/sms/US/TEN_DLC` changes the brand and documents only, and
        refuses a campaign or numbers (`400`).

        Returns **the market**, in the shape `GET /v3/channels/sms/US/TEN_DLC` returns,
        with `202`.

        Args:
          description: What this programme sends. TCR description: what recipients will get and why, in
              a sentence. The only one of these TCR takes verbatim as a description of the
              programme, which is why it is asked for rather than derived from the customer's
              name. Required when `compliance.campaign.inherit != true`.

          help_keywords: Help keywords. TCR helpKeywords, comma separated, e.g. HELP,INFO. Required when
              `compliance.campaign.inherit != true`.

          help_message: Help reply. TCR helpMessage. Its presence is what sets subscriberHelp. Required
              when `compliance.campaign.inherit != true`.

          message_flow: Consent narrative. TCR messageFlow: how recipients opt in, in prose. Under 40
              characters is refused, and carriers reject vague descriptions — say where opt-in
              happens, that the box is unchecked by default, and that consent is not a
              condition of purchase. Required when `compliance.campaign.inherit != true`.

          opt_in_keywords: Opt-in keywords. TCR optinKeywords, comma separated, e.g. START,YES. Required
              when `compliance.campaign.inherit != true`.

          opt_in_message: Opt-in confirmation. TCR optinMessage. Should state message frequency and that
              rates may apply. Its presence is what sets subscriberOptin. Required when
              `compliance.campaign.inherit != true`.

          opt_out_keywords: Opt-out keywords. TCR optoutKeywords, comma separated. STOP, END, CANCEL,
              UNSUBSCRIBE and QUIT are honoured regardless of what is declared. Required when
              `compliance.campaign.inherit != true`.

          opt_out_message: Opt-out confirmation. TCR optoutMessage. Its presence is what sets
              subscriberOptout. Required when `compliance.campaign.inherit != true`.

          privacy_policy_link: Privacy policy URL. TCR privacyPolicyLink. Required when
              `compliance.campaign.inherit != true`.

          terms_and_conditions_link: Terms and conditions URL. TCR termsAndConditionsLink. Required when
              `compliance.campaign.inherit != true`.

          use_cases: Use cases. What the campaign sends, and an example of each. One to five entries;
              how they register is decided by volume, never declared. Required when
              `compliance.campaign.inherit != true`.

          volume: Expected monthly volume. Required whenever the campaign's fields are written. A
              whole number of messages, e.g. 1000 or 10000. Decides how the campaign registers
              and which fee tier applies: below the low-volume threshold it registers as
              LOW_VOLUME with sub-use-cases, above it as a single use case or MIXED. Omitting
              it registers the campaign at the higher-fee standard tier. Required when
              `compliance.campaign.inherit != true`, whenever its block is written.

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
            "/v3/channels/sms/US/TEN_DLC/campaigns",
            body=maybe_transform(
                {
                    "description": description,
                    "help_keywords": help_keywords,
                    "help_message": help_message,
                    "message_flow": message_flow,
                    "opt_in_keywords": opt_in_keywords,
                    "opt_in_message": opt_in_message,
                    "opt_out_keywords": opt_out_keywords,
                    "opt_out_message": opt_out_message,
                    "privacy_policy_link": privacy_policy_link,
                    "terms_and_conditions_link": terms_and_conditions_link,
                    "use_cases": use_cases,
                    "volume": volume,
                    "sandbox": sandbox,
                },
                ten_dlc_add_campaign_params.TenDlcAddCampaignParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfChannelMarket,
        )

    def list_campaigns(
        self,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenDlcListCampaignsResponse:
        """
        Every campaign your US `TEN_DLC` market registers, oldest first, each with its
        `id`, where it stands and `inherit` (`true` for your organization's) beside its
        fields — the list `GET /v3/channels/sms/US/TEN_DLC` reports under
        `compliance.campaigns`. Add one with `POST` on this path, and change one of your
        own with `PATCH /v3/channels/sms/US/TEN_DLC/campaigns/{id}`.

        Each campaign has a `status` of its own, so a market on several says which is
        approved: `ACTIVE` once the carriers have elected it, `PENDING_REVIEW` until
        then, `ACTION_NEEDED` when it came back for correction, `DECLINED` when the
        carriers refused it, `INACTIVE` once it has ended. Why the market is held up is
        the market's own `reason`, which names the campaign concerned. `status` is
        read-only and ignored when the entry is sent back.

        A customer without a US `TEN_DLC` market is `404`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            "/v3/channels/sms/US/TEN_DLC/campaigns",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenDlcListCampaignsResponse,
        )

    def update_campaign(
        self,
        campaign_id: str,
        *,
        description: str | Omit = omit,
        help_keywords: str | Omit = omit,
        help_message: str | Omit = omit,
        message_flow: str | Omit = omit,
        opt_in_keywords: str | Omit = omit,
        opt_in_message: str | Omit = omit,
        opt_out_keywords: str | Omit = omit,
        opt_out_message: str | Omit = omit,
        privacy_policy_link: str | Omit = omit,
        sandbox: bool | Omit = omit,
        terms_and_conditions_link: str | Omit = omit,
        use_cases: Iterable[TenDlcCampaignUseCaseParam] | Omit = omit,
        volume: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfChannelMarket:
        """
        Changes **one campaign of your own** on the US `TEN_DLC` market, named by its
        `id` in the market's `compliance.campaigns`.

        ## What to send

        The fields to change, at the top level of the body, under their keys
        (`description`, `message_flow`, `use_cases`, `help_message`, …). A field you
        leave out keeps its value, and a rejected one is keyed by its name. `id` and
        `"inherit": false` are ignored, so an entry of `campaigns` can be sent as read;
        `"inherit": true` is `400`, because this call changes a campaign's fields, not
        whose campaign you run on. The campaign only: add numbers with
        `POST /v3/channels/sms/US/TEN_DLC/numbers`, and change the brand or documents
        with `PATCH /v3/channels/sms/US/TEN_DLC`.

        ## When it can be changed

        Until it is filed with The Campaign Registry, and again when we ask you to
        correct it. That correction sends it back for review. A filed campaign is
        otherwise `409`, and so is a change between low and high volume once it is
        registered. A campaign you run on from your organization is `409` too: it is the
        organization's to change. So is one out of service: expired, deactivated or
        released.

        Returns **the market**, in the shape `GET /v3/channels/sms/US/TEN_DLC` returns.

        Args:
          description: What this programme sends. TCR description: what recipients will get and why, in
              a sentence. The only one of these TCR takes verbatim as a description of the
              programme, which is why it is asked for rather than derived from the customer's
              name. Required when `compliance.campaign.inherit != true`.

          help_keywords: Help keywords. TCR helpKeywords, comma separated, e.g. HELP,INFO. Required when
              `compliance.campaign.inherit != true`.

          help_message: Help reply. TCR helpMessage. Its presence is what sets subscriberHelp. Required
              when `compliance.campaign.inherit != true`.

          message_flow: Consent narrative. TCR messageFlow: how recipients opt in, in prose. Under 40
              characters is refused, and carriers reject vague descriptions — say where opt-in
              happens, that the box is unchecked by default, and that consent is not a
              condition of purchase. Required when `compliance.campaign.inherit != true`.

          opt_in_keywords: Opt-in keywords. TCR optinKeywords, comma separated, e.g. START,YES. Required
              when `compliance.campaign.inherit != true`.

          opt_in_message: Opt-in confirmation. TCR optinMessage. Should state message frequency and that
              rates may apply. Its presence is what sets subscriberOptin. Required when
              `compliance.campaign.inherit != true`.

          opt_out_keywords: Opt-out keywords. TCR optoutKeywords, comma separated. STOP, END, CANCEL,
              UNSUBSCRIBE and QUIT are honoured regardless of what is declared. Required when
              `compliance.campaign.inherit != true`.

          opt_out_message: Opt-out confirmation. TCR optoutMessage. Its presence is what sets
              subscriberOptout. Required when `compliance.campaign.inherit != true`.

          privacy_policy_link: Privacy policy URL. TCR privacyPolicyLink. Required when
              `compliance.campaign.inherit != true`.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          terms_and_conditions_link: Terms and conditions URL. TCR termsAndConditionsLink. Required when
              `compliance.campaign.inherit != true`.

          use_cases: Use cases. What the campaign sends, and an example of each. One to five entries;
              how they register is decided by volume, never declared. Required when
              `compliance.campaign.inherit != true`.

          volume: Expected monthly volume. Required whenever the campaign's fields are written. A
              whole number of messages, e.g. 1000 or 10000. Decides how the campaign registers
              and which fee tier applies: below the low-volume threshold it registers as
              LOW_VOLUME with sub-use-cases, above it as a single use case or MIXED. Omitting
              it registers the campaign at the higher-fee standard tier. Required when
              `compliance.campaign.inherit != true`, whenever its block is written.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
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
            path_template("/v3/channels/sms/US/TEN_DLC/campaigns/{campaign_id}", campaign_id=campaign_id),
            body=maybe_transform(
                {
                    "description": description,
                    "help_keywords": help_keywords,
                    "help_message": help_message,
                    "message_flow": message_flow,
                    "opt_in_keywords": opt_in_keywords,
                    "opt_in_message": opt_in_message,
                    "opt_out_keywords": opt_out_keywords,
                    "opt_out_message": opt_out_message,
                    "privacy_policy_link": privacy_policy_link,
                    "sandbox": sandbox,
                    "terms_and_conditions_link": terms_and_conditions_link,
                    "use_cases": use_cases,
                    "volume": volume,
                },
                ten_dlc_update_campaign_params.TenDlcUpdateCampaignParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfChannelMarket,
        )


class AsyncTenDlcResource(AsyncAPIResource):
    """The senders you send from, one per channel.

    **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

    ## Compliance lives on the market

    Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

    `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

    Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTenDlcResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTenDlcResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTenDlcResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncTenDlcResourceWithStreamingResponse(self)

    async def add_campaign(
        self,
        *,
        description: str,
        help_keywords: str,
        help_message: str,
        message_flow: str,
        opt_in_keywords: str,
        opt_in_message: str,
        opt_out_keywords: str,
        opt_out_message: str,
        privacy_policy_link: str,
        terms_and_conditions_link: str,
        use_cases: Iterable[TenDlcCampaignUseCaseParam],
        volume: str,
        idempotency_key: str,
        sandbox: bool | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfChannelMarket:
        """
        Registers **a new campaign** on the US `TEN_DLC` market you already hold — the
        one market that registers campaigns. Use it when you want numbers for a
        different use case than the market's existing campaign covers. The campaign is
        filed under the brand the market files under — your organization's when you
        inherit its identity.

        ## What to send

        The new campaign's fields, at the top level of the body: use cases, consent
        narrative, volume, sample messages and keywords, under their keys
        (`description`, `message_flow`, `use_cases`, `volume`, …). It has to be
        complete. A rejected field is keyed by its name (`description`). `id` and
        `inherit` are ignored, so an entry of `campaigns` can be sent as read.

        The identity is the market's and is not sent here. A market whose identity has
        no registration yet, or one not yet submitted for review, is `400`.

        ## What happens

        The campaign is recorded and goes for review; it is not filed with The Campaign
        Registry by this call. **It comes without numbers**: send its `id` from
        `compliance.campaigns` to `POST /v3/channels/sms/{country}/{type}/numbers` to
        give it some. **The campaign you already have, and its numbers, are not
        touched** — including a campaign you run on from your organization.

        **Each call files a new campaign**, which is charged when it is submitted. Send
        an `Idempotency-Key` so a retried request does not file a second one.

        To change a campaign, use
        `PATCH /v3/channels/sms/US/TEN_DLC/campaigns/{campaignId}`;
        `PATCH /v3/channels/sms/US/TEN_DLC` changes the brand and documents only, and
        refuses a campaign or numbers (`400`).

        Returns **the market**, in the shape `GET /v3/channels/sms/US/TEN_DLC` returns,
        with `202`.

        Args:
          description: What this programme sends. TCR description: what recipients will get and why, in
              a sentence. The only one of these TCR takes verbatim as a description of the
              programme, which is why it is asked for rather than derived from the customer's
              name. Required when `compliance.campaign.inherit != true`.

          help_keywords: Help keywords. TCR helpKeywords, comma separated, e.g. HELP,INFO. Required when
              `compliance.campaign.inherit != true`.

          help_message: Help reply. TCR helpMessage. Its presence is what sets subscriberHelp. Required
              when `compliance.campaign.inherit != true`.

          message_flow: Consent narrative. TCR messageFlow: how recipients opt in, in prose. Under 40
              characters is refused, and carriers reject vague descriptions — say where opt-in
              happens, that the box is unchecked by default, and that consent is not a
              condition of purchase. Required when `compliance.campaign.inherit != true`.

          opt_in_keywords: Opt-in keywords. TCR optinKeywords, comma separated, e.g. START,YES. Required
              when `compliance.campaign.inherit != true`.

          opt_in_message: Opt-in confirmation. TCR optinMessage. Should state message frequency and that
              rates may apply. Its presence is what sets subscriberOptin. Required when
              `compliance.campaign.inherit != true`.

          opt_out_keywords: Opt-out keywords. TCR optoutKeywords, comma separated. STOP, END, CANCEL,
              UNSUBSCRIBE and QUIT are honoured regardless of what is declared. Required when
              `compliance.campaign.inherit != true`.

          opt_out_message: Opt-out confirmation. TCR optoutMessage. Its presence is what sets
              subscriberOptout. Required when `compliance.campaign.inherit != true`.

          privacy_policy_link: Privacy policy URL. TCR privacyPolicyLink. Required when
              `compliance.campaign.inherit != true`.

          terms_and_conditions_link: Terms and conditions URL. TCR termsAndConditionsLink. Required when
              `compliance.campaign.inherit != true`.

          use_cases: Use cases. What the campaign sends, and an example of each. One to five entries;
              how they register is decided by volume, never declared. Required when
              `compliance.campaign.inherit != true`.

          volume: Expected monthly volume. Required whenever the campaign's fields are written. A
              whole number of messages, e.g. 1000 or 10000. Decides how the campaign registers
              and which fee tier applies: below the low-volume threshold it registers as
              LOW_VOLUME with sub-use-cases, above it as a single use case or MIXED. Omitting
              it registers the campaign at the higher-fee standard tier. Required when
              `compliance.campaign.inherit != true`, whenever its block is written.

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
            "/v3/channels/sms/US/TEN_DLC/campaigns",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "help_keywords": help_keywords,
                    "help_message": help_message,
                    "message_flow": message_flow,
                    "opt_in_keywords": opt_in_keywords,
                    "opt_in_message": opt_in_message,
                    "opt_out_keywords": opt_out_keywords,
                    "opt_out_message": opt_out_message,
                    "privacy_policy_link": privacy_policy_link,
                    "terms_and_conditions_link": terms_and_conditions_link,
                    "use_cases": use_cases,
                    "volume": volume,
                    "sandbox": sandbox,
                },
                ten_dlc_add_campaign_params.TenDlcAddCampaignParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfChannelMarket,
        )

    async def list_campaigns(
        self,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenDlcListCampaignsResponse:
        """
        Every campaign your US `TEN_DLC` market registers, oldest first, each with its
        `id`, where it stands and `inherit` (`true` for your organization's) beside its
        fields — the list `GET /v3/channels/sms/US/TEN_DLC` reports under
        `compliance.campaigns`. Add one with `POST` on this path, and change one of your
        own with `PATCH /v3/channels/sms/US/TEN_DLC/campaigns/{id}`.

        Each campaign has a `status` of its own, so a market on several says which is
        approved: `ACTIVE` once the carriers have elected it, `PENDING_REVIEW` until
        then, `ACTION_NEEDED` when it came back for correction, `DECLINED` when the
        carriers refused it, `INACTIVE` once it has ended. Why the market is held up is
        the market's own `reason`, which names the campaign concerned. `status` is
        read-only and ignored when the entry is sent back.

        A customer without a US `TEN_DLC` market is `404`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            "/v3/channels/sms/US/TEN_DLC/campaigns",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TenDlcListCampaignsResponse,
        )

    async def update_campaign(
        self,
        campaign_id: str,
        *,
        description: str | Omit = omit,
        help_keywords: str | Omit = omit,
        help_message: str | Omit = omit,
        message_flow: str | Omit = omit,
        opt_in_keywords: str | Omit = omit,
        opt_in_message: str | Omit = omit,
        opt_out_keywords: str | Omit = omit,
        opt_out_message: str | Omit = omit,
        privacy_policy_link: str | Omit = omit,
        sandbox: bool | Omit = omit,
        terms_and_conditions_link: str | Omit = omit,
        use_cases: Iterable[TenDlcCampaignUseCaseParam] | Omit = omit,
        volume: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfChannelMarket:
        """
        Changes **one campaign of your own** on the US `TEN_DLC` market, named by its
        `id` in the market's `compliance.campaigns`.

        ## What to send

        The fields to change, at the top level of the body, under their keys
        (`description`, `message_flow`, `use_cases`, `help_message`, …). A field you
        leave out keeps its value, and a rejected one is keyed by its name. `id` and
        `"inherit": false` are ignored, so an entry of `campaigns` can be sent as read;
        `"inherit": true` is `400`, because this call changes a campaign's fields, not
        whose campaign you run on. The campaign only: add numbers with
        `POST /v3/channels/sms/US/TEN_DLC/numbers`, and change the brand or documents
        with `PATCH /v3/channels/sms/US/TEN_DLC`.

        ## When it can be changed

        Until it is filed with The Campaign Registry, and again when we ask you to
        correct it. That correction sends it back for review. A filed campaign is
        otherwise `409`, and so is a change between low and high volume once it is
        registered. A campaign you run on from your organization is `409` too: it is the
        organization's to change. So is one out of service: expired, deactivated or
        released.

        Returns **the market**, in the shape `GET /v3/channels/sms/US/TEN_DLC` returns.

        Args:
          description: What this programme sends. TCR description: what recipients will get and why, in
              a sentence. The only one of these TCR takes verbatim as a description of the
              programme, which is why it is asked for rather than derived from the customer's
              name. Required when `compliance.campaign.inherit != true`.

          help_keywords: Help keywords. TCR helpKeywords, comma separated, e.g. HELP,INFO. Required when
              `compliance.campaign.inherit != true`.

          help_message: Help reply. TCR helpMessage. Its presence is what sets subscriberHelp. Required
              when `compliance.campaign.inherit != true`.

          message_flow: Consent narrative. TCR messageFlow: how recipients opt in, in prose. Under 40
              characters is refused, and carriers reject vague descriptions — say where opt-in
              happens, that the box is unchecked by default, and that consent is not a
              condition of purchase. Required when `compliance.campaign.inherit != true`.

          opt_in_keywords: Opt-in keywords. TCR optinKeywords, comma separated, e.g. START,YES. Required
              when `compliance.campaign.inherit != true`.

          opt_in_message: Opt-in confirmation. TCR optinMessage. Should state message frequency and that
              rates may apply. Its presence is what sets subscriberOptin. Required when
              `compliance.campaign.inherit != true`.

          opt_out_keywords: Opt-out keywords. TCR optoutKeywords, comma separated. STOP, END, CANCEL,
              UNSUBSCRIBE and QUIT are honoured regardless of what is declared. Required when
              `compliance.campaign.inherit != true`.

          opt_out_message: Opt-out confirmation. TCR optoutMessage. Its presence is what sets
              subscriberOptout. Required when `compliance.campaign.inherit != true`.

          privacy_policy_link: Privacy policy URL. TCR privacyPolicyLink. Required when
              `compliance.campaign.inherit != true`.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          terms_and_conditions_link: Terms and conditions URL. TCR termsAndConditionsLink. Required when
              `compliance.campaign.inherit != true`.

          use_cases: Use cases. What the campaign sends, and an example of each. One to five entries;
              how they register is decided by volume, never declared. Required when
              `compliance.campaign.inherit != true`.

          volume: Expected monthly volume. Required whenever the campaign's fields are written. A
              whole number of messages, e.g. 1000 or 10000. Decides how the campaign registers
              and which fee tier applies: below the low-volume threshold it registers as
              LOW_VOLUME with sub-use-cases, above it as a single use case or MIXED. Omitting
              it registers the campaign at the higher-fee standard tier. Required when
              `compliance.campaign.inherit != true`, whenever its block is written.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not campaign_id:
            raise ValueError(f"Expected a non-empty value for `campaign_id` but received {campaign_id!r}")
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
            path_template("/v3/channels/sms/US/TEN_DLC/campaigns/{campaign_id}", campaign_id=campaign_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "help_keywords": help_keywords,
                    "help_message": help_message,
                    "message_flow": message_flow,
                    "opt_in_keywords": opt_in_keywords,
                    "opt_in_message": opt_in_message,
                    "opt_out_keywords": opt_out_keywords,
                    "opt_out_message": opt_out_message,
                    "privacy_policy_link": privacy_policy_link,
                    "sandbox": sandbox,
                    "terms_and_conditions_link": terms_and_conditions_link,
                    "use_cases": use_cases,
                    "volume": volume,
                },
                ten_dlc_update_campaign_params.TenDlcUpdateCampaignParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfChannelMarket,
        )


class TenDlcResourceWithRawResponse:
    def __init__(self, ten_dlc: TenDlcResource) -> None:
        self._ten_dlc = ten_dlc

        self.add_campaign = to_raw_response_wrapper(
            ten_dlc.add_campaign,
        )
        self.list_campaigns = to_raw_response_wrapper(
            ten_dlc.list_campaigns,
        )
        self.update_campaign = to_raw_response_wrapper(
            ten_dlc.update_campaign,
        )


class AsyncTenDlcResourceWithRawResponse:
    def __init__(self, ten_dlc: AsyncTenDlcResource) -> None:
        self._ten_dlc = ten_dlc

        self.add_campaign = async_to_raw_response_wrapper(
            ten_dlc.add_campaign,
        )
        self.list_campaigns = async_to_raw_response_wrapper(
            ten_dlc.list_campaigns,
        )
        self.update_campaign = async_to_raw_response_wrapper(
            ten_dlc.update_campaign,
        )


class TenDlcResourceWithStreamingResponse:
    def __init__(self, ten_dlc: TenDlcResource) -> None:
        self._ten_dlc = ten_dlc

        self.add_campaign = to_streamed_response_wrapper(
            ten_dlc.add_campaign,
        )
        self.list_campaigns = to_streamed_response_wrapper(
            ten_dlc.list_campaigns,
        )
        self.update_campaign = to_streamed_response_wrapper(
            ten_dlc.update_campaign,
        )


class AsyncTenDlcResourceWithStreamingResponse:
    def __init__(self, ten_dlc: AsyncTenDlcResource) -> None:
        self._ten_dlc = ten_dlc

        self.add_campaign = async_to_streamed_response_wrapper(
            ten_dlc.add_campaign,
        )
        self.list_campaigns = async_to_streamed_response_wrapper(
            ten_dlc.list_campaigns,
        )
        self.update_campaign = async_to_streamed_response_wrapper(
            ten_dlc.update_campaign,
        )
