# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import SentDm, AsyncSentDm
from tests.utils import assert_matches_type
from sent_dm.types import (
    BrandListResponse,
    APIResponseBrandWithKYC,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrands:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: SentDm) -> None:
        brand = client.brands.create(
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
            },
        )
        assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: SentDm) -> None:
        brand = client.brands.create(
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
                "brand_name": None,
                "business_legal_name": "Acme Corporation LLC",
                "business_name": "Acme Corp",
                "business_role": "CEO",
                "business_url": "https://acmecorp.com",
                "city": "New York",
                "contact_email": "john@acmecorp.com",
                "contact_phone": "+12025551234",
                "contact_phone_country_code": "1",
                "country": "US",
                "country_of_registration": "US",
                "destination_countries": [
                    {
                        "id": "US",
                        "is_main": False,
                    }
                ],
                "entity_type": "PRIVATE_PROFIT",
                "expected_messaging_volume": "10000",
                "is_tcr_application": True,
                "notes": None,
                "phone_number_prefix": "+1",
                "postal_code": "10001",
                "primary_use_case": "Customer notifications and appointment reminders",
                "state": "NY",
                "street": "123 Main Street",
                "tax_id": "12-3456789",
                "tax_id_type": "us_ein",
            },
            test_mode=False,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: SentDm) -> None:
        response = client.brands.with_raw_response.create(
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: SentDm) -> None:
        with client.brands.with_streaming_response.create(
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: SentDm) -> None:
        brand = client.brands.update(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
            },
        )
        assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: SentDm) -> None:
        brand = client.brands.update(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
                "brand_name": None,
                "business_legal_name": "Acme Corporation LLC",
                "business_name": "Acme Corp Updated",
                "business_role": "CTO",
                "business_url": None,
                "city": None,
                "contact_email": "john@acmecorp.com",
                "contact_phone": "+12025551234",
                "contact_phone_country_code": "1",
                "country": "US",
                "country_of_registration": None,
                "destination_countries": [
                    {
                        "id": "id",
                        "is_main": True,
                    }
                ],
                "entity_type": None,
                "expected_messaging_volume": None,
                "is_tcr_application": None,
                "notes": None,
                "phone_number_prefix": None,
                "postal_code": None,
                "primary_use_case": None,
                "state": None,
                "street": None,
                "tax_id": None,
                "tax_id_type": None,
            },
            test_mode=False,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: SentDm) -> None:
        response = client.brands.with_raw_response.update(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: SentDm) -> None:
        with client.brands.with_streaming_response.update(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brands.with_raw_response.update(
                brand_id="",
                brand={
                    "brand_relationship": "SMALL_ACCOUNT",
                    "contact_name": "John Smith",
                    "vertical": "PROFESSIONAL",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: SentDm) -> None:
        brand = client.brands.list()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: SentDm) -> None:
        response = client.brands.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: SentDm) -> None:
        with client.brands.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandListResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: SentDm) -> None:
        brand = client.brands.delete(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={},
        )
        assert brand is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: SentDm) -> None:
        brand = client.brands.delete(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={"test_mode": False},
        )
        assert brand is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: SentDm) -> None:
        response = client.brands.with_raw_response.delete(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert brand is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: SentDm) -> None:
        with client.brands.with_streaming_response.delete(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert brand is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brands.with_raw_response.delete(
                brand_id="",
                body={},
            )


class TestAsyncBrands:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSentDm) -> None:
        brand = await async_client.brands.create(
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
            },
        )
        assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSentDm) -> None:
        brand = await async_client.brands.create(
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
                "brand_name": None,
                "business_legal_name": "Acme Corporation LLC",
                "business_name": "Acme Corp",
                "business_role": "CEO",
                "business_url": "https://acmecorp.com",
                "city": "New York",
                "contact_email": "john@acmecorp.com",
                "contact_phone": "+12025551234",
                "contact_phone_country_code": "1",
                "country": "US",
                "country_of_registration": "US",
                "destination_countries": [
                    {
                        "id": "US",
                        "is_main": False,
                    }
                ],
                "entity_type": "PRIVATE_PROFIT",
                "expected_messaging_volume": "10000",
                "is_tcr_application": True,
                "notes": None,
                "phone_number_prefix": "+1",
                "postal_code": "10001",
                "primary_use_case": "Customer notifications and appointment reminders",
                "state": "NY",
                "street": "123 Main Street",
                "tax_id": "12-3456789",
                "tax_id_type": "us_ein",
            },
            test_mode=False,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSentDm) -> None:
        response = await async_client.brands.with_raw_response.create(
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSentDm) -> None:
        async with async_client.brands.with_streaming_response.create(
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSentDm) -> None:
        brand = await async_client.brands.update(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
            },
        )
        assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSentDm) -> None:
        brand = await async_client.brands.update(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
                "brand_name": None,
                "business_legal_name": "Acme Corporation LLC",
                "business_name": "Acme Corp Updated",
                "business_role": "CTO",
                "business_url": None,
                "city": None,
                "contact_email": "john@acmecorp.com",
                "contact_phone": "+12025551234",
                "contact_phone_country_code": "1",
                "country": "US",
                "country_of_registration": None,
                "destination_countries": [
                    {
                        "id": "id",
                        "is_main": True,
                    }
                ],
                "entity_type": None,
                "expected_messaging_volume": None,
                "is_tcr_application": None,
                "notes": None,
                "phone_number_prefix": None,
                "postal_code": None,
                "primary_use_case": None,
                "state": None,
                "street": None,
                "tax_id": None,
                "tax_id_type": None,
            },
            test_mode=False,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSentDm) -> None:
        response = await async_client.brands.with_raw_response.update(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSentDm) -> None:
        async with async_client.brands.with_streaming_response.update(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            brand={
                "brand_relationship": "SMALL_ACCOUNT",
                "contact_name": "John Smith",
                "vertical": "PROFESSIONAL",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(APIResponseBrandWithKYC, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brands.with_raw_response.update(
                brand_id="",
                brand={
                    "brand_relationship": "SMALL_ACCOUNT",
                    "contact_name": "John Smith",
                    "vertical": "PROFESSIONAL",
                },
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSentDm) -> None:
        brand = await async_client.brands.list()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSentDm) -> None:
        response = await async_client.brands.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSentDm) -> None:
        async with async_client.brands.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandListResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncSentDm) -> None:
        brand = await async_client.brands.delete(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={},
        )
        assert brand is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSentDm) -> None:
        brand = await async_client.brands.delete(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={"test_mode": False},
        )
        assert brand is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSentDm) -> None:
        response = await async_client.brands.with_raw_response.delete(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert brand is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSentDm) -> None:
        async with async_client.brands.with_streaming_response.delete(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert brand is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brands.with_raw_response.delete(
                brand_id="",
                body={},
            )
