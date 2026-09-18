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
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncTemplatesPage, AsyncTemplatesPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.template import Template
from ..types.api_response_template import APIResponseTemplate
from ..types.template_definition_param import TemplateDefinitionParam

__all__ = ["TemplatesResource", "AsyncTemplatesResource"]


class TemplatesResource(SyncAPIResource):
    """Reusable message bodies with named variables.

    A template is substituted at send time from the values you pass, so the copy lives here rather than in your application. WhatsApp templates additionally need Meta's approval before they can be sent, and a template's channel status reports where that stands — an approved SMS template and an unapproved WhatsApp one are the same template in two states.
    """

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
        sandbox: bool | Omit = omit,
        submit_for_review: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
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
        submission. There is no `name` field on create — the display name is derived
        from the template's content and can be changed afterwards with
        `PUT /v3/templates/{id}`.

        Args:
          category: Template category: MARKETING, UTILITY, AUTHENTICATION (optional, auto-detected
              if not provided)

          creation_source: Source of template creation (default: from-api)

          definition: Complete definition of a message template including header, body, footer, and
              buttons

          language: Template language code (e.g., en_US) (optional, auto-detected if not provided)

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          submit_for_review: Whether to submit the template for review after creation (default: false)

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
            "/v3/templates",
            body=maybe_transform(
                {
                    "category": category,
                    "creation_source": creation_source,
                    "definition": definition,
                    "language": language,
                    "sandbox": sandbox,
                    "submit_for_review": submit_for_review,
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
        x_profile_id: str | Omit = omit,
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
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v3/templates/{id}", id=id),
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
        sandbox: bool | Omit = omit,
        submit_for_review: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseTemplate:
        """
        Updates an existing template's name, category, language, definition, or submits
        it for review. While the template is in review (status PENDING, or any channel
        awaiting a verdict) its definition, category and language are frozen and a
        resubmission is refused — those requests answer 409 CONFLICT_006. The display
        name stays editable throughout.

        `definition`, `category` and `language` are editable only from status DRAFT,
        REJECTED or APPROVED. An edit to any of them on a template in another state
        (PAUSED, DISABLED or REVOKED) is refused with 400 VALIDATION_001 and the detail
        "Template (except display name) cannot be updated unless it is in draft or
        rejected status"; `name` stays editable in every state. `submit_for_review` on a
        PAUSED, DISABLED or REVOKED template is accepted and answers 200, but opens no
        review and does not move the status — only the reviewer can reinstate it.

        Editing an APPROVED template is a live edit: the new content is stored
        immediately, and sending `submit_for_review: true` re-opens review, which
        returns the affected channels to PENDING so they stop sending until they are
        approved again. The previously approved content is never sent during re-review.
        Watch the per-channel `templates` webhook events rather than assuming the
        template-level status.

        Templates provisioned by Sent (light-onboarding templates, whose names carry the
        reserved `sent_` prefix) are read-only: every field is refused with 400
        VALIDATION*001 and the detail "This template is read-only. Only 'submit for
        review' is allowed.", and only `submit_for_review` is accepted. A `name`
        starting with `sent*` is refused for the same reason — the prefix is reserved.

        Args:
          category: Template category: MARKETING, UTILITY, AUTHENTICATION

          definition: Complete definition of a message template including header, body, footer, and
              buttons

          language: Template language code (e.g., en_US)

          name: Template display name

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          submit_for_review: Whether to submit the template for review after updating (default: false)

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
        return self._put(
            path_template("/v3/templates/{id}", id=id),
            body=maybe_transform(
                {
                    "category": category,
                    "definition": definition,
                    "language": language,
                    "name": name,
                    "sandbox": sandbox,
                    "submit_for_review": submit_for_review,
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
        category: Optional[str] | Omit = omit,
        is_welcome_playground: Optional[bool] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: Optional[str] | Omit = omit,
        status: Optional[str] | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncTemplatesPage[Template]:
        """
        Retrieves a paginated list of message templates for the authenticated customer.
        Supports filtering by status, category, and search term.

        Args:
          category: Optional category filter: MARKETING, UTILITY, AUTHENTICATION

          is_welcome_playground: Accepted and ignored. It used to filter on the welcome-playground marker inside
              a template's LOB details; that filter is gone and nothing reads this value, so
              sending it neither narrows nor widens the result. Retained only so a client
              still passing is_welcome_playground keeps binding instead of the request shape
              changing under it.

          page: Page number (1-indexed)

          page_size: Number of items per page

          search: Optional search term for filtering templates

          status: Optional status filter: APPROVED, PENDING, REJECTED

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get_api_list(
            "/v3/templates",
            page=SyncTemplatesPage[Template],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "is_welcome_playground": is_welcome_playground,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                        "status": status,
                    },
                    template_list_params.TemplateListParams,
                ),
            ),
            model=Template,
        )

    def delete(
        self,
        id: str,
        *,
        delete_from_meta: Optional[bool] | Omit = omit,
        sandbox: bool | Omit = omit,
        x_profile_id: str | Omit = omit,
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
            path_template("/v3/templates/{id}", id=id),
            body=maybe_transform(
                {
                    "delete_from_meta": delete_from_meta,
                    "sandbox": sandbox,
                },
                template_delete_params.TemplateDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTemplatesResource(AsyncAPIResource):
    """Reusable message bodies with named variables.

    A template is substituted at send time from the values you pass, so the copy lives here rather than in your application. WhatsApp templates additionally need Meta's approval before they can be sent, and a template's channel status reports where that stands — an approved SMS template and an unapproved WhatsApp one are the same template in two states.
    """

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
        sandbox: bool | Omit = omit,
        submit_for_review: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
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
        submission. There is no `name` field on create — the display name is derived
        from the template's content and can be changed afterwards with
        `PUT /v3/templates/{id}`.

        Args:
          category: Template category: MARKETING, UTILITY, AUTHENTICATION (optional, auto-detected
              if not provided)

          creation_source: Source of template creation (default: from-api)

          definition: Complete definition of a message template including header, body, footer, and
              buttons

          language: Template language code (e.g., en_US) (optional, auto-detected if not provided)

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          submit_for_review: Whether to submit the template for review after creation (default: false)

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
            "/v3/templates",
            body=await async_maybe_transform(
                {
                    "category": category,
                    "creation_source": creation_source,
                    "definition": definition,
                    "language": language,
                    "sandbox": sandbox,
                    "submit_for_review": submit_for_review,
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
        x_profile_id: str | Omit = omit,
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
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v3/templates/{id}", id=id),
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
        sandbox: bool | Omit = omit,
        submit_for_review: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseTemplate:
        """
        Updates an existing template's name, category, language, definition, or submits
        it for review. While the template is in review (status PENDING, or any channel
        awaiting a verdict) its definition, category and language are frozen and a
        resubmission is refused — those requests answer 409 CONFLICT_006. The display
        name stays editable throughout.

        `definition`, `category` and `language` are editable only from status DRAFT,
        REJECTED or APPROVED. An edit to any of them on a template in another state
        (PAUSED, DISABLED or REVOKED) is refused with 400 VALIDATION_001 and the detail
        "Template (except display name) cannot be updated unless it is in draft or
        rejected status"; `name` stays editable in every state. `submit_for_review` on a
        PAUSED, DISABLED or REVOKED template is accepted and answers 200, but opens no
        review and does not move the status — only the reviewer can reinstate it.

        Editing an APPROVED template is a live edit: the new content is stored
        immediately, and sending `submit_for_review: true` re-opens review, which
        returns the affected channels to PENDING so they stop sending until they are
        approved again. The previously approved content is never sent during re-review.
        Watch the per-channel `templates` webhook events rather than assuming the
        template-level status.

        Templates provisioned by Sent (light-onboarding templates, whose names carry the
        reserved `sent_` prefix) are read-only: every field is refused with 400
        VALIDATION*001 and the detail "This template is read-only. Only 'submit for
        review' is allowed.", and only `submit_for_review` is accepted. A `name`
        starting with `sent*` is refused for the same reason — the prefix is reserved.

        Args:
          category: Template category: MARKETING, UTILITY, AUTHENTICATION

          definition: Complete definition of a message template including header, body, footer, and
              buttons

          language: Template language code (e.g., en_US)

          name: Template display name

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          submit_for_review: Whether to submit the template for review after updating (default: false)

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
        return await self._put(
            path_template("/v3/templates/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "category": category,
                    "definition": definition,
                    "language": language,
                    "name": name,
                    "sandbox": sandbox,
                    "submit_for_review": submit_for_review,
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
        category: Optional[str] | Omit = omit,
        is_welcome_playground: Optional[bool] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        search: Optional[str] | Omit = omit,
        status: Optional[str] | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Template, AsyncTemplatesPage[Template]]:
        """
        Retrieves a paginated list of message templates for the authenticated customer.
        Supports filtering by status, category, and search term.

        Args:
          category: Optional category filter: MARKETING, UTILITY, AUTHENTICATION

          is_welcome_playground: Accepted and ignored. It used to filter on the welcome-playground marker inside
              a template's LOB details; that filter is gone and nothing reads this value, so
              sending it neither narrows nor widens the result. Retained only so a client
              still passing is_welcome_playground keeps binding instead of the request shape
              changing under it.

          page: Page number (1-indexed)

          page_size: Number of items per page

          search: Optional search term for filtering templates

          status: Optional status filter: APPROVED, PENDING, REJECTED

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get_api_list(
            "/v3/templates",
            page=AsyncTemplatesPage[Template],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "is_welcome_playground": is_welcome_playground,
                        "page": page,
                        "page_size": page_size,
                        "search": search,
                        "status": status,
                    },
                    template_list_params.TemplateListParams,
                ),
            ),
            model=Template,
        )

    async def delete(
        self,
        id: str,
        *,
        delete_from_meta: Optional[bool] | Omit = omit,
        sandbox: bool | Omit = omit,
        x_profile_id: str | Omit = omit,
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
            path_template("/v3/templates/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "delete_from_meta": delete_from_meta,
                    "sandbox": sandbox,
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
