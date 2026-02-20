# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import SentDm, AsyncSentDm
from tests.utils import assert_matches_type
from sent_dm.types import (
    UserListResponse,
    APIResponseOfUser,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: SentDm) -> None:
        user = client.users.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: SentDm) -> None:
        response = client.users.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: SentDm) -> None:
        with client.users.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(APIResponseOfUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: SentDm) -> None:
        user = client.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: SentDm) -> None:
        response = client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: SentDm) -> None:
        with client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_invite(self, client: SentDm) -> None:
        user = client.users.invite()
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_invite_with_all_params(self, client: SentDm) -> None:
        user = client.users.invite(
            email="newuser@example.com",
            name="New User",
            role="developer",
            test_mode=False,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_invite(self, client: SentDm) -> None:
        response = client.users.with_raw_response.invite()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_invite(self, client: SentDm) -> None:
        with client.users.with_streaming_response.invite() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(APIResponseOfUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: SentDm) -> None:
        user = client.users.remove(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_with_all_params(self, client: SentDm) -> None:
        user = client.users.remove(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_mode=False,
            body_user_id="aa0e8400-e29b-41d4-a716-446655440005",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: SentDm) -> None:
        response = client.users.with_raw_response.remove(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: SentDm) -> None:
        with client.users.with_streaming_response.remove(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_user_id` but received ''"):
            client.users.with_raw_response.remove(
                path_user_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_role(self, client: SentDm) -> None:
        user = client.users.update_role(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_role_with_all_params(self, client: SentDm) -> None:
        user = client.users.update_role(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="billing",
            test_mode=False,
            body_user_id="aa0e8400-e29b-41d4-a716-446655440005",
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_role(self, client: SentDm) -> None:
        response = client.users.with_raw_response.update_role(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_role(self, client: SentDm) -> None:
        with client.users.with_streaming_response.update_role(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(APIResponseOfUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_role(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_user_id` but received ''"):
            client.users.with_raw_response.update_role(
                path_user_id="",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSentDm) -> None:
        user = await async_client.users.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSentDm) -> None:
        response = await async_client.users.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSentDm) -> None:
        async with async_client.users.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(APIResponseOfUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSentDm) -> None:
        user = await async_client.users.list()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSentDm) -> None:
        response = await async_client.users.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSentDm) -> None:
        async with async_client.users.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_invite(self, async_client: AsyncSentDm) -> None:
        user = await async_client.users.invite()
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_invite_with_all_params(self, async_client: AsyncSentDm) -> None:
        user = await async_client.users.invite(
            email="newuser@example.com",
            name="New User",
            role="developer",
            test_mode=False,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_invite(self, async_client: AsyncSentDm) -> None:
        response = await async_client.users.with_raw_response.invite()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_invite(self, async_client: AsyncSentDm) -> None:
        async with async_client.users.with_streaming_response.invite() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(APIResponseOfUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncSentDm) -> None:
        user = await async_client.users.remove(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncSentDm) -> None:
        user = await async_client.users.remove(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            test_mode=False,
            body_user_id="aa0e8400-e29b-41d4-a716-446655440005",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncSentDm) -> None:
        response = await async_client.users.with_raw_response.remove(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncSentDm) -> None:
        async with async_client.users.with_streaming_response.remove(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_user_id` but received ''"):
            await async_client.users.with_raw_response.remove(
                path_user_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_role(self, async_client: AsyncSentDm) -> None:
        user = await async_client.users.update_role(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_role_with_all_params(self, async_client: AsyncSentDm) -> None:
        user = await async_client.users.update_role(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="billing",
            test_mode=False,
            body_user_id="aa0e8400-e29b-41d4-a716-446655440005",
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_role(self, async_client: AsyncSentDm) -> None:
        response = await async_client.users.with_raw_response.update_role(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(APIResponseOfUser, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_role(self, async_client: AsyncSentDm) -> None:
        async with async_client.users.with_streaming_response.update_role(
            path_user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(APIResponseOfUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_role(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_user_id` but received ''"):
            await async_client.users.with_raw_response.update_role(
                path_user_id="",
            )
