# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..types import message_send_to_phone_params, message_send_to_contact_params, message_send_quick_message_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.message_retrieve_response import MessageRetrieveResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        Retrieves comprehensive details about a specific message using the message ID.
        Returns complete message data including delivery status, channel information,
        template details, contact information, and pricing. The customer ID is extracted
        from the authentication token to ensure the message belongs to the authenticated
        customer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v2/messages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    def send_quick_message(
        self,
        *,
        custom_message: str,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Sends a message to a phone number using the default template.

        This endpoint is
        rate limited to 5 messages per customer per day. The customer ID is extracted
        from the authentication token.

        Args:
          custom_message: The custom message content to include in the template

          phone_number: The phone number to send the message to, in international format (e.g.,
              +1234567890)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v2/messages/quick-message",
            body=maybe_transform(
                {
                    "custom_message": custom_message,
                    "phone_number": phone_number,
                },
                message_send_quick_message_params.MessageSendQuickMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def send_to_contact(
        self,
        *,
        contact_id: str,
        template_id: str,
        template_variables: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Sends a message to a specific contact using a template.

        The message can be sent
        via SMS or WhatsApp depending on the contact's capabilities. Optionally specify
        a webhook URL to receive delivery status updates. The customer ID is extracted
        from the authentication token.

        Args:
          contact_id: The unique identifier of the contact to send the message to

          template_id: The unique identifier of the template to use for the message

          template_variables: Optional key-value pairs of template variables to replace in the template body.
              For example, if your template contains "Hello {{name}}", you would provide {
              "name": "John Doe" }

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v2/messages/contact",
            body=maybe_transform(
                {
                    "contact_id": contact_id,
                    "template_id": template_id,
                    "template_variables": template_variables,
                },
                message_send_to_contact_params.MessageSendToContactParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def send_to_phone(
        self,
        *,
        phone_number: str,
        template_id: str,
        template_variables: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Sends a message to a phone number using a template.

        The phone number doesn't
        need to be a pre-existing contact. The message can be sent via SMS or WhatsApp.
        Optionally specify a webhook URL to receive delivery status updates. The
        customer ID is extracted from the authentication token.

        Args:
          phone_number: The phone number to send the message to, in international format (e.g.,
              +1234567890)

          template_id: The unique identifier of the template to use for the message

          template_variables: Optional key-value pairs of template variables to replace in the template body.
              For example, if your template contains "Hello {{name}}", you would provide {
              "name": "John Doe" }

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v2/messages/phone",
            body=maybe_transform(
                {
                    "phone_number": phone_number,
                    "template_id": template_id,
                    "template_variables": template_variables,
                },
                message_send_to_phone_params.MessageSendToPhoneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        Retrieves comprehensive details about a specific message using the message ID.
        Returns complete message data including delivery status, channel information,
        template details, contact information, and pricing. The customer ID is extracted
        from the authentication token to ensure the message belongs to the authenticated
        customer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v2/messages/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    async def send_quick_message(
        self,
        *,
        custom_message: str,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Sends a message to a phone number using the default template.

        This endpoint is
        rate limited to 5 messages per customer per day. The customer ID is extracted
        from the authentication token.

        Args:
          custom_message: The custom message content to include in the template

          phone_number: The phone number to send the message to, in international format (e.g.,
              +1234567890)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v2/messages/quick-message",
            body=await async_maybe_transform(
                {
                    "custom_message": custom_message,
                    "phone_number": phone_number,
                },
                message_send_quick_message_params.MessageSendQuickMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def send_to_contact(
        self,
        *,
        contact_id: str,
        template_id: str,
        template_variables: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Sends a message to a specific contact using a template.

        The message can be sent
        via SMS or WhatsApp depending on the contact's capabilities. Optionally specify
        a webhook URL to receive delivery status updates. The customer ID is extracted
        from the authentication token.

        Args:
          contact_id: The unique identifier of the contact to send the message to

          template_id: The unique identifier of the template to use for the message

          template_variables: Optional key-value pairs of template variables to replace in the template body.
              For example, if your template contains "Hello {{name}}", you would provide {
              "name": "John Doe" }

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v2/messages/contact",
            body=await async_maybe_transform(
                {
                    "contact_id": contact_id,
                    "template_id": template_id,
                    "template_variables": template_variables,
                },
                message_send_to_contact_params.MessageSendToContactParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def send_to_phone(
        self,
        *,
        phone_number: str,
        template_id: str,
        template_variables: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Sends a message to a phone number using a template.

        The phone number doesn't
        need to be a pre-existing contact. The message can be sent via SMS or WhatsApp.
        Optionally specify a webhook URL to receive delivery status updates. The
        customer ID is extracted from the authentication token.

        Args:
          phone_number: The phone number to send the message to, in international format (e.g.,
              +1234567890)

          template_id: The unique identifier of the template to use for the message

          template_variables: Optional key-value pairs of template variables to replace in the template body.
              For example, if your template contains "Hello {{name}}", you would provide {
              "name": "John Doe" }

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v2/messages/phone",
            body=await async_maybe_transform(
                {
                    "phone_number": phone_number,
                    "template_id": template_id,
                    "template_variables": template_variables,
                },
                message_send_to_phone_params.MessageSendToPhoneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.send_quick_message = to_raw_response_wrapper(
            messages.send_quick_message,
        )
        self.send_to_contact = to_raw_response_wrapper(
            messages.send_to_contact,
        )
        self.send_to_phone = to_raw_response_wrapper(
            messages.send_to_phone,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.send_quick_message = async_to_raw_response_wrapper(
            messages.send_quick_message,
        )
        self.send_to_contact = async_to_raw_response_wrapper(
            messages.send_to_contact,
        )
        self.send_to_phone = async_to_raw_response_wrapper(
            messages.send_to_phone,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.send_quick_message = to_streamed_response_wrapper(
            messages.send_quick_message,
        )
        self.send_to_contact = to_streamed_response_wrapper(
            messages.send_to_contact,
        )
        self.send_to_phone = to_streamed_response_wrapper(
            messages.send_to_phone,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.send_quick_message = async_to_streamed_response_wrapper(
            messages.send_quick_message,
        )
        self.send_to_contact = async_to_streamed_response_wrapper(
            messages.send_to_contact,
        )
        self.send_to_phone = async_to_streamed_response_wrapper(
            messages.send_to_phone,
        )
