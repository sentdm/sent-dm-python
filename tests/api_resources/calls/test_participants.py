# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types import APIResponseOfCall
from sent_dm.types.calls import (
    APIResponseOfListOfCallParticipant,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParticipants:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Sent) -> None:
        participant = client.calls.participants.update(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Sent) -> None:
        participant = client.calls.participants.update(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
            muted=True,
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Sent) -> None:
        response = client.calls.participants.with_raw_response.update(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Sent) -> None:
        with client.calls.participants.with_streaming_response.update(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert participant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.calls.participants.with_raw_response.update(
                participant_id="call_9f2ab000-0000-4000-8000-000000000002",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            client.calls.participants.with_raw_response.update(
                participant_id="",
                id="call_9f2ab000-0000-4000-8000-000000000001",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Sent) -> None:
        participant = client.calls.participants.list(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert_matches_type(APIResponseOfListOfCallParticipant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Sent) -> None:
        participant = client.calls.participants.list(
            id="call_9f2ab000-0000-4000-8000-000000000001",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfListOfCallParticipant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Sent) -> None:
        response = client.calls.participants.with_raw_response.list(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(APIResponseOfListOfCallParticipant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Sent) -> None:
        with client.calls.participants.with_streaming_response.list(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(APIResponseOfListOfCallParticipant, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.calls.participants.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Sent) -> None:
        participant = client.calls.participants.add(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert_matches_type(APIResponseOfCall, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_with_all_params(self, client: Sent) -> None:
        participant = client.calls.participants.add(
            id="call_9f2ab000-0000-4000-8000-000000000001",
            caller_id="+12025550123",
            sandbox=False,
            to={
                "kind": "number",
                "value": "+14155551234",
            },
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfCall, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Sent) -> None:
        response = client.calls.participants.with_raw_response.add(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert_matches_type(APIResponseOfCall, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Sent) -> None:
        with client.calls.participants.with_streaming_response.add(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert_matches_type(APIResponseOfCall, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.calls.participants.with_raw_response.add(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Sent) -> None:
        participant = client.calls.participants.remove(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_with_all_params(self, client: Sent) -> None:
        participant = client.calls.participants.remove(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
            sandbox=False,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Sent) -> None:
        response = client.calls.participants.with_raw_response.remove(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Sent) -> None:
        with client.calls.participants.with_streaming_response.remove(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert participant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.calls.participants.with_raw_response.remove(
                participant_id="call_9f2ab000-0000-4000-8000-000000000002",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            client.calls.participants.with_raw_response.remove(
                participant_id="",
                id="call_9f2ab000-0000-4000-8000-000000000001",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_all(self, client: Sent) -> None:
        participant = client.calls.participants.remove_all(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_all_with_all_params(self, client: Sent) -> None:
        participant = client.calls.participants.remove_all(
            id="call_9f2ab000-0000-4000-8000-000000000001",
            sandbox=False,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_all(self, client: Sent) -> None:
        response = client.calls.participants.with_raw_response.remove_all(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = response.parse()
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_all(self, client: Sent) -> None:
        with client.calls.participants.with_streaming_response.remove_all(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = response.parse()
            assert participant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove_all(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.calls.participants.with_raw_response.remove_all(
                id="",
            )


class TestAsyncParticipants:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSent) -> None:
        participant = await async_client.calls.participants.update(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSent) -> None:
        participant = await async_client.calls.participants.update(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
            muted=True,
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSent) -> None:
        response = await async_client.calls.participants.with_raw_response.update(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSent) -> None:
        async with async_client.calls.participants.with_streaming_response.update(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert participant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.calls.participants.with_raw_response.update(
                participant_id="call_9f2ab000-0000-4000-8000-000000000002",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            await async_client.calls.participants.with_raw_response.update(
                participant_id="",
                id="call_9f2ab000-0000-4000-8000-000000000001",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSent) -> None:
        participant = await async_client.calls.participants.list(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert_matches_type(APIResponseOfListOfCallParticipant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSent) -> None:
        participant = await async_client.calls.participants.list(
            id="call_9f2ab000-0000-4000-8000-000000000001",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfListOfCallParticipant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSent) -> None:
        response = await async_client.calls.participants.with_raw_response.list(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(APIResponseOfListOfCallParticipant, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSent) -> None:
        async with async_client.calls.participants.with_streaming_response.list(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(APIResponseOfListOfCallParticipant, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.calls.participants.with_raw_response.list(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncSent) -> None:
        participant = await async_client.calls.participants.add(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert_matches_type(APIResponseOfCall, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncSent) -> None:
        participant = await async_client.calls.participants.add(
            id="call_9f2ab000-0000-4000-8000-000000000001",
            caller_id="+12025550123",
            sandbox=False,
            to={
                "kind": "number",
                "value": "+14155551234",
            },
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfCall, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncSent) -> None:
        response = await async_client.calls.participants.with_raw_response.add(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert_matches_type(APIResponseOfCall, participant, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncSent) -> None:
        async with async_client.calls.participants.with_streaming_response.add(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert_matches_type(APIResponseOfCall, participant, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.calls.participants.with_raw_response.add(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncSent) -> None:
        participant = await async_client.calls.participants.remove(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncSent) -> None:
        participant = await async_client.calls.participants.remove(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
            sandbox=False,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncSent) -> None:
        response = await async_client.calls.participants.with_raw_response.remove(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncSent) -> None:
        async with async_client.calls.participants.with_streaming_response.remove(
            participant_id="call_9f2ab000-0000-4000-8000-000000000002",
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert participant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.calls.participants.with_raw_response.remove(
                participant_id="call_9f2ab000-0000-4000-8000-000000000002",
                id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            await async_client.calls.participants.with_raw_response.remove(
                participant_id="",
                id="call_9f2ab000-0000-4000-8000-000000000001",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_all(self, async_client: AsyncSent) -> None:
        participant = await async_client.calls.participants.remove_all(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_all_with_all_params(self, async_client: AsyncSent) -> None:
        participant = await async_client.calls.participants.remove_all(
            id="call_9f2ab000-0000-4000-8000-000000000001",
            sandbox=False,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_all(self, async_client: AsyncSent) -> None:
        response = await async_client.calls.participants.with_raw_response.remove_all(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        participant = await response.parse()
        assert participant is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_all(self, async_client: AsyncSent) -> None:
        async with async_client.calls.participants.with_streaming_response.remove_all(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            participant = await response.parse()
            assert participant is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove_all(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.calls.participants.with_raw_response.remove_all(
                id="",
            )
