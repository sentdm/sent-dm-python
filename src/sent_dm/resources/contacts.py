# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import contact_list_params, contact_retrieve_id_params, contact_retrieve_by_phone_params
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
from ..types.contact_list_item import ContactListItem
from ..types.contact_list_response import ContactListResponse

__all__ = ["ContactsResource", "AsyncContactsResource"]


class ContactsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return ContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return ContactsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        page: int,
        page_size: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListResponse:
        """Retrieves a paginated list of contacts for the authenticated customer.

        Supports
        server-side pagination with configurable page size. The customer ID is extracted
        from the authentication token.

        Args:
          page: The page number (zero-indexed). Default is 0.

          page_size: The number of items per page. Default is 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/contacts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    contact_list_params.ContactListParams,
                ),
            ),
            cast_to=ContactListResponse,
        )

    def retrieve_by_phone(
        self,
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListItem:
        """Retrieves a contact by their phone number for the authenticated customer.

        Phone
        number should be in international format (e.g., +1234567890). The customer ID is
        extracted from the authentication token.

        Args:
          phone_number: The phone number in international format (e.g., +1234567890)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/contacts/phone",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"phone_number": phone_number}, contact_retrieve_by_phone_params.ContactRetrieveByPhoneParams
                ),
            ),
            cast_to=ContactListItem,
        )

    def retrieve_id(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListItem:
        """
        Retrieves a specific contact by their unique identifier for the authenticated
        customer. The customer ID is extracted from the authentication token. Returns
        detailed contact information including phone number and creation timestamp.

        Args:
          id: The unique identifier (GUID) of the resource to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/contacts/id",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, contact_retrieve_id_params.ContactRetrieveIDParams),
            ),
            cast_to=ContactListItem,
        )


class AsyncContactsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncContactsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        page: int,
        page_size: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListResponse:
        """Retrieves a paginated list of contacts for the authenticated customer.

        Supports
        server-side pagination with configurable page size. The customer ID is extracted
        from the authentication token.

        Args:
          page: The page number (zero-indexed). Default is 0.

          page_size: The number of items per page. Default is 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/contacts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    contact_list_params.ContactListParams,
                ),
            ),
            cast_to=ContactListResponse,
        )

    async def retrieve_by_phone(
        self,
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListItem:
        """Retrieves a contact by their phone number for the authenticated customer.

        Phone
        number should be in international format (e.g., +1234567890). The customer ID is
        extracted from the authentication token.

        Args:
          phone_number: The phone number in international format (e.g., +1234567890)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/contacts/phone",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"phone_number": phone_number}, contact_retrieve_by_phone_params.ContactRetrieveByPhoneParams
                ),
            ),
            cast_to=ContactListItem,
        )

    async def retrieve_id(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListItem:
        """
        Retrieves a specific contact by their unique identifier for the authenticated
        customer. The customer ID is extracted from the authentication token. Returns
        detailed contact information including phone number and creation timestamp.

        Args:
          id: The unique identifier (GUID) of the resource to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/contacts/id",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, contact_retrieve_id_params.ContactRetrieveIDParams),
            ),
            cast_to=ContactListItem,
        )


class ContactsResourceWithRawResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.list = to_raw_response_wrapper(
            contacts.list,
        )
        self.retrieve_by_phone = to_raw_response_wrapper(
            contacts.retrieve_by_phone,
        )
        self.retrieve_id = to_raw_response_wrapper(
            contacts.retrieve_id,
        )


class AsyncContactsResourceWithRawResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.list = async_to_raw_response_wrapper(
            contacts.list,
        )
        self.retrieve_by_phone = async_to_raw_response_wrapper(
            contacts.retrieve_by_phone,
        )
        self.retrieve_id = async_to_raw_response_wrapper(
            contacts.retrieve_id,
        )


class ContactsResourceWithStreamingResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.list = to_streamed_response_wrapper(
            contacts.list,
        )
        self.retrieve_by_phone = to_streamed_response_wrapper(
            contacts.retrieve_by_phone,
        )
        self.retrieve_id = to_streamed_response_wrapper(
            contacts.retrieve_id,
        )


class AsyncContactsResourceWithStreamingResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.list = async_to_streamed_response_wrapper(
            contacts.list,
        )
        self.retrieve_by_phone = async_to_streamed_response_wrapper(
            contacts.retrieve_by_phone,
        )
        self.retrieve_id = async_to_streamed_response_wrapper(
            contacts.retrieve_id,
        )
