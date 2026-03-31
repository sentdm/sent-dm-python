# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types import (
    MessageSendResponse,
    MessageRetrieveStatusResponse,
    MessageRetrieveActivitiesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_activities(self, client: Sent) -> None:
        message = client.messages.retrieve_activities(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
        )
        assert_matches_type(MessageRetrieveActivitiesResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_activities_with_all_params(self, client: Sent) -> None:
        message = client.messages.retrieve_activities(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessageRetrieveActivitiesResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_activities(self, client: Sent) -> None:
        response = client.messages.with_raw_response.retrieve_activities(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageRetrieveActivitiesResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_activities(self, client: Sent) -> None:
        with client.messages.with_streaming_response.retrieve_activities(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageRetrieveActivitiesResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_activities(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messages.with_raw_response.retrieve_activities(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: Sent) -> None:
        message = client.messages.retrieve_status(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
        )
        assert_matches_type(MessageRetrieveStatusResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status_with_all_params(self, client: Sent) -> None:
        message = client.messages.retrieve_status(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessageRetrieveStatusResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: Sent) -> None:
        response = client.messages.with_raw_response.retrieve_status(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageRetrieveStatusResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: Sent) -> None:
        with client.messages.with_streaming_response.retrieve_status(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageRetrieveStatusResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_status(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messages.with_raw_response.retrieve_status(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: Sent) -> None:
        message = client.messages.send()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: Sent) -> None:
        message = client.messages.send(
            channel=["sms", "whatsapp"],
            sandbox=False,
            template={
                "id": "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
                "name": "order_confirmation",
                "parameters": {
                    "name": "John Doe",
                    "order_id": "12345",
                },
            },
            to=["+14155551234", "+14155555678"],
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Sent) -> None:
        response = client.messages.with_raw_response.send()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Sent) -> None:
        with client.messages.with_streaming_response.send() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageSendResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_activities(self, async_client: AsyncSent) -> None:
        message = await async_client.messages.retrieve_activities(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
        )
        assert_matches_type(MessageRetrieveActivitiesResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_activities_with_all_params(self, async_client: AsyncSent) -> None:
        message = await async_client.messages.retrieve_activities(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessageRetrieveActivitiesResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_activities(self, async_client: AsyncSent) -> None:
        response = await async_client.messages.with_raw_response.retrieve_activities(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageRetrieveActivitiesResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_activities(self, async_client: AsyncSent) -> None:
        async with async_client.messages.with_streaming_response.retrieve_activities(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageRetrieveActivitiesResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_activities(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messages.with_raw_response.retrieve_activities(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncSent) -> None:
        message = await async_client.messages.retrieve_status(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
        )
        assert_matches_type(MessageRetrieveStatusResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status_with_all_params(self, async_client: AsyncSent) -> None:
        message = await async_client.messages.retrieve_status(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessageRetrieveStatusResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncSent) -> None:
        response = await async_client.messages.with_raw_response.retrieve_status(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageRetrieveStatusResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncSent) -> None:
        async with async_client.messages.with_streaming_response.retrieve_status(
            id="8ba7b830-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageRetrieveStatusResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messages.with_raw_response.retrieve_status(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncSent) -> None:
        message = await async_client.messages.send()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncSent) -> None:
        message = await async_client.messages.send(
            channel=["sms", "whatsapp"],
            sandbox=False,
            template={
                "id": "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
                "name": "order_confirmation",
                "parameters": {
                    "name": "John Doe",
                    "order_id": "12345",
                },
            },
            to=["+14155551234", "+14155555678"],
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncSent) -> None:
        response = await async_client.messages.with_raw_response.send()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncSent) -> None:
        async with async_client.messages.with_streaming_response.send() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageSendResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True
