# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types.channels import (
    APIResponseOfVoiceToken,
    APIResponseOfVoiceNumber,
    APIResponseOfVoiceSecret,
    APIResponseOfListOfVoiceNumber,
    APIResponseOfVoiceCallbackTest,
    APIResponseOfVoiceNumberCreated,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Sent) -> None:
        voice = client.channels.voice.create(
            callback_url="https://example.com/voice",
        )
        assert_matches_type(APIResponseOfVoiceNumberCreated, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Sent) -> None:
        voice = client.channels.voice.create(
            callback_url="https://example.com/voice",
            area_code=None,
            default_for_app_calls=False,
            number="+12125550100",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfVoiceNumberCreated, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Sent) -> None:
        response = client.channels.voice.with_raw_response.create(
            callback_url="https://example.com/voice",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(APIResponseOfVoiceNumberCreated, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Sent) -> None:
        with client.channels.voice.with_streaming_response.create(
            callback_url="https://example.com/voice",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(APIResponseOfVoiceNumberCreated, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Sent) -> None:
        voice = client.channels.voice.retrieve(
            number="+12125550100",
        )
        assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Sent) -> None:
        voice = client.channels.voice.retrieve(
            number="+12125550100",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Sent) -> None:
        response = client.channels.voice.with_raw_response.retrieve(
            number="+12125550100",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Sent) -> None:
        with client.channels.voice.with_streaming_response.retrieve(
            number="+12125550100",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number` but received ''"):
            client.channels.voice.with_raw_response.retrieve(
                number="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Sent) -> None:
        voice = client.channels.voice.update(
            number="+12125550100",
        )
        assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Sent) -> None:
        voice = client.channels.voice.update(
            number="+12125550100",
            callback_url="https://example.com/voice",
            default_for_app_calls=True,
            sandbox=False,
            status="ACTIVE",
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Sent) -> None:
        response = client.channels.voice.with_raw_response.update(
            number="+12125550100",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Sent) -> None:
        with client.channels.voice.with_streaming_response.update(
            number="+12125550100",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number` but received ''"):
            client.channels.voice.with_raw_response.update(
                number="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Sent) -> None:
        voice = client.channels.voice.list()
        assert_matches_type(APIResponseOfListOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Sent) -> None:
        voice = client.channels.voice.list(
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfListOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Sent) -> None:
        response = client.channels.voice.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(APIResponseOfListOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Sent) -> None:
        with client.channels.voice.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(APIResponseOfListOfVoiceNumber, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_token(self, client: Sent) -> None:
        voice = client.channels.voice.create_token()
        assert_matches_type(APIResponseOfVoiceToken, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_token_with_all_params(self, client: Sent) -> None:
        voice = client.channels.voice.create_token(
            identity="agent-42",
            number="+12025550123",
            sandbox=False,
            ttl=600,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfVoiceToken, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_token(self, client: Sent) -> None:
        response = client.channels.voice.with_raw_response.create_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(APIResponseOfVoiceToken, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_token(self, client: Sent) -> None:
        with client.channels.voice.with_streaming_response.create_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(APIResponseOfVoiceToken, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rotate_secret(self, client: Sent) -> None:
        voice = client.channels.voice.rotate_secret(
            number="+12125550100",
        )
        assert_matches_type(APIResponseOfVoiceSecret, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rotate_secret_with_all_params(self, client: Sent) -> None:
        voice = client.channels.voice.rotate_secret(
            number="+12125550100",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfVoiceSecret, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rotate_secret(self, client: Sent) -> None:
        response = client.channels.voice.with_raw_response.rotate_secret(
            number="+12125550100",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(APIResponseOfVoiceSecret, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rotate_secret(self, client: Sent) -> None:
        with client.channels.voice.with_streaming_response.rotate_secret(
            number="+12125550100",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(APIResponseOfVoiceSecret, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rotate_secret(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number` but received ''"):
            client.channels.voice.with_raw_response.rotate_secret(
                number="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test(self, client: Sent) -> None:
        voice = client.channels.voice.test(
            number="+12025550123",
        )
        assert_matches_type(APIResponseOfVoiceCallbackTest, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test_with_all_params(self, client: Sent) -> None:
        voice = client.channels.voice.test(
            number="+12025550123",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfVoiceCallbackTest, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test(self, client: Sent) -> None:
        response = client.channels.voice.with_raw_response.test(
            number="+12025550123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(APIResponseOfVoiceCallbackTest, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test(self, client: Sent) -> None:
        with client.channels.voice.with_streaming_response.test(
            number="+12025550123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(APIResponseOfVoiceCallbackTest, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number` but received ''"):
            client.channels.voice.with_raw_response.test(
                number="",
            )


class TestAsyncVoice:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSent) -> None:
        voice = await async_client.channels.voice.create(
            callback_url="https://example.com/voice",
        )
        assert_matches_type(APIResponseOfVoiceNumberCreated, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSent) -> None:
        voice = await async_client.channels.voice.create(
            callback_url="https://example.com/voice",
            area_code=None,
            default_for_app_calls=False,
            number="+12125550100",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfVoiceNumberCreated, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.voice.with_raw_response.create(
            callback_url="https://example.com/voice",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(APIResponseOfVoiceNumberCreated, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSent) -> None:
        async with async_client.channels.voice.with_streaming_response.create(
            callback_url="https://example.com/voice",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(APIResponseOfVoiceNumberCreated, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSent) -> None:
        voice = await async_client.channels.voice.retrieve(
            number="+12125550100",
        )
        assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSent) -> None:
        voice = await async_client.channels.voice.retrieve(
            number="+12125550100",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.voice.with_raw_response.retrieve(
            number="+12125550100",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSent) -> None:
        async with async_client.channels.voice.with_streaming_response.retrieve(
            number="+12125550100",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number` but received ''"):
            await async_client.channels.voice.with_raw_response.retrieve(
                number="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSent) -> None:
        voice = await async_client.channels.voice.update(
            number="+12125550100",
        )
        assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSent) -> None:
        voice = await async_client.channels.voice.update(
            number="+12125550100",
            callback_url="https://example.com/voice",
            default_for_app_calls=True,
            sandbox=False,
            status="ACTIVE",
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.voice.with_raw_response.update(
            number="+12125550100",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSent) -> None:
        async with async_client.channels.voice.with_streaming_response.update(
            number="+12125550100",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(APIResponseOfVoiceNumber, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number` but received ''"):
            await async_client.channels.voice.with_raw_response.update(
                number="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSent) -> None:
        voice = await async_client.channels.voice.list()
        assert_matches_type(APIResponseOfListOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSent) -> None:
        voice = await async_client.channels.voice.list(
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfListOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.voice.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(APIResponseOfListOfVoiceNumber, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSent) -> None:
        async with async_client.channels.voice.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(APIResponseOfListOfVoiceNumber, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_token(self, async_client: AsyncSent) -> None:
        voice = await async_client.channels.voice.create_token()
        assert_matches_type(APIResponseOfVoiceToken, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_token_with_all_params(self, async_client: AsyncSent) -> None:
        voice = await async_client.channels.voice.create_token(
            identity="agent-42",
            number="+12025550123",
            sandbox=False,
            ttl=600,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfVoiceToken, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_token(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.voice.with_raw_response.create_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(APIResponseOfVoiceToken, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_token(self, async_client: AsyncSent) -> None:
        async with async_client.channels.voice.with_streaming_response.create_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(APIResponseOfVoiceToken, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rotate_secret(self, async_client: AsyncSent) -> None:
        voice = await async_client.channels.voice.rotate_secret(
            number="+12125550100",
        )
        assert_matches_type(APIResponseOfVoiceSecret, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rotate_secret_with_all_params(self, async_client: AsyncSent) -> None:
        voice = await async_client.channels.voice.rotate_secret(
            number="+12125550100",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfVoiceSecret, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rotate_secret(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.voice.with_raw_response.rotate_secret(
            number="+12125550100",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(APIResponseOfVoiceSecret, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rotate_secret(self, async_client: AsyncSent) -> None:
        async with async_client.channels.voice.with_streaming_response.rotate_secret(
            number="+12125550100",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(APIResponseOfVoiceSecret, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rotate_secret(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number` but received ''"):
            await async_client.channels.voice.with_raw_response.rotate_secret(
                number="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test(self, async_client: AsyncSent) -> None:
        voice = await async_client.channels.voice.test(
            number="+12025550123",
        )
        assert_matches_type(APIResponseOfVoiceCallbackTest, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test_with_all_params(self, async_client: AsyncSent) -> None:
        voice = await async_client.channels.voice.test(
            number="+12025550123",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfVoiceCallbackTest, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.voice.with_raw_response.test(
            number="+12025550123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(APIResponseOfVoiceCallbackTest, voice, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncSent) -> None:
        async with async_client.channels.voice.with_streaming_response.test(
            number="+12025550123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(APIResponseOfVoiceCallbackTest, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `number` but received ''"):
            await async_client.channels.voice.with_raw_response.test(
                number="",
            )
