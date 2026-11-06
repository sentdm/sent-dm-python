# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types import (
    SenderProfile,
    APIResponseOfSenderProfile,
)
from sent_dm.pagination import SyncSenderProfilesPage, AsyncSenderProfilesPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSenderProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Sent) -> None:
        sender_profile = client.sender_profiles.create()
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Sent) -> None:
        sender_profile = client.sender_profiles.create(
            billing={"inherit": True},
            channels={
                "rcs": {
                    "description": "description",
                    "agent_use_case": "agent_use_case",
                    "banner_url": "banner_url",
                    "billing_category": "billing_category",
                    "brand_color": "brand_color",
                    "brand_email": "brand_email",
                    "brand_name": "brand_name",
                    "brand_phone_number": "brand_phone_number",
                    "brief_company_description": "brief_company_description",
                    "company_ein": "company_ein",
                    "contact_name_and_title": "contact_name_and_title",
                    "customer_support_email": "customer_support_email",
                    "customer_support_phone_number": "customer_support_phone_number",
                    "display_name": "display_name",
                    "entity_type": "entity_type",
                    "help_message": "help_message",
                    "hosting_region": "hosting_region",
                    "logo_url": "logo_url",
                    "official_address": {
                        "city": "city",
                        "country": "country",
                        "postal_code": "postal_code",
                        "state": "state",
                        "street": "street",
                    },
                    "opt_in_process_description": "opt_in_process_description",
                    "opt_in_screenshot_url": "opt_in_screenshot_url",
                    "privacy_policy_url": "privacy_policy_url",
                    "sample_messages": ["string"],
                    "start_message": "start_message",
                    "stop_message": "stop_message",
                    "terms_and_conditions_url": "terms_and_conditions_url",
                    "website_url": "website_url",
                },
                "sms": {
                    "country": "US",
                    "area_codes": ["string"],
                    "number_type": "TEN_DLC",
                    "numbers": [
                        {
                            "area_code": "area_code",
                            "quantity": 0,
                        }
                    ],
                    "sender_value": "sender_value",
                },
                "whatsapp": {
                    "phone_number_id": "phone_number_id",
                    "waba_id": "waba_id",
                },
            },
            compliance={
                "brand": {
                    "business_name": "business_name",
                    "city": "city",
                    "contact_email": "dev@stainless.com",
                    "contact_name": "contact_name",
                    "contact_phone": "contact_phone",
                    "country": "country",
                    "ein_issuing_country": "ein_issuing_country",
                    "entity_type": "PRIVATE_PROFIT",
                    "inherit": True,
                    "legal_name": "legal_name",
                    "postal_code": "postal_code",
                    "state": "state",
                    "street": "street",
                    "tax_id": "tax_id",
                    "tax_id_type": "tax_id_type",
                    "website": "website",
                },
                "campaign": {
                    "description": "description",
                    "help_keywords": "help_keywords",
                    "help_message": "help_message",
                    "inherit": True,
                    "message_flow": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "opt_in_keywords": "opt_in_keywords",
                    "opt_in_message": "opt_in_message",
                    "opt_out_keywords": "opt_out_keywords",
                    "opt_out_message": "opt_out_message",
                    "privacy_policy_link": "privacy_policy_link",
                    "terms_and_conditions_link": "terms_and_conditions_link",
                    "use_cases": [
                        {
                            "sample_messages": [{}],
                            "use_case": "MARKETING",
                        }
                    ],
                    "volume": "volume",
                },
            },
            description=None,
            name="Example Retail",
            notifications=None,
            sandbox=False,
            short_name="Example",
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Sent) -> None:
        response = client.sender_profiles.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender_profile = response.parse()
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Sent) -> None:
        with client.sender_profiles.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender_profile = response.parse()
            assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Sent) -> None:
        sender_profile = client.sender_profiles.retrieve(
            "770e8400-e29b-41d4-a716-446655440002",
        )
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Sent) -> None:
        response = client.sender_profiles.with_raw_response.retrieve(
            "770e8400-e29b-41d4-a716-446655440002",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender_profile = response.parse()
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Sent) -> None:
        with client.sender_profiles.with_streaming_response.retrieve(
            "770e8400-e29b-41d4-a716-446655440002",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender_profile = response.parse()
            assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sender_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Sent) -> None:
        sender_profile = client.sender_profiles.update(
            id="770e8400-e29b-41d4-a716-446655440002",
        )
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Sent) -> None:
        sender_profile = client.sender_profiles.update(
            id="770e8400-e29b-41d4-a716-446655440002",
            description=None,
            name="Example Retail Renamed",
            notifications=None,
            sandbox=False,
            short_name="EXMPL",
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Sent) -> None:
        response = client.sender_profiles.with_raw_response.update(
            id="770e8400-e29b-41d4-a716-446655440002",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender_profile = response.parse()
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Sent) -> None:
        with client.sender_profiles.with_streaming_response.update(
            id="770e8400-e29b-41d4-a716-446655440002",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender_profile = response.parse()
            assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sender_profiles.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Sent) -> None:
        sender_profile = client.sender_profiles.list()
        assert_matches_type(SyncSenderProfilesPage[SenderProfile], sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Sent) -> None:
        sender_profile = client.sender_profiles.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(SyncSenderProfilesPage[SenderProfile], sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Sent) -> None:
        response = client.sender_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender_profile = response.parse()
        assert_matches_type(SyncSenderProfilesPage[SenderProfile], sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Sent) -> None:
        with client.sender_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender_profile = response.parse()
            assert_matches_type(SyncSenderProfilesPage[SenderProfile], sender_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Sent) -> None:
        sender_profile = client.sender_profiles.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert sender_profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Sent) -> None:
        response = client.sender_profiles.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender_profile = response.parse()
        assert sender_profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Sent) -> None:
        with client.sender_profiles.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender_profile = response.parse()
            assert sender_profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sender_profiles.with_raw_response.delete(
                "",
            )


class TestAsyncSenderProfiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSent) -> None:
        sender_profile = await async_client.sender_profiles.create()
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSent) -> None:
        sender_profile = await async_client.sender_profiles.create(
            billing={"inherit": True},
            channels={
                "rcs": {
                    "description": "description",
                    "agent_use_case": "agent_use_case",
                    "banner_url": "banner_url",
                    "billing_category": "billing_category",
                    "brand_color": "brand_color",
                    "brand_email": "brand_email",
                    "brand_name": "brand_name",
                    "brand_phone_number": "brand_phone_number",
                    "brief_company_description": "brief_company_description",
                    "company_ein": "company_ein",
                    "contact_name_and_title": "contact_name_and_title",
                    "customer_support_email": "customer_support_email",
                    "customer_support_phone_number": "customer_support_phone_number",
                    "display_name": "display_name",
                    "entity_type": "entity_type",
                    "help_message": "help_message",
                    "hosting_region": "hosting_region",
                    "logo_url": "logo_url",
                    "official_address": {
                        "city": "city",
                        "country": "country",
                        "postal_code": "postal_code",
                        "state": "state",
                        "street": "street",
                    },
                    "opt_in_process_description": "opt_in_process_description",
                    "opt_in_screenshot_url": "opt_in_screenshot_url",
                    "privacy_policy_url": "privacy_policy_url",
                    "sample_messages": ["string"],
                    "start_message": "start_message",
                    "stop_message": "stop_message",
                    "terms_and_conditions_url": "terms_and_conditions_url",
                    "website_url": "website_url",
                },
                "sms": {
                    "country": "US",
                    "area_codes": ["string"],
                    "number_type": "TEN_DLC",
                    "numbers": [
                        {
                            "area_code": "area_code",
                            "quantity": 0,
                        }
                    ],
                    "sender_value": "sender_value",
                },
                "whatsapp": {
                    "phone_number_id": "phone_number_id",
                    "waba_id": "waba_id",
                },
            },
            compliance={
                "brand": {
                    "business_name": "business_name",
                    "city": "city",
                    "contact_email": "dev@stainless.com",
                    "contact_name": "contact_name",
                    "contact_phone": "contact_phone",
                    "country": "country",
                    "ein_issuing_country": "ein_issuing_country",
                    "entity_type": "PRIVATE_PROFIT",
                    "inherit": True,
                    "legal_name": "legal_name",
                    "postal_code": "postal_code",
                    "state": "state",
                    "street": "street",
                    "tax_id": "tax_id",
                    "tax_id_type": "tax_id_type",
                    "website": "website",
                },
                "campaign": {
                    "description": "description",
                    "help_keywords": "help_keywords",
                    "help_message": "help_message",
                    "inherit": True,
                    "message_flow": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "opt_in_keywords": "opt_in_keywords",
                    "opt_in_message": "opt_in_message",
                    "opt_out_keywords": "opt_out_keywords",
                    "opt_out_message": "opt_out_message",
                    "privacy_policy_link": "privacy_policy_link",
                    "terms_and_conditions_link": "terms_and_conditions_link",
                    "use_cases": [
                        {
                            "sample_messages": [{}],
                            "use_case": "MARKETING",
                        }
                    ],
                    "volume": "volume",
                },
            },
            description=None,
            name="Example Retail",
            notifications=None,
            sandbox=False,
            short_name="Example",
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSent) -> None:
        response = await async_client.sender_profiles.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender_profile = await response.parse()
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSent) -> None:
        async with async_client.sender_profiles.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender_profile = await response.parse()
            assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSent) -> None:
        sender_profile = await async_client.sender_profiles.retrieve(
            "770e8400-e29b-41d4-a716-446655440002",
        )
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSent) -> None:
        response = await async_client.sender_profiles.with_raw_response.retrieve(
            "770e8400-e29b-41d4-a716-446655440002",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender_profile = await response.parse()
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSent) -> None:
        async with async_client.sender_profiles.with_streaming_response.retrieve(
            "770e8400-e29b-41d4-a716-446655440002",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender_profile = await response.parse()
            assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sender_profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSent) -> None:
        sender_profile = await async_client.sender_profiles.update(
            id="770e8400-e29b-41d4-a716-446655440002",
        )
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSent) -> None:
        sender_profile = await async_client.sender_profiles.update(
            id="770e8400-e29b-41d4-a716-446655440002",
            description=None,
            name="Example Retail Renamed",
            notifications=None,
            sandbox=False,
            short_name="EXMPL",
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSent) -> None:
        response = await async_client.sender_profiles.with_raw_response.update(
            id="770e8400-e29b-41d4-a716-446655440002",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender_profile = await response.parse()
        assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSent) -> None:
        async with async_client.sender_profiles.with_streaming_response.update(
            id="770e8400-e29b-41d4-a716-446655440002",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender_profile = await response.parse()
            assert_matches_type(APIResponseOfSenderProfile, sender_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sender_profiles.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSent) -> None:
        sender_profile = await async_client.sender_profiles.list()
        assert_matches_type(AsyncSenderProfilesPage[SenderProfile], sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSent) -> None:
        sender_profile = await async_client.sender_profiles.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(AsyncSenderProfilesPage[SenderProfile], sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSent) -> None:
        response = await async_client.sender_profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender_profile = await response.parse()
        assert_matches_type(AsyncSenderProfilesPage[SenderProfile], sender_profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSent) -> None:
        async with async_client.sender_profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender_profile = await response.parse()
            assert_matches_type(AsyncSenderProfilesPage[SenderProfile], sender_profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncSent) -> None:
        sender_profile = await async_client.sender_profiles.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert sender_profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSent) -> None:
        response = await async_client.sender_profiles.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sender_profile = await response.parse()
        assert sender_profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSent) -> None:
        async with async_client.sender_profiles.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sender_profile = await response.parse()
            assert sender_profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sender_profiles.with_raw_response.delete(
                "",
            )
