# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import SentDm, AsyncSentDm
from tests.utils import assert_matches_type
from sent_dm.types import OrganizationListResponse, OrganizationRetrieveProfilesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: SentDm) -> None:
        organization = client.organizations.list()
        assert_matches_type(OrganizationListResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: SentDm) -> None:
        response = client.organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationListResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: SentDm) -> None:
        with client.organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationListResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_profiles(self, client: SentDm) -> None:
        organization = client.organizations.retrieve_profiles(
            "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
        )
        assert_matches_type(OrganizationRetrieveProfilesResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_profiles(self, client: SentDm) -> None:
        response = client.organizations.with_raw_response.retrieve_profiles(
            "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationRetrieveProfilesResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_profiles(self, client: SentDm) -> None:
        with client.organizations.with_streaming_response.retrieve_profiles(
            "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationRetrieveProfilesResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_profiles(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.organizations.with_raw_response.retrieve_profiles(
                "",
            )


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSentDm) -> None:
        organization = await async_client.organizations.list()
        assert_matches_type(OrganizationListResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSentDm) -> None:
        response = await async_client.organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationListResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSentDm) -> None:
        async with async_client.organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationListResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_profiles(self, async_client: AsyncSentDm) -> None:
        organization = await async_client.organizations.retrieve_profiles(
            "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
        )
        assert_matches_type(OrganizationRetrieveProfilesResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_profiles(self, async_client: AsyncSentDm) -> None:
        response = await async_client.organizations.with_raw_response.retrieve_profiles(
            "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationRetrieveProfilesResponse, organization, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_profiles(self, async_client: AsyncSentDm) -> None:
        async with async_client.organizations.with_streaming_response.retrieve_profiles(
            "6ba7b810-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationRetrieveProfilesResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_profiles(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.organizations.with_raw_response.retrieve_profiles(
                "",
            )
