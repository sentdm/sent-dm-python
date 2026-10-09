# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime

import httpx

from ..types import message_send_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.message_send_response import MessageSendResponse
from ..types.message_retrieve_status_response import MessageRetrieveStatusResponse
from ..types.message_retrieve_activities_response import MessageRetrieveActivitiesResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    """Send a message and follow what happened to it.

    One endpoint sends on any channel: pass `channel: "sent"` and we pick between SMS, WhatsApp and RCS per recipient using your routing rules, or name a channel to pin it. A send is accepted asynchronously — `POST /v3/messages` returns an id, and delivery is reported through `GET /v3/messages/{id}`, its activities, or a webhook.

    **A message needs a sender.** What you can send, where, and at what cost is decided by the markets under **Channels** — so a recipient in a country you hold no sender for is refused here rather than queued.

    **A message can be resent on its id.** `POST /v3/messages/{id}/resend` puts a finished message — typically one BLOCKED for insufficient balance — back through the send pipeline. It is a new attempt, not a free retry: every policy runs again, the message is billed again, and its status webhooks fire again. A FILTERED message is never resendable.

    **A scheduled message can be called off.** `POST /v3/messages/{id}/cancel` cancels a send you scheduled with `scheduled_at`, as long as it has not been released yet. Cancelling is free, fires `message.cancelled`, and is final — a cancelled message cannot be resent.
    """

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

    def retrieve_activities(
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
    ) -> MessageRetrieveActivitiesResponse:
        """Retrieves the activity log for a specific message.

        Activities track the message
        lifecycle including acceptance, processing, sending, delivery, and any errors. A
        SCHEDULED entry carries scheduled_at, the release instant in UTC as it stood at
        that moment. Other entries have no scheduled_at key.

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
            path_template("/v3/messages/{id}/activities", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveActivitiesResponse,
        )

    def retrieve_status(
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
    ) -> MessageRetrieveStatusResponse:
        """Retrieves the current status and details of a message by ID.

        Includes delivery
        status, timestamps, and error information if applicable. A message that is or
        was held for a later time (a send you scheduled with scheduled_at, a quiet-hours
        hold, or a message you cancelled while it was held) is returned as a
        ScheduledMessageResponse: the same fields plus scheduled_at, the instant it is
        held for in UTC — or, on a CANCELLED message, the instant that was called off. A
        message sent immediately has no scheduled_at key.

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
            path_template("/v3/messages/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveStatusResponse,
        )

    def send(
        self,
        *,
        channel: Optional[SequenceNotStr[str]] | Omit = omit,
        channels: Optional[Dict[str, Iterable[message_send_params.Channel]]] | Omit = omit,
        media_urls: Optional[SequenceNotStr[str]] | Omit = omit,
        sandbox: bool | Omit = omit,
        scheduled_at: Union[str, datetime, None] | Omit = omit,
        subject: Optional[str] | Omit = omit,
        template: Optional[message_send_params.Template] | Omit = omit,
        text: Optional[str] | Omit = omit,
        to: SequenceNotStr[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """Sends a message to one or more recipients using a template.

        Supports
        multi-channel broadcast — when multiple channels are specified (e.g. ["sms",
        "whatsapp"]), a separate message is created for each (recipient, channel) pair.
        To choose which of your own numbers a send goes out from, use 'channels':
        {"sms": [{"from": ["+12125550000", "+14155550000"]}]}. Each channel holds a list
        of entries, each with 'from' and optionally 'country' and 'strategy'; 'country'
        and 'strategy' are stored but not acted on yet, so every entry's numbers apply
        to every recipient on that channel. Every number listed must be an active sender
        on your account. Like the other account-level preconditions below, that is
        checked per message rather than when the request is received: the request is
        still accepted with 202, and each affected message is reported as BLOCKED with
        error code BUSINESS_029 on GET /messages/{id} and the message.blocked webhook.
        Each channel's numbers restrict which numbers that channel may use; it does not
        choose channels — 'channel' does, and the two can be combined. With 'channel'
        left at auto-detect, a recipient best served by a channel you listed no numbers
        for still goes out on it. Where several of the listed numbers could serve a
        recipient, routing prefers the one whose area code matches theirs. Keys: sms,
        whatsapp, rcs, mms. Returns immediately with per-recipient message IDs for async
        tracking via webhooks or the GET /messages/{id} endpoint. Sends gated before any
        delivery attempt do not reject the request — an account-level precondition such
        as insufficient balance, a template not approved for sending, or free-form
        content with no open conversation with the contact. The send is accepted with
        202 and the affected messages are reported as BLOCKED on GET /messages/{id} and
        the message.blocked webhook. To send later, set scheduled_at (ISO-8601 with an
        explicit UTC offset; a value without one is rejected) between 1 minute and 30
        days ahead: the response is a ScheduledSendMessageResponse (the same fields plus
        scheduled_at; status is still QUEUED), each message then moves to SCHEDULED, is
        held and released at that time (within a few minutes), and a message.scheduled
        webhook fires once it is held. Balance and template approval are evaluated at
        release, not at acceptance. Quiet hours are not checked when the request is
        accepted: if the time falls inside a legally protected quiet-hours window for a
        recipient, that message is moved to the next allowed time at release and a
        second message.scheduled webhook reports the new scheduled_at. An account may
        hold at most 1,000,000 scheduled messages at once (429 LIMIT_001).

        Args:
          channel: Channels to broadcast on, e.g. ["whatsapp", "sms"]. Each channel produces a
              separate message per recipient. "sent" = auto-detect. Defaults to ["sent"]
              (auto-detect) if omitted.

          channels: Which of your own numbers to send from, keyed by channel, each channel holding a
              list of entries: {"sms": [{"country": "US", "from": ["+12125550000",
              "+14155550000"]}, {"from": ["+447700800001"]}]}. Any real channel may be a key;
              sent, which is auto-detect rather than a channel, is rejected. country and
              strategy are accepted and stored but not acted on yet: every entry's numbers
              apply to every recipient on that channel.

              This does not choose channels — Channel does, and the two combine: "channel":
              ["sms"] with an sms list sends on SMS from those numbers. Each list only narrows
              which of its own channel's routes may win, so with Channel left at auto-detect a
              recipient best served by a channel with no list still goes out on it. Routing
              itself is unchanged: the same rules are scored and ranked the same way, with
              routes pinned to numbers you did not list removed from the running.

              Every number must be an active sender on your account. The request itself is
              still accepted (202) if one is not — like every other send-time rule, that is
              decided per message, so each affected message is recorded BLOCKED with error
              code BUSINESS_029 and reported on GET /v3/messages and the status webhook.

          media_urls: Attachments for this send, as publicly fetchable https URLs. Used by the MMS
              channel and ignored by every other one.

              Supplying these replaces the media on the template's mms body rather than adding
              to it, so a template can hold a default creative while a caller still sends
              something recipient-specific.

              Their presence is also what makes a message eligible for MMS on an auto-detect
              send: a message with nothing attached is delivered as SMS, because an MMS with
              no media is a more expensive text message.

              The recipient's carrier fetches each URL after the send is accepted, so it must
              stay publicly reachable — a link that expires, or one behind auth, arrives as a
              failed message.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          scheduled_at: Optional future send time as an ISO-8601 timestamp with an explicit UTC offset,
              e.g. 2026-10-01T09:00:00+02:00 or 2026-10-01T07:00:00Z. A value without an
              offset is rejected (400) rather than read in the server's zone. The offset only
              fixes the instant: it is stored and echoed in UTC as scheduled_at. Omit to send
              now. Must be at least one minute ahead and at most 30 days ahead. Accepted
              messages report SCHEDULED and are released for delivery at this time. Quiet
              hours, balance and template approval are evaluated at release, not at
              acceptance: a message whose time falls inside a recipient's protected
              quiet-hours window is moved to the next allowed time and a second
              message.scheduled webhook reports the new scheduled_at.

          subject: Subject line for this send, overriding the template's. MMS only; ignored on
              every other channel. Most handsets render it above the body, some ignore it
              entirely.

          template: SDK-style template reference: resolve by ID or by name, with optional
              parameters.

          text: Plain-text (free-form) message body. Provide either Template or this.

          to: List of recipient phone numbers in E.164 format (multi-recipient fan-out)

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
            "/v3/messages",
            body=maybe_transform(
                {
                    "channel": channel,
                    "channels": channels,
                    "media_urls": media_urls,
                    "sandbox": sandbox,
                    "scheduled_at": scheduled_at,
                    "subject": subject,
                    "template": template,
                    "text": text,
                    "to": to,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    """Send a message and follow what happened to it.

    One endpoint sends on any channel: pass `channel: "sent"` and we pick between SMS, WhatsApp and RCS per recipient using your routing rules, or name a channel to pin it. A send is accepted asynchronously — `POST /v3/messages` returns an id, and delivery is reported through `GET /v3/messages/{id}`, its activities, or a webhook.

    **A message needs a sender.** What you can send, where, and at what cost is decided by the markets under **Channels** — so a recipient in a country you hold no sender for is refused here rather than queued.

    **A message can be resent on its id.** `POST /v3/messages/{id}/resend` puts a finished message — typically one BLOCKED for insufficient balance — back through the send pipeline. It is a new attempt, not a free retry: every policy runs again, the message is billed again, and its status webhooks fire again. A FILTERED message is never resendable.

    **A scheduled message can be called off.** `POST /v3/messages/{id}/cancel` cancels a send you scheduled with `scheduled_at`, as long as it has not been released yet. Cancelling is free, fires `message.cancelled`, and is final — a cancelled message cannot be resent.
    """

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

    async def retrieve_activities(
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
    ) -> MessageRetrieveActivitiesResponse:
        """Retrieves the activity log for a specific message.

        Activities track the message
        lifecycle including acceptance, processing, sending, delivery, and any errors. A
        SCHEDULED entry carries scheduled_at, the release instant in UTC as it stood at
        that moment. Other entries have no scheduled_at key.

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
            path_template("/v3/messages/{id}/activities", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveActivitiesResponse,
        )

    async def retrieve_status(
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
    ) -> MessageRetrieveStatusResponse:
        """Retrieves the current status and details of a message by ID.

        Includes delivery
        status, timestamps, and error information if applicable. A message that is or
        was held for a later time (a send you scheduled with scheduled_at, a quiet-hours
        hold, or a message you cancelled while it was held) is returned as a
        ScheduledMessageResponse: the same fields plus scheduled_at, the instant it is
        held for in UTC — or, on a CANCELLED message, the instant that was called off. A
        message sent immediately has no scheduled_at key.

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
            path_template("/v3/messages/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveStatusResponse,
        )

    async def send(
        self,
        *,
        channel: Optional[SequenceNotStr[str]] | Omit = omit,
        channels: Optional[Dict[str, Iterable[message_send_params.Channel]]] | Omit = omit,
        media_urls: Optional[SequenceNotStr[str]] | Omit = omit,
        sandbox: bool | Omit = omit,
        scheduled_at: Union[str, datetime, None] | Omit = omit,
        subject: Optional[str] | Omit = omit,
        template: Optional[message_send_params.Template] | Omit = omit,
        text: Optional[str] | Omit = omit,
        to: SequenceNotStr[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """Sends a message to one or more recipients using a template.

        Supports
        multi-channel broadcast — when multiple channels are specified (e.g. ["sms",
        "whatsapp"]), a separate message is created for each (recipient, channel) pair.
        To choose which of your own numbers a send goes out from, use 'channels':
        {"sms": [{"from": ["+12125550000", "+14155550000"]}]}. Each channel holds a list
        of entries, each with 'from' and optionally 'country' and 'strategy'; 'country'
        and 'strategy' are stored but not acted on yet, so every entry's numbers apply
        to every recipient on that channel. Every number listed must be an active sender
        on your account. Like the other account-level preconditions below, that is
        checked per message rather than when the request is received: the request is
        still accepted with 202, and each affected message is reported as BLOCKED with
        error code BUSINESS_029 on GET /messages/{id} and the message.blocked webhook.
        Each channel's numbers restrict which numbers that channel may use; it does not
        choose channels — 'channel' does, and the two can be combined. With 'channel'
        left at auto-detect, a recipient best served by a channel you listed no numbers
        for still goes out on it. Where several of the listed numbers could serve a
        recipient, routing prefers the one whose area code matches theirs. Keys: sms,
        whatsapp, rcs, mms. Returns immediately with per-recipient message IDs for async
        tracking via webhooks or the GET /messages/{id} endpoint. Sends gated before any
        delivery attempt do not reject the request — an account-level precondition such
        as insufficient balance, a template not approved for sending, or free-form
        content with no open conversation with the contact. The send is accepted with
        202 and the affected messages are reported as BLOCKED on GET /messages/{id} and
        the message.blocked webhook. To send later, set scheduled_at (ISO-8601 with an
        explicit UTC offset; a value without one is rejected) between 1 minute and 30
        days ahead: the response is a ScheduledSendMessageResponse (the same fields plus
        scheduled_at; status is still QUEUED), each message then moves to SCHEDULED, is
        held and released at that time (within a few minutes), and a message.scheduled
        webhook fires once it is held. Balance and template approval are evaluated at
        release, not at acceptance. Quiet hours are not checked when the request is
        accepted: if the time falls inside a legally protected quiet-hours window for a
        recipient, that message is moved to the next allowed time at release and a
        second message.scheduled webhook reports the new scheduled_at. An account may
        hold at most 1,000,000 scheduled messages at once (429 LIMIT_001).

        Args:
          channel: Channels to broadcast on, e.g. ["whatsapp", "sms"]. Each channel produces a
              separate message per recipient. "sent" = auto-detect. Defaults to ["sent"]
              (auto-detect) if omitted.

          channels: Which of your own numbers to send from, keyed by channel, each channel holding a
              list of entries: {"sms": [{"country": "US", "from": ["+12125550000",
              "+14155550000"]}, {"from": ["+447700800001"]}]}. Any real channel may be a key;
              sent, which is auto-detect rather than a channel, is rejected. country and
              strategy are accepted and stored but not acted on yet: every entry's numbers
              apply to every recipient on that channel.

              This does not choose channels — Channel does, and the two combine: "channel":
              ["sms"] with an sms list sends on SMS from those numbers. Each list only narrows
              which of its own channel's routes may win, so with Channel left at auto-detect a
              recipient best served by a channel with no list still goes out on it. Routing
              itself is unchanged: the same rules are scored and ranked the same way, with
              routes pinned to numbers you did not list removed from the running.

              Every number must be an active sender on your account. The request itself is
              still accepted (202) if one is not — like every other send-time rule, that is
              decided per message, so each affected message is recorded BLOCKED with error
              code BUSINESS_029 and reported on GET /v3/messages and the status webhook.

          media_urls: Attachments for this send, as publicly fetchable https URLs. Used by the MMS
              channel and ignored by every other one.

              Supplying these replaces the media on the template's mms body rather than adding
              to it, so a template can hold a default creative while a caller still sends
              something recipient-specific.

              Their presence is also what makes a message eligible for MMS on an auto-detect
              send: a message with nothing attached is delivered as SMS, because an MMS with
              no media is a more expensive text message.

              The recipient's carrier fetches each URL after the send is accepted, so it must
              stay publicly reachable — a link that expires, or one behind auth, arrives as a
              failed message.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          scheduled_at: Optional future send time as an ISO-8601 timestamp with an explicit UTC offset,
              e.g. 2026-10-01T09:00:00+02:00 or 2026-10-01T07:00:00Z. A value without an
              offset is rejected (400) rather than read in the server's zone. The offset only
              fixes the instant: it is stored and echoed in UTC as scheduled_at. Omit to send
              now. Must be at least one minute ahead and at most 30 days ahead. Accepted
              messages report SCHEDULED and are released for delivery at this time. Quiet
              hours, balance and template approval are evaluated at release, not at
              acceptance: a message whose time falls inside a recipient's protected
              quiet-hours window is moved to the next allowed time and a second
              message.scheduled webhook reports the new scheduled_at.

          subject: Subject line for this send, overriding the template's. MMS only; ignored on
              every other channel. Most handsets render it above the body, some ignore it
              entirely.

          template: SDK-style template reference: resolve by ID or by name, with optional
              parameters.

          text: Plain-text (free-form) message body. Provide either Template or this.

          to: List of recipient phone numbers in E.164 format (multi-recipient fan-out)

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
            "/v3/messages",
            body=await async_maybe_transform(
                {
                    "channel": channel,
                    "channels": channels,
                    "media_urls": media_urls,
                    "sandbox": sandbox,
                    "scheduled_at": scheduled_at,
                    "subject": subject,
                    "template": template,
                    "text": text,
                    "to": to,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve_activities = to_raw_response_wrapper(
            messages.retrieve_activities,
        )
        self.retrieve_status = to_raw_response_wrapper(
            messages.retrieve_status,
        )
        self.send = to_raw_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve_activities = async_to_raw_response_wrapper(
            messages.retrieve_activities,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            messages.retrieve_status,
        )
        self.send = async_to_raw_response_wrapper(
            messages.send,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve_activities = to_streamed_response_wrapper(
            messages.retrieve_activities,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            messages.retrieve_status,
        )
        self.send = to_streamed_response_wrapper(
            messages.send,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve_activities = async_to_streamed_response_wrapper(
            messages.retrieve_activities,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            messages.retrieve_status,
        )
        self.send = async_to_streamed_response_wrapper(
            messages.send,
        )
