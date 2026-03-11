# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import SentDm, AsyncSentDm
from tests.utils import assert_matches_type
from sent_dm.types import NumberLookupResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNumbers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup(self, client: SentDm) -> None:
        number = client.numbers.lookup(
            phone_number="+12025551234",
        )
        assert_matches_type(NumberLookupResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_lookup_with_all_params(self, client: SentDm) -> None:
        number = client.numbers.lookup(
            phone_number="+12025551234",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NumberLookupResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_lookup(self, client: SentDm) -> None:
        response = client.numbers.with_raw_response.lookup(
            phone_number="+12025551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = response.parse()
        assert_matches_type(NumberLookupResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_lookup(self, client: SentDm) -> None:
        with client.numbers.with_streaming_response.lookup(
            phone_number="+12025551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = response.parse()
            assert_matches_type(NumberLookupResponse, number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_lookup(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.numbers.with_raw_response.lookup(
                phone_number="",
            )


class TestAsyncNumbers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup(self, async_client: AsyncSentDm) -> None:
        number = await async_client.numbers.lookup(
            phone_number="+12025551234",
        )
        assert_matches_type(NumberLookupResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_lookup_with_all_params(self, async_client: AsyncSentDm) -> None:
        number = await async_client.numbers.lookup(
            phone_number="+12025551234",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NumberLookupResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_lookup(self, async_client: AsyncSentDm) -> None:
        response = await async_client.numbers.with_raw_response.lookup(
            phone_number="+12025551234",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        number = await response.parse()
        assert_matches_type(NumberLookupResponse, number, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_lookup(self, async_client: AsyncSentDm) -> None:
        async with async_client.numbers.with_streaming_response.lookup(
            phone_number="+12025551234",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            number = await response.parse()
            assert_matches_type(NumberLookupResponse, number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_lookup(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.numbers.with_raw_response.lookup(
                phone_number="",
            )
