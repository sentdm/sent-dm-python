# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.channels import rc_create_params
from ...types.channels.rcs_address_param import RcsAddressParam
from ...types.channels.api_response_of_rcs_agent import APIResponseOfRcsAgent

__all__ = ["RcsResource", "AsyncRcsResource"]


class RcsResource(SyncAPIResource):
    """The senders you send from, one per channel.

    **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

    ## Compliance lives on the market

    Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

    `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

    Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
    """

    @cached_property
    def with_raw_response(self) -> RcsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return RcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RcsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return RcsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_use_case: Literal["VERIFICATION", "NOTIFICATIONS", "MARKETING", "MULTI_USE"] | Omit = omit,
        banner_url: str | Omit = omit,
        brand_color: str | Omit = omit,
        brand_email: str | Omit = omit,
        brand_name: str | Omit = omit,
        brand_phone_number: str | Omit = omit,
        brief_company_description: str | Omit = omit,
        company_ein: str | Omit = omit,
        contact_name_and_title: str | Omit = omit,
        customer_support_email: str | Omit = omit,
        customer_support_phone_number: str | Omit = omit,
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        entity_type: str | Omit = omit,
        help_message: str | Omit = omit,
        logo_url: str | Omit = omit,
        official_address: RcsAddressParam | Omit = omit,
        opt_in_process_description: str | Omit = omit,
        opt_in_screenshot_url: Optional[str] | Omit = omit,
        privacy_policy_url: str | Omit = omit,
        sample_messages: SequenceNotStr[str] | Omit = omit,
        sandbox: bool | Omit = omit,
        start_message: str | Omit = omit,
        stop_message: str | Omit = omit,
        terms_and_conditions_url: str | Omit = omit,
        website_url: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfRcsAgent:
        """
        Asks for an RCS agent and records the order form the carriers vet it against.
        Always `202`: an agent is approved by the carriers, not by this call, and
        nothing here can make that happen sooner.

        ## What it asks for

        The RCS Agent Order Form — the same one our team fills in on your behalf today,
        so nothing has to be collected from you twice. **All fields are required** and
        must be submitted together so the carrier review has everything it needs. The
        only exception is `opt_in_screenshot_url`.

        **Agent identity:** `display_name`, `description`, `agent_use_case` (must be one
        of the accepted use cases; the error names the set), `brand_color` (six-digit
        hex, `#RRGGBB`).

        **Brand identity:** `brand_name` — the brand this agent presents. Not taken from
        `compliance.brand`: a business may present a different brand on RCS than the one
        its 10DLC registration is filed against, and the carriers vet this one.
        `privacy_policy_url`, `terms_and_conditions_url`, `website_url`, `logo_url`, and
        `banner_url` must be absolute `http(s)` URLs that the carriers can fetch without
        authentication. The form specifies 224×224 px and 50 KB for the logo and
        1440×448 px and 200 KB for the banner; these cannot be checked without the image
        bytes.

        **Contact details:** `brand_phone_number`, `customer_support_phone_number`,
        `brand_email`, `customer_support_email`, `contact_name_and_title`.

        **Company:** `company_ein`, `entity_type`, `official_address` (street, city,
        state, postal_code, country), `brief_company_description`.

        **Consent and messages:** `opt_in_process_description`, `start_message`,
        `help_message`, `stop_message`, `sample_messages` (at least one example
        message).

        **Optional:** `opt_in_screenshot_url` (validated as an http(s) URL if supplied).

        Anything supplied is checked against accepted values rather than passed through:
        a value the provider rejects would otherwise surface days later, to somebody who
        cannot fix it without asking you.

        **A customer has one agent.** Asking again while you have one is `409`.

        ## What comes back, and what does not

        Returns **the agent** — the form as stored, plus `id` and `status`. Not your
        other channels, which this call cannot have changed.

        `status` is `PROVISIONING` until the agent is handed to the carriers and
        approved. **`GET /v3/channels` reports `rcs: null` until then** — a channel row
        is what routing reads to decide you are sendable, and writing one for an
        unapproved agent would claim a channel that cannot carry traffic.

        Send `x-profile-id` with an organization key to ask for one of your profiles'
        agents.

        Args:
          agent_use_case: Which kind of traffic the agent carries. One of the accepted use cases; the
              error names the set.

              - `VERIFICATION` - One-time passcodes and identity checks. Expects no reply, and
                is held to the strictest delivery review.
              - `NOTIFICATIONS` - Transactional updates the recipient asked for — orders,
                deliveries, appointments, account activity.
              - `MARKETING` - Promotional content. Requires the clearest opt-in evidence of
                the four, because the carriers review consent hardest here.
              - `MULTI_USE` - More than one of the above from a single agent. Vetted against
                the strictest use case it covers, so declare it only if you genuinely need one
                agent to do several jobs.

          brand_color: Primary brand colour, as #RRGGBB. Three-digit shorthand is refused: the value is
              submitted verbatim, so two spellings of one colour is only a way for the stored
              value to disagree with the form.

          brand_name: The brand this agent presents over RCS.

              Not taken from your compliance.brand: a business may present a different brand
              on RCS than the one its 10DLC registration is filed against, and the carriers
              vet this one.

          brand_phone_number: The brand's own number. Also becomes the agent's canonical sending number for
              routing, which is why it is normalised to E.164 rather than stored as sent.

          description: What the agent is for, shown to recipients. Capped by the carriers, not by us.

          display_name: The name the agent shows in the messaging client.

          logo_url: Publicly reachable logo. It has to be fetchable without authentication at review
              time, so a URL behind a login passes this call and fails the review.

          official_address: The registered address of the company behind the agent.

          opt_in_process_description: How recipients opt in, in prose. The carriers read this one.

          opt_in_screenshot_url: A screenshot of the opt-in, as a publicly fetchable URL.

          privacy_policy_url: Required by US carriers. Must be an absolute http(s) URL they can fetch.

          sample_messages: Examples of what the agent will send, for the review.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          website_url: The brand's own site.

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
            "/v3/channels/rcs",
            body=maybe_transform(
                {
                    "agent_use_case": agent_use_case,
                    "banner_url": banner_url,
                    "brand_color": brand_color,
                    "brand_email": brand_email,
                    "brand_name": brand_name,
                    "brand_phone_number": brand_phone_number,
                    "brief_company_description": brief_company_description,
                    "company_ein": company_ein,
                    "contact_name_and_title": contact_name_and_title,
                    "customer_support_email": customer_support_email,
                    "customer_support_phone_number": customer_support_phone_number,
                    "description": description,
                    "display_name": display_name,
                    "entity_type": entity_type,
                    "help_message": help_message,
                    "logo_url": logo_url,
                    "official_address": official_address,
                    "opt_in_process_description": opt_in_process_description,
                    "opt_in_screenshot_url": opt_in_screenshot_url,
                    "privacy_policy_url": privacy_policy_url,
                    "sample_messages": sample_messages,
                    "sandbox": sandbox,
                    "start_message": start_message,
                    "stop_message": stop_message,
                    "terms_and_conditions_url": terms_and_conditions_url,
                    "website_url": website_url,
                },
                rc_create_params.RcCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfRcsAgent,
        )


class AsyncRcsResource(AsyncAPIResource):
    """The senders you send from, one per channel.

    **SMS is a list of markets**, each keyed by `(country, number_type)` — a customer can hold `us/10dlc` and `gb/alphanumeric` at once, so a market is addressed by the pair rather than by country alone. **WhatsApp and RCS are single**: a customer has one business account and one agent. **Voice is per number**: each number you hold can carry phone calls on its own (`POST /v3/channels/voice`), each with the callback URL Sent asks what to do with its calls, one of them is the default line for calls placed from your app, and voice tokens are minted with `POST /v3/voice/tokens`. Read your voice numbers with `GET /v3/channels/voice` and change one with `PATCH /v3/channels/voice/{number}`.

    ## Compliance lives on the market

    Adding a market records everything that market registers with, in its `compliance` object. Only **US `TEN_DLC`** registers with a regime — The Campaign Registry — and it is the only market whose compliance carries `brand` and `campaign`. Everywhere else compliance is documents, and many markets ask for none at all.

    `GET` and `PATCH` on a market return and accept the same shape, so what comes back can be sent back: an omitted key is left alone, and a key reported in `requirements` is the path into the body that clears it.

    Call `GET /v3/compliance/requirements` first — it answers what a market demands before you hold it, with a body you can fill in and post.
    """

    @cached_property
    def with_raw_response(self) -> AsyncRcsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRcsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncRcsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_use_case: Literal["VERIFICATION", "NOTIFICATIONS", "MARKETING", "MULTI_USE"] | Omit = omit,
        banner_url: str | Omit = omit,
        brand_color: str | Omit = omit,
        brand_email: str | Omit = omit,
        brand_name: str | Omit = omit,
        brand_phone_number: str | Omit = omit,
        brief_company_description: str | Omit = omit,
        company_ein: str | Omit = omit,
        contact_name_and_title: str | Omit = omit,
        customer_support_email: str | Omit = omit,
        customer_support_phone_number: str | Omit = omit,
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        entity_type: str | Omit = omit,
        help_message: str | Omit = omit,
        logo_url: str | Omit = omit,
        official_address: RcsAddressParam | Omit = omit,
        opt_in_process_description: str | Omit = omit,
        opt_in_screenshot_url: Optional[str] | Omit = omit,
        privacy_policy_url: str | Omit = omit,
        sample_messages: SequenceNotStr[str] | Omit = omit,
        sandbox: bool | Omit = omit,
        start_message: str | Omit = omit,
        stop_message: str | Omit = omit,
        terms_and_conditions_url: str | Omit = omit,
        website_url: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfRcsAgent:
        """
        Asks for an RCS agent and records the order form the carriers vet it against.
        Always `202`: an agent is approved by the carriers, not by this call, and
        nothing here can make that happen sooner.

        ## What it asks for

        The RCS Agent Order Form — the same one our team fills in on your behalf today,
        so nothing has to be collected from you twice. **All fields are required** and
        must be submitted together so the carrier review has everything it needs. The
        only exception is `opt_in_screenshot_url`.

        **Agent identity:** `display_name`, `description`, `agent_use_case` (must be one
        of the accepted use cases; the error names the set), `brand_color` (six-digit
        hex, `#RRGGBB`).

        **Brand identity:** `brand_name` — the brand this agent presents. Not taken from
        `compliance.brand`: a business may present a different brand on RCS than the one
        its 10DLC registration is filed against, and the carriers vet this one.
        `privacy_policy_url`, `terms_and_conditions_url`, `website_url`, `logo_url`, and
        `banner_url` must be absolute `http(s)` URLs that the carriers can fetch without
        authentication. The form specifies 224×224 px and 50 KB for the logo and
        1440×448 px and 200 KB for the banner; these cannot be checked without the image
        bytes.

        **Contact details:** `brand_phone_number`, `customer_support_phone_number`,
        `brand_email`, `customer_support_email`, `contact_name_and_title`.

        **Company:** `company_ein`, `entity_type`, `official_address` (street, city,
        state, postal_code, country), `brief_company_description`.

        **Consent and messages:** `opt_in_process_description`, `start_message`,
        `help_message`, `stop_message`, `sample_messages` (at least one example
        message).

        **Optional:** `opt_in_screenshot_url` (validated as an http(s) URL if supplied).

        Anything supplied is checked against accepted values rather than passed through:
        a value the provider rejects would otherwise surface days later, to somebody who
        cannot fix it without asking you.

        **A customer has one agent.** Asking again while you have one is `409`.

        ## What comes back, and what does not

        Returns **the agent** — the form as stored, plus `id` and `status`. Not your
        other channels, which this call cannot have changed.

        `status` is `PROVISIONING` until the agent is handed to the carriers and
        approved. **`GET /v3/channels` reports `rcs: null` until then** — a channel row
        is what routing reads to decide you are sendable, and writing one for an
        unapproved agent would claim a channel that cannot carry traffic.

        Send `x-profile-id` with an organization key to ask for one of your profiles'
        agents.

        Args:
          agent_use_case: Which kind of traffic the agent carries. One of the accepted use cases; the
              error names the set.

              - `VERIFICATION` - One-time passcodes and identity checks. Expects no reply, and
                is held to the strictest delivery review.
              - `NOTIFICATIONS` - Transactional updates the recipient asked for — orders,
                deliveries, appointments, account activity.
              - `MARKETING` - Promotional content. Requires the clearest opt-in evidence of
                the four, because the carriers review consent hardest here.
              - `MULTI_USE` - More than one of the above from a single agent. Vetted against
                the strictest use case it covers, so declare it only if you genuinely need one
                agent to do several jobs.

          brand_color: Primary brand colour, as #RRGGBB. Three-digit shorthand is refused: the value is
              submitted verbatim, so two spellings of one colour is only a way for the stored
              value to disagree with the form.

          brand_name: The brand this agent presents over RCS.

              Not taken from your compliance.brand: a business may present a different brand
              on RCS than the one its 10DLC registration is filed against, and the carriers
              vet this one.

          brand_phone_number: The brand's own number. Also becomes the agent's canonical sending number for
              routing, which is why it is normalised to E.164 rather than stored as sent.

          description: What the agent is for, shown to recipients. Capped by the carriers, not by us.

          display_name: The name the agent shows in the messaging client.

          logo_url: Publicly reachable logo. It has to be fetchable without authentication at review
              time, so a URL behind a login passes this call and fails the review.

          official_address: The registered address of the company behind the agent.

          opt_in_process_description: How recipients opt in, in prose. The carriers read this one.

          opt_in_screenshot_url: A screenshot of the opt-in, as a publicly fetchable URL.

          privacy_policy_url: Required by US carriers. Must be an absolute http(s) URL they can fetch.

          sample_messages: Examples of what the agent will send, for the review.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          website_url: The brand's own site.

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
            "/v3/channels/rcs",
            body=await async_maybe_transform(
                {
                    "agent_use_case": agent_use_case,
                    "banner_url": banner_url,
                    "brand_color": brand_color,
                    "brand_email": brand_email,
                    "brand_name": brand_name,
                    "brand_phone_number": brand_phone_number,
                    "brief_company_description": brief_company_description,
                    "company_ein": company_ein,
                    "contact_name_and_title": contact_name_and_title,
                    "customer_support_email": customer_support_email,
                    "customer_support_phone_number": customer_support_phone_number,
                    "description": description,
                    "display_name": display_name,
                    "entity_type": entity_type,
                    "help_message": help_message,
                    "logo_url": logo_url,
                    "official_address": official_address,
                    "opt_in_process_description": opt_in_process_description,
                    "opt_in_screenshot_url": opt_in_screenshot_url,
                    "privacy_policy_url": privacy_policy_url,
                    "sample_messages": sample_messages,
                    "sandbox": sandbox,
                    "start_message": start_message,
                    "stop_message": stop_message,
                    "terms_and_conditions_url": terms_and_conditions_url,
                    "website_url": website_url,
                },
                rc_create_params.RcCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfRcsAgent,
        )


class RcsResourceWithRawResponse:
    def __init__(self, rcs: RcsResource) -> None:
        self._rcs = rcs

        self.create = to_raw_response_wrapper(
            rcs.create,
        )


class AsyncRcsResourceWithRawResponse:
    def __init__(self, rcs: AsyncRcsResource) -> None:
        self._rcs = rcs

        self.create = async_to_raw_response_wrapper(
            rcs.create,
        )


class RcsResourceWithStreamingResponse:
    def __init__(self, rcs: RcsResource) -> None:
        self._rcs = rcs

        self.create = to_streamed_response_wrapper(
            rcs.create,
        )


class AsyncRcsResourceWithStreamingResponse:
    def __init__(self, rcs: AsyncRcsResource) -> None:
        self._rcs = rcs

        self.create = async_to_streamed_response_wrapper(
            rcs.create,
        )
