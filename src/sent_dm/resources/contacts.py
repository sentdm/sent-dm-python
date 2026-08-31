# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Optional

import httpx

from ..types import contact_list_params, contact_create_params, contact_delete_params, contact_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.contact_list_response import ContactListResponse
from ..types.contact_create_response import ContactCreateResponse
from ..types.contact_update_response import ContactUpdateResponse
from ..types.contact_retrieve_response import ContactRetrieveResponse
from ..types.contact_retrieve_message_summary_response import ContactRetrieveMessageSummaryResponse

__all__ = ["ContactsResource", "AsyncContactsResource"]


class ContactsResource(SyncAPIResource):
    """The people you message, and their channel identities.

    A contact holds one identity per channel — a phone number, a WhatsApp number — so routing can choose between them for the same person. Opt-out is recorded against the contact and honoured on every send, whichever channel it came through.

    `GET /v3/contacts/{id}/message-summary` is the per-contact view of what you have sent and what happened to it.
    """

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

    def create(
        self,
        *,
        phone_number: str,
        sandbox: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCreateResponse:
        """
        Creates a new contact by phone number and associates it with the authenticated
        customer.

        Args:
          phone_number: Phone number of the contact to create

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
            "/v3/contacts",
            body=maybe_transform(
                {
                    "phone_number": phone_number,
                    "sandbox": sandbox,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactRetrieveResponse:
        """Retrieves a specific contact by their unique identifier.

        Returns detailed
        contact information including phone formats, available channels, and opt-out
        status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v3/contacts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        default_channel: Optional[str] | Omit = omit,
        opt_out: Optional[bool] | Omit = omit,
        sandbox: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactUpdateResponse:
        """
        Updates a contact's default channel and/or opt-out status.

        Args:
          default_channel: Default messaging channel: "sms" or "whatsapp"

          opt_out: Whether the contact has opted out of messaging. Single source of truth — opt-out
              is per-contact, not per-channel.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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
            path_template("/v3/contacts/{id}", id=id),
            body=maybe_transform(
                {
                    "default_channel": default_channel,
                    "opt_out": opt_out,
                    "sandbox": sandbox,
                },
                contact_update_params.ContactUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactUpdateResponse,
        )

    def list(
        self,
        *,
        page: int,
        page_size: int,
        channel: Optional[str] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        search: Optional[str] | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListResponse:
        """Retrieves a paginated list of contacts for the authenticated customer.

        Supports
        filtering by search term, channel, or phone number.

        Args:
          page: Page number (1-indexed)

          page_size: Number of items per page

          channel: Optional channel filter (sms, whatsapp)

          phone: Optional phone number filter (alternative to list view)

          search: Optional search term for filtering contacts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            "/v3/contacts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "channel": channel,
                        "phone": phone,
                        "search": search,
                    },
                    contact_list_params.ContactListParams,
                ),
            ),
            cast_to=ContactListResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def delete(
        self,
        id: str,
        *,
        sandbox: bool | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        **Deprecated.** Use `PATCH /v3/contacts/{id}` with `{"opt_out": true}` instead,
        and expect this to be removed in a future release. It still behaves exactly as
        before, so nothing needs to change today.

        Opting a contact out stops every send to them, which is what deleting one was
        mostly used for — and it keeps the record of who they were and that they asked.
        A delete discards the consent history along with the contact, which is the part
        you need if anyone ever asks why you stopped, or why you started again.

        Dissociates a contact from the authenticated customer.

        Args:
          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._delete(
            path_template("/v3/contacts/{id}", id=id),
            body=maybe_transform({"sandbox": sandbox}, contact_delete_params.ContactDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_message_summary(
        self,
        contact_id: str,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactRetrieveMessageSummaryResponse:
        """
        Returns aggregate message counts, time bounds, channels used, and per-channel
        success/fail scores (each as a percentage 0-100 of messages on that channel) for
        one of your contacts. Successful terminal states: SENT/DELIVERED/READ for
        outbound, RECEIVED for inbound. Fail: FAILED.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v3/contacts/{contact_id}/message-summary", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactRetrieveMessageSummaryResponse,
        )


class AsyncContactsResource(AsyncAPIResource):
    """The people you message, and their channel identities.

    A contact holds one identity per channel — a phone number, a WhatsApp number — so routing can choose between them for the same person. Opt-out is recorded against the contact and honoured on every send, whichever channel it came through.

    `GET /v3/contacts/{id}/message-summary` is the per-contact view of what you have sent and what happened to it.
    """

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

    async def create(
        self,
        *,
        phone_number: str,
        sandbox: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactCreateResponse:
        """
        Creates a new contact by phone number and associates it with the authenticated
        customer.

        Args:
          phone_number: Phone number of the contact to create

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
            "/v3/contacts",
            body=await async_maybe_transform(
                {
                    "phone_number": phone_number,
                    "sandbox": sandbox,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactRetrieveResponse:
        """Retrieves a specific contact by their unique identifier.

        Returns detailed
        contact information including phone formats, available channels, and opt-out
        status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v3/contacts/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        default_channel: Optional[str] | Omit = omit,
        opt_out: Optional[bool] | Omit = omit,
        sandbox: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactUpdateResponse:
        """
        Updates a contact's default channel and/or opt-out status.

        Args:
          default_channel: Default messaging channel: "sms" or "whatsapp"

          opt_out: Whether the contact has opted out of messaging. Single source of truth — opt-out
              is per-contact, not per-channel.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
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
            path_template("/v3/contacts/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "default_channel": default_channel,
                    "opt_out": opt_out,
                    "sandbox": sandbox,
                },
                contact_update_params.ContactUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactUpdateResponse,
        )

    async def list(
        self,
        *,
        page: int,
        page_size: int,
        channel: Optional[str] | Omit = omit,
        phone: Optional[str] | Omit = omit,
        search: Optional[str] | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListResponse:
        """Retrieves a paginated list of contacts for the authenticated customer.

        Supports
        filtering by search term, channel, or phone number.

        Args:
          page: Page number (1-indexed)

          page_size: Number of items per page

          channel: Optional channel filter (sms, whatsapp)

          phone: Optional phone number filter (alternative to list view)

          search: Optional search term for filtering contacts

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            "/v3/contacts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "channel": channel,
                        "phone": phone,
                        "search": search,
                    },
                    contact_list_params.ContactListParams,
                ),
            ),
            cast_to=ContactListResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def delete(
        self,
        id: str,
        *,
        sandbox: bool | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        **Deprecated.** Use `PATCH /v3/contacts/{id}` with `{"opt_out": true}` instead,
        and expect this to be removed in a future release. It still behaves exactly as
        before, so nothing needs to change today.

        Opting a contact out stops every send to them, which is what deleting one was
        mostly used for — and it keeps the record of who they were and that they asked.
        A delete discards the consent history along with the contact, which is the part
        you need if anyone ever asks why you stopped, or why you started again.

        Dissociates a contact from the authenticated customer.

        Args:
          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/contacts/{id}", id=id),
            body=await async_maybe_transform({"sandbox": sandbox}, contact_delete_params.ContactDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_message_summary(
        self,
        contact_id: str,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactRetrieveMessageSummaryResponse:
        """
        Returns aggregate message counts, time bounds, channels used, and per-channel
        success/fail scores (each as a percentage 0-100 of messages on that channel) for
        one of your contacts. Successful terminal states: SENT/DELIVERED/READ for
        outbound, RECEIVED for inbound. Fail: FAILED.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v3/contacts/{contact_id}/message-summary", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactRetrieveMessageSummaryResponse,
        )


class ContactsResourceWithRawResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.create = to_raw_response_wrapper(
            contacts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            contacts.update,
        )
        self.list = to_raw_response_wrapper(
            contacts.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                contacts.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve_message_summary = to_raw_response_wrapper(
            contacts.retrieve_message_summary,
        )


class AsyncContactsResourceWithRawResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.create = async_to_raw_response_wrapper(
            contacts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            contacts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            contacts.update,
        )
        self.list = async_to_raw_response_wrapper(
            contacts.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                contacts.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve_message_summary = async_to_raw_response_wrapper(
            contacts.retrieve_message_summary,
        )


class ContactsResourceWithStreamingResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.create = to_streamed_response_wrapper(
            contacts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            contacts.update,
        )
        self.list = to_streamed_response_wrapper(
            contacts.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                contacts.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve_message_summary = to_streamed_response_wrapper(
            contacts.retrieve_message_summary,
        )


class AsyncContactsResourceWithStreamingResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.create = async_to_streamed_response_wrapper(
            contacts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            contacts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            contacts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            contacts.list,
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                contacts.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve_message_summary = async_to_streamed_response_wrapper(
            contacts.retrieve_message_summary,
        )
