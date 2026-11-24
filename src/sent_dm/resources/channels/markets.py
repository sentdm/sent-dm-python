# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

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
    market_update_params,
    market_add_numbers_params,
    market_list_numbers_params,
    market_replace_numbers_params,
)
from ...types.channels.market_compliance_param import MarketComplianceParam
from ...types.channels.sms_number_request_param import SMSNumberRequestParam
from ...types.channels.api_response_of_channel_market import APIResponseOfChannelMarket
from ...types.channels.api_response_of_market_numbers import APIResponseOfMarketNumbers
from ...types.channels.api_response_of_list_of_channel_market import APIResponseOfListOfChannelMarket

__all__ = ["MarketsResource", "AsyncMarketsResource"]


class MarketsResource(SyncAPIResource):
    """The senders you send from, one per channel.

    **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

    ## Compliance lives on the market

    Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

    `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

    Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
    """

    @cached_property
    def with_raw_response(self) -> MarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return MarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return MarketsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        type: str,
        *,
        channel: str,
        country: str,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfChannelMarket:
        """
        Reads one market you send in — its sender, where that sender stands, and
        everything its compliance holds.

        ## What `compliance` carries

        A market that registers with a compliance regime reports `brand` — the identity
        the registration is filed against — and `campaign`, the programme filed against
        it. Each carries `inherit`, saying whether it is yours or your organization's.

        `compliance.brand.vetting` is the brand's external vetting at The Campaign
        Registry, read-only: `score` (0-100, the figure US carriers set 10DLC throughput
        by), `status` (`PENDING`, `UNSCORE`, `ACTIVE`, `FAILED` or `EXPIRED`; carriers
        read the score of an `ACTIVE` vet only), `vetted_at` and `expires_at`. It is
        `null` while no vetting record is held for the brand, and `score` is `null` for
        a vet that has none yet. A profile on your organization's brand reads your
        organization's vetting.

        A market that registers with nobody has neither, so **both keys are absent**
        rather than null: absent says this market does not ask, where null would say it
        asks and you supplied nothing. It reports `documents` instead.

        `GET /v3/compliance/requirements` says what a market demands of any new
        customer; this says what you gave it.

        ## Writing it back

        **`PATCH` this same path**, with the `compliance` object from this response:

        ```json
        { "compliance": { "brand": { "tax_id": "12-3456789" } } }
        ```

        Nothing else to learn — what comes back can be sent back, an omitted key is left
        alone. There is no sub-resource for either half: both are singletons of the
        market, so both are written here.

        `GET /v3/compliance/requirements` says what a market demands of anybody; this
        says what you gave it.

        Send `x-profile-id` with an organization key to read one of your profiles'
        markets.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel:
            raise ValueError(f"Expected a non-empty value for `channel` but received {channel!r}")
        if not country:
            raise ValueError(f"Expected a non-empty value for `country` but received {country!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v3/channels/{channel}/{country}/{type}", channel=channel, country=country, type=type),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfChannelMarket,
        )

    def update(
        self,
        type: str,
        *,
        channel: str,
        country: str,
        compliance: MarketComplianceParam | Omit = omit,
        sandbox: bool | Omit = omit,
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
        Supplies the market's identity and documents, and answers with the market as
        stored — the same shape `GET` on this path returns.

        | To change                               | Send                                                                                                     |
        | --------------------------------------- | -------------------------------------------------------------------------------------------------------- |
        | a `brand` value (US `TEN_DLC`)          | `compliance.brand`, as below                                                                             |
        | a registration sent back for correction | `compliance.brand` — the identity is accepted even once filed, and the registration goes back for review |
        | a document, in any market               | a multipart file named after the document's key                                                          |
        | a campaign                              | `PATCH /v3/channels/sms/US/TEN_DLC/campaigns/{id}` — `compliance.campaign` here is `400`                 |
        | the numbers                             | `POST /v3/channels/{channel}/{country}/{type}/numbers` — `numbers` here is `400`                         |

        ## Partial, at every level

        **An omitted key is left alone. An explicit `null` clears it.** Those are
        different requests, so `{}` changes nothing and is refused rather than silently
        accepted, and correcting one field does not blank the others.

        ```json
        { "compliance": { "brand": { "contact_phone": "+12125550123" } } }
        ```

        | Body                           | Effect                                                       |
        | ------------------------------ | ------------------------------------------------------------ |
        | `"brand": { … }`               | supplies or corrects the identity, and takes one of your own |
        | `"brand": { "inherit": true }` | runs on your organization's, giving up your own              |
        | `"brand": null`                | the same thing, said the short way                           |
        | key omitted                    | left exactly as it is                                        |

        The brand read on this path, its `id` and `vetting` included, can be sent back
        unchanged: both are read-only and ignored.

        ## Every other market

        Markets that register with no regime have no brand, so `compliance` is `400`
        there. Their compliance is documents, sent here as multipart.

        ## Documents

        Send `multipart/form-data` with **each file named after the compliance key it
        satisfies** — the key `GET /v3/channels/{channel}/{country}/compliance` lists. A
        file that matches no document the market asks for is `400` naming the keys that
        would, and a file the upload rules refuse (empty, too large, an unsupported
        type) is `422`. `compliance` may ride in the same form as a text part holding
        its JSON.

        ## What it will refuse

        **A filed identity is `409`.** Once the registration has gone to The Campaign
        Registry they hold a copy, and a local change would diverge from it silently.
        The exception is a registration sent back for correction: the identity is
        accepted, and the registration goes back for review. Refiling it with The
        Campaign Registry stays with Sent.

        Nothing is submitted to a regime here. Send `x-profile-id` with an organization
        key to write one of your profiles' markets.

        Args:
          compliance: The compliance values a market registers with. `brand` and `campaign` apply to
              US `TEN_DLC`; other markets fill this map with the document keys their own
              requirements name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel:
            raise ValueError(f"Expected a non-empty value for `channel` but received {channel!r}")
        if not country:
            raise ValueError(f"Expected a non-empty value for `country` but received {country!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
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
            path_template("/v3/channels/{channel}/{country}/{type}", channel=channel, country=country, type=type),
            body=maybe_transform(
                {
                    "compliance": compliance,
                    "sandbox": sandbox,
                },
                market_update_params.MarketUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfChannelMarket,
        )

    def list(
        self,
        channel: str,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfListOfChannelMarket:
        """
        Every market you send SMS in, each with its sender, where that sender stands,
        and what its compliance holds.

        The same entries `GET /v3/channels` reports under `sms`, and the same shape
        `GET /v3/channels/sms/{country}/{type}` returns for one of them — so a list, a
        member read and the all-channels read cannot describe a market differently.

        Send `x-profile-id` with an organization key to list one of your profiles'
        markets.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel:
            raise ValueError(f"Expected a non-empty value for `channel` but received {channel!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v3/channels/{channel}", channel=channel),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfListOfChannelMarket,
        )

    def add_numbers(
        self,
        type: str,
        *,
        channel: str,
        country: str,
        numbers: Iterable[Optional[SMSNumberRequestParam]],
        idempotency_key: str,
        campaign_id: Optional[str] | Omit = omit,
        sandbox: bool | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfChannelMarket:
        """Adds numbers to a market you hold.

        They are **added** to what it already asks
        for, never replacing it — with one exception: a US `TEN_DLC` campaign opened
        without `numbers` asks for one number in any area code by default, and while it
        holds no number yet, the first numbers added replace that default. Once it holds
        one, they are added beside it.

        ## Where they go

        - **SMS US `TEN_DLC`**: to **one campaign of your own**, named by `campaign_id`
          — the `id` of an entry in the market's `compliance.campaigns`
          (`GET /v3/channels/sms/US/TEN_DLC`). Required: left out it is `400` naming
          your campaigns in service. One you inherit from your organization is `400`:
          its numbers are the organization's. One out of service — expired, deactivated
          or released — is `409`. A campaign the carriers have not approved yet gets its
          numbers when they do; an approved one gets them now. With everything it asks
          for, a campaign holds at most 49 numbers, counting one for each sender profile
          inheriting it.
        - **`LOCAL`**: to the market, claimed from inventory now; what inventory cannot
          cover stays pending. No `campaign_id`. A market holds at most 49 numbers.
        - **Any other sender type** takes no numbers: `400`.

        ## What to send

        `numbers` — the list `POST /v3/channels/sms` takes, one entry per area code —
        and, on US `TEN_DLC`, `campaign_id`, required.

        Until a number is assigned it reads as `PROVISIONING` in the market's `numbers`,
        with the area code it was asked for. Returns **the market**, in the shape
        `GET /v3/channels/sms/{country}/{type}` returns, with `202`.

        Args:
          numbers: The numbers, one entry per area code, e.g. [{"area_code": "415", "quantity": 2},
              {"quantity": 1}]. quantity defaults to 1, and an entry without area_code means
              any area code. Required.

              POST adds them to what the market or campaign already asks for; PATCH replaces
              that list with them, and has to cover every number already held, since none is
              ever released.

          campaign_id: The campaign to add the numbers to, as campaigns[].id reports it. Required on
              SMS US TEN_DLC, where every number belongs to a campaign; refused on a market
              without campaigns.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel:
            raise ValueError(f"Expected a non-empty value for `channel` but received {channel!r}")
        if not country:
            raise ValueError(f"Expected a non-empty value for `country` but received {country!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
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
            path_template(
                "/v3/channels/{channel}/{country}/{type}/numbers", channel=channel, country=country, type=type
            ),
            body=maybe_transform(
                {
                    "numbers": numbers,
                    "campaign_id": campaign_id,
                    "sandbox": sandbox,
                },
                market_add_numbers_params.MarketAddNumbersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfChannelMarket,
        )

    def list_numbers(
        self,
        type: str,
        *,
        channel: str,
        country: str,
        campaign_id: Optional[str] | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfMarketNumbers:
        """
        Every number you hold in one market (country and sender type): `ACTIVE` once it
        can send, `PROVISIONING` while it is still to be assigned (it then has no
        `sender_value` yet), `INACTIVE` once it could send and no longer can. US
        `TEN_DLC` numbers name their `campaign_id`, and `?campaign_id=` keeps one
        campaign's.

        A market you do not hold is `404`. Add numbers with `POST` on the same path.

        Args:
          campaign_id: Only the numbers of this campaign (US TEN_DLC); all of the market's when absent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel:
            raise ValueError(f"Expected a non-empty value for `channel` but received {channel!r}")
        if not country:
            raise ValueError(f"Expected a non-empty value for `country` but received {country!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            path_template(
                "/v3/channels/{channel}/{country}/{type}/numbers", channel=channel, country=country, type=type
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"campaign_id": campaign_id}, market_list_numbers_params.MarketListNumbersParams),
            ),
            cast_to=APIResponseOfMarketNumbers,
        )

    def replace_numbers(
        self,
        type: str,
        *,
        channel: str,
        country: str,
        numbers: Iterable[Optional[SMSNumberRequestParam]],
        campaign_id: Optional[str] | Omit = omit,
        sandbox: bool | Omit = omit,
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
        Replaces the numbers a market you hold asks for — their area codes and counts —
        with the list you send. To add to them instead, use `POST` on this path.

        ## Whose numbers

        - **SMS US `TEN_DLC`**: **one campaign of your own**, named by `campaign_id` —
          the `id` of an entry in the market's `compliance.campaigns`. Required. So a
          campaign sent back for correction can change its area codes without being
          recreated. One you inherit from your organization is `400`; one out of service
          is `409`. With everything it asks for, a campaign holds at most 49 numbers,
          counting one for each sender profile inheriting it.
        - **`LOCAL`**: the market's own, claimed from inventory now; what inventory
          cannot cover stays pending. No `campaign_id`.
        - **Any other sender type** takes no numbers: `400`.

        ## What to send

        `numbers` — the list `POST /v3/channels/sms` takes, one entry per area code, an
        entry without `area_code` meaning any — and, on US `TEN_DLC`, `campaign_id`.

        **Numbers already assigned are kept.** Nothing is released here, so a list that
        no longer covers a number already held is `400`, naming how many it leaves out.
        Lowering a count nothing has filled yet is fine.

        Until a number is assigned it reads as `PROVISIONING` in the market's `numbers`,
        with the area code it was asked for. Returns **the market**, in the shape
        `GET /v3/channels/sms/{country}/{type}` returns.

        Args:
          numbers: The numbers, one entry per area code, e.g. [{"area_code": "415", "quantity": 2},
              {"quantity": 1}]. quantity defaults to 1, and an entry without area_code means
              any area code. Required.

              POST adds them to what the market or campaign already asks for; PATCH replaces
              that list with them, and has to cover every number already held, since none is
              ever released.

          campaign_id: The campaign to add the numbers to, as campaigns[].id reports it. Required on
              SMS US TEN_DLC, where every number belongs to a campaign; refused on a market
              without campaigns.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel:
            raise ValueError(f"Expected a non-empty value for `channel` but received {channel!r}")
        if not country:
            raise ValueError(f"Expected a non-empty value for `country` but received {country!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
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
            path_template(
                "/v3/channels/{channel}/{country}/{type}/numbers", channel=channel, country=country, type=type
            ),
            body=maybe_transform(
                {
                    "numbers": numbers,
                    "campaign_id": campaign_id,
                    "sandbox": sandbox,
                },
                market_replace_numbers_params.MarketReplaceNumbersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfChannelMarket,
        )


class AsyncMarketsResource(AsyncAPIResource):
    """The senders you send from, one per channel.

    **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

    ## Compliance lives on the market

    Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

    `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

    Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
    """

    @cached_property
    def with_raw_response(self) -> AsyncMarketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncMarketsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        type: str,
        *,
        channel: str,
        country: str,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfChannelMarket:
        """
        Reads one market you send in — its sender, where that sender stands, and
        everything its compliance holds.

        ## What `compliance` carries

        A market that registers with a compliance regime reports `brand` — the identity
        the registration is filed against — and `campaign`, the programme filed against
        it. Each carries `inherit`, saying whether it is yours or your organization's.

        `compliance.brand.vetting` is the brand's external vetting at The Campaign
        Registry, read-only: `score` (0-100, the figure US carriers set 10DLC throughput
        by), `status` (`PENDING`, `UNSCORE`, `ACTIVE`, `FAILED` or `EXPIRED`; carriers
        read the score of an `ACTIVE` vet only), `vetted_at` and `expires_at`. It is
        `null` while no vetting record is held for the brand, and `score` is `null` for
        a vet that has none yet. A profile on your organization's brand reads your
        organization's vetting.

        A market that registers with nobody has neither, so **both keys are absent**
        rather than null: absent says this market does not ask, where null would say it
        asks and you supplied nothing. It reports `documents` instead.

        `GET /v3/compliance/requirements` says what a market demands of any new
        customer; this says what you gave it.

        ## Writing it back

        **`PATCH` this same path**, with the `compliance` object from this response:

        ```json
        { "compliance": { "brand": { "tax_id": "12-3456789" } } }
        ```

        Nothing else to learn — what comes back can be sent back, an omitted key is left
        alone. There is no sub-resource for either half: both are singletons of the
        market, so both are written here.

        `GET /v3/compliance/requirements` says what a market demands of anybody; this
        says what you gave it.

        Send `x-profile-id` with an organization key to read one of your profiles'
        markets.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel:
            raise ValueError(f"Expected a non-empty value for `channel` but received {channel!r}")
        if not country:
            raise ValueError(f"Expected a non-empty value for `country` but received {country!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v3/channels/{channel}/{country}/{type}", channel=channel, country=country, type=type),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfChannelMarket,
        )

    async def update(
        self,
        type: str,
        *,
        channel: str,
        country: str,
        compliance: MarketComplianceParam | Omit = omit,
        sandbox: bool | Omit = omit,
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
        Supplies the market's identity and documents, and answers with the market as
        stored — the same shape `GET` on this path returns.

        | To change                               | Send                                                                                                     |
        | --------------------------------------- | -------------------------------------------------------------------------------------------------------- |
        | a `brand` value (US `TEN_DLC`)          | `compliance.brand`, as below                                                                             |
        | a registration sent back for correction | `compliance.brand` — the identity is accepted even once filed, and the registration goes back for review |
        | a document, in any market               | a multipart file named after the document's key                                                          |
        | a campaign                              | `PATCH /v3/channels/sms/US/TEN_DLC/campaigns/{id}` — `compliance.campaign` here is `400`                 |
        | the numbers                             | `POST /v3/channels/{channel}/{country}/{type}/numbers` — `numbers` here is `400`                         |

        ## Partial, at every level

        **An omitted key is left alone. An explicit `null` clears it.** Those are
        different requests, so `{}` changes nothing and is refused rather than silently
        accepted, and correcting one field does not blank the others.

        ```json
        { "compliance": { "brand": { "contact_phone": "+12125550123" } } }
        ```

        | Body                           | Effect                                                       |
        | ------------------------------ | ------------------------------------------------------------ |
        | `"brand": { … }`               | supplies or corrects the identity, and takes one of your own |
        | `"brand": { "inherit": true }` | runs on your organization's, giving up your own              |
        | `"brand": null`                | the same thing, said the short way                           |
        | key omitted                    | left exactly as it is                                        |

        The brand read on this path, its `id` and `vetting` included, can be sent back
        unchanged: both are read-only and ignored.

        ## Every other market

        Markets that register with no regime have no brand, so `compliance` is `400`
        there. Their compliance is documents, sent here as multipart.

        ## Documents

        Send `multipart/form-data` with **each file named after the compliance key it
        satisfies** — the key `GET /v3/channels/{channel}/{country}/compliance` lists. A
        file that matches no document the market asks for is `400` naming the keys that
        would, and a file the upload rules refuse (empty, too large, an unsupported
        type) is `422`. `compliance` may ride in the same form as a text part holding
        its JSON.

        ## What it will refuse

        **A filed identity is `409`.** Once the registration has gone to The Campaign
        Registry they hold a copy, and a local change would diverge from it silently.
        The exception is a registration sent back for correction: the identity is
        accepted, and the registration goes back for review. Refiling it with The
        Campaign Registry stays with Sent.

        Nothing is submitted to a regime here. Send `x-profile-id` with an organization
        key to write one of your profiles' markets.

        Args:
          compliance: The compliance values a market registers with. `brand` and `campaign` apply to
              US `TEN_DLC`; other markets fill this map with the document keys their own
              requirements name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel:
            raise ValueError(f"Expected a non-empty value for `channel` but received {channel!r}")
        if not country:
            raise ValueError(f"Expected a non-empty value for `country` but received {country!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
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
            path_template("/v3/channels/{channel}/{country}/{type}", channel=channel, country=country, type=type),
            body=await async_maybe_transform(
                {
                    "compliance": compliance,
                    "sandbox": sandbox,
                },
                market_update_params.MarketUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfChannelMarket,
        )

    async def list(
        self,
        channel: str,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfListOfChannelMarket:
        """
        Every market you send SMS in, each with its sender, where that sender stands,
        and what its compliance holds.

        The same entries `GET /v3/channels` reports under `sms`, and the same shape
        `GET /v3/channels/sms/{country}/{type}` returns for one of them — so a list, a
        member read and the all-channels read cannot describe a market differently.

        Send `x-profile-id` with an organization key to list one of your profiles'
        markets.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel:
            raise ValueError(f"Expected a non-empty value for `channel` but received {channel!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v3/channels/{channel}", channel=channel),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfListOfChannelMarket,
        )

    async def add_numbers(
        self,
        type: str,
        *,
        channel: str,
        country: str,
        numbers: Iterable[Optional[SMSNumberRequestParam]],
        idempotency_key: str,
        campaign_id: Optional[str] | Omit = omit,
        sandbox: bool | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfChannelMarket:
        """Adds numbers to a market you hold.

        They are **added** to what it already asks
        for, never replacing it — with one exception: a US `TEN_DLC` campaign opened
        without `numbers` asks for one number in any area code by default, and while it
        holds no number yet, the first numbers added replace that default. Once it holds
        one, they are added beside it.

        ## Where they go

        - **SMS US `TEN_DLC`**: to **one campaign of your own**, named by `campaign_id`
          — the `id` of an entry in the market's `compliance.campaigns`
          (`GET /v3/channels/sms/US/TEN_DLC`). Required: left out it is `400` naming
          your campaigns in service. One you inherit from your organization is `400`:
          its numbers are the organization's. One out of service — expired, deactivated
          or released — is `409`. A campaign the carriers have not approved yet gets its
          numbers when they do; an approved one gets them now. With everything it asks
          for, a campaign holds at most 49 numbers, counting one for each sender profile
          inheriting it.
        - **`LOCAL`**: to the market, claimed from inventory now; what inventory cannot
          cover stays pending. No `campaign_id`. A market holds at most 49 numbers.
        - **Any other sender type** takes no numbers: `400`.

        ## What to send

        `numbers` — the list `POST /v3/channels/sms` takes, one entry per area code —
        and, on US `TEN_DLC`, `campaign_id`, required.

        Until a number is assigned it reads as `PROVISIONING` in the market's `numbers`,
        with the area code it was asked for. Returns **the market**, in the shape
        `GET /v3/channels/sms/{country}/{type}` returns, with `202`.

        Args:
          numbers: The numbers, one entry per area code, e.g. [{"area_code": "415", "quantity": 2},
              {"quantity": 1}]. quantity defaults to 1, and an entry without area_code means
              any area code. Required.

              POST adds them to what the market or campaign already asks for; PATCH replaces
              that list with them, and has to cover every number already held, since none is
              ever released.

          campaign_id: The campaign to add the numbers to, as campaigns[].id reports it. Required on
              SMS US TEN_DLC, where every number belongs to a campaign; refused on a market
              without campaigns.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel:
            raise ValueError(f"Expected a non-empty value for `channel` but received {channel!r}")
        if not country:
            raise ValueError(f"Expected a non-empty value for `country` but received {country!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
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
            path_template(
                "/v3/channels/{channel}/{country}/{type}/numbers", channel=channel, country=country, type=type
            ),
            body=await async_maybe_transform(
                {
                    "numbers": numbers,
                    "campaign_id": campaign_id,
                    "sandbox": sandbox,
                },
                market_add_numbers_params.MarketAddNumbersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfChannelMarket,
        )

    async def list_numbers(
        self,
        type: str,
        *,
        channel: str,
        country: str,
        campaign_id: Optional[str] | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfMarketNumbers:
        """
        Every number you hold in one market (country and sender type): `ACTIVE` once it
        can send, `PROVISIONING` while it is still to be assigned (it then has no
        `sender_value` yet), `INACTIVE` once it could send and no longer can. US
        `TEN_DLC` numbers name their `campaign_id`, and `?campaign_id=` keeps one
        campaign's.

        A market you do not hold is `404`. Add numbers with `POST` on the same path.

        Args:
          campaign_id: Only the numbers of this campaign (US TEN_DLC); all of the market's when absent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel:
            raise ValueError(f"Expected a non-empty value for `channel` but received {channel!r}")
        if not country:
            raise ValueError(f"Expected a non-empty value for `country` but received {country!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            path_template(
                "/v3/channels/{channel}/{country}/{type}/numbers", channel=channel, country=country, type=type
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"campaign_id": campaign_id}, market_list_numbers_params.MarketListNumbersParams
                ),
            ),
            cast_to=APIResponseOfMarketNumbers,
        )

    async def replace_numbers(
        self,
        type: str,
        *,
        channel: str,
        country: str,
        numbers: Iterable[Optional[SMSNumberRequestParam]],
        campaign_id: Optional[str] | Omit = omit,
        sandbox: bool | Omit = omit,
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
        Replaces the numbers a market you hold asks for — their area codes and counts —
        with the list you send. To add to them instead, use `POST` on this path.

        ## Whose numbers

        - **SMS US `TEN_DLC`**: **one campaign of your own**, named by `campaign_id` —
          the `id` of an entry in the market's `compliance.campaigns`. Required. So a
          campaign sent back for correction can change its area codes without being
          recreated. One you inherit from your organization is `400`; one out of service
          is `409`. With everything it asks for, a campaign holds at most 49 numbers,
          counting one for each sender profile inheriting it.
        - **`LOCAL`**: the market's own, claimed from inventory now; what inventory
          cannot cover stays pending. No `campaign_id`.
        - **Any other sender type** takes no numbers: `400`.

        ## What to send

        `numbers` — the list `POST /v3/channels/sms` takes, one entry per area code, an
        entry without `area_code` meaning any — and, on US `TEN_DLC`, `campaign_id`.

        **Numbers already assigned are kept.** Nothing is released here, so a list that
        no longer covers a number already held is `400`, naming how many it leaves out.
        Lowering a count nothing has filled yet is fine.

        Until a number is assigned it reads as `PROVISIONING` in the market's `numbers`,
        with the area code it was asked for. Returns **the market**, in the shape
        `GET /v3/channels/sms/{country}/{type}` returns.

        Args:
          numbers: The numbers, one entry per area code, e.g. [{"area_code": "415", "quantity": 2},
              {"quantity": 1}]. quantity defaults to 1, and an entry without area_code means
              any area code. Required.

              POST adds them to what the market or campaign already asks for; PATCH replaces
              that list with them, and has to cover every number already held, since none is
              ever released.

          campaign_id: The campaign to add the numbers to, as campaigns[].id reports it. Required on
              SMS US TEN_DLC, where every number belongs to a campaign; refused on a market
              without campaigns.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not channel:
            raise ValueError(f"Expected a non-empty value for `channel` but received {channel!r}")
        if not country:
            raise ValueError(f"Expected a non-empty value for `country` but received {country!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
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
            path_template(
                "/v3/channels/{channel}/{country}/{type}/numbers", channel=channel, country=country, type=type
            ),
            body=await async_maybe_transform(
                {
                    "numbers": numbers,
                    "campaign_id": campaign_id,
                    "sandbox": sandbox,
                },
                market_replace_numbers_params.MarketReplaceNumbersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfChannelMarket,
        )


class MarketsResourceWithRawResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.retrieve = to_raw_response_wrapper(
            markets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            markets.update,
        )
        self.list = to_raw_response_wrapper(
            markets.list,
        )
        self.add_numbers = to_raw_response_wrapper(
            markets.add_numbers,
        )
        self.list_numbers = to_raw_response_wrapper(
            markets.list_numbers,
        )
        self.replace_numbers = to_raw_response_wrapper(
            markets.replace_numbers,
        )


class AsyncMarketsResourceWithRawResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.retrieve = async_to_raw_response_wrapper(
            markets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            markets.update,
        )
        self.list = async_to_raw_response_wrapper(
            markets.list,
        )
        self.add_numbers = async_to_raw_response_wrapper(
            markets.add_numbers,
        )
        self.list_numbers = async_to_raw_response_wrapper(
            markets.list_numbers,
        )
        self.replace_numbers = async_to_raw_response_wrapper(
            markets.replace_numbers,
        )


class MarketsResourceWithStreamingResponse:
    def __init__(self, markets: MarketsResource) -> None:
        self._markets = markets

        self.retrieve = to_streamed_response_wrapper(
            markets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            markets.update,
        )
        self.list = to_streamed_response_wrapper(
            markets.list,
        )
        self.add_numbers = to_streamed_response_wrapper(
            markets.add_numbers,
        )
        self.list_numbers = to_streamed_response_wrapper(
            markets.list_numbers,
        )
        self.replace_numbers = to_streamed_response_wrapper(
            markets.replace_numbers,
        )


class AsyncMarketsResourceWithStreamingResponse:
    def __init__(self, markets: AsyncMarketsResource) -> None:
        self._markets = markets

        self.retrieve = async_to_streamed_response_wrapper(
            markets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            markets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            markets.list,
        )
        self.add_numbers = async_to_streamed_response_wrapper(
            markets.add_numbers,
        )
        self.list_numbers = async_to_streamed_response_wrapper(
            markets.list_numbers,
        )
        self.replace_numbers = async_to_streamed_response_wrapper(
            markets.replace_numbers,
        )
