# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types import (
    Call,
    APIResponseOfCall,
    APIResponseOfCallRecordings,
)
from sent_dm._utils import parse_datetime
from sent_dm.pagination import SyncCallsPage, AsyncCallsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Sent) -> None:
        call = client.calls.retrieve(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert_matches_type(APIResponseOfCall, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Sent) -> None:
        call = client.calls.retrieve(
            id="call_9f2ab000-0000-4000-8000-000000000001",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfCall, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Sent) -> None:
        response = client.calls.with_raw_response.retrieve(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(APIResponseOfCall, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Sent) -> None:
        with client.calls.with_streaming_response.retrieve(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(APIResponseOfCall, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.calls.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Sent) -> None:
        call = client.calls.list()
        assert_matches_type(SyncCallsPage[Call], call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Sent) -> None:
        call = client.calls.list(
            direction="direction",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            number="number",
            page=0,
            page_size=0,
            status="status",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncCallsPage[Call], call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Sent) -> None:
        response = client.calls.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(SyncCallsPage[Call], call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Sent) -> None:
        with client.calls.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(SyncCallsPage[Call], call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_hangup(self, client: Sent) -> None:
        call = client.calls.hangup(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert call is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_hangup_with_all_params(self, client: Sent) -> None:
        call = client.calls.hangup(
            id="call_9f2ab000-0000-4000-8000-000000000001",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert call is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_hangup(self, client: Sent) -> None:
        response = client.calls.with_raw_response.hangup(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert call is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_hangup(self, client: Sent) -> None:
        with client.calls.with_streaming_response.hangup(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert call is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_hangup(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.calls.with_raw_response.hangup(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_recordings(self, client: Sent) -> None:
        call = client.calls.list_recordings(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert_matches_type(APIResponseOfCallRecordings, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_recordings_with_all_params(self, client: Sent) -> None:
        call = client.calls.list_recordings(
            id="call_9f2ab000-0000-4000-8000-000000000001",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfCallRecordings, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_recordings(self, client: Sent) -> None:
        response = client.calls.with_raw_response.list_recordings(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(APIResponseOfCallRecordings, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_recordings(self, client: Sent) -> None:
        with client.calls.with_streaming_response.list_recordings(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(APIResponseOfCallRecordings, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_recordings(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.calls.with_raw_response.list_recordings(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_record(self, client: Sent) -> None:
        call = client.calls.record(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert call is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_record_with_all_params(self, client: Sent) -> None:
        call = client.calls.record(
            id="call_9f2ab000-0000-4000-8000-000000000001",
            action="start",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert call is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_record(self, client: Sent) -> None:
        response = client.calls.with_raw_response.record(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert call is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_record(self, client: Sent) -> None:
        with client.calls.with_streaming_response.record(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert call is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_record(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.calls.with_raw_response.record(
                id="",
            )


class TestAsyncCalls:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSent) -> None:
        call = await async_client.calls.retrieve(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert_matches_type(APIResponseOfCall, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSent) -> None:
        call = await async_client.calls.retrieve(
            id="call_9f2ab000-0000-4000-8000-000000000001",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfCall, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSent) -> None:
        response = await async_client.calls.with_raw_response.retrieve(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(APIResponseOfCall, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSent) -> None:
        async with async_client.calls.with_streaming_response.retrieve(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(APIResponseOfCall, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.calls.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSent) -> None:
        call = await async_client.calls.list()
        assert_matches_type(AsyncCallsPage[Call], call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSent) -> None:
        call = await async_client.calls.list(
            direction="direction",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            number="number",
            page=0,
            page_size=0,
            status="status",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncCallsPage[Call], call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSent) -> None:
        response = await async_client.calls.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(AsyncCallsPage[Call], call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSent) -> None:
        async with async_client.calls.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(AsyncCallsPage[Call], call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_hangup(self, async_client: AsyncSent) -> None:
        call = await async_client.calls.hangup(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert call is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_hangup_with_all_params(self, async_client: AsyncSent) -> None:
        call = await async_client.calls.hangup(
            id="call_9f2ab000-0000-4000-8000-000000000001",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert call is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_hangup(self, async_client: AsyncSent) -> None:
        response = await async_client.calls.with_raw_response.hangup(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert call is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_hangup(self, async_client: AsyncSent) -> None:
        async with async_client.calls.with_streaming_response.hangup(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert call is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_hangup(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.calls.with_raw_response.hangup(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_recordings(self, async_client: AsyncSent) -> None:
        call = await async_client.calls.list_recordings(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert_matches_type(APIResponseOfCallRecordings, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_recordings_with_all_params(self, async_client: AsyncSent) -> None:
        call = await async_client.calls.list_recordings(
            id="call_9f2ab000-0000-4000-8000-000000000001",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfCallRecordings, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_recordings(self, async_client: AsyncSent) -> None:
        response = await async_client.calls.with_raw_response.list_recordings(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(APIResponseOfCallRecordings, call, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_recordings(self, async_client: AsyncSent) -> None:
        async with async_client.calls.with_streaming_response.list_recordings(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(APIResponseOfCallRecordings, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_recordings(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.calls.with_raw_response.list_recordings(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_record(self, async_client: AsyncSent) -> None:
        call = await async_client.calls.record(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )
        assert call is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_record_with_all_params(self, async_client: AsyncSent) -> None:
        call = await async_client.calls.record(
            id="call_9f2ab000-0000-4000-8000-000000000001",
            action="start",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert call is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_record(self, async_client: AsyncSent) -> None:
        response = await async_client.calls.with_raw_response.record(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert call is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_record(self, async_client: AsyncSent) -> None:
        async with async_client.calls.with_streaming_response.record(
            id="call_9f2ab000-0000-4000-8000-000000000001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert call is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_record(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.calls.with_raw_response.record(
                id="",
            )
