# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import template_list_params, template_create_params
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
from ..types.template_response import TemplateResponse
from ..types.template_list_response import TemplateListResponse
from ..types.template_definition_param import TemplateDefinitionParam

__all__ = ["TemplatesResource", "AsyncTemplatesResource"]


class TemplatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return TemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return TemplatesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        definition: TemplateDefinitionParam,
        category: Optional[str] | Omit = omit,
        language: Optional[str] | Omit = omit,
        submit_for_review: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateResponse:
        """
        Creates a new message template for the authenticated customer with comprehensive
        template definitions including headers, body, footer, and interactive buttons.
        Supports automatic metadata generation using AI (display name, language,
        category). Optionally submits the template for WhatsApp review. The customer ID
        is extracted from the authentication token.

        Args:
          definition: Template definition containing header, body, footer, and buttons

          category: The template category (e.g., MARKETING, UTILITY, AUTHENTICATION). Can only be
              set when creating a new template. If not provided, will be auto-generated using
              AI.

          language: The template language code (e.g., en_US, es_ES). Can only be set when creating a
              new template. If not provided, will be auto-detected using AI.

          submit_for_review: When false, the template will be saved as draft. When true, the template will be
              submitted for review.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/templates",
            body=maybe_transform(
                {
                    "definition": definition,
                    "category": category,
                    "language": language,
                    "submit_for_review": submit_for_review,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateResponse,
        )

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
    ) -> TemplateResponse:
        """
        Retrieves a specific message template by its unique identifier for the
        authenticated customer with comprehensive template definitions including
        headers, body, footer, and interactive buttons. The customer ID is extracted
        from the authentication token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v2/templates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateResponse,
        )

    def list(
        self,
        *,
        page: int,
        page_size: int,
        category: Optional[str] | Omit = omit,
        search: Optional[str] | Omit = omit,
        status: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateListResponse:
        """
        Retrieves all message templates available for the authenticated customer with
        comprehensive template definitions including headers, body, footer, and
        interactive buttons. Supports advanced filtering by search term, status, and
        category, plus pagination. The customer ID is extracted from the authentication
        token.

        Args:
          page: The page number (zero-indexed). Default is 0.

          page_size: The number of items per page (1-1000). Default is 100.

          category: Optional filter by template category (e.g., MARKETING, UTILITY, AUTHENTICATION)

          search: Optional search term to filter templates by name or content

          status: Optional filter by template status (e.g., APPROVED, PENDING, REJECTED, DRAFT)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "category": category,
                        "search": search,
                        "status": status,
                    },
                    template_list_params.TemplateListParams,
                ),
            ),
            cast_to=TemplateListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a specific message template by its unique identifier for the
        authenticated customer with smart deletion strategy. Deletion behavior: - If
        template has NO messages: Permanently deleted from database (hard delete). - If
        template has messages: Marked as deleted but preserved for message history (soft
        delete with snapshot). The template must exist and belong to the authenticated
        customer to be deleted successfully. The customer ID is extracted from the
        authentication token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/templates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTemplatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncTemplatesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        definition: TemplateDefinitionParam,
        category: Optional[str] | Omit = omit,
        language: Optional[str] | Omit = omit,
        submit_for_review: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateResponse:
        """
        Creates a new message template for the authenticated customer with comprehensive
        template definitions including headers, body, footer, and interactive buttons.
        Supports automatic metadata generation using AI (display name, language,
        category). Optionally submits the template for WhatsApp review. The customer ID
        is extracted from the authentication token.

        Args:
          definition: Template definition containing header, body, footer, and buttons

          category: The template category (e.g., MARKETING, UTILITY, AUTHENTICATION). Can only be
              set when creating a new template. If not provided, will be auto-generated using
              AI.

          language: The template language code (e.g., en_US, es_ES). Can only be set when creating a
              new template. If not provided, will be auto-detected using AI.

          submit_for_review: When false, the template will be saved as draft. When true, the template will be
              submitted for review.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/templates",
            body=await async_maybe_transform(
                {
                    "definition": definition,
                    "category": category,
                    "language": language,
                    "submit_for_review": submit_for_review,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateResponse,
        )

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
    ) -> TemplateResponse:
        """
        Retrieves a specific message template by its unique identifier for the
        authenticated customer with comprehensive template definitions including
        headers, body, footer, and interactive buttons. The customer ID is extracted
        from the authentication token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v2/templates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TemplateResponse,
        )

    async def list(
        self,
        *,
        page: int,
        page_size: int,
        category: Optional[str] | Omit = omit,
        search: Optional[str] | Omit = omit,
        status: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TemplateListResponse:
        """
        Retrieves all message templates available for the authenticated customer with
        comprehensive template definitions including headers, body, footer, and
        interactive buttons. Supports advanced filtering by search term, status, and
        category, plus pagination. The customer ID is extracted from the authentication
        token.

        Args:
          page: The page number (zero-indexed). Default is 0.

          page_size: The number of items per page (1-1000). Default is 100.

          category: Optional filter by template category (e.g., MARKETING, UTILITY, AUTHENTICATION)

          search: Optional search term to filter templates by name or content

          status: Optional filter by template status (e.g., APPROVED, PENDING, REJECTED, DRAFT)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/templates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                        "category": category,
                        "search": search,
                        "status": status,
                    },
                    template_list_params.TemplateListParams,
                ),
            ),
            cast_to=TemplateListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a specific message template by its unique identifier for the
        authenticated customer with smart deletion strategy. Deletion behavior: - If
        template has NO messages: Permanently deleted from database (hard delete). - If
        template has messages: Marked as deleted but preserved for message history (soft
        delete with snapshot). The template must exist and belong to the authenticated
        customer to be deleted successfully. The customer ID is extracted from the
        authentication token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/templates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TemplatesResourceWithRawResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.create = to_raw_response_wrapper(
            templates.create,
        )
        self.retrieve = to_raw_response_wrapper(
            templates.retrieve,
        )
        self.list = to_raw_response_wrapper(
            templates.list,
        )
        self.delete = to_raw_response_wrapper(
            templates.delete,
        )


class AsyncTemplatesResourceWithRawResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.create = async_to_raw_response_wrapper(
            templates.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            templates.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            templates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            templates.delete,
        )


class TemplatesResourceWithStreamingResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.create = to_streamed_response_wrapper(
            templates.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            templates.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            templates.list,
        )
        self.delete = to_streamed_response_wrapper(
            templates.delete,
        )


class AsyncTemplatesResourceWithStreamingResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.create = async_to_streamed_response_wrapper(
            templates.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            templates.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            templates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            templates.delete,
        )
