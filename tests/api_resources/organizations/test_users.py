# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import SentDm, AsyncSentDm
from tests.utils import assert_matches_type
from sent_dm.types.organizations import (
    CustomerUser,
    UserListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: SentDm) -> None:
        user = client.organizations.users.retrieve(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: SentDm) -> None:
        response = client.organizations.users.with_raw_response.retrieve(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: SentDm) -> None:
        with client.organizations.users.with_streaming_response.retrieve(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(CustomerUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.organizations.users.with_raw_response.retrieve(
                user_id="650e8400-e29b-41d4-a716-446655440000",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.organizations.users.with_raw_response.retrieve(
                user_id="",
                customer_id="550e8400-e29b-41d4-a716-446655440000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: SentDm) -> None:
        user = client.organizations.users.list(
            customer_id="550e8400-e29b-41d4-a716-446655440000",
            page=0,
            page_size=0,
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: SentDm) -> None:
        response = client.organizations.users.with_raw_response.list(
            customer_id="550e8400-e29b-41d4-a716-446655440000",
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: SentDm) -> None:
        with client.organizations.users.with_streaming_response.list(
            customer_id="550e8400-e29b-41d4-a716-446655440000",
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.organizations.users.with_raw_response.list(
                customer_id="",
                page=0,
                page_size=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: SentDm) -> None:
        user = client.organizations.users.delete(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: SentDm) -> None:
        response = client.organizations.users.with_raw_response.delete(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: SentDm) -> None:
        with client.organizations.users.with_streaming_response.delete(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.organizations.users.with_raw_response.delete(
                user_id="650e8400-e29b-41d4-a716-446655440000",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.organizations.users.with_raw_response.delete(
                user_id="",
                customer_id="550e8400-e29b-41d4-a716-446655440000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_invite(self, client: SentDm) -> None:
        user = client.organizations.users.invite(
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_invite_with_all_params(self, client: SentDm) -> None:
        user = client.organizations.users.invite(
            customer_id="550e8400-e29b-41d4-a716-446655440000",
            email="user@example.com",
            invited_by="650e8400-e29b-41d4-a716-446655440000",
            name="John Doe",
            role="admin",
        )
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_invite(self, client: SentDm) -> None:
        response = client.organizations.users.with_raw_response.invite(
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_invite(self, client: SentDm) -> None:
        with client.organizations.users.with_streaming_response.invite(
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(CustomerUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_invite(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.organizations.users.with_raw_response.invite(
                customer_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_role(self, client: SentDm) -> None:
        user = client.organizations.users.update_role(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_role_with_all_params(self, client: SentDm) -> None:
        user = client.organizations.users.update_role(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
            role="admin",
        )
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_role(self, client: SentDm) -> None:
        response = client.organizations.users.with_raw_response.update_role(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_role(self, client: SentDm) -> None:
        with client.organizations.users.with_streaming_response.update_role(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(CustomerUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_role(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.organizations.users.with_raw_response.update_role(
                user_id="650e8400-e29b-41d4-a716-446655440000",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.organizations.users.with_raw_response.update_role(
                user_id="",
                customer_id="550e8400-e29b-41d4-a716-446655440000",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSentDm) -> None:
        user = await async_client.organizations.users.retrieve(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSentDm) -> None:
        response = await async_client.organizations.users.with_raw_response.retrieve(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSentDm) -> None:
        async with async_client.organizations.users.with_streaming_response.retrieve(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(CustomerUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.organizations.users.with_raw_response.retrieve(
                user_id="650e8400-e29b-41d4-a716-446655440000",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.organizations.users.with_raw_response.retrieve(
                user_id="",
                customer_id="550e8400-e29b-41d4-a716-446655440000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSentDm) -> None:
        user = await async_client.organizations.users.list(
            customer_id="550e8400-e29b-41d4-a716-446655440000",
            page=0,
            page_size=0,
        )
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSentDm) -> None:
        response = await async_client.organizations.users.with_raw_response.list(
            customer_id="550e8400-e29b-41d4-a716-446655440000",
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListResponse, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSentDm) -> None:
        async with async_client.organizations.users.with_streaming_response.list(
            customer_id="550e8400-e29b-41d4-a716-446655440000",
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.organizations.users.with_raw_response.list(
                customer_id="",
                page=0,
                page_size=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncSentDm) -> None:
        user = await async_client.organizations.users.delete(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSentDm) -> None:
        response = await async_client.organizations.users.with_raw_response.delete(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSentDm) -> None:
        async with async_client.organizations.users.with_streaming_response.delete(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.organizations.users.with_raw_response.delete(
                user_id="650e8400-e29b-41d4-a716-446655440000",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.organizations.users.with_raw_response.delete(
                user_id="",
                customer_id="550e8400-e29b-41d4-a716-446655440000",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_invite(self, async_client: AsyncSentDm) -> None:
        user = await async_client.organizations.users.invite(
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_invite_with_all_params(self, async_client: AsyncSentDm) -> None:
        user = await async_client.organizations.users.invite(
            customer_id="550e8400-e29b-41d4-a716-446655440000",
            email="user@example.com",
            invited_by="650e8400-e29b-41d4-a716-446655440000",
            name="John Doe",
            role="admin",
        )
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_invite(self, async_client: AsyncSentDm) -> None:
        response = await async_client.organizations.users.with_raw_response.invite(
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_invite(self, async_client: AsyncSentDm) -> None:
        async with async_client.organizations.users.with_streaming_response.invite(
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(CustomerUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_invite(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.organizations.users.with_raw_response.invite(
                customer_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_role(self, async_client: AsyncSentDm) -> None:
        user = await async_client.organizations.users.update_role(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_role_with_all_params(self, async_client: AsyncSentDm) -> None:
        user = await async_client.organizations.users.update_role(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
            role="admin",
        )
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_role(self, async_client: AsyncSentDm) -> None:
        response = await async_client.organizations.users.with_raw_response.update_role(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(CustomerUser, user, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_role(self, async_client: AsyncSentDm) -> None:
        async with async_client.organizations.users.with_streaming_response.update_role(
            user_id="650e8400-e29b-41d4-a716-446655440000",
            customer_id="550e8400-e29b-41d4-a716-446655440000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(CustomerUser, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_role(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.organizations.users.with_raw_response.update_role(
                user_id="650e8400-e29b-41d4-a716-446655440000",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.organizations.users.with_raw_response.update_role(
                user_id="",
                customer_id="550e8400-e29b-41d4-a716-446655440000",
            )
