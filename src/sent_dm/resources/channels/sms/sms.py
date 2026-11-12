# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from .ten_dlc import (
    TenDlcResource,
    AsyncTenDlcResource,
    TenDlcResourceWithRawResponse,
    AsyncTenDlcResourceWithRawResponse,
    TenDlcResourceWithStreamingResponse,
    AsyncTenDlcResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.channels import sms_create_params, sms_update_params
from ....types.channels.market_compliance_param import MarketComplianceParam
from ....types.channels.sms_number_request_param import SMSNumberRequestParam
from ....types.channels.api_response_of_sms_market import APIResponseOfSMSMarket
from ....types.channels.api_response_of_list_of_sms_market import APIResponseOfListOfSMSMarket

__all__ = ["SMSResource", "AsyncSMSResource"]


class SMSResource(SyncAPIResource):
    """The senders you send from, one per channel.

    **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

    ## Compliance lives on the market

    Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

    `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

    Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
    """

    @cached_property
    def ten_dlc(self) -> TenDlcResource:
        """The senders you send from, one per channel.

        **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

        ## Compliance lives on the market

        Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

        `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

        Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
        """
        return TenDlcResource(self._client)

    @cached_property
    def with_raw_response(self) -> SMSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return SMSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SMSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return SMSResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        number_type: Literal["LOCAL", "TOLL_FREE", "SHORT_CODE", "ALPHANUMERIC", "TEN_DLC", "MOBILE", "10DLC"],
        area_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        compliance: MarketComplianceParam | Omit = omit,
        country: str | Omit = omit,
        numbers: Optional[Iterable[SMSNumberRequestParam]] | Omit = omit,
        sandbox: bool | Omit = omit,
        sender_value: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfSMSMarket:
        """
        Gives the customer a sender in one country — the first market it sends in, and
        the fifth.

        ## What to have in place first

        **Call `GET /v3/compliance/requirements?country=US&type=TEN_DLC` first.** It
        returns this request's body ready to fill in, plus the brand and campaign calls
        to make before it, in order. You never have to track forty countries' rules
        yourself.

        **A market that registers with a compliance regime needs an identity, and this
        call takes one.** US `TEN_DLC` registers with The Campaign Registry and files
        that registration against a business identity. Send it in `compliance.brand` and
        it is recorded here, before the registration that attaches to it — so a customer
        with no identity reaches a first 10DLC market in one call.

        `{ "inherit": true }` runs on your organization's instead. A market with neither
        — none stored, none sent — is `400`, because accepting it would write a channel
        that could never register and leave it provisioning for ever with nothing saying
        why.

        **Everything the regime wants arrives in this request's `compliance`**, as two
        declared objects: `brand` — the identity the registration is filed against — and
        `campaign`, with the use case, the consent narrative, the volume, the sample
        messages and the keywords. There is nothing to set up first. Nothing is
        submitted here either: the rows are what a submission is later assembled from,
        and filing is externally rejectable so it happens on its own path.

        **A half you run yourself has to be complete here.** Whichever of `brand` and
        `campaign` is your own rather than your organization's must carry every field
        the regime asks of it, counting what you already hold — send the rest in this
        request. A missing one is `400` naming each field, rather than a `202` for a
        market that could never be filed. A half you inherit is asked for nothing.

        A market that registers with nobody — an alphanumeric sender in most countries —
        needs neither, and may need documents instead.

        ## Sending it

        Takes the same fields `channels.sms` takes on `POST /v3/sender-profiles`,
        because it is the same work, and both run one provisioning path. `compliance` is
        top-level and answers for the market in this request, carrying `brand` and
        `campaign` where the market registers.

        **Accepts multipart as well as JSON**, with each file named after the compliance
        key it satisfies — a market that pre-registers its sender needs its documents at
        the same moment it needs the sender. Every required document must be attached to
        this request; a missing or invalid file is rejected before the market is added.

        **`area_codes` puts the sender somewhere specific**, in your order of
        preference, for a `LOCAL` sender in any country or a US `TEN_DLC` sender — a
        10DLC number is an ordinary local long code bound to a registered campaign, so
        both take the same codes out of the same inventory. It is honoured exactly: you
        get a number in one of the codes you named or you get none, never one in a code
        you left out.

        ## Several numbers

        **`numbers` lists the numbers you want, one entry per area code**, e.g.
        `[{"area_code": "212", "quantity": 2}, {"quantity": 1}]` for two numbers in 212
        and one in any area code. `quantity` defaults to 1, and an entry without
        `area_code` means any area code. Omit `numbers` for one number. It is for
        `LOCAL` and `TEN_DLC` only and cannot be combined with `area_codes`. A market
        holds at most 49 numbers, counting the ones it already has.

        **On a `LOCAL` market you already hold, `numbers` adds those numbers to it**
        instead of `409`. US `TEN_DLC` numbers belong to the market's campaign and are
        assigned when the campaign is approved, not at request time. Until then they
        read as `PROVISIONING` in the response's `numbers`, each with the area code it
        was asked for. A profile inheriting your organization's campaign cannot request
        `numbers` (`400`). `numbers` on a `TEN_DLC` market you already hold is `409`:
        change its campaign's numbers with `PATCH /v3/channels/sms/{country}/{type}`,
        add numbers to one of its campaigns with
        `POST /v3/channels/sms/numbers/US/TEN_DLC`, or add a new campaign with
        `POST /v3/channels/sms/compliances/US/TEN_DLC/campaigns`.

        **A market you already send in is `409`**: adding what is already there is a
        mistake worth reporting rather than a silent no-op. A market is a
        `(country, sender_type)` pair, so a **second sender type in a country you
        already send in is fine** — `US TOLL_FREE` alongside `US TEN_DLC` is the
        ordinary case. Two of the same type is not.

        **A market you hold that has no sender yet is not a duplicate**, and re-sending
        it re-asks for a sender rather than being refused. That is the way out of an
        area-code request nothing could fill: send the call again to name different
        codes, or no codes at all to take a number anywhere in the country. It answers
        `201` with the sender when the pool has one, otherwise `202` with the codes
        recorded — and changes nothing else; compliance on a market you hold is
        `PATCH /v3/channels/sms/{country}/{type}`.

        One exception: while a market's sender type is still unassigned, adding any type
        to that country is `409` once it has a sender, because the market you have may
        be about to become the one you asked for.

        Returns **the market**, in the shape `GET` and `PATCH` on
        `/v3/channels/sms/{country}/{type}` use — so what this answers can be read back
        and written back without reshaping. Not every channel you have: adding a market
        cannot change an RCS agent or a WhatsApp account, and `GET /v3/channels` is the
        whole picture. `201` when the market is ready; `202` while a sender or a
        registration is still outstanding.

        Send `x-profile-id` with an organization key to add a market to one of your
        profiles.

        Args:
          number_type: Sender type. Decides the provisioning flow and what compliance is asked for.

              [Required] so the published document says so. The validator has always demanded
              it, but requiredness reached the schema by matching a rule to a property name —
              which works for country, whose wire name is its camel-cased C# name, and
              silently does not for number_type. A client generating a request from our
              OpenAPI therefore sent what the document called sufficient and was answered 400.

          area_codes: The area codes to put this sender in, in your own order of preference, e.g.
              ["415", "628"] for the US or ["20"] for London. Omit it and a number is claimed
              anywhere in the country.

              Ordered, and the order is the request. The claim tries each code in turn and
              stops at the first that yields a number. Nothing sorts the list and a code
              listed twice is refused.

              One to fifty entries, each the area code as digits: 415, with the trunk prefix
              as 020, or with the country's dialing prefix as +1415 (all are stored as the
              bare code). A dialing prefix from a different country than country is refused.
              Each code is checked against the country's numbering plan: it must start real
              local or mobile numbers there, so toll-free and premium ranges, service codes
              and another country's codes are refused with a reason.

              LOCAL senders in any country, and US TEN_DLC senders. No other sender type has a
              geographic area code, and the list is refused with one rather than accepted and
              dropped.

              Honoured exactly or not at all. Ask for 415 and you get a 415 number or you get
              none, never a neighbouring code you did not name. A miss leaves the market with
              no sender yet and the codes recorded on it, so it is filled when stock appears
              rather than filled now from somewhere else. Many countries outside North America
              require address or business documents before a local number can be bought, which
              can delay or prevent the fill.

          compliance: The compliance values a market registers with. `brand` and `campaign` apply to
              US `TEN_DLC`; other markets fill this map with the document keys their own
              requirements name.

          country: ISO 3166-1 alpha-2 country the sender operates in.

          numbers: The numbers to assign, one entry per area code, e.g. [{"area_code": "212",
              "quantity": 2}, {"area_code": "415"}, {"quantity": 1}]: two numbers in 212, one
              in 415 and one in any area code. quantity defaults to 1, and an entry without
              area_code means any area code. Omit numbers for one number.

              Only with LOCAL or TEN_DLC, and not together with area_codes. Each area code is
              validated against country the same way area_codes is and may appear once, and at
              most one entry may leave area_code out. On a LOCAL market you already hold, this
              adds the numbers to it. US TEN_DLC numbers are assigned when the campaign is
              approved, not at request time. Not available when the profile inherits the
              organization's campaign.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          sender_value: The sender's identity where the caller chooses it. Required when number_type is
              ALPHANUMERIC; optional for carrier-assigned types, which are procured
              afterwards.

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
            "/v3/channels/sms",
            body=maybe_transform(
                {
                    "number_type": number_type,
                    "area_codes": area_codes,
                    "compliance": compliance,
                    "country": country,
                    "numbers": numbers,
                    "sandbox": sandbox,
                    "sender_value": sender_value,
                },
                sms_create_params.SMSCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfSMSMarket,
        )

    def retrieve(
        self,
        type: str,
        *,
        country: str,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfSMSMarket:
        """
        Reads one market you send in — its sender, where that sender stands, and
        everything its compliance holds.

        ## What `compliance` carries

        A market that registers with a compliance regime reports `brand` — the identity
        the registration is filed against — and `campaign`, the programme filed against
        it. Each carries `inherit`, saying whether it is yours or your organization's.

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
        if not country:
            raise ValueError(f"Expected a non-empty value for `country` but received {country!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v3/channels/sms/{country}/{type}", country=country, type=type),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfSMSMarket,
        )

    def update(
        self,
        type: str,
        *,
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
    ) -> APIResponseOfSMSMarket:
        """
        Supplies whatever this market is waiting on, and answers with the market as
        stored — the same shape `GET` on this path returns, so **what comes back can be
        sent back**.

        **A market reporting `ACTION_NEEDED` is fixed here**, whatever it is waiting on:

        | Outstanding                                  | Send                                                                                                                                  |
        | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
        | a `brand` or `campaign` value (US `TEN_DLC`) | `compliance`, as below                                                                                                                |
        | a document, in any market                    | a multipart file named after the document's key                                                                                       |
        | a registration sent back for correction      | `compliance.brand` and/or `compliance.campaign` — the identity is accepted even once filed, and the registration goes back for review |
        | different numbers                            | `numbers`, the list the market asks for from now on                                                                                   |

        ## Partial, at every level

        **An omitted key is left alone. An explicit `null` clears it.** Those are
        different requests, so `{}` changes nothing and is refused rather than silently
        accepted, and correcting one field does not blank the others.

        ```json
        { "compliance": { "brand": { "contact_phone": "+12125550123" } } }
        ```

        That leaves the campaign untouched, along with every other field of the
        identity.

        ## What a US `TEN_DLC` market holds

        Two halves, both singular: `brand`, the identity the registration is filed
        against, and `campaign`, the programme filed against it. Each carries `inherit`.

        | Body                              | Effect                                                        |
        | --------------------------------- | ------------------------------------------------------------- |
        | `"brand": { … }`                  | supplies or corrects the identity, and takes one of your own  |
        | `"brand": { "inherit": true }`    | runs on your organization's, giving up your own               |
        | `"brand": null`                   | the same thing, said the short way                            |
        | `"campaign": { … }`               | supplies or corrects the programme, and takes one of your own |
        | `"campaign": { "inherit": true }` | runs on your organization's                                   |
        | key omitted                       | left exactly as it is                                         |

        **Nothing here creates a second anything.** One identity and one campaign per
        market, so a write is an upsert and a replayed request lands on the row it
        already wrote. Sending the campaign twice does not file two registrations.

        ## Every other market

        Markets that register with no regime have neither half, so `compliance` is `400`
        there. Their compliance is documents, sent here as multipart.

        ## Documents

        Send `multipart/form-data` with **each file named after the compliance key it
        satisfies** — the key the market's `requirements` names. A file that matches no
        document the market asks for is `400` naming the keys that would, and a file the
        upload rules refuse (empty, too large, an unsupported type) is `422`.
        `compliance` and `numbers` may ride in the same form as text parts holding their
        JSON.

        ## Numbers

        `numbers` takes the list `POST /v3/channels/sms` takes, for a `LOCAL` or
        `TEN_DLC` market, and **replaces** what the market asks for — send the list you
        want, not a difference. Numbers already assigned stay; a list that leaves one of
        them out is `400`, because nothing here releases a number.

        ```json
        { "numbers": [{ "area_code": "415", "quantity": 2 }, { "quantity": 1 }] }
        ```

        A `LOCAL` market is claimed from inventory at once, and whatever inventory
        cannot cover stays pending. A `TEN_DLC` market's numbers are recorded on its
        campaign and assigned once the carriers elect it — on the next acquisition cycle
        when it already has been. They need a campaign of the profile's own: one
        inherited from the organization is `400`.

        ## What it will refuse

        **A filed identity is `409`.** Once the registration has gone to The Campaign
        Registry they hold a copy, and a local change would diverge from it silently.
        The campaign is not frozen — omit `brand` and the same body is accepted. The
        exception is a registration sent back for correction: the identity is accepted,
        and a correction to either half sends the registration back for review. Refiling
        it with The Campaign Registry stays with Sent.

        **More than one campaign is `409`.** The schema permits several and an account
        built on the admin side may hold them; this surface writes one, and editing
        whichever sorted first would leave the others unmentioned and unedited.

        Nothing is submitted to a regime here. These are the rows a submission is later
        assembled from, which is what lets them be corrected without waiting on
        something externally rejectable.

        Send `x-profile-id` with an organization key to write one of your profiles'
        markets.

        Args:
          compliance: The compliance values a market registers with. `brand` and `campaign` apply to
              US `TEN_DLC`; other markets fill this map with the document keys their own
              requirements name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
            path_template("/v3/channels/sms/{country}/{type}", country=country, type=type),
            body=maybe_transform(
                {
                    "compliance": compliance,
                    "sandbox": sandbox,
                },
                sms_update_params.SMSUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfSMSMarket,
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
    ) -> APIResponseOfListOfSMSMarket:
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
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            "/v3/channels/sms",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfListOfSMSMarket,
        )


class AsyncSMSResource(AsyncAPIResource):
    """The senders you send from, one per channel.

    **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

    ## Compliance lives on the market

    Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

    `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

    Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
    """

    @cached_property
    def ten_dlc(self) -> AsyncTenDlcResource:
        """The senders you send from, one per channel.

        **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

        ## Compliance lives on the market

        Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

        `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

        Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
        """
        return AsyncTenDlcResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSMSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSMSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSMSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncSMSResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        number_type: Literal["LOCAL", "TOLL_FREE", "SHORT_CODE", "ALPHANUMERIC", "TEN_DLC", "MOBILE", "10DLC"],
        area_codes: Optional[SequenceNotStr[str]] | Omit = omit,
        compliance: MarketComplianceParam | Omit = omit,
        country: str | Omit = omit,
        numbers: Optional[Iterable[SMSNumberRequestParam]] | Omit = omit,
        sandbox: bool | Omit = omit,
        sender_value: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfSMSMarket:
        """
        Gives the customer a sender in one country — the first market it sends in, and
        the fifth.

        ## What to have in place first

        **Call `GET /v3/compliance/requirements?country=US&type=TEN_DLC` first.** It
        returns this request's body ready to fill in, plus the brand and campaign calls
        to make before it, in order. You never have to track forty countries' rules
        yourself.

        **A market that registers with a compliance regime needs an identity, and this
        call takes one.** US `TEN_DLC` registers with The Campaign Registry and files
        that registration against a business identity. Send it in `compliance.brand` and
        it is recorded here, before the registration that attaches to it — so a customer
        with no identity reaches a first 10DLC market in one call.

        `{ "inherit": true }` runs on your organization's instead. A market with neither
        — none stored, none sent — is `400`, because accepting it would write a channel
        that could never register and leave it provisioning for ever with nothing saying
        why.

        **Everything the regime wants arrives in this request's `compliance`**, as two
        declared objects: `brand` — the identity the registration is filed against — and
        `campaign`, with the use case, the consent narrative, the volume, the sample
        messages and the keywords. There is nothing to set up first. Nothing is
        submitted here either: the rows are what a submission is later assembled from,
        and filing is externally rejectable so it happens on its own path.

        **A half you run yourself has to be complete here.** Whichever of `brand` and
        `campaign` is your own rather than your organization's must carry every field
        the regime asks of it, counting what you already hold — send the rest in this
        request. A missing one is `400` naming each field, rather than a `202` for a
        market that could never be filed. A half you inherit is asked for nothing.

        A market that registers with nobody — an alphanumeric sender in most countries —
        needs neither, and may need documents instead.

        ## Sending it

        Takes the same fields `channels.sms` takes on `POST /v3/sender-profiles`,
        because it is the same work, and both run one provisioning path. `compliance` is
        top-level and answers for the market in this request, carrying `brand` and
        `campaign` where the market registers.

        **Accepts multipart as well as JSON**, with each file named after the compliance
        key it satisfies — a market that pre-registers its sender needs its documents at
        the same moment it needs the sender. Every required document must be attached to
        this request; a missing or invalid file is rejected before the market is added.

        **`area_codes` puts the sender somewhere specific**, in your order of
        preference, for a `LOCAL` sender in any country or a US `TEN_DLC` sender — a
        10DLC number is an ordinary local long code bound to a registered campaign, so
        both take the same codes out of the same inventory. It is honoured exactly: you
        get a number in one of the codes you named or you get none, never one in a code
        you left out.

        ## Several numbers

        **`numbers` lists the numbers you want, one entry per area code**, e.g.
        `[{"area_code": "212", "quantity": 2}, {"quantity": 1}]` for two numbers in 212
        and one in any area code. `quantity` defaults to 1, and an entry without
        `area_code` means any area code. Omit `numbers` for one number. It is for
        `LOCAL` and `TEN_DLC` only and cannot be combined with `area_codes`. A market
        holds at most 49 numbers, counting the ones it already has.

        **On a `LOCAL` market you already hold, `numbers` adds those numbers to it**
        instead of `409`. US `TEN_DLC` numbers belong to the market's campaign and are
        assigned when the campaign is approved, not at request time. Until then they
        read as `PROVISIONING` in the response's `numbers`, each with the area code it
        was asked for. A profile inheriting your organization's campaign cannot request
        `numbers` (`400`). `numbers` on a `TEN_DLC` market you already hold is `409`:
        change its campaign's numbers with `PATCH /v3/channels/sms/{country}/{type}`,
        add numbers to one of its campaigns with
        `POST /v3/channels/sms/numbers/US/TEN_DLC`, or add a new campaign with
        `POST /v3/channels/sms/compliances/US/TEN_DLC/campaigns`.

        **A market you already send in is `409`**: adding what is already there is a
        mistake worth reporting rather than a silent no-op. A market is a
        `(country, sender_type)` pair, so a **second sender type in a country you
        already send in is fine** — `US TOLL_FREE` alongside `US TEN_DLC` is the
        ordinary case. Two of the same type is not.

        **A market you hold that has no sender yet is not a duplicate**, and re-sending
        it re-asks for a sender rather than being refused. That is the way out of an
        area-code request nothing could fill: send the call again to name different
        codes, or no codes at all to take a number anywhere in the country. It answers
        `201` with the sender when the pool has one, otherwise `202` with the codes
        recorded — and changes nothing else; compliance on a market you hold is
        `PATCH /v3/channels/sms/{country}/{type}`.

        One exception: while a market's sender type is still unassigned, adding any type
        to that country is `409` once it has a sender, because the market you have may
        be about to become the one you asked for.

        Returns **the market**, in the shape `GET` and `PATCH` on
        `/v3/channels/sms/{country}/{type}` use — so what this answers can be read back
        and written back without reshaping. Not every channel you have: adding a market
        cannot change an RCS agent or a WhatsApp account, and `GET /v3/channels` is the
        whole picture. `201` when the market is ready; `202` while a sender or a
        registration is still outstanding.

        Send `x-profile-id` with an organization key to add a market to one of your
        profiles.

        Args:
          number_type: Sender type. Decides the provisioning flow and what compliance is asked for.

              [Required] so the published document says so. The validator has always demanded
              it, but requiredness reached the schema by matching a rule to a property name —
              which works for country, whose wire name is its camel-cased C# name, and
              silently does not for number_type. A client generating a request from our
              OpenAPI therefore sent what the document called sufficient and was answered 400.

          area_codes: The area codes to put this sender in, in your own order of preference, e.g.
              ["415", "628"] for the US or ["20"] for London. Omit it and a number is claimed
              anywhere in the country.

              Ordered, and the order is the request. The claim tries each code in turn and
              stops at the first that yields a number. Nothing sorts the list and a code
              listed twice is refused.

              One to fifty entries, each the area code as digits: 415, with the trunk prefix
              as 020, or with the country's dialing prefix as +1415 (all are stored as the
              bare code). A dialing prefix from a different country than country is refused.
              Each code is checked against the country's numbering plan: it must start real
              local or mobile numbers there, so toll-free and premium ranges, service codes
              and another country's codes are refused with a reason.

              LOCAL senders in any country, and US TEN_DLC senders. No other sender type has a
              geographic area code, and the list is refused with one rather than accepted and
              dropped.

              Honoured exactly or not at all. Ask for 415 and you get a 415 number or you get
              none, never a neighbouring code you did not name. A miss leaves the market with
              no sender yet and the codes recorded on it, so it is filled when stock appears
              rather than filled now from somewhere else. Many countries outside North America
              require address or business documents before a local number can be bought, which
              can delay or prevent the fill.

          compliance: The compliance values a market registers with. `brand` and `campaign` apply to
              US `TEN_DLC`; other markets fill this map with the document keys their own
              requirements name.

          country: ISO 3166-1 alpha-2 country the sender operates in.

          numbers: The numbers to assign, one entry per area code, e.g. [{"area_code": "212",
              "quantity": 2}, {"area_code": "415"}, {"quantity": 1}]: two numbers in 212, one
              in 415 and one in any area code. quantity defaults to 1, and an entry without
              area_code means any area code. Omit numbers for one number.

              Only with LOCAL or TEN_DLC, and not together with area_codes. Each area code is
              validated against country the same way area_codes is and may appear once, and at
              most one entry may leave area_code out. On a LOCAL market you already hold, this
              adds the numbers to it. US TEN_DLC numbers are assigned when the campaign is
              approved, not at request time. Not available when the profile inherits the
              organization's campaign.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          sender_value: The sender's identity where the caller chooses it. Required when number_type is
              ALPHANUMERIC; optional for carrier-assigned types, which are procured
              afterwards.

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
            "/v3/channels/sms",
            body=await async_maybe_transform(
                {
                    "number_type": number_type,
                    "area_codes": area_codes,
                    "compliance": compliance,
                    "country": country,
                    "numbers": numbers,
                    "sandbox": sandbox,
                    "sender_value": sender_value,
                },
                sms_create_params.SMSCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfSMSMarket,
        )

    async def retrieve(
        self,
        type: str,
        *,
        country: str,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfSMSMarket:
        """
        Reads one market you send in — its sender, where that sender stands, and
        everything its compliance holds.

        ## What `compliance` carries

        A market that registers with a compliance regime reports `brand` — the identity
        the registration is filed against — and `campaign`, the programme filed against
        it. Each carries `inherit`, saying whether it is yours or your organization's.

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
        if not country:
            raise ValueError(f"Expected a non-empty value for `country` but received {country!r}")
        if not type:
            raise ValueError(f"Expected a non-empty value for `type` but received {type!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v3/channels/sms/{country}/{type}", country=country, type=type),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfSMSMarket,
        )

    async def update(
        self,
        type: str,
        *,
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
    ) -> APIResponseOfSMSMarket:
        """
        Supplies whatever this market is waiting on, and answers with the market as
        stored — the same shape `GET` on this path returns, so **what comes back can be
        sent back**.

        **A market reporting `ACTION_NEEDED` is fixed here**, whatever it is waiting on:

        | Outstanding                                  | Send                                                                                                                                  |
        | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
        | a `brand` or `campaign` value (US `TEN_DLC`) | `compliance`, as below                                                                                                                |
        | a document, in any market                    | a multipart file named after the document's key                                                                                       |
        | a registration sent back for correction      | `compliance.brand` and/or `compliance.campaign` — the identity is accepted even once filed, and the registration goes back for review |
        | different numbers                            | `numbers`, the list the market asks for from now on                                                                                   |

        ## Partial, at every level

        **An omitted key is left alone. An explicit `null` clears it.** Those are
        different requests, so `{}` changes nothing and is refused rather than silently
        accepted, and correcting one field does not blank the others.

        ```json
        { "compliance": { "brand": { "contact_phone": "+12125550123" } } }
        ```

        That leaves the campaign untouched, along with every other field of the
        identity.

        ## What a US `TEN_DLC` market holds

        Two halves, both singular: `brand`, the identity the registration is filed
        against, and `campaign`, the programme filed against it. Each carries `inherit`.

        | Body                              | Effect                                                        |
        | --------------------------------- | ------------------------------------------------------------- |
        | `"brand": { … }`                  | supplies or corrects the identity, and takes one of your own  |
        | `"brand": { "inherit": true }`    | runs on your organization's, giving up your own               |
        | `"brand": null`                   | the same thing, said the short way                            |
        | `"campaign": { … }`               | supplies or corrects the programme, and takes one of your own |
        | `"campaign": { "inherit": true }` | runs on your organization's                                   |
        | key omitted                       | left exactly as it is                                         |

        **Nothing here creates a second anything.** One identity and one campaign per
        market, so a write is an upsert and a replayed request lands on the row it
        already wrote. Sending the campaign twice does not file two registrations.

        ## Every other market

        Markets that register with no regime have neither half, so `compliance` is `400`
        there. Their compliance is documents, sent here as multipart.

        ## Documents

        Send `multipart/form-data` with **each file named after the compliance key it
        satisfies** — the key the market's `requirements` names. A file that matches no
        document the market asks for is `400` naming the keys that would, and a file the
        upload rules refuse (empty, too large, an unsupported type) is `422`.
        `compliance` and `numbers` may ride in the same form as text parts holding their
        JSON.

        ## Numbers

        `numbers` takes the list `POST /v3/channels/sms` takes, for a `LOCAL` or
        `TEN_DLC` market, and **replaces** what the market asks for — send the list you
        want, not a difference. Numbers already assigned stay; a list that leaves one of
        them out is `400`, because nothing here releases a number.

        ```json
        { "numbers": [{ "area_code": "415", "quantity": 2 }, { "quantity": 1 }] }
        ```

        A `LOCAL` market is claimed from inventory at once, and whatever inventory
        cannot cover stays pending. A `TEN_DLC` market's numbers are recorded on its
        campaign and assigned once the carriers elect it — on the next acquisition cycle
        when it already has been. They need a campaign of the profile's own: one
        inherited from the organization is `400`.

        ## What it will refuse

        **A filed identity is `409`.** Once the registration has gone to The Campaign
        Registry they hold a copy, and a local change would diverge from it silently.
        The campaign is not frozen — omit `brand` and the same body is accepted. The
        exception is a registration sent back for correction: the identity is accepted,
        and a correction to either half sends the registration back for review. Refiling
        it with The Campaign Registry stays with Sent.

        **More than one campaign is `409`.** The schema permits several and an account
        built on the admin side may hold them; this surface writes one, and editing
        whichever sorted first would leave the others unmentioned and unedited.

        Nothing is submitted to a regime here. These are the rows a submission is later
        assembled from, which is what lets them be corrected without waiting on
        something externally rejectable.

        Send `x-profile-id` with an organization key to write one of your profiles'
        markets.

        Args:
          compliance: The compliance values a market registers with. `brand` and `campaign` apply to
              US `TEN_DLC`; other markets fill this map with the document keys their own
              requirements name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
            path_template("/v3/channels/sms/{country}/{type}", country=country, type=type),
            body=await async_maybe_transform(
                {
                    "compliance": compliance,
                    "sandbox": sandbox,
                },
                sms_update_params.SMSUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfSMSMarket,
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
    ) -> APIResponseOfListOfSMSMarket:
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
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            "/v3/channels/sms",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfListOfSMSMarket,
        )


