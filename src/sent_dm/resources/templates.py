# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    template_list_params,
    template_create_params,
    template_delete_params,
    template_update_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.api_response_template import APIResponseTemplate
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
        category: Optional[str] | Omit = omit,
        creation_source: Optional[str] | Omit = omit,
        definition: TemplateDefinitionParam | Omit = omit,
        language: Optional[str] | Omit = omit,
        submit_for_review: bool | Omit = omit,
        test_mode: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseTemplate:
        """Creates a new message template with header, body, footer, and buttons.

        The
        template can be submitted for review immediately or saved as draft for later
        submission.

        Args:
          category: Template category: MARKETING, UTILITY, AUTHENTICATION (optional, auto-detected
              if not provided)

          creation_source: Source of template creation (default: from-api)

          definition: Template definition including header, body, footer, and buttons

          language: Template language code (e.g., en_US) (optional, auto-detected if not provided)

          submit_for_review: Whether to submit the template for review after creation (default: false)

          test_mode: Test mode flag - when true, the operation is simulated without side effects
              Useful for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/v3/templates",
            body=maybe_transform(
                {
                    "category": category,
                    "creation_source": creation_source,
                    "definition": definition,
                    "language": language,
                    "submit_for_review": submit_for_review,
                    "test_mode": test_mode,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseTemplate,
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
    ) -> APIResponseTemplate:
        """Retrieves a specific template by its ID.

        Returns template details including
        name, category, language, status, and definition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v3/templates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseTemplate,
        )

    def update(
        self,
        id: str,
        *,
        category: Optional[str] | Omit = omit,
        definition: Optional[TemplateDefinitionParam] | Omit = omit,
        language: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        submit_for_review: bool | Omit = omit,
        test_mode: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseTemplate:
        """
        Updates an existing template's name, category, language, definition, or submits
        it for review.

        Args:
          category: Template category: MARKETING, UTILITY, AUTHENTICATION

          definition: Template definition including header, body, footer, and buttons

          language: Template language code (e.g., en_US)

          name: Template display name

          submit_for_review: Whether to submit the template for review after updating (default: false)

          test_mode: Test mode flag - when true, the operation is simulated without side effects
              Useful for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._put(
            f"/v3/templates/{id}",
            body=maybe_transform(
                {
                    "category": category,
                    "definition": definition,
                    "language": language,
                    "name": name,
                    "submit_for_review": submit_for_review,
                    "test_mode": test_mode,
                },
                template_update_params.TemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseTemplate,
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
        Retrieves a paginated list of message templates for the authenticated customer.
        Supports filtering by status, category, and search term.

        Args:
          page: Page number (1-indexed)

          category: Optional category filter: MARKETING, UTILITY, AUTHENTICATION

          search: Optional search term for filtering templates

          status: Optional status filter: APPROVED, PENDING, REJECTED

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v3/templates",
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
        delete_from_meta: Optional[bool] | Omit = omit,
        test_mode: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a template by ID.

        Optionally, you can also delete the template from
        WhatsApp/Meta by setting delete_from_meta=true.

        Args:
          delete_from_meta: Whether to also delete the template from WhatsApp/Meta (optional, defaults to
              false)

          test_mode: Test mode flag - when true, the operation is simulated without side effects
              Useful for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v3/templates/{id}",
            body=maybe_transform(
                {
                    "delete_from_meta": delete_from_meta,
                    "test_mode": test_mode,
                },
                template_delete_params.TemplateDeleteParams,
            ),
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
        category: Optional[str] | Omit = omit,
        creation_source: Optional[str] | Omit = omit,
        definition: TemplateDefinitionParam | Omit = omit,
        language: Optional[str] | Omit = omit,
        submit_for_review: bool | Omit = omit,
        test_mode: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseTemplate:
        """Creates a new message template with header, body, footer, and buttons.

        The
        template can be submitted for review immediately or saved as draft for later
        submission.

        Args:
          category: Template category: MARKETING, UTILITY, AUTHENTICATION (optional, auto-detected
              if not provided)

          creation_source: Source of template creation (default: from-api)

          definition: Template definition including header, body, footer, and buttons

          language: Template language code (e.g., en_US) (optional, auto-detected if not provided)

          submit_for_review: Whether to submit the template for review after creation (default: false)

          test_mode: Test mode flag - when true, the operation is simulated without side effects
              Useful for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/v3/templates",
            body=await async_maybe_transform(
                {
                    "category": category,
                    "creation_source": creation_source,
                    "definition": definition,
                    "language": language,
                    "submit_for_review": submit_for_review,
                    "test_mode": test_mode,
                },
                template_create_params.TemplateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseTemplate,
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
    ) -> APIResponseTemplate:
        """Retrieves a specific template by its ID.

        Returns template details including
        name, category, language, status, and definition.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v3/templates/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseTemplate,
        )

    async def update(
        self,
        id: str,
        *,
        category: Optional[str] | Omit = omit,
        definition: Optional[TemplateDefinitionParam] | Omit = omit,
        language: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        submit_for_review: bool | Omit = omit,
        test_mode: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseTemplate:
        """
        Updates an existing template's name, category, language, definition, or submits
        it for review.

        Args:
          category: Template category: MARKETING, UTILITY, AUTHENTICATION

          definition: Template definition including header, body, footer, and buttons

          language: Template language code (e.g., en_US)

          name: Template display name

          submit_for_review: Whether to submit the template for review after updating (default: false)

          test_mode: Test mode flag - when true, the operation is simulated without side effects
              Useful for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._put(
            f"/v3/templates/{id}",
            body=await async_maybe_transform(
                {
                    "category": category,
                    "definition": definition,
                    "language": language,
                    "name": name,
                    "submit_for_review": submit_for_review,
                    "test_mode": test_mode,
                },
                template_update_params.TemplateUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseTemplate,
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
        Retrieves a paginated list of message templates for the authenticated customer.
        Supports filtering by status, category, and search term.

        Args:
          page: Page number (1-indexed)

          category: Optional category filter: MARKETING, UTILITY, AUTHENTICATION

          search: Optional search term for filtering templates

          status: Optional status filter: APPROVED, PENDING, REJECTED

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v3/templates",
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
        delete_from_meta: Optional[bool] | Omit = omit,
        test_mode: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a template by ID.

        Optionally, you can also delete the template from
        WhatsApp/Meta by setting delete_from_meta=true.

        Args:
          delete_from_meta: Whether to also delete the template from WhatsApp/Meta (optional, defaults to
              false)

          test_mode: Test mode flag - when true, the operation is simulated without side effects
              Useful for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v3/templates/{id}",
            body=await async_maybe_transform(
                {
                    "delete_from_meta": delete_from_meta,
                    "test_mode": test_mode,
                },
                template_delete_params.TemplateDeleteParams,
            ),
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
        self.update = to_raw_response_wrapper(
            templates.update,
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
        self.update = async_to_raw_response_wrapper(
            templates.update,
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
        self.update = to_streamed_response_wrapper(
            templates.update,
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
        self.update = async_to_streamed_response_wrapper(
            templates.update,
        )
        self.list = async_to_streamed_response_wrapper(
            templates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            templates.delete,
        )
