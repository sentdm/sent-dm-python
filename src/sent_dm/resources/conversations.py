# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import conversation_list_params, conversation_list_messages_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.api_response_of_conversation_messages_list import APIResponseOfConversationMessagesList

__all__ = ["ConversationsResource", "AsyncConversationsResource"]


class ConversationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return ConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return ConversationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        page: int,
        page_size: int,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfConversationMessagesList:
        """
        Retrieves a paginated list of the authenticated customer's messages across all
        conversations, ordered by created date (most recent first).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            "/v3/conversations",
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
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=APIResponseOfConversationMessagesList,
        )

    def list_messages(
        self,
        id: str,
        *,
        page: int,
        page_size: int,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfConversationMessagesList:
        """
        Retrieves a paginated list of the messages in a single conversation (scoped to
        the authenticated customer), ordered by created date (most recent first).

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
            path_template("/v3/conversations/{id}", id=id),
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
                    conversation_list_messages_params.ConversationListMessagesParams,
                ),
            ),
            cast_to=APIResponseOfConversationMessagesList,
        )


class AsyncConversationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConversationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncConversationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        page: int,
        page_size: int,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfConversationMessagesList:
        """
        Retrieves a paginated list of the authenticated customer's messages across all
        conversations, ordered by created date (most recent first).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            "/v3/conversations",
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
                    conversation_list_params.ConversationListParams,
                ),
            ),
            cast_to=APIResponseOfConversationMessagesList,
        )

    async def list_messages(
        self,
        id: str,
        *,
        page: int,
        page_size: int,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfConversationMessagesList:
        """
        Retrieves a paginated list of the messages in a single conversation (scoped to
        the authenticated customer), ordered by created date (most recent first).

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
            path_template("/v3/conversations/{id}", id=id),
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
                    conversation_list_messages_params.ConversationListMessagesParams,
                ),
            ),
            cast_to=APIResponseOfConversationMessagesList,
        )


class ConversationsResourceWithRawResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.list = to_raw_response_wrapper(
            conversations.list,
        )
        self.list_messages = to_raw_response_wrapper(
            conversations.list_messages,
        )


class AsyncConversationsResourceWithRawResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.list = async_to_raw_response_wrapper(
            conversations.list,
        )
        self.list_messages = async_to_raw_response_wrapper(
            conversations.list_messages,
        )


class ConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: ConversationsResource) -> None:
        self._conversations = conversations

        self.list = to_streamed_response_wrapper(
            conversations.list,
        )
        self.list_messages = to_streamed_response_wrapper(
            conversations.list_messages,
        )


class AsyncConversationsResourceWithStreamingResponse:
    def __init__(self, conversations: AsyncConversationsResource) -> None:
        self._conversations = conversations

        self.list = async_to_streamed_response_wrapper(
            conversations.list,
        )
        self.list_messages = async_to_streamed_response_wrapper(
            conversations.list_messages,
        )
