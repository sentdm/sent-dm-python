# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types.channels import APIResponseOfChannelMarket

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSMS:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Sent) -> None:
        sms = client.channels.sms.create(
            number_type="TEN_DLC",
        )
        assert_matches_type(APIResponseOfChannelMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Sent) -> None:
        sms = client.channels.sms.create(
            number_type="TEN_DLC",
            area_codes=["415", "628"],
            compliance={
                "brand": {
                    "business_name": "xxx",
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
                    "tax_id": "xx",
                    "tax_id_type": "tax_id_type",
                    "website": "website",
                },
                "campaign": {
                    "description": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "help_keywords": "help_keywords",
                    "help_message": "xxxxxxxxxxxxxxxxxxxx",
                    "inherit": True,
                    "message_flow": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "opt_in_keywords": "opt_in_keywords",
                    "opt_in_message": "xxxxxxxxxxxxxxxxxxxx",
                    "opt_out_keywords": "opt_out_keywords",
                    "opt_out_message": "xxxxxxxxxxxxxxxxxxxx",
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
        assert_matches_type(APIResponseOfChannelMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Sent) -> None:
        response = client.channels.sms.with_raw_response.create(
            number_type="TEN_DLC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms = response.parse()
        assert_matches_type(APIResponseOfChannelMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Sent) -> None:
        with client.channels.sms.with_streaming_response.create(
            number_type="TEN_DLC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms = response.parse()
            assert_matches_type(APIResponseOfChannelMarket, sms, path=["response"])

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
        assert_matches_type(APIResponseOfChannelMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSent) -> None:
        sms = await async_client.channels.sms.create(
            number_type="TEN_DLC",
            area_codes=["415", "628"],
            compliance={
                "brand": {
                    "business_name": "xxx",
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
                    "tax_id": "xx",
                    "tax_id_type": "tax_id_type",
                    "website": "website",
                },
                "campaign": {
                    "description": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "help_keywords": "help_keywords",
                    "help_message": "xxxxxxxxxxxxxxxxxxxx",
                    "inherit": True,
                    "message_flow": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                    "opt_in_keywords": "opt_in_keywords",
                    "opt_in_message": "xxxxxxxxxxxxxxxxxxxx",
                    "opt_out_keywords": "opt_out_keywords",
                    "opt_out_message": "xxxxxxxxxxxxxxxxxxxx",
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
        assert_matches_type(APIResponseOfChannelMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.sms.with_raw_response.create(
            number_type="TEN_DLC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sms = await response.parse()
        assert_matches_type(APIResponseOfChannelMarket, sms, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSent) -> None:
        async with async_client.channels.sms.with_streaming_response.create(
            number_type="TEN_DLC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sms = await response.parse()
            assert_matches_type(APIResponseOfChannelMarket, sms, path=["response"])

        assert cast(Any, response.is_closed) is True
