# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types import (
    ConversationListResponse,
    ConversationListMessagesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConversations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Sent) -> None:
        conversation = client.conversations.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Sent) -> None:
        conversation = client.conversations.list(
            page=0,
            page_size=0,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Sent) -> None:
        response = client.conversations.with_raw_response.list(
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Sent) -> None:
        with client.conversations.with_streaming_response.list(
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationListResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_messages(self, client: Sent) -> None:
        conversation = client.conversations.list_messages(
            id="08fab313-c9e2-502c-975e-08b0356c432e",
            page=0,
            page_size=0,
        )
        assert_matches_type(ConversationListMessagesResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_messages_with_all_params(self, client: Sent) -> None:
        conversation = client.conversations.list_messages(
            id="08fab313-c9e2-502c-975e-08b0356c432e",
            page=0,
            page_size=0,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConversationListMessagesResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_messages(self, client: Sent) -> None:
        response = client.conversations.with_raw_response.list_messages(
            id="08fab313-c9e2-502c-975e-08b0356c432e",
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = response.parse()
        assert_matches_type(ConversationListMessagesResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_messages(self, client: Sent) -> None:
        with client.conversations.with_streaming_response.list_messages(
            id="08fab313-c9e2-502c-975e-08b0356c432e",
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = response.parse()
            assert_matches_type(ConversationListMessagesResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_messages(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.conversations.with_raw_response.list_messages(
                id="",
                page=0,
                page_size=0,
            )


class TestAsyncConversations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSent) -> None:
        conversation = await async_client.conversations.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSent) -> None:
        conversation = await async_client.conversations.list(
            page=0,
            page_size=0,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSent) -> None:
        response = await async_client.conversations.with_raw_response.list(
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationListResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSent) -> None:
        async with async_client.conversations.with_streaming_response.list(
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationListResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_messages(self, async_client: AsyncSent) -> None:
        conversation = await async_client.conversations.list_messages(
            id="08fab313-c9e2-502c-975e-08b0356c432e",
            page=0,
            page_size=0,
        )
        assert_matches_type(ConversationListMessagesResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_messages_with_all_params(self, async_client: AsyncSent) -> None:
        conversation = await async_client.conversations.list_messages(
            id="08fab313-c9e2-502c-975e-08b0356c432e",
            page=0,
            page_size=0,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConversationListMessagesResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_messages(self, async_client: AsyncSent) -> None:
        response = await async_client.conversations.with_raw_response.list_messages(
            id="08fab313-c9e2-502c-975e-08b0356c432e",
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation = await response.parse()
        assert_matches_type(ConversationListMessagesResponse, conversation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_messages(self, async_client: AsyncSent) -> None:
        async with async_client.conversations.with_streaming_response.list_messages(
            id="08fab313-c9e2-502c-975e-08b0356c432e",
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation = await response.parse()
            assert_matches_type(ConversationListMessagesResponse, conversation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_messages(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.conversations.with_raw_response.list_messages(
                id="",
                page=0,
                page_size=0,
            )
