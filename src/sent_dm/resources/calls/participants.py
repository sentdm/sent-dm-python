# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.calls import (
    participant_add_params,
    participant_remove_params,
    participant_update_params,
    participant_remove_all_params,
)
from ..._base_client import make_request_options
from ...types.api_response_of_call import APIResponseOfCall
from ...types.calls.call_participant_target_param import CallParticipantTargetParam
from ...types.calls.api_response_of_list_of_call_participant import APIResponseOfListOfCallParticipant

__all__ = ["ParticipantsResource", "AsyncParticipantsResource"]


class ParticipantsResource(SyncAPIResource):
    """Phone calls from the numbers you hold, driven by your own callback URL.

    `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/channels/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

    Every call is a record under `/v3/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
    """

    @cached_property
    def with_raw_response(self) -> ParticipantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return ParticipantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParticipantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return ParticipantsResourceWithStreamingResponse(self)

    def update(
        self,
        participant_id: str,
        *,
        id: str,
        muted: bool | Omit = omit,
        sandbox: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Mutes or unmutes one participant of the conference room a live call is in, named
        by the participant's own call id from the participants list: send muted true to
        silence them, muted false to let them be heard again. Muting a participant who
        is already muted succeeds, as does unmuting one who is not. A participant who is
        not in this call's room answers 404. A call that has ended answers 409, as does
        a call that is not in a conference.

        Args:
          muted: true to mute the participant, false to unmute them

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
            path_template("/v3/calls/{id}/participants/{participant_id}", id=id, participant_id=participant_id),
            body=maybe_transform(
                {
                    "muted": muted,
                    "sandbox": sandbox,
                },
                participant_update_params.ParticipantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
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
    ) -> APIResponseOfListOfCallParticipant:
        """
        Lists who is in the conference room one of your live calls is in: each
        participant's own call id, who they are, whether the room mutes them, and how
        long they have been connected. The call itself is one of the participants. Use a
        participant's id to mute or remove them; it is also a call id, so GET
        /v3/calls/{id} accepts it. A call that has ended answers 409, as does a call
        that is not in a conference.

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
            path_template("/v3/calls/{id}/participants", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfListOfCallParticipant,
        )

    def add(
        self,
        id: str,
        *,
        caller_id: Optional[str] | Omit = omit,
        sandbox: bool | Omit = omit,
        to: CallParticipantTargetParam | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfCall:
        """
        Dials one of your app users or a phone number into a call that is in a
        conference room, and answers with the participant's own call record. The
        participant is a call of their own: it has its own id, can be looked up and hung
        up, and is billed and reported through call.completed and call.failed like any
        other call. A phone participant is called from caller_id, which must be one of
        your numbers, or from the call's owning number when omitted, and needs a
        destination you may call and a positive balance. Only a call your answer
        connected to a conference can take participants: a call connected to a user or a
        number answers 409.

        Args:
          caller_id: The number shown to a phone participant as the caller, in E.164 format. Must be
              one of your numbers. The call's owning number when omitted

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          to: A participant to add to a call

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
        return self._post(
            path_template("/v3/calls/{id}/participants", id=id),
            body=maybe_transform(
                {
                    "caller_id": caller_id,
                    "sandbox": sandbox,
                    "to": to,
                },
                participant_add_params.ParticipantAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfCall,
        )

    def remove(
        self,
        participant_id: str,
        *,
        id: str,
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
        Removes one participant from the conference room a live call is in, named by the
        participant's own call id from the participants list. Their leg ends and is
        reported through call.completed like any other call; everyone else stays
        connected. A participant who is not in this call's room answers 404. A call that
        has ended answers 409, as does a call that is not in a conference.

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
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._delete(
            path_template("/v3/calls/{id}/participants/{participant_id}", id=id, participant_id=participant_id),
            body=maybe_transform({"sandbox": sandbox}, participant_remove_params.ParticipantRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def remove_all(
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
        Removes every participant from the conference room a live call is in, the call
        itself included. Every leg ends and is reported through call.completed like any
        other call. A room that is already empty answers 204 as well. A call that has
        ended answers 409, as does a call that is not in a conference.

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
            path_template("/v3/calls/{id}/participants", id=id),
            body=maybe_transform({"sandbox": sandbox}, participant_remove_all_params.ParticipantRemoveAllParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncParticipantsResource(AsyncAPIResource):
    """Phone calls from the numbers you hold, driven by your own callback URL.

    `POST /v3/channels/voice` enables a number for calls, with the callback URL Sent asks what to do with each call on it, and `POST /v3/channels/voice/tokens` mints a short-lived token that lets a user of your app place and receive calls as that number. When a call arrives or a caller presses a key, a signed question is POSTed to the callback URL and the answer decides the call; `POST /v3/channels/voice/{number}/test` checks the URL answers the way we need before a real call reaches it, and `POST /v3/channels/voice/{number}/rotate-secret` replaces the signing secret. The call events themselves (`call.completed` and the rest) arrive through your webhooks.

    Every call is a record under `/v3/calls`: read it, list its recordings once one is ready, hang it up, start or stop recording, and add, mute or remove conference participants while it is live. A leg to a phone number runs for at most what your balance affords at the destination's rate.
    """

    @cached_property
    def with_raw_response(self) -> AsyncParticipantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncParticipantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParticipantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncParticipantsResourceWithStreamingResponse(self)

    async def update(
        self,
        participant_id: str,
        *,
        id: str,
        muted: bool | Omit = omit,
        sandbox: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Mutes or unmutes one participant of the conference room a live call is in, named
        by the participant's own call id from the participants list: send muted true to
        silence them, muted false to let them be heard again. Muting a participant who
        is already muted succeeds, as does unmuting one who is not. A participant who is
        not in this call's room answers 404. A call that has ended answers 409, as does
        a call that is not in a conference.

        Args:
          muted: true to mute the participant, false to unmute them

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
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
            path_template("/v3/calls/{id}/participants/{participant_id}", id=id, participant_id=participant_id),
            body=await async_maybe_transform(
                {
                    "muted": muted,
                    "sandbox": sandbox,
                },
                participant_update_params.ParticipantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
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
    ) -> APIResponseOfListOfCallParticipant:
        """
        Lists who is in the conference room one of your live calls is in: each
        participant's own call id, who they are, whether the room mutes them, and how
        long they have been connected. The call itself is one of the participants. Use a
        participant's id to mute or remove them; it is also a call id, so GET
        /v3/calls/{id} accepts it. A call that has ended answers 409, as does a call
        that is not in a conference.

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
            path_template("/v3/calls/{id}/participants", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfListOfCallParticipant,
        )

    async def add(
        self,
        id: str,
        *,
        caller_id: Optional[str] | Omit = omit,
        sandbox: bool | Omit = omit,
        to: CallParticipantTargetParam | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfCall:
        """
        Dials one of your app users or a phone number into a call that is in a
        conference room, and answers with the participant's own call record. The
        participant is a call of their own: it has its own id, can be looked up and hung
        up, and is billed and reported through call.completed and call.failed like any
        other call. A phone participant is called from caller_id, which must be one of
        your numbers, or from the call's owning number when omitted, and needs a
        destination you may call and a positive balance. Only a call your answer
        connected to a conference can take participants: a call connected to a user or a
        number answers 409.

        Args:
          caller_id: The number shown to a phone participant as the caller, in E.164 format. Must be
              one of your numbers. The call's owning number when omitted

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          to: A participant to add to a call

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
        return await self._post(
            path_template("/v3/calls/{id}/participants", id=id),
            body=await async_maybe_transform(
                {
                    "caller_id": caller_id,
                    "sandbox": sandbox,
                    "to": to,
                },
                participant_add_params.ParticipantAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfCall,
        )

    async def remove(
        self,
        participant_id: str,
        *,
        id: str,
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
        Removes one participant from the conference room a live call is in, named by the
        participant's own call id from the participants list. Their leg ends and is
        reported through call.completed like any other call; everyone else stays
        connected. A participant who is not in this call's room answers 404. A call that
        has ended answers 409, as does a call that is not in a conference.

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
        if not participant_id:
            raise ValueError(f"Expected a non-empty value for `participant_id` but received {participant_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/calls/{id}/participants/{participant_id}", id=id, participant_id=participant_id),
            body=await async_maybe_transform({"sandbox": sandbox}, participant_remove_params.ParticipantRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def remove_all(
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
        Removes every participant from the conference room a live call is in, the call
        itself included. Every leg ends and is reported through call.completed like any
        other call. A room that is already empty answers 204 as well. A call that has
        ended answers 409, as does a call that is not in a conference.

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
            path_template("/v3/calls/{id}/participants", id=id),
            body=await async_maybe_transform(
                {"sandbox": sandbox}, participant_remove_all_params.ParticipantRemoveAllParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ParticipantsResourceWithRawResponse:
    def __init__(self, participants: ParticipantsResource) -> None:
        self._participants = participants

        self.update = to_raw_response_wrapper(
            participants.update,
        )
        self.list = to_raw_response_wrapper(
            participants.list,
        )
        self.add = to_raw_response_wrapper(
            participants.add,
        )
        self.remove = to_raw_response_wrapper(
            participants.remove,
        )
        self.remove_all = to_raw_response_wrapper(
            participants.remove_all,
        )


class AsyncParticipantsResourceWithRawResponse:
    def __init__(self, participants: AsyncParticipantsResource) -> None:
        self._participants = participants

        self.update = async_to_raw_response_wrapper(
            participants.update,
        )
        self.list = async_to_raw_response_wrapper(
            participants.list,
        )
        self.add = async_to_raw_response_wrapper(
            participants.add,
        )
        self.remove = async_to_raw_response_wrapper(
            participants.remove,
        )
        self.remove_all = async_to_raw_response_wrapper(
            participants.remove_all,
        )


class ParticipantsResourceWithStreamingResponse:
    def __init__(self, participants: ParticipantsResource) -> None:
        self._participants = participants

        self.update = to_streamed_response_wrapper(
            participants.update,
        )
        self.list = to_streamed_response_wrapper(
            participants.list,
        )
        self.add = to_streamed_response_wrapper(
            participants.add,
        )
        self.remove = to_streamed_response_wrapper(
            participants.remove,
        )
        self.remove_all = to_streamed_response_wrapper(
            participants.remove_all,
        )


class AsyncParticipantsResourceWithStreamingResponse:
    def __init__(self, participants: AsyncParticipantsResource) -> None:
        self._participants = participants

        self.update = async_to_streamed_response_wrapper(
            participants.update,
        )
        self.list = async_to_streamed_response_wrapper(
            participants.list,
        )
        self.add = async_to_streamed_response_wrapper(
            participants.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            participants.remove,
        )
        self.remove_all = async_to_streamed_response_wrapper(
            participants.remove_all,
        )
