# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types import (
    ProfileListResponse,
    ProfileCreateResponse,
    ProfileUpdateResponse,
    ProfileCompleteResponse,
    ProfileRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Sent) -> None:
        profile = client.profiles.create()
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Sent) -> None:
        profile = client.profiles.create(
            allow_contact_sharing=True,
            allow_template_sharing=False,
            billing_contact={
                "email": "billing@acmecorp.com",
                "name": "Acme Corp",
                "address": "123 Main Street, New York, NY 10001, US",
                "phone": "+12025551234",
            },
            billing_model="profile",
            brand={
                "compliance": {
                    "brand_relationship": "SMALL_ACCOUNT",
                    "vertical": "PROFESSIONAL",
                    "destination_countries": [
                        {
                            "id": "US",
                            "is_main": False,
                        }
                    ],
                    "expected_messaging_volume": "10000",
                    "is_tcr_application": True,
                    "notes": None,
                    "phone_number_prefix": "+1",
                    "primary_use_case": "Customer notifications and appointment reminders",
                },
                "contact": {
                    "name": "John Smith",
                    "business_name": "Acme Corp",
                    "email": "john@acmecorp.com",
                    "phone": "+12025551234",
                    "phone_country_code": "1",
                    "role": "CEO",
                },
                "business": {
                    "city": "New York",
                    "country": "US",
                    "country_of_registration": "US",
                    "entity_type": "PRIVATE_PROFIT",
                    "legal_name": "Acme Corporation LLC",
                    "postal_code": "10001",
                    "state": "NY",
                    "street": "123 Main Street",
                    "tax_id": "12-3456789",
                    "tax_id_type": "us_ein",
                    "url": "https://acmecorp.com",
                },
            },
            description="Sales department sender profile",
            icon="https://example.com/sales-icon.png",
            inherit_contacts=True,
            inherit_tcr_brand=False,
            inherit_tcr_campaign=False,
            inherit_templates=True,
            name="Sales Team",
            payment_details={
                "card_number": "4111111111111111",
                "cvc": "123",
                "expiry": "09/27",
                "zip_code": "10001",
            },
            sandbox=False,
            short_name="SALES",
            whatsapp_business_account={
                "access_token": "EAAxxxxxxxxxxxxxxx",
                "waba_id": "123456789012345",
                "phone_number_id": "987654321098765",
            },
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Sent) -> None:
        response = client.profiles.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Sent) -> None:
        with client.profiles.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileCreateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Sent) -> None:
        profile = client.profiles.retrieve(
            profile_id="profileId",
        )
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Sent) -> None:
        profile = client.profiles.retrieve(
            profile_id="profileId",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Sent) -> None:
        response = client.profiles.with_raw_response.retrieve(
            profile_id="profileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Sent) -> None:
        with client.profiles.with_streaming_response.retrieve(
            profile_id="profileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.with_raw_response.retrieve(
                profile_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Sent) -> None:
        profile = client.profiles.update(
            profile_id="profileId",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Sent) -> None:
        profile = client.profiles.update(
            profile_id="profileId",
            allow_contact_sharing=True,
            allow_number_change_during_onboarding=None,
            allow_template_sharing=None,
            billing_contact={
                "email": "dev@stainless.com",
                "name": "x",
                "address": "address",
                "phone": "phone",
            },
            billing_model="organization",
            brand={
                "compliance": {
                    "brand_relationship": "SMALL_ACCOUNT",
                    "vertical": "PROFESSIONAL",
                    "destination_countries": [
                        {
                            "id": "US",
                            "is_main": False,
                        }
                    ],
                    "expected_messaging_volume": "10000",
                    "is_tcr_application": True,
                    "notes": None,
                    "phone_number_prefix": "+1",
                    "primary_use_case": "Customer notifications and appointment reminders",
                },
                "contact": {
                    "name": "John Smith",
                    "business_name": "Acme Corp",
                    "email": "john@acmecorp.com",
                    "phone": "+12025551234",
                    "phone_country_code": "1",
                    "role": "CEO",
                },
                "business": {
                    "city": "New York",
                    "country": "US",
                    "country_of_registration": "US",
                    "entity_type": "PRIVATE_PROFIT",
                    "legal_name": "Acme Corporation LLC",
                    "postal_code": "10001",
                    "state": "NY",
                    "street": "123 Main Street",
                    "tax_id": "12-3456789",
                    "tax_id_type": "us_ein",
                    "url": "https://acmecorp.com",
                },
            },
            description="Updated sales department sender profile",
            icon=None,
            inherit_contacts=None,
            inherit_tcr_brand=None,
            inherit_tcr_campaign=None,
            inherit_templates=None,
            name="Sales Team - Updated",
            payment_details={
                "card_number": "3216699102256101",
                "cvc": "3216",
                "expiry": "11/66",
                "zip_code": "x",
            },
            sandbox=False,
            sending_phone_number=None,
            sending_phone_number_profile_id=None,
            sending_whatsapp_number_profile_id=None,
            short_name="SALES",
            whatsapp_phone_number=None,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Sent) -> None:
        response = client.profiles.with_raw_response.update(
            profile_id="profileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Sent) -> None:
        with client.profiles.with_streaming_response.update(
            profile_id="profileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.with_raw_response.update(
                profile_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Sent) -> None:
        profile = client.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Sent) -> None:
        profile = client.profiles.list(
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Sent) -> None:
        response = client.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Sent) -> None:
        with client.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Sent) -> None:
        profile = client.profiles.delete(
            profile_id="profileId",
        )
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Sent) -> None:
        profile = client.profiles.delete(
            profile_id="profileId",
            sandbox=False,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Sent) -> None:
        response = client.profiles.with_raw_response.delete(
            profile_id="profileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Sent) -> None:
        with client.profiles.with_streaming_response.delete(
            profile_id="profileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.with_raw_response.delete(
                profile_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete(self, client: Sent) -> None:
        profile = client.profiles.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
        )
        assert_matches_type(ProfileCompleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete_with_all_params(self, client: Sent) -> None:
        profile = client.profiles.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProfileCompleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_complete(self, client: Sent) -> None:
        response = client.profiles.with_raw_response.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileCompleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_complete(self, client: Sent) -> None:
        with client.profiles.with_streaming_response.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileCompleteResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_complete(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.with_raw_response.complete(
                profile_id="",
                web_hook_url="https://your-app.com/webhook/profile-complete",
            )


class TestAsyncProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSent) -> None:
        profile = await async_client.profiles.create()
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSent) -> None:
        profile = await async_client.profiles.create(
            allow_contact_sharing=True,
            allow_template_sharing=False,
            billing_contact={
                "email": "billing@acmecorp.com",
                "name": "Acme Corp",
                "address": "123 Main Street, New York, NY 10001, US",
                "phone": "+12025551234",
            },
            billing_model="profile",
            brand={
                "compliance": {
                    "brand_relationship": "SMALL_ACCOUNT",
                    "vertical": "PROFESSIONAL",
                    "destination_countries": [
                        {
                            "id": "US",
                            "is_main": False,
                        }
                    ],
                    "expected_messaging_volume": "10000",
                    "is_tcr_application": True,
                    "notes": None,
                    "phone_number_prefix": "+1",
                    "primary_use_case": "Customer notifications and appointment reminders",
                },
                "contact": {
                    "name": "John Smith",
                    "business_name": "Acme Corp",
                    "email": "john@acmecorp.com",
                    "phone": "+12025551234",
                    "phone_country_code": "1",
                    "role": "CEO",
                },
                "business": {
                    "city": "New York",
                    "country": "US",
                    "country_of_registration": "US",
                    "entity_type": "PRIVATE_PROFIT",
                    "legal_name": "Acme Corporation LLC",
                    "postal_code": "10001",
                    "state": "NY",
                    "street": "123 Main Street",
                    "tax_id": "12-3456789",
                    "tax_id_type": "us_ein",
                    "url": "https://acmecorp.com",
                },
            },
            description="Sales department sender profile",
            icon="https://example.com/sales-icon.png",
            inherit_contacts=True,
            inherit_tcr_brand=False,
            inherit_tcr_campaign=False,
            inherit_templates=True,
            name="Sales Team",
            payment_details={
                "card_number": "4111111111111111",
                "cvc": "123",
                "expiry": "09/27",
                "zip_code": "10001",
            },
            sandbox=False,
            short_name="SALES",
            whatsapp_business_account={
                "access_token": "EAAxxxxxxxxxxxxxxx",
                "waba_id": "123456789012345",
                "phone_number_id": "987654321098765",
            },
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSent) -> None:
        response = await async_client.profiles.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileCreateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSent) -> None:
        async with async_client.profiles.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileCreateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSent) -> None:
        profile = await async_client.profiles.retrieve(
            profile_id="profileId",
        )
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSent) -> None:
        profile = await async_client.profiles.retrieve(
            profile_id="profileId",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSent) -> None:
        response = await async_client.profiles.with_raw_response.retrieve(
            profile_id="profileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSent) -> None:
        async with async_client.profiles.with_streaming_response.retrieve(
            profile_id="profileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileRetrieveResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.with_raw_response.retrieve(
                profile_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSent) -> None:
        profile = await async_client.profiles.update(
            profile_id="profileId",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSent) -> None:
        profile = await async_client.profiles.update(
            profile_id="profileId",
            allow_contact_sharing=True,
            allow_number_change_during_onboarding=None,
            allow_template_sharing=None,
            billing_contact={
                "email": "dev@stainless.com",
                "name": "x",
                "address": "address",
                "phone": "phone",
            },
            billing_model="organization",
            brand={
                "compliance": {
                    "brand_relationship": "SMALL_ACCOUNT",
                    "vertical": "PROFESSIONAL",
                    "destination_countries": [
                        {
                            "id": "US",
                            "is_main": False,
                        }
                    ],
                    "expected_messaging_volume": "10000",
                    "is_tcr_application": True,
                    "notes": None,
                    "phone_number_prefix": "+1",
                    "primary_use_case": "Customer notifications and appointment reminders",
                },
                "contact": {
                    "name": "John Smith",
                    "business_name": "Acme Corp",
                    "email": "john@acmecorp.com",
                    "phone": "+12025551234",
                    "phone_country_code": "1",
                    "role": "CEO",
                },
                "business": {
                    "city": "New York",
                    "country": "US",
                    "country_of_registration": "US",
                    "entity_type": "PRIVATE_PROFIT",
                    "legal_name": "Acme Corporation LLC",
                    "postal_code": "10001",
                    "state": "NY",
                    "street": "123 Main Street",
                    "tax_id": "12-3456789",
                    "tax_id_type": "us_ein",
                    "url": "https://acmecorp.com",
                },
            },
            description="Updated sales department sender profile",
            icon=None,
            inherit_contacts=None,
            inherit_tcr_brand=None,
            inherit_tcr_campaign=None,
            inherit_templates=None,
            name="Sales Team - Updated",
            payment_details={
                "card_number": "3216699102256101",
                "cvc": "3216",
                "expiry": "11/66",
                "zip_code": "x",
            },
            sandbox=False,
            sending_phone_number=None,
            sending_phone_number_profile_id=None,
            sending_whatsapp_number_profile_id=None,
            short_name="SALES",
            whatsapp_phone_number=None,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSent) -> None:
        response = await async_client.profiles.with_raw_response.update(
            profile_id="profileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSent) -> None:
        async with async_client.profiles.with_streaming_response.update(
            profile_id="profileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileUpdateResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.with_raw_response.update(
                profile_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSent) -> None:
        profile = await async_client.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSent) -> None:
        profile = await async_client.profiles.list(
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSent) -> None:
        response = await async_client.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSent) -> None:
        async with async_client.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncSent) -> None:
        profile = await async_client.profiles.delete(
            profile_id="profileId",
        )
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSent) -> None:
        profile = await async_client.profiles.delete(
            profile_id="profileId",
            sandbox=False,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSent) -> None:
        response = await async_client.profiles.with_raw_response.delete(
            profile_id="profileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSent) -> None:
        async with async_client.profiles.with_streaming_response.delete(
            profile_id="profileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.with_raw_response.delete(
                profile_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete(self, async_client: AsyncSent) -> None:
        profile = await async_client.profiles.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
        )
        assert_matches_type(ProfileCompleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete_with_all_params(self, async_client: AsyncSent) -> None:
        profile = await async_client.profiles.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProfileCompleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncSent) -> None:
        response = await async_client.profiles.with_raw_response.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileCompleteResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncSent) -> None:
        async with async_client.profiles.with_streaming_response.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileCompleteResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_complete(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.with_raw_response.complete(
                profile_id="",
                web_hook_url="https://your-app.com/webhook/profile-complete",
            )