class SMSResourceWithRawResponse:
    def __init__(self, sms: SMSResource) -> None:
        self._sms = sms

        self.create = to_raw_response_wrapper(
            sms.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sms.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sms.update,
        )
        self.list = to_raw_response_wrapper(
            sms.list,
        )

    @cached_property
    def ten_dlc(self) -> TenDlcResourceWithRawResponse:
        """The senders you send from, one per channel.

        **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

        ## Compliance lives on the market

        Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

        `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

        Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
        """
        return TenDlcResourceWithRawResponse(self._sms.ten_dlc)


class AsyncSMSResourceWithRawResponse:
    def __init__(self, sms: AsyncSMSResource) -> None:
        self._sms = sms

        self.create = async_to_raw_response_wrapper(
            sms.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sms.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sms.update,
        )
        self.list = async_to_raw_response_wrapper(
            sms.list,
        )

    @cached_property
    def ten_dlc(self) -> AsyncTenDlcResourceWithRawResponse:
        """The senders you send from, one per channel.

        **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

        ## Compliance lives on the market

        Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

        `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

        Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
        """
        return AsyncTenDlcResourceWithRawResponse(self._sms.ten_dlc)


class SMSResourceWithStreamingResponse:
    def __init__(self, sms: SMSResource) -> None:
        self._sms = sms

        self.create = to_streamed_response_wrapper(
            sms.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sms.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sms.update,
        )
        self.list = to_streamed_response_wrapper(
            sms.list,
        )

    @cached_property
    def ten_dlc(self) -> TenDlcResourceWithStreamingResponse:
        """The senders you send from, one per channel.

        **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

        ## Compliance lives on the market

        Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

        `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

        Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
        """
        return TenDlcResourceWithStreamingResponse(self._sms.ten_dlc)


class AsyncSMSResourceWithStreamingResponse:
    def __init__(self, sms: AsyncSMSResource) -> None:
        self._sms = sms

        self.create = async_to_streamed_response_wrapper(
            sms.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sms.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sms.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sms.list,
        )

    @cached_property
    def ten_dlc(self) -> AsyncTenDlcResourceWithStreamingResponse:
        """The senders you send from, one per channel.

        **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

        ## Compliance lives on the market

        Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

        `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

        Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
        """
        return AsyncTenDlcResourceWithStreamingResponse(self._sms.ten_dlc)
