# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import SentDmError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import contacts, messages, templates, number_lookup, organizations
    from .resources.contacts import ContactsResource, AsyncContactsResource
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.templates import TemplatesResource, AsyncTemplatesResource
    from .resources.number_lookup import NumberLookupResource, AsyncNumberLookupResource
    from .resources.organizations.organizations import OrganizationsResource, AsyncOrganizationsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "SentDm", "AsyncSentDm", "Client", "AsyncClient"]


class SentDm(SyncAPIClient):
    # client options
    api_key: str
    sender_id: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        sender_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous SentDm client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `SENT_DM_API_KEY`
        - `sender_id` from `SENT_DM_SENDER_ID`
        """
        if api_key is None:
            api_key = os.environ.get("SENT_DM_API_KEY")
        if api_key is None:
            raise SentDmError(
                "The api_key client option must be set either by passing api_key to the client or by setting the SENT_DM_API_KEY environment variable"
            )
        self.api_key = api_key

        if sender_id is None:
            sender_id = os.environ.get("SENT_DM_SENDER_ID")
        if sender_id is None:
            raise SentDmError(
                "The sender_id client option must be set either by passing sender_id to the client or by setting the SENT_DM_SENDER_ID environment variable"
            )
        self.sender_id = sender_id

        if base_url is None:
            base_url = os.environ.get("SENT_DM_BASE_URL")
        if base_url is None:
            base_url = f"https://api.sent.dm"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def templates(self) -> TemplatesResource:
        from .resources.templates import TemplatesResource

        return TemplatesResource(self)

    @cached_property
    def contacts(self) -> ContactsResource:
        from .resources.contacts import ContactsResource

        return ContactsResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def number_lookup(self) -> NumberLookupResource:
        from .resources.number_lookup import NumberLookupResource

        return NumberLookupResource(self)

    @cached_property
    def organizations(self) -> OrganizationsResource:
        from .resources.organizations import OrganizationsResource

        return OrganizationsResource(self)

    @cached_property
    def with_raw_response(self) -> SentDmWithRawResponse:
        return SentDmWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SentDmWithStreamedResponse:
        return SentDmWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._customer_api_key, **self._customer_sender_id}

    @property
    def _customer_api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    def _customer_sender_id(self) -> dict[str, str]:
        sender_id = self.sender_id
        return {"x-sender-id": sender_id}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        sender_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            sender_id=sender_id or self.sender_id,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncSentDm(AsyncAPIClient):
    # client options
    api_key: str
    sender_id: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        sender_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncSentDm client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `SENT_DM_API_KEY`
        - `sender_id` from `SENT_DM_SENDER_ID`
        """
        if api_key is None:
            api_key = os.environ.get("SENT_DM_API_KEY")
        if api_key is None:
            raise SentDmError(
                "The api_key client option must be set either by passing api_key to the client or by setting the SENT_DM_API_KEY environment variable"
            )
        self.api_key = api_key

        if sender_id is None:
            sender_id = os.environ.get("SENT_DM_SENDER_ID")
        if sender_id is None:
            raise SentDmError(
                "The sender_id client option must be set either by passing sender_id to the client or by setting the SENT_DM_SENDER_ID environment variable"
            )
        self.sender_id = sender_id

        if base_url is None:
            base_url = os.environ.get("SENT_DM_BASE_URL")
        if base_url is None:
            base_url = f"https://api.sent.dm"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        from .resources.templates import AsyncTemplatesResource

        return AsyncTemplatesResource(self)

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        from .resources.contacts import AsyncContactsResource

        return AsyncContactsResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def number_lookup(self) -> AsyncNumberLookupResource:
        from .resources.number_lookup import AsyncNumberLookupResource

        return AsyncNumberLookupResource(self)

    @cached_property
    def organizations(self) -> AsyncOrganizationsResource:
        from .resources.organizations import AsyncOrganizationsResource

        return AsyncOrganizationsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncSentDmWithRawResponse:
        return AsyncSentDmWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSentDmWithStreamedResponse:
        return AsyncSentDmWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._customer_api_key, **self._customer_sender_id}

    @property
    def _customer_api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    def _customer_sender_id(self) -> dict[str, str]:
        sender_id = self.sender_id
        return {"x-sender-id": sender_id}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        sender_id: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            sender_id=sender_id or self.sender_id,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class SentDmWithRawResponse:
    _client: SentDm

    def __init__(self, client: SentDm) -> None:
        self._client = client

    @cached_property
    def templates(self) -> templates.TemplatesResourceWithRawResponse:
        from .resources.templates import TemplatesResourceWithRawResponse

        return TemplatesResourceWithRawResponse(self._client.templates)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithRawResponse:
        from .resources.contacts import ContactsResourceWithRawResponse

        return ContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def number_lookup(self) -> number_lookup.NumberLookupResourceWithRawResponse:
        from .resources.number_lookup import NumberLookupResourceWithRawResponse

        return NumberLookupResourceWithRawResponse(self._client.number_lookup)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithRawResponse:
        from .resources.organizations import OrganizationsResourceWithRawResponse

        return OrganizationsResourceWithRawResponse(self._client.organizations)


