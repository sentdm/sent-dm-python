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
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import SentError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import me, users, numbers, contacts, messages, profiles, webhooks, templates, conversations
    from .resources.me import MeResource, AsyncMeResource
    from .resources.users import UsersResource, AsyncUsersResource
    from .resources.numbers import NumbersResource, AsyncNumbersResource
    from .resources.contacts import ContactsResource, AsyncContactsResource
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.templates import TemplatesResource, AsyncTemplatesResource
    from .resources.conversations import ConversationsResource, AsyncConversationsResource
    from .resources.profiles.profiles import ProfilesResource, AsyncProfilesResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Sent", "AsyncSent", "Client", "AsyncClient"]


class Sent(SyncAPIClient):
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
        """Construct a new synchronous Sent client instance.

        This automatically infers the `api_key` argument from the `SENT_DM_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("SENT_DM_API_KEY")
        if api_key is None:
            raise SentError(
                "The api_key client option must be set either by passing api_key to the client or by setting the SENT_DM_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("SENT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.sent.dm"

        custom_headers_env = os.environ.get("SENT_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

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
        """Delivery reports and inbound messages, pushed to you.

        Subscribe an endpoint to the event types you care about — `GET /v3/webhooks/event-types` lists them — and we POST each one as it happens, retrying on failure. Polling `GET /v3/messages/{id}` works and does not scale.

        **Verify the signature.** Every delivery is signed with your endpoint's secret; an unverified endpoint is one anybody can post to. `rotate-secret` replaces it, `test` sends a specimen event, and `GET /v3/webhooks/{id}/events` shows what we tried to deliver and what your endpoint answered — which is the first place to look when something appears to be missing.
        """
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def users(self) -> UsersResource:
        """The people who can sign in to your organization, and what each may do.

        Users are dashboard access and nothing else — they do not send, and removing one does not affect traffic. An API key is not a user: it belongs to the organization or to a sender profile, so revoking a person's access leaves your integration running.
        """
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def templates(self) -> TemplatesResource:
        """Reusable message bodies with named variables.

        A template is substituted at send time from the values you pass, so the copy lives here rather than in your application. WhatsApp templates additionally need Meta's approval before they can be sent, and a template's channel status reports where that stands — an approved SMS template and an unapproved WhatsApp one are the same template in two states.
        """
        from .resources.templates import TemplatesResource

        return TemplatesResource(self)

    @cached_property
    def profiles(self) -> ProfilesResource:
        """**Deprecated — use Sender Profiles.**

        The original profile resource, kept because it has live callers. It still works, and its replacement is `/v3/sender-profiles`, which takes the identity and the campaign in one call instead of across three.

        New integrations should not start here.
        """
        from .resources.profiles import ProfilesResource

        return ProfilesResource(self)

    @cached_property
    def numbers(self) -> NumbersResource:
        """What a phone number actually is, before you send to it.

        A lookup returns the number's country, line type and carrier, which is what decides whether it is reachable on a channel and what it costs. Worth doing on import rather than on send: a landline in a contact list is a message that can never be delivered.
        """
        from .resources.numbers import NumbersResource

        return NumbersResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        """Send a message and follow what happened to it.

        One endpoint sends on any channel: pass `channel: "sent"` and we pick between SMS, WhatsApp and RCS per recipient using your routing rules, or name a channel to pin it. A send is accepted asynchronously — `POST /v3/messages` returns an id, and delivery is reported through `GET /v3/messages/{id}`, its activities, or a webhook.

        **A message needs a sender.** What you can send, where, and at what cost is decided by the markets under **Channels** — so a recipient in a country you hold no sender for is refused here rather than queued.
        """
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def contacts(self) -> ContactsResource:
        """The people you message, and their channel identities.

        A contact holds one identity per channel — a phone number, a WhatsApp number — so routing can choose between them for the same person. Opt-out is recorded against the contact and honoured on every send, whichever channel it came through.

        `GET /v3/contacts/{id}/message-summary` is the per-contact view of what you have sent and what happened to it.
        """
        from .resources.contacts import ContactsResource

        return ContactsResource(self)

    @cached_property
    def conversations(self) -> ConversationsResource:
        """Inbound and outbound messages, grouped by the person they are with.

        A conversation is the thread for one contact across every channel — a reply by SMS and one by WhatsApp belong to the same conversation, because they are the same person talking to you.

        Read-only. Sending is **Messages**; a reply arrives here and through your webhooks.
        """
        from .resources.conversations import ConversationsResource

        return ConversationsResource(self)

    @cached_property
    def me(self) -> MeResource:
        """Who the current key is.

        `GET /v3/me` answers with the account the key authenticates as, which is the quickest way to tell a live key from a test one, an organization key from a sender profile's, and to confirm `x-profile-id` resolved to the profile you meant.
        """
        from .resources.me import MeResource

        return MeResource(self)

    @cached_property
    def with_raw_response(self) -> SentWithRawResponse:
        return SentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SentWithStreamedResponse:
        return SentWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        headers: dict[str, str] = {}
        if security.get("customer_api_key", False):
            for key, value in self._customer_api_key.items():
                headers.setdefault(key, value)
        return headers

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


class AsyncSent(AsyncAPIClient):
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
        """Construct a new async AsyncSent client instance.

        This automatically infers the `api_key` argument from the `SENT_DM_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("SENT_DM_API_KEY")
        if api_key is None:
            raise SentError(
                "The api_key client option must be set either by passing api_key to the client or by setting the SENT_DM_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("SENT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.sent.dm"

        custom_headers_env = os.environ.get("SENT_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

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
        """Delivery reports and inbound messages, pushed to you.

        Subscribe an endpoint to the event types you care about — `GET /v3/webhooks/event-types` lists them — and we POST each one as it happens, retrying on failure. Polling `GET /v3/messages/{id}` works and does not scale.

        **Verify the signature.** Every delivery is signed with your endpoint's secret; an unverified endpoint is one anybody can post to. `rotate-secret` replaces it, `test` sends a specimen event, and `GET /v3/webhooks/{id}/events` shows what we tried to deliver and what your endpoint answered — which is the first place to look when something appears to be missing.
        """
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        """The people who can sign in to your organization, and what each may do.

        Users are dashboard access and nothing else — they do not send, and removing one does not affect traffic. An API key is not a user: it belongs to the organization or to a sender profile, so revoking a person's access leaves your integration running.
        """
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        """Reusable message bodies with named variables.

        A template is substituted at send time from the values you pass, so the copy lives here rather than in your application. WhatsApp templates additionally need Meta's approval before they can be sent, and a template's channel status reports where that stands — an approved SMS template and an unapproved WhatsApp one are the same template in two states.
        """
        from .resources.templates import AsyncTemplatesResource

        return AsyncTemplatesResource(self)

    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        """**Deprecated — use Sender Profiles.**

        The original profile resource, kept because it has live callers. It still works, and its replacement is `/v3/sender-profiles`, which takes the identity and the campaign in one call instead of across three.

        New integrations should not start here.
        """
        from .resources.profiles import AsyncProfilesResource

        return AsyncProfilesResource(self)

    @cached_property
    def numbers(self) -> AsyncNumbersResource:
        """What a phone number actually is, before you send to it.

        A lookup returns the number's country, line type and carrier, which is what decides whether it is reachable on a channel and what it costs. Worth doing on import rather than on send: a landline in a contact list is a message that can never be delivered.
        """
        from .resources.numbers import AsyncNumbersResource

        return AsyncNumbersResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        """Send a message and follow what happened to it.

        One endpoint sends on any channel: pass `channel: "sent"` and we pick between SMS, WhatsApp and RCS per recipient using your routing rules, or name a channel to pin it. A send is accepted asynchronously — `POST /v3/messages` returns an id, and delivery is reported through `GET /v3/messages/{id}`, its activities, or a webhook.

        **A message needs a sender.** What you can send, where, and at what cost is decided by the markets under **Channels** — so a recipient in a country you hold no sender for is refused here rather than queued.
        """
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def contacts(self) -> AsyncContactsResource:
        """The people you message, and their channel identities.

        A contact holds one identity per channel — a phone number, a WhatsApp number — so routing can choose between them for the same person. Opt-out is recorded against the contact and honoured on every send, whichever channel it came through.

        `GET /v3/contacts/{id}/message-summary` is the per-contact view of what you have sent and what happened to it.
        """
        from .resources.contacts import AsyncContactsResource

        return AsyncContactsResource(self)

    @cached_property
    def conversations(self) -> AsyncConversationsResource:
        """Inbound and outbound messages, grouped by the person they are with.

        A conversation is the thread for one contact across every channel — a reply by SMS and one by WhatsApp belong to the same conversation, because they are the same person talking to you.

        Read-only. Sending is **Messages**; a reply arrives here and through your webhooks.
        """
        from .resources.conversations import AsyncConversationsResource

        return AsyncConversationsResource(self)

    @cached_property
    def me(self) -> AsyncMeResource:
        """Who the current key is.

        `GET /v3/me` answers with the account the key authenticates as, which is the quickest way to tell a live key from a test one, an organization key from a sender profile's, and to confirm `x-profile-id` resolved to the profile you meant.
        """
        from .resources.me import AsyncMeResource

        return AsyncMeResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncSentWithRawResponse:
        return AsyncSentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSentWithStreamedResponse:
        return AsyncSentWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        headers: dict[str, str] = {}
        if security.get("customer_api_key", False):
            for key, value in self._customer_api_key.items():
                headers.setdefault(key, value)
        return headers

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


class SentWithRawResponse:
    _client: Sent

    def __init__(self, client: Sent) -> None:
        self._client = client

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        """Delivery reports and inbound messages, pushed to you.

        Subscribe an endpoint to the event types you care about — `GET /v3/webhooks/event-types` lists them — and we POST each one as it happens, retrying on failure. Polling `GET /v3/messages/{id}` works and does not scale.

        **Verify the signature.** Every delivery is signed with your endpoint's secret; an unverified endpoint is one anybody can post to. `rotate-secret` replaces it, `test` sends a specimen event, and `GET /v3/webhooks/{id}/events` shows what we tried to deliver and what your endpoint answered — which is the first place to look when something appears to be missing.
        """
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        """The people who can sign in to your organization, and what each may do.

        Users are dashboard access and nothing else — they do not send, and removing one does not affect traffic. An API key is not a user: it belongs to the organization or to a sender profile, so revoking a person's access leaves your integration running.
        """
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def templates(self) -> templates.TemplatesResourceWithRawResponse:
        """Reusable message bodies with named variables.

        A template is substituted at send time from the values you pass, so the copy lives here rather than in your application. WhatsApp templates additionally need Meta's approval before they can be sent, and a template's channel status reports where that stands — an approved SMS template and an unapproved WhatsApp one are the same template in two states.
        """
        from .resources.templates import TemplatesResourceWithRawResponse

        return TemplatesResourceWithRawResponse(self._client.templates)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithRawResponse:
        """**Deprecated — use Sender Profiles.**

        The original profile resource, kept because it has live callers. It still works, and its replacement is `/v3/sender-profiles`, which takes the identity and the campaign in one call instead of across three.

        New integrations should not start here.
        """
        from .resources.profiles import ProfilesResourceWithRawResponse

        return ProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def numbers(self) -> numbers.NumbersResourceWithRawResponse:
        """What a phone number actually is, before you send to it.

        A lookup returns the number's country, line type and carrier, which is what decides whether it is reachable on a channel and what it costs. Worth doing on import rather than on send: a landline in a contact list is a message that can never be delivered.
        """
        from .resources.numbers import NumbersResourceWithRawResponse

        return NumbersResourceWithRawResponse(self._client.numbers)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        """Send a message and follow what happened to it.

        One endpoint sends on any channel: pass `channel: "sent"` and we pick between SMS, WhatsApp and RCS per recipient using your routing rules, or name a channel to pin it. A send is accepted asynchronously — `POST /v3/messages` returns an id, and delivery is reported through `GET /v3/messages/{id}`, its activities, or a webhook.

        **A message needs a sender.** What you can send, where, and at what cost is decided by the markets under **Channels** — so a recipient in a country you hold no sender for is refused here rather than queued.
        """
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithRawResponse:
        """The people you message, and their channel identities.

        A contact holds one identity per channel — a phone number, a WhatsApp number — so routing can choose between them for the same person. Opt-out is recorded against the contact and honoured on every send, whichever channel it came through.

        `GET /v3/contacts/{id}/message-summary` is the per-contact view of what you have sent and what happened to it.
        """
        from .resources.contacts import ContactsResourceWithRawResponse

        return ContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def conversations(self) -> conversations.ConversationsResourceWithRawResponse:
        """Inbound and outbound messages, grouped by the person they are with.

        A conversation is the thread for one contact across every channel — a reply by SMS and one by WhatsApp belong to the same conversation, because they are the same person talking to you.

        Read-only. Sending is **Messages**; a reply arrives here and through your webhooks.
        """
        from .resources.conversations import ConversationsResourceWithRawResponse

        return ConversationsResourceWithRawResponse(self._client.conversations)

    @cached_property
    def me(self) -> me.MeResourceWithRawResponse:
        """Who the current key is.

        `GET /v3/me` answers with the account the key authenticates as, which is the quickest way to tell a live key from a test one, an organization key from a sender profile's, and to confirm `x-profile-id` resolved to the profile you meant.
        """
        from .resources.me import MeResourceWithRawResponse

        return MeResourceWithRawResponse(self._client.me)


class AsyncSentWithRawResponse:
    _client: AsyncSent

    def __init__(self, client: AsyncSent) -> None:
        self._client = client

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        """Delivery reports and inbound messages, pushed to you.

        Subscribe an endpoint to the event types you care about — `GET /v3/webhooks/event-types` lists them — and we POST each one as it happens, retrying on failure. Polling `GET /v3/messages/{id}` works and does not scale.

        **Verify the signature.** Every delivery is signed with your endpoint's secret; an unverified endpoint is one anybody can post to. `rotate-secret` replaces it, `test` sends a specimen event, and `GET /v3/webhooks/{id}/events` shows what we tried to deliver and what your endpoint answered — which is the first place to look when something appears to be missing.
        """
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        """The people who can sign in to your organization, and what each may do.

        Users are dashboard access and nothing else — they do not send, and removing one does not affect traffic. An API key is not a user: it belongs to the organization or to a sender profile, so revoking a person's access leaves your integration running.
        """
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def templates(self) -> templates.AsyncTemplatesResourceWithRawResponse:
        """Reusable message bodies with named variables.

        A template is substituted at send time from the values you pass, so the copy lives here rather than in your application. WhatsApp templates additionally need Meta's approval before they can be sent, and a template's channel status reports where that stands — an approved SMS template and an unapproved WhatsApp one are the same template in two states.
        """
        from .resources.templates import AsyncTemplatesResourceWithRawResponse

        return AsyncTemplatesResourceWithRawResponse(self._client.templates)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithRawResponse:
        """**Deprecated — use Sender Profiles.**

        The original profile resource, kept because it has live callers. It still works, and its replacement is `/v3/sender-profiles`, which takes the identity and the campaign in one call instead of across three.

        New integrations should not start here.
        """
        from .resources.profiles import AsyncProfilesResourceWithRawResponse

        return AsyncProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def numbers(self) -> numbers.AsyncNumbersResourceWithRawResponse:
        """What a phone number actually is, before you send to it.

        A lookup returns the number's country, line type and carrier, which is what decides whether it is reachable on a channel and what it costs. Worth doing on import rather than on send: a landline in a contact list is a message that can never be delivered.
        """
        from .resources.numbers import AsyncNumbersResourceWithRawResponse

        return AsyncNumbersResourceWithRawResponse(self._client.numbers)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        """Send a message and follow what happened to it.

        One endpoint sends on any channel: pass `channel: "sent"` and we pick between SMS, WhatsApp and RCS per recipient using your routing rules, or name a channel to pin it. A send is accepted asynchronously — `POST /v3/messages` returns an id, and delivery is reported through `GET /v3/messages/{id}`, its activities, or a webhook.

        **A message needs a sender.** What you can send, where, and at what cost is decided by the markets under **Channels** — so a recipient in a country you hold no sender for is refused here rather than queued.
        """
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithRawResponse:
        """The people you message, and their channel identities.

        A contact holds one identity per channel — a phone number, a WhatsApp number — so routing can choose between them for the same person. Opt-out is recorded against the contact and honoured on every send, whichever channel it came through.

        `GET /v3/contacts/{id}/message-summary` is the per-contact view of what you have sent and what happened to it.
        """
        from .resources.contacts import AsyncContactsResourceWithRawResponse

        return AsyncContactsResourceWithRawResponse(self._client.contacts)

    @cached_property
    def conversations(self) -> conversations.AsyncConversationsResourceWithRawResponse:
        """Inbound and outbound messages, grouped by the person they are with.

        A conversation is the thread for one contact across every channel — a reply by SMS and one by WhatsApp belong to the same conversation, because they are the same person talking to you.

        Read-only. Sending is **Messages**; a reply arrives here and through your webhooks.
        """
        from .resources.conversations import AsyncConversationsResourceWithRawResponse

        return AsyncConversationsResourceWithRawResponse(self._client.conversations)

    @cached_property
    def me(self) -> me.AsyncMeResourceWithRawResponse:
        """Who the current key is.

        `GET /v3/me` answers with the account the key authenticates as, which is the quickest way to tell a live key from a test one, an organization key from a sender profile's, and to confirm `x-profile-id` resolved to the profile you meant.
        """
        from .resources.me import AsyncMeResourceWithRawResponse

        return AsyncMeResourceWithRawResponse(self._client.me)


class SentWithStreamedResponse:
    _client: Sent

    def __init__(self, client: Sent) -> None:
        self._client = client

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        """Delivery reports and inbound messages, pushed to you.

        Subscribe an endpoint to the event types you care about — `GET /v3/webhooks/event-types` lists them — and we POST each one as it happens, retrying on failure. Polling `GET /v3/messages/{id}` works and does not scale.

        **Verify the signature.** Every delivery is signed with your endpoint's secret; an unverified endpoint is one anybody can post to. `rotate-secret` replaces it, `test` sends a specimen event, and `GET /v3/webhooks/{id}/events` shows what we tried to deliver and what your endpoint answered — which is the first place to look when something appears to be missing.
        """
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        """The people who can sign in to your organization, and what each may do.

        Users are dashboard access and nothing else — they do not send, and removing one does not affect traffic. An API key is not a user: it belongs to the organization or to a sender profile, so revoking a person's access leaves your integration running.
        """
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def templates(self) -> templates.TemplatesResourceWithStreamingResponse:
        """Reusable message bodies with named variables.

        A template is substituted at send time from the values you pass, so the copy lives here rather than in your application. WhatsApp templates additionally need Meta's approval before they can be sent, and a template's channel status reports where that stands — an approved SMS template and an unapproved WhatsApp one are the same template in two states.
        """
        from .resources.templates import TemplatesResourceWithStreamingResponse

        return TemplatesResourceWithStreamingResponse(self._client.templates)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithStreamingResponse:
        """**Deprecated — use Sender Profiles.**

        The original profile resource, kept because it has live callers. It still works, and its replacement is `/v3/sender-profiles`, which takes the identity and the campaign in one call instead of across three.

        New integrations should not start here.
        """
        from .resources.profiles import ProfilesResourceWithStreamingResponse

        return ProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def numbers(self) -> numbers.NumbersResourceWithStreamingResponse:
        """What a phone number actually is, before you send to it.

        A lookup returns the number's country, line type and carrier, which is what decides whether it is reachable on a channel and what it costs. Worth doing on import rather than on send: a landline in a contact list is a message that can never be delivered.
        """
        from .resources.numbers import NumbersResourceWithStreamingResponse

        return NumbersResourceWithStreamingResponse(self._client.numbers)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        """Send a message and follow what happened to it.

        One endpoint sends on any channel: pass `channel: "sent"` and we pick between SMS, WhatsApp and RCS per recipient using your routing rules, or name a channel to pin it. A send is accepted asynchronously — `POST /v3/messages` returns an id, and delivery is reported through `GET /v3/messages/{id}`, its activities, or a webhook.

        **A message needs a sender.** What you can send, where, and at what cost is decided by the markets under **Channels** — so a recipient in a country you hold no sender for is refused here rather than queued.
        """
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def contacts(self) -> contacts.ContactsResourceWithStreamingResponse:
        """The people you message, and their channel identities.

        A contact holds one identity per channel — a phone number, a WhatsApp number — so routing can choose between them for the same person. Opt-out is recorded against the contact and honoured on every send, whichever channel it came through.

        `GET /v3/contacts/{id}/message-summary` is the per-contact view of what you have sent and what happened to it.
        """
        from .resources.contacts import ContactsResourceWithStreamingResponse

        return ContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def conversations(self) -> conversations.ConversationsResourceWithStreamingResponse:
        """Inbound and outbound messages, grouped by the person they are with.

        A conversation is the thread for one contact across every channel — a reply by SMS and one by WhatsApp belong to the same conversation, because they are the same person talking to you.

        Read-only. Sending is **Messages**; a reply arrives here and through your webhooks.
        """
        from .resources.conversations import ConversationsResourceWithStreamingResponse

        return ConversationsResourceWithStreamingResponse(self._client.conversations)

    @cached_property
    def me(self) -> me.MeResourceWithStreamingResponse:
        """Who the current key is.

        `GET /v3/me` answers with the account the key authenticates as, which is the quickest way to tell a live key from a test one, an organization key from a sender profile's, and to confirm `x-profile-id` resolved to the profile you meant.
        """
        from .resources.me import MeResourceWithStreamingResponse

        return MeResourceWithStreamingResponse(self._client.me)


class AsyncSentWithStreamedResponse:
    _client: AsyncSent

    def __init__(self, client: AsyncSent) -> None:
        self._client = client

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        """Delivery reports and inbound messages, pushed to you.

        Subscribe an endpoint to the event types you care about — `GET /v3/webhooks/event-types` lists them — and we POST each one as it happens, retrying on failure. Polling `GET /v3/messages/{id}` works and does not scale.

        **Verify the signature.** Every delivery is signed with your endpoint's secret; an unverified endpoint is one anybody can post to. `rotate-secret` replaces it, `test` sends a specimen event, and `GET /v3/webhooks/{id}/events` shows what we tried to deliver and what your endpoint answered — which is the first place to look when something appears to be missing.
        """
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        """The people who can sign in to your organization, and what each may do.

        Users are dashboard access and nothing else — they do not send, and removing one does not affect traffic. An API key is not a user: it belongs to the organization or to a sender profile, so revoking a person's access leaves your integration running.
        """
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def templates(self) -> templates.AsyncTemplatesResourceWithStreamingResponse:
        """Reusable message bodies with named variables.

        A template is substituted at send time from the values you pass, so the copy lives here rather than in your application. WhatsApp templates additionally need Meta's approval before they can be sent, and a template's channel status reports where that stands — an approved SMS template and an unapproved WhatsApp one are the same template in two states.
        """
        from .resources.templates import AsyncTemplatesResourceWithStreamingResponse

        return AsyncTemplatesResourceWithStreamingResponse(self._client.templates)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithStreamingResponse:
        """**Deprecated — use Sender Profiles.**

        The original profile resource, kept because it has live callers. It still works, and its replacement is `/v3/sender-profiles`, which takes the identity and the campaign in one call instead of across three.

        New integrations should not start here.
        """
        from .resources.profiles import AsyncProfilesResourceWithStreamingResponse

        return AsyncProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def numbers(self) -> numbers.AsyncNumbersResourceWithStreamingResponse:
        """What a phone number actually is, before you send to it.

        A lookup returns the number's country, line type and carrier, which is what decides whether it is reachable on a channel and what it costs. Worth doing on import rather than on send: a landline in a contact list is a message that can never be delivered.
        """
        from .resources.numbers import AsyncNumbersResourceWithStreamingResponse

        return AsyncNumbersResourceWithStreamingResponse(self._client.numbers)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        """Send a message and follow what happened to it.

        One endpoint sends on any channel: pass `channel: "sent"` and we pick between SMS, WhatsApp and RCS per recipient using your routing rules, or name a channel to pin it. A send is accepted asynchronously — `POST /v3/messages` returns an id, and delivery is reported through `GET /v3/messages/{id}`, its activities, or a webhook.

        **A message needs a sender.** What you can send, where, and at what cost is decided by the markets under **Channels** — so a recipient in a country you hold no sender for is refused here rather than queued.
        """
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def contacts(self) -> contacts.AsyncContactsResourceWithStreamingResponse:
        """The people you message, and their channel identities.

        A contact holds one identity per channel — a phone number, a WhatsApp number — so routing can choose between them for the same person. Opt-out is recorded against the contact and honoured on every send, whichever channel it came through.

        `GET /v3/contacts/{id}/message-summary` is the per-contact view of what you have sent and what happened to it.
        """
        from .resources.contacts import AsyncContactsResourceWithStreamingResponse

        return AsyncContactsResourceWithStreamingResponse(self._client.contacts)

    @cached_property
    def conversations(self) -> conversations.AsyncConversationsResourceWithStreamingResponse:
        """Inbound and outbound messages, grouped by the person they are with.

        A conversation is the thread for one contact across every channel — a reply by SMS and one by WhatsApp belong to the same conversation, because they are the same person talking to you.

        Read-only. Sending is **Messages**; a reply arrives here and through your webhooks.
        """
        from .resources.conversations import AsyncConversationsResourceWithStreamingResponse

        return AsyncConversationsResourceWithStreamingResponse(self._client.conversations)

    @cached_property
    def me(self) -> me.AsyncMeResourceWithStreamingResponse:
        """Who the current key is.

        `GET /v3/me` answers with the account the key authenticates as, which is the quickest way to tell a live key from a test one, an organization key from a sender profile's, and to confirm `x-profile-id` resolved to the profile you meant.
        """
        from .resources.me import AsyncMeResourceWithStreamingResponse

        return AsyncMeResourceWithStreamingResponse(self._client.me)


Client = Sent

AsyncClient = AsyncSent
