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
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import SentDmError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import me, users, brands, lookup, contacts, messages, profiles, webhooks, templates
    from .resources.me import MeResource, AsyncMeResource
    from .resources.users import UsersResource, AsyncUsersResource
    from .resources.lookup import LookupResource, AsyncLookupResource
    from .resources.contacts import ContactsResource, AsyncContactsResource
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.profiles import ProfilesResource, AsyncProfilesResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.templates import TemplatesResource, AsyncTemplatesResource
    from .resources.brands.brands import BrandsResource, AsyncBrandsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "SentDm", "AsyncSentDm", "Client", "AsyncClient"]


class SentDm(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
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

        This automatically infers the `api_key` argument from the `SENT_DM_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("SENT_DM_API_KEY")
        if api_key is None:
            raise SentDmError(
                "The api_key client option must be set either by passing api_key to the client or by setting the SENT_DM_API_KEY environment variable"
            )
        self.api_key = api_key

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
    def webhooks(self) -> WebhooksResource:
        """Configure webhook endpoints for real-time event delivery"""
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def users(self) -> UsersResource:
        """Invite, update, and manage organization users and roles"""
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def templates(self) -> TemplatesResource:
        """Manage message templates with variable substitution"""
        from .resources.templates import TemplatesResource

        return TemplatesResource(self)

    @cached_property
    def profiles(self) -> ProfilesResource:
        """Manage organization profiles"""
        from .resources.profiles import ProfilesResource

        return ProfilesResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        """Send and track SMS and WhatsApp messages"""
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def lookup(self) -> LookupResource:
        from .resources.lookup import LookupResource

        return LookupResource(self)

    @cached_property
    def contacts(self) -> ContactsResource:
        """Create, update, and manage customer contact lists"""
        from .resources.contacts import ContactsResource

        return ContactsResource(self)

    @cached_property
    def brands(self) -> BrandsResource:
        """Register and manage 10DLC brands for SMS compliance"""
        from .resources.brands import BrandsResource

        return BrandsResource(self)

    @cached_property
    def me(self) -> MeResource:
        """Retrieve account details"""
        from .resources.me import MeResource

        return MeResource(self)

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

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._customer_api_key if security.get("customer_api_key", False) else {}),
        }

    @property
    def _customer_api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

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

    def __init__(
        self,
        *,
        api_key: str | None = None,
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

        This automatically infers the `api_key` argument from the `SENT_DM_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("SENT_DM_API_KEY")
        if api_key is None:
            raise SentDmError(
                "The api_key client option must be set either by passing api_key to the client or by setting the SENT_DM_API_KEY environment variable"
            )
        self.api_key = api_key

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
    def webhooks(self) -> AsyncWebhooksResource:
        """Configure webhook endpoints for real-time event delivery"""
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        """Invite, update, and manage organization users and roles"""
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        """Manage message templates with variable substitution"""
        from .resources.templates import AsyncTemplatesResource

        return AsyncTemplatesResource(self)

    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        """Manage organization profiles"""
        from .resources.profiles import AsyncProfilesResource

        return AsyncProfilesResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        """Send and track SMS and WhatsApp messages"""
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def lookup(self) -> AsyncLookupResource:
        from .resources.lookup import AsyncLookupResource

        return AsyncLookupResource(self)

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        """Create, update, and manage customer contact lists"""
        from .resources.contacts import AsyncContactsResource

        return AsyncContactsResource(self)

    @cached_property
    def brands(self) -> AsyncBrandsResource:
        """Register and manage 10DLC brands for SMS compliance"""
        from .resources.brands import AsyncBrandsResource

        return AsyncBrandsResource(self)

    @cached_property
    def me(self) -> AsyncMeResource:
        """Retrieve account details"""
        from .resources.me import AsyncMeResource

        return AsyncMeResource(self)

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

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._customer_api_key if security.get("customer_api_key", False) else {}),
        }

    @property
    def _customer_api_key(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

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
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        """Configure webhook endpoints for real-time event delivery"""
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        """Invite, update, and manage organization users and roles"""
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def templates(self) -> templates.TemplatesResourceWithRawResponse:
        """Manage message templates with variable substitution"""
        from .resources.templates import TemplatesResourceWithRawResponse

        return TemplatesResourceWithRawResponse(self._client.templates)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithRawResponse:
        """Manage organization profiles"""
        from .resources.profiles import ProfilesResourceWithRawResponse

        return ProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        """Send and track SMS and WhatsApp messages"""
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def lookup(self) -> lookup.LookupResourceWithRawResponse:
        from .resources.lookup import LookupResourceWithRawResponse

        return LookupResourceWithRawResponse(self._client.lookup)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithRawResponse:
        """Create, update, and manage customer contact lists"""
        from .resources.contacts import ContactsResourceWithRawResponse

        return ContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def brands(self) -> brands.BrandsResourceWithRawResponse:
        """Register and manage 10DLC brands for SMS compliance"""
        from .resources.brands import BrandsResourceWithRawResponse

        return BrandsResourceWithRawResponse(self._client.brands)

    @cached_property
    def me(self) -> me.MeResourceWithRawResponse:
        """Retrieve account details"""
        from .resources.me import MeResourceWithRawResponse

        return MeResourceWithRawResponse(self._client.me)


class AsyncSentDmWithRawResponse:
    _client: AsyncSentDm

    def __init__(self, client: AsyncSentDm) -> None:
        self._client = client

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        """Configure webhook endpoints for real-time event delivery"""
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        """Invite, update, and manage organization users and roles"""
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def templates(self) -> templates.AsyncTemplatesResourceWithRawResponse:
        """Manage message templates with variable substitution"""
        from .resources.templates import AsyncTemplatesResourceWithRawResponse

        return AsyncTemplatesResourceWithRawResponse(self._client.templates)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithRawResponse:
        """Manage organization profiles"""
        from .resources.profiles import AsyncProfilesResourceWithRawResponse

        return AsyncProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        """Send and track SMS and WhatsApp messages"""
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def lookup(self) -> lookup.AsyncLookupResourceWithRawResponse:
        from .resources.lookup import AsyncLookupResourceWithRawResponse

        return AsyncLookupResourceWithRawResponse(self._client.lookup)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithRawResponse:
        """Create, update, and manage customer contact lists"""
        from .resources.contacts import AsyncContactsResourceWithRawResponse

        return AsyncContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def brands(self) -> brands.AsyncBrandsResourceWithRawResponse:
        """Register and manage 10DLC brands for SMS compliance"""
        from .resources.brands import AsyncBrandsResourceWithRawResponse

        return AsyncBrandsResourceWithRawResponse(self._client.brands)

    @cached_property
    def me(self) -> me.AsyncMeResourceWithRawResponse:
        """Retrieve account details"""
        from .resources.me import AsyncMeResourceWithRawResponse

        return AsyncMeResourceWithRawResponse(self._client.me)


class SentDmWithStreamedResponse:
    _client: SentDm

    def __init__(self, client: SentDm) -> None:
        self._client = client

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        """Configure webhook endpoints for real-time event delivery"""
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        """Invite, update, and manage organization users and roles"""
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def templates(self) -> templates.TemplatesResourceWithStreamingResponse:
        """Manage message templates with variable substitution"""
        from .resources.templates import TemplatesResourceWithStreamingResponse

        return TemplatesResourceWithStreamingResponse(self._client.templates)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithStreamingResponse:
        """Manage organization profiles"""
        from .resources.profiles import ProfilesResourceWithStreamingResponse

        return ProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        """Send and track SMS and WhatsApp messages"""
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def lookup(self) -> lookup.LookupResourceWithStreamingResponse:
        from .resources.lookup import LookupResourceWithStreamingResponse

        return LookupResourceWithStreamingResponse(self._client.lookup)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithStreamingResponse:
        """Create, update, and manage customer contact lists"""
        from .resources.contacts import ContactsResourceWithStreamingResponse

        return ContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def brands(self) -> brands.BrandsResourceWithStreamingResponse:
        """Register and manage 10DLC brands for SMS compliance"""
        from .resources.brands import BrandsResourceWithStreamingResponse

        return BrandsResourceWithStreamingResponse(self._client.brands)

    @cached_property
    def me(self) -> me.MeResourceWithStreamingResponse:
        """Retrieve account details"""
        from .resources.me import MeResourceWithStreamingResponse

        return MeResourceWithStreamingResponse(self._client.me)


class AsyncSentDmWithStreamedResponse:
    _client: AsyncSentDm

    def __init__(self, client: AsyncSentDm) -> None:
        self._client = client

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        """Configure webhook endpoints for real-time event delivery"""
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        """Invite, update, and manage organization users and roles"""
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def templates(self) -> templates.AsyncTemplatesResourceWithStreamingResponse:
        """Manage message templates with variable substitution"""
        from .resources.templates import AsyncTemplatesResourceWithStreamingResponse

        return AsyncTemplatesResourceWithStreamingResponse(self._client.templates)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithStreamingResponse:
        """Manage organization profiles"""
        from .resources.profiles import AsyncProfilesResourceWithStreamingResponse

        return AsyncProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        """Send and track SMS and WhatsApp messages"""
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def lookup(self) -> lookup.AsyncLookupResourceWithStreamingResponse:
        from .resources.lookup import AsyncLookupResourceWithStreamingResponse

        return AsyncLookupResourceWithStreamingResponse(self._client.lookup)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithStreamingResponse:
        """Create, update, and manage customer contact lists"""
        from .resources.contacts import AsyncContactsResourceWithStreamingResponse

        return AsyncContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def brands(self) -> brands.AsyncBrandsResourceWithStreamingResponse:
        """Register and manage 10DLC brands for SMS compliance"""
        from .resources.brands import AsyncBrandsResourceWithStreamingResponse

        return AsyncBrandsResourceWithStreamingResponse(self._client.brands)

    @cached_property
    def me(self) -> me.AsyncMeResourceWithStreamingResponse:
        """Retrieve account details"""
        from .resources.me import AsyncMeResourceWithStreamingResponse

        return AsyncMeResourceWithStreamingResponse(self._client.me)


Client = SentDm

AsyncClient = AsyncSentDm
