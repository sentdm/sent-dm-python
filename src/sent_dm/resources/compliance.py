# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import compliance_retrieve_requirements_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.api_response_of_compliance_requirements import APIResponseOfComplianceRequirements

__all__ = ["ComplianceResource", "AsyncComplianceResource"]


class ComplianceResource(SyncAPIResource):
    """What a market demands, before you have it.

    Requirements vary enormously and change without notice. US `TEN_DLC` registers a brand and a campaign with The Campaign Registry and asks a substantial set of questions; an alphanumeric sender pre-registers with documents in one country and needs nothing in another.

    This is the authoritative answer for whichever market you ask about, and it is generated from the same declaration that validates the calls themselves — so it cannot drift from what is actually enforced. The response includes the request body to send, with every key that market wants already present and blank.

    What you supplied, as opposed to what is asked of you, is reported on the market under **Channels**.
    """

    @cached_property
    def with_raw_response(self) -> ComplianceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return ComplianceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ComplianceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return ComplianceResourceWithStreamingResponse(self)

    def retrieve_requirements(
        self,
        *,
        channel: Optional[str] | Omit = omit,
        country: Optional[str] | Omit = omit,
        type: Optional[str] | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfComplianceRequirements:
        """
        **Call this first.** It returns what a channel, country and sender type demand
        before you can send there — and `setup[]`, the calls that satisfy those demands,
        in order, each with a body you can copy and send as it stands. You never have to
        track forty countries' rules yourself.

        ## Channel

        `channel` is `sms`, `whatsapp` or `rcs`, and **defaults to `sms`** — so a caller
        that omits it gets exactly what this endpoint has always returned.

        `sms` is the only one answered today; the other two are `501` until their
        requirements are declared. They are refused rather than answered with an empty
        requirement set, because empty would say the channel demands nothing, and both
        demand plenty — WhatsApp a business verification and a display name review, RCS
        a carrier approval. Saying "not yet" is the true answer and the same one
        `POST /v3/sender-profiles` gives for `channels.whatsapp`.

        `type` is an SMS sender type, and SMS is the only channel whose senders have
        one.

        Requirements vary enormously. US `TEN_DLC` registers a brand and a campaign with
        The Campaign Registry and asks for a substantial set of values. An alphanumeric
        sender in one country pre-registers with supporting documents; in another it
        needs nothing at all. This is the authoritative answer for whichever market you
        are asking about, and it is the same declaration used to validate the calls
        themselves — so it can never drift from what is actually enforced.

        ## `setup[]` — what to do

        **One step.** `POST /v3/channels/sms` adds the market and records everything it
        registers with — the identity in `compliance.brand`, the programme in
        `compliance.campaign`. There were three, in a load-bearing order, while the
        identity and the campaign were resources of their own; they are members of this
        call's body now, so there is nothing to sequence.

        Correct any of it afterwards with `PATCH /v3/channels/sms/{country}/{type}`,
        which takes the same `compliance` object one key at a time.

        Each step's `body` has every key that market wants already present, with the
        values left **blank**. Blank rather than filled with placeholders, because the
        body is meant to be sent: a null value counts as not supplied, so posting a step
        verbatim comes back naming every blank you left. `attachments[]` lists files to
        send as multipart on the channel call, each under the field name given — a file
        cannot be a JSON value, so documents are never listed in `compliance[]`.

        Every step is a call for whoever holds the key. To set a **sender profile** up
        instead, send the same requests with the `x-profile-id` header naming it; there
        is no separate path.

        ## `requirements[]` — what each value means

        Each entry names a key for the `compliance` array, its value type, and whether
        it is required. `required_when` marks values needed only in certain cases —
        evaluate it against your own payload, e.g. `brand.entity_type == PUBLIC_PROFIT`.
        `options` lists accepted values where the market constrains them, and `label` is
        suitable for rendering a form field.

        Values Sent supplies on your behalf are never listed: correlation ids,
        environment flags, carrier elections, and booleans derivable from what you
        already send.

        ## When nothing is required

        `required` is `false` and `requirements` is empty, and the single `setup` step
        carries no `compliance` array at all. A `sender_id_pattern` may still be present
        — many markets constrain the sender string without registering anything.

        Args:
          channel: Channel the sender is for: sms, whatsapp or rcs. Defaults to sms, which is the
              only one answered today — the other two are 501 until their requirements are
              declared.

          country: ISO 3166-1 alpha-2 country code, e.g. US, XK, IN

          type: Sender type: LOCAL, MOBILE, TEN_DLC, TOLL_FREE, SHORT_CODE, ALPHANUMERIC. 10DLC
              is accepted as a synonym of TEN_DLC, the same as on POST /v3/sender-profiles.
              Applies to channel=sms, the only channel whose senders have a type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            "/v3/compliance/requirements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channel": channel,
                        "country": country,
                        "type": type,
                    },
                    compliance_retrieve_requirements_params.ComplianceRetrieveRequirementsParams,
                ),
            ),
            cast_to=APIResponseOfComplianceRequirements,
        )


class AsyncComplianceResource(AsyncAPIResource):
    """What a market demands, before you have it.

    Requirements vary enormously and change without notice. US `TEN_DLC` registers a brand and a campaign with The Campaign Registry and asks a substantial set of questions; an alphanumeric sender pre-registers with documents in one country and needs nothing in another.

    This is the authoritative answer for whichever market you ask about, and it is generated from the same declaration that validates the calls themselves — so it cannot drift from what is actually enforced. The response includes the request body to send, with every key that market wants already present and blank.

    What you supplied, as opposed to what is asked of you, is reported on the market under **Channels**.
    """

    @cached_property
    def with_raw_response(self) -> AsyncComplianceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncComplianceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncComplianceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncComplianceResourceWithStreamingResponse(self)

    async def retrieve_requirements(
        self,
        *,
        channel: Optional[str] | Omit = omit,
        country: Optional[str] | Omit = omit,
        type: Optional[str] | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfComplianceRequirements:
        """
        **Call this first.** It returns what a channel, country and sender type demand
        before you can send there — and `setup[]`, the calls that satisfy those demands,
        in order, each with a body you can copy and send as it stands. You never have to
        track forty countries' rules yourself.

        ## Channel

        `channel` is `sms`, `whatsapp` or `rcs`, and **defaults to `sms`** — so a caller
        that omits it gets exactly what this endpoint has always returned.

        `sms` is the only one answered today; the other two are `501` until their
        requirements are declared. They are refused rather than answered with an empty
        requirement set, because empty would say the channel demands nothing, and both
        demand plenty — WhatsApp a business verification and a display name review, RCS
        a carrier approval. Saying "not yet" is the true answer and the same one
        `POST /v3/sender-profiles` gives for `channels.whatsapp`.

        `type` is an SMS sender type, and SMS is the only channel whose senders have
        one.

        Requirements vary enormously. US `TEN_DLC` registers a brand and a campaign with
        The Campaign Registry and asks for a substantial set of values. An alphanumeric
        sender in one country pre-registers with supporting documents; in another it
        needs nothing at all. This is the authoritative answer for whichever market you
        are asking about, and it is the same declaration used to validate the calls
        themselves — so it can never drift from what is actually enforced.

        ## `setup[]` — what to do

        **One step.** `POST /v3/channels/sms` adds the market and records everything it
        registers with — the identity in `compliance.brand`, the programme in
        `compliance.campaign`. There were three, in a load-bearing order, while the
        identity and the campaign were resources of their own; they are members of this
        call's body now, so there is nothing to sequence.

        Correct any of it afterwards with `PATCH /v3/channels/sms/{country}/{type}`,
        which takes the same `compliance` object one key at a time.

        Each step's `body` has every key that market wants already present, with the
        values left **blank**. Blank rather than filled with placeholders, because the
        body is meant to be sent: a null value counts as not supplied, so posting a step
        verbatim comes back naming every blank you left. `attachments[]` lists files to
        send as multipart on the channel call, each under the field name given — a file
        cannot be a JSON value, so documents are never listed in `compliance[]`.

        Every step is a call for whoever holds the key. To set a **sender profile** up
        instead, send the same requests with the `x-profile-id` header naming it; there
        is no separate path.

        ## `requirements[]` — what each value means

        Each entry names a key for the `compliance` array, its value type, and whether
        it is required. `required_when` marks values needed only in certain cases —
        evaluate it against your own payload, e.g. `brand.entity_type == PUBLIC_PROFIT`.
        `options` lists accepted values where the market constrains them, and `label` is
        suitable for rendering a form field.

        Values Sent supplies on your behalf are never listed: correlation ids,
        environment flags, carrier elections, and booleans derivable from what you
        already send.

        ## When nothing is required

        `required` is `false` and `requirements` is empty, and the single `setup` step
        carries no `compliance` array at all. A `sender_id_pattern` may still be present
        — many markets constrain the sender string without registering anything.

        Args:
          channel: Channel the sender is for: sms, whatsapp or rcs. Defaults to sms, which is the
              only one answered today — the other two are 501 until their requirements are
              declared.

          country: ISO 3166-1 alpha-2 country code, e.g. US, XK, IN

          type: Sender type: LOCAL, MOBILE, TEN_DLC, TOLL_FREE, SHORT_CODE, ALPHANUMERIC. 10DLC
              is accepted as a synonym of TEN_DLC, the same as on POST /v3/sender-profiles.
              Applies to channel=sms, the only channel whose senders have a type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            "/v3/compliance/requirements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channel": channel,
                        "country": country,
                        "type": type,
                    },
                    compliance_retrieve_requirements_params.ComplianceRetrieveRequirementsParams,
                ),
            ),
            cast_to=APIResponseOfComplianceRequirements,
        )


class ComplianceResourceWithRawResponse:
    def __init__(self, compliance: ComplianceResource) -> None:
        self._compliance = compliance

        self.retrieve_requirements = to_raw_response_wrapper(
            compliance.retrieve_requirements,
        )


class AsyncComplianceResourceWithRawResponse:
    def __init__(self, compliance: AsyncComplianceResource) -> None:
        self._compliance = compliance

        self.retrieve_requirements = async_to_raw_response_wrapper(
            compliance.retrieve_requirements,
        )


class ComplianceResourceWithStreamingResponse:
    def __init__(self, compliance: ComplianceResource) -> None:
        self._compliance = compliance

        self.retrieve_requirements = to_streamed_response_wrapper(
            compliance.retrieve_requirements,
        )


class AsyncComplianceResourceWithStreamingResponse:
    def __init__(self, compliance: AsyncComplianceResource) -> None:
        self._compliance = compliance

        self.retrieve_requirements = async_to_streamed_response_wrapper(
            compliance.retrieve_requirements,
        )