class AsyncSentDmWithRawResponse:
    _client: AsyncSentDm

    def __init__(self, client: AsyncSentDm) -> None:
        self._client = client

    @cached_property
    def templates(self) -> templates.AsyncTemplatesResourceWithRawResponse:
        from .resources.templates import AsyncTemplatesResourceWithRawResponse

        return AsyncTemplatesResourceWithRawResponse(self._client.templates)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithRawResponse:
        from .resources.contacts import AsyncContactsResourceWithRawResponse

        return AsyncContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def number_lookup(self) -> number_lookup.AsyncNumberLookupResourceWithRawResponse:
        from .resources.number_lookup import AsyncNumberLookupResourceWithRawResponse

        return AsyncNumberLookupResourceWithRawResponse(self._client.number_lookup)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithRawResponse:
        from .resources.organizations import AsyncOrganizationsResourceWithRawResponse

        return AsyncOrganizationsResourceWithRawResponse(self._client.organizations)


class SentDmWithStreamedResponse:
    _client: SentDm

    def __init__(self, client: SentDm) -> None:
        self._client = client

    @cached_property
    def templates(self) -> templates.TemplatesResourceWithStreamingResponse:
        from .resources.templates import TemplatesResourceWithStreamingResponse

        return TemplatesResourceWithStreamingResponse(self._client.templates)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithStreamingResponse:
        from .resources.contacts import ContactsResourceWithStreamingResponse

        return ContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def number_lookup(self) -> number_lookup.NumberLookupResourceWithStreamingResponse:
        from .resources.number_lookup import NumberLookupResourceWithStreamingResponse

        return NumberLookupResourceWithStreamingResponse(self._client.number_lookup)

    @cached_property
    def organizations(self) -> organizations.OrganizationsResourceWithStreamingResponse:
        from .resources.organizations import OrganizationsResourceWithStreamingResponse

        return OrganizationsResourceWithStreamingResponse(self._client.organizations)


class AsyncSentDmWithStreamedResponse:
    _client: AsyncSentDm

    def __init__(self, client: AsyncSentDm) -> None:
        self._client = client

    @cached_property
    def templates(self) -> templates.AsyncTemplatesResourceWithStreamingResponse:
        from .resources.templates import AsyncTemplatesResourceWithStreamingResponse

        return AsyncTemplatesResourceWithStreamingResponse(self._client.templates)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithStreamingResponse:
        from .resources.contacts import AsyncContactsResourceWithStreamingResponse

        return AsyncContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def number_lookup(self) -> number_lookup.AsyncNumberLookupResourceWithStreamingResponse:
        from .resources.number_lookup import AsyncNumberLookupResourceWithStreamingResponse

        return AsyncNumberLookupResourceWithStreamingResponse(self._client.number_lookup)

    @cached_property
    def organizations(self) -> organizations.AsyncOrganizationsResourceWithStreamingResponse:
        from .resources.organizations import AsyncOrganizationsResourceWithStreamingResponse

        return AsyncOrganizationsResourceWithStreamingResponse(self._client.organizations)


Client = SentDm

AsyncClient = AsyncSentDm
