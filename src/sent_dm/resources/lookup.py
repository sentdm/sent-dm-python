# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.lookup_retrieve_phone_info_response import LookupRetrievePhoneInfoResponse

__all__ = ["LookupResource", "AsyncLookupResource"]


class LookupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LookupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return LookupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LookupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return LookupResourceWithStreamingResponse(self)

    def retrieve_phone_info(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LookupRetrievePhoneInfoResponse:
        """
        Validates a phone number and retrieves formatting, country, and timezone
        information from the internal index. Provider-agnostic and works for all
        customers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            f"/v3/lookup/number/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LookupRetrievePhoneInfoResponse,
        )


class AsyncLookupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLookupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLookupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLookupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncLookupResourceWithStreamingResponse(self)

    async def retrieve_phone_info(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LookupRetrievePhoneInfoResponse:
        """
        Validates a phone number and retrieves formatting, country, and timezone
        information from the internal index. Provider-agnostic and works for all
        customers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            f"/v3/lookup/number/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LookupRetrievePhoneInfoResponse,
        )


class LookupResourceWithRawResponse:
    def __init__(self, lookup: LookupResource) -> None:
        self._lookup = lookup

        self.retrieve_phone_info = to_raw_response_wrapper(
            lookup.retrieve_phone_info,
        )


class AsyncLookupResourceWithRawResponse:
    def __init__(self, lookup: AsyncLookupResource) -> None:
        self._lookup = lookup

        self.retrieve_phone_info = async_to_raw_response_wrapper(
            lookup.retrieve_phone_info,
        )


class LookupResourceWithStreamingResponse:
    def __init__(self, lookup: LookupResource) -> None:
        self._lookup = lookup

        self.retrieve_phone_info = to_streamed_response_wrapper(
            lookup.retrieve_phone_info,
        )


class AsyncLookupResourceWithStreamingResponse:
    def __init__(self, lookup: AsyncLookupResource) -> None:
        self._lookup = lookup

        self.retrieve_phone_info = async_to_streamed_response_wrapper(
            lookup.retrieve_phone_info,
        )
