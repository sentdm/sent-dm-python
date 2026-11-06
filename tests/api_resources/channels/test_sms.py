# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types.channels import (
    APIResponseOfSMSMarket,
    APIResponseOfListOfSMSMarket,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSMS:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Sent) -> None:
        sms = client.channels.sms.create(
            number_type="TEN_DLC",
        )
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Sent) -> None:
        sms = client.channels.sms.create(
            number_type="TEN_DLC",
            area_codes=["415", "628"],
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
            country="US",
            numbers=[
                {
                    "area_code": "area_code",
                    "quantity": 0,
                }
            ],
            sandbox=False,
            sender_value=None,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Sent) -> None:
        response = client.channels.sms.with_raw_response.create(
            number_type="TEN_DLC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms = response.parse()
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Sent) -> None:
        with client.channels.sms.with_streaming_response.create(
            number_type="TEN_DLC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms = response.parse()
            assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Sent) -> None:
        sms = client.channels.sms.retrieve(
            type="ten_dlc",
            country="US",
        )
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Sent) -> None:
        sms = client.channels.sms.retrieve(
            type="ten_dlc",
            country="US",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Sent) -> None:
        response = client.channels.sms.with_raw_response.retrieve(
            type="ten_dlc",
            country="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms = response.parse()
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Sent) -> None:
        with client.channels.sms.with_streaming_response.retrieve(
            type="ten_dlc",
            country="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms = response.parse()
            assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country` but received ''"):
            client.channels.sms.with_raw_response.retrieve(
                type="ten_dlc",
                country="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            client.channels.sms.with_raw_response.retrieve(
                type="",
                country="US",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Sent) -> None:
        sms = client.channels.sms.update(
            type="ten_dlc",
            country="US",
        )
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Sent) -> None:
        sms = client.channels.sms.update(
            type="ten_dlc",
            country="US",
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
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Sent) -> None:
        response = client.channels.sms.with_raw_response.update(
            type="ten_dlc",
            country="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms = response.parse()
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Sent) -> None:
        with client.channels.sms.with_streaming_response.update(
            type="ten_dlc",
            country="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms = response.parse()
            assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country` but received ''"):
            client.channels.sms.with_raw_response.update(
                type="ten_dlc",
                country="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            client.channels.sms.with_raw_response.update(
                type="",
                country="US",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Sent) -> None:
        sms = client.channels.sms.list()
        assert_matches_type(APIResponseOfListOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Sent) -> None:
        sms = client.channels.sms.list(
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfListOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Sent) -> None:
        response = client.channels.sms.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms = response.parse()
        assert_matches_type(APIResponseOfListOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Sent) -> None:
        with client.channels.sms.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms = response.parse()
            assert_matches_type(APIResponseOfListOfSMSMarket, sms, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSMS:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSent) -> None:
        sms = await async_client.channels.sms.create(
            number_type="TEN_DLC",
        )
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSent) -> None:
        sms = await async_client.channels.sms.create(
            number_type="TEN_DLC",
            area_codes=["415", "628"],
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
            country="US",
            numbers=[
                {
                    "area_code": "area_code",
                    "quantity": 0,
                }
            ],
            sandbox=False,
            sender_value=None,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.sms.with_raw_response.create(
            number_type="TEN_DLC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms = await response.parse()
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSent) -> None:
        async with async_client.channels.sms.with_streaming_response.create(
            number_type="TEN_DLC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms = await response.parse()
            assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSent) -> None:
        sms = await async_client.channels.sms.retrieve(
            type="ten_dlc",
            country="US",
        )
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSent) -> None:
        sms = await async_client.channels.sms.retrieve(
            type="ten_dlc",
            country="US",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.sms.with_raw_response.retrieve(
            type="ten_dlc",
            country="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms = await response.parse()
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSent) -> None:
        async with async_client.channels.sms.with_streaming_response.retrieve(
            type="ten_dlc",
            country="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms = await response.parse()
            assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country` but received ''"):
            await async_client.channels.sms.with_raw_response.retrieve(
                type="ten_dlc",
                country="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            await async_client.channels.sms.with_raw_response.retrieve(
                type="",
                country="US",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSent) -> None:
        sms = await async_client.channels.sms.update(
            type="ten_dlc",
            country="US",
        )
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSent) -> None:
        sms = await async_client.channels.sms.update(
            type="ten_dlc",
            country="US",
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
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.sms.with_raw_response.update(
            type="ten_dlc",
            country="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms = await response.parse()
        assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSent) -> None:
        async with async_client.channels.sms.with_streaming_response.update(
            type="ten_dlc",
            country="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms = await response.parse()
            assert_matches_type(APIResponseOfSMSMarket, sms, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country` but received ''"):
            await async_client.channels.sms.with_raw_response.update(
                type="ten_dlc",
                country="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            await async_client.channels.sms.with_raw_response.update(
                type="",
                country="US",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSent) -> None:
        sms = await async_client.channels.sms.list()
        assert_matches_type(APIResponseOfListOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSent) -> None:
        sms = await async_client.channels.sms.list(
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfListOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.sms.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms = await response.parse()
        assert_matches_type(APIResponseOfListOfSMSMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSent) -> None:
        async with async_client.channels.sms.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms = await response.parse()
            assert_matches_type(APIResponseOfListOfSMSMarket, sms, path=["response"])

        assert cast(Any, response.is_closed) is True
