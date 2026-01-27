# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import SentDm, AsyncSentDm
from tests.utils import assert_matches_type
from sent_dm.types import (
    MessageRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: SentDm) -> None:
        message = client.messages.retrieve(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: SentDm) -> None:
        response = client.messages.with_raw_response.retrieve(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: SentDm) -> None:
        with client.messages.with_streaming_response.retrieve(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageRetrieveResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_quick_message(self, client: SentDm) -> None:
        message = client.messages.send_quick_message(
            custom_message="Hello, this is a test message!",
            phone_number="+1234567890",
        )
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_quick_message(self, client: SentDm) -> None:
        response = client.messages.with_raw_response.send_quick_message(
            custom_message="Hello, this is a test message!",
            phone_number="+1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_quick_message(self, client: SentDm) -> None:
        with client.messages.with_streaming_response.send_quick_message(
            custom_message="Hello, this is a test message!",
            phone_number="+1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_to_contact(self, client: SentDm) -> None:
        message = client.messages.send_to_contact(
            contact_id="6ba7b810-9dad-11d1-80b4-00c04fd430c8",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_to_contact_with_all_params(self, client: SentDm) -> None:
        message = client.messages.send_to_contact(
            contact_id="6ba7b810-9dad-11d1-80b4-00c04fd430c8",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
            template_variables={
                "name": "John Doe",
                "order_id": "12345",
            },
        )
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_to_contact(self, client: SentDm) -> None:
        response = client.messages.with_raw_response.send_to_contact(
            contact_id="6ba7b810-9dad-11d1-80b4-00c04fd430c8",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_to_contact(self, client: SentDm) -> None:
        with client.messages.with_streaming_response.send_to_contact(
            contact_id="6ba7b810-9dad-11d1-80b4-00c04fd430c8",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_to_phone(self, client: SentDm) -> None:
        message = client.messages.send_to_phone(
            phone_number="+1234567890",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_to_phone_with_all_params(self, client: SentDm) -> None:
        message = client.messages.send_to_phone(
            phone_number="+1234567890",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
            template_variables={
                "name": "John Doe",
                "order_id": "12345",
            },
        )
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_to_phone(self, client: SentDm) -> None:
        response = client.messages.with_raw_response.send_to_phone(
            phone_number="+1234567890",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_to_phone(self, client: SentDm) -> None:
        with client.messages.with_streaming_response.send_to_phone(
            phone_number="+1234567890",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSentDm) -> None:
        message = await async_client.messages.retrieve(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSentDm) -> None:
        response = await async_client.messages.with_raw_response.retrieve(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSentDm) -> None:
        async with async_client.messages.with_streaming_response.retrieve(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageRetrieveResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.messages.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_quick_message(self, async_client: AsyncSentDm) -> None:
        message = await async_client.messages.send_quick_message(
            custom_message="Hello, this is a test message!",
            phone_number="+1234567890",
        )
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_quick_message(self, async_client: AsyncSentDm) -> None:
        response = await async_client.messages.with_raw_response.send_quick_message(
            custom_message="Hello, this is a test message!",
            phone_number="+1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_quick_message(self, async_client: AsyncSentDm) -> None:
        async with async_client.messages.with_streaming_response.send_quick_message(
            custom_message="Hello, this is a test message!",
            phone_number="+1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_to_contact(self, async_client: AsyncSentDm) -> None:
        message = await async_client.messages.send_to_contact(
            contact_id="6ba7b810-9dad-11d1-80b4-00c04fd430c8",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_to_contact_with_all_params(self, async_client: AsyncSentDm) -> None:
        message = await async_client.messages.send_to_contact(
            contact_id="6ba7b810-9dad-11d1-80b4-00c04fd430c8",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
            template_variables={
                "name": "John Doe",
                "order_id": "12345",
            },
        )
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_to_contact(self, async_client: AsyncSentDm) -> None:
        response = await async_client.messages.with_raw_response.send_to_contact(
            contact_id="6ba7b810-9dad-11d1-80b4-00c04fd430c8",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_to_contact(self, async_client: AsyncSentDm) -> None:
        async with async_client.messages.with_streaming_response.send_to_contact(
            contact_id="6ba7b810-9dad-11d1-80b4-00c04fd430c8",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_to_phone(self, async_client: AsyncSentDm) -> None:
        message = await async_client.messages.send_to_phone(
            phone_number="+1234567890",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_to_phone_with_all_params(self, async_client: AsyncSentDm) -> None:
        message = await async_client.messages.send_to_phone(
            phone_number="+1234567890",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
            template_variables={
                "name": "John Doe",
                "order_id": "12345",
            },
        )
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_to_phone(self, async_client: AsyncSentDm) -> None:
        response = await async_client.messages.with_raw_response.send_to_phone(
            phone_number="+1234567890",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert message is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_to_phone(self, async_client: AsyncSentDm) -> None:
        async with async_client.messages.with_streaming_response.send_to_phone(
            phone_number="+1234567890",
            template_id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True
