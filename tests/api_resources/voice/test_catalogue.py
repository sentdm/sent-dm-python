# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types.voice import APIResponseOfVoiceCatalogue

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCatalogue:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Sent) -> None:
        catalogue = client.voice.catalogue.list()
        assert_matches_type(APIResponseOfVoiceCatalogue, catalogue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Sent) -> None:
        catalogue = client.voice.catalogue.list(
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfVoiceCatalogue, catalogue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Sent) -> None:
        response = client.voice.catalogue.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalogue = response.parse()
        assert_matches_type(APIResponseOfVoiceCatalogue, catalogue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Sent) -> None:
        with client.voice.catalogue.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalogue = response.parse()
            assert_matches_type(APIResponseOfVoiceCatalogue, catalogue, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCatalogue:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSent) -> None:
        catalogue = await async_client.voice.catalogue.list()
        assert_matches_type(APIResponseOfVoiceCatalogue, catalogue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSent) -> None:
        catalogue = await async_client.voice.catalogue.list(
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfVoiceCatalogue, catalogue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSent) -> None:
        response = await async_client.voice.catalogue.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        catalogue = await response.parse()
        assert_matches_type(APIResponseOfVoiceCatalogue, catalogue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSent) -> None:
        async with async_client.voice.catalogue.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            catalogue = await response.parse()
            assert_matches_type(APIResponseOfVoiceCatalogue, catalogue, path=["response"])

        assert cast(Any, response.is_closed) is True
