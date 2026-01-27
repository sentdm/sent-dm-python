# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import number_lookup_retrieve_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.number_lookup_retrieve_response import NumberLookupRetrieveResponse

__all__ = ["NumberLookupResource", "AsyncNumberLookupResource"]


class NumberLookupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NumberLookupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return NumberLookupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NumberLookupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return NumberLookupResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberLookupRetrieveResponse:
        """
        Retrieves detailed information about a phone number including validation,
        formatting, country information, and available messaging channels. The customer
        ID is extracted from the authentication token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/number-lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"phone_number": phone_number}, number_lookup_retrieve_params.NumberLookupRetrieveParams
                ),
            ),
            cast_to=NumberLookupRetrieveResponse,
        )


class AsyncNumberLookupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNumberLookupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNumberLookupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNumberLookupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncNumberLookupResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NumberLookupRetrieveResponse:
        """
        Retrieves detailed information about a phone number including validation,
        formatting, country information, and available messaging channels. The customer
        ID is extracted from the authentication token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/number-lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"phone_number": phone_number}, number_lookup_retrieve_params.NumberLookupRetrieveParams
                ),
            ),
            cast_to=NumberLookupRetrieveResponse,
        )


class NumberLookupResourceWithRawResponse:
    def __init__(self, number_lookup: NumberLookupResource) -> None:
        self._number_lookup = number_lookup

        self.retrieve = to_raw_response_wrapper(
            number_lookup.retrieve,
        )


class AsyncNumberLookupResourceWithRawResponse:
    def __init__(self, number_lookup: AsyncNumberLookupResource) -> None:
        self._number_lookup = number_lookup

        self.retrieve = async_to_raw_response_wrapper(
            number_lookup.retrieve,
        )


class NumberLookupResourceWithStreamingResponse:
    def __init__(self, number_lookup: NumberLookupResource) -> None:
        self._number_lookup = number_lookup

        self.retrieve = to_streamed_response_wrapper(
            number_lookup.retrieve,
        )


class AsyncNumberLookupResourceWithStreamingResponse:
    def __init__(self, number_lookup: AsyncNumberLookupResource) -> None:
        self._number_lookup = number_lookup

        self.retrieve = async_to_streamed_response_wrapper(
            number_lookup.retrieve,
        )
