# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import SentDm, AsyncSentDm
from tests.utils import assert_matches_type
from sent_dm.types import (
    ContactListItem,
    ContactListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: SentDm) -> None:
        contact = client.contacts.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: SentDm) -> None:
        response = client.contacts.with_raw_response.list(
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: SentDm) -> None:
        with client.contacts.with_streaming_response.list(
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_by_phone(self, client: SentDm) -> None:
        contact = client.contacts.retrieve_by_phone(
            phone_number="phoneNumber",
        )
        assert_matches_type(ContactListItem, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_by_phone(self, client: SentDm) -> None:
        response = client.contacts.with_raw_response.retrieve_by_phone(
            phone_number="phoneNumber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactListItem, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_by_phone(self, client: SentDm) -> None:
        with client.contacts.with_streaming_response.retrieve_by_phone(
            phone_number="phoneNumber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactListItem, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_id(self, client: SentDm) -> None:
        contact = client.contacts.retrieve_id(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ContactListItem, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_id(self, client: SentDm) -> None:
        response = client.contacts.with_raw_response.retrieve_id(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactListItem, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_id(self, client: SentDm) -> None:
        with client.contacts.with_streaming_response.retrieve_id(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactListItem, contact, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncContacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSentDm) -> None:
        contact = await async_client.contacts.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSentDm) -> None:
        response = await async_client.contacts.with_raw_response.list(
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSentDm) -> None:
        async with async_client.contacts.with_streaming_response.list(
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_by_phone(self, async_client: AsyncSentDm) -> None:
        contact = await async_client.contacts.retrieve_by_phone(
            phone_number="phoneNumber",
        )
        assert_matches_type(ContactListItem, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_by_phone(self, async_client: AsyncSentDm) -> None:
        response = await async_client.contacts.with_raw_response.retrieve_by_phone(
            phone_number="phoneNumber",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactListItem, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_by_phone(self, async_client: AsyncSentDm) -> None:
        async with async_client.contacts.with_streaming_response.retrieve_by_phone(
            phone_number="phoneNumber",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactListItem, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_id(self, async_client: AsyncSentDm) -> None:
        contact = await async_client.contacts.retrieve_id(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ContactListItem, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_id(self, async_client: AsyncSentDm) -> None:
        response = await async_client.contacts.with_raw_response.retrieve_id(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactListItem, contact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_id(self, async_client: AsyncSentDm) -> None:
        async with async_client.contacts.with_streaming_response.retrieve_id(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactListItem, contact, path=["response"])

        assert cast(Any, response.is_closed) is True
