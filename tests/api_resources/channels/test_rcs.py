# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types.channels import APIResponseOfRcsAgent

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRcs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Sent) -> None:
        rc = client.channels.rcs.create()
        assert_matches_type(APIResponseOfRcsAgent, rc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Sent) -> None:
        rc = client.channels.rcs.create(
            agent_use_case="NOTIFICATIONS",
            banner_url="https://example.com/assets/banner-1440x448.png",
            brand_color="#1a73e8",
            brand_email="hello@example.com",
            brand_name="Example Retail",
            brand_phone_number="+12125550100",
            brief_company_description="Example Retail sells home goods across the US and ships to 48 states.",
            company_ein="12-3456789",
            contact_name_and_title="Jane Smith, Head of Marketing",
            customer_support_email="support@example.com",
            customer_support_phone_number="+18005550100",
            description="Order and delivery notifications for Example Retail customers.",
            display_name="Example Retail",
            entity_type="PRIVATE_PROFIT",
            help_message="For help, visit https://example.com/support or call 1-800-555-0100.",
            logo_url="https://example.com/assets/logo-224x224.png",
            official_address={
                "city": "New York",
                "country": "US",
                "postal_code": "10001",
                "state": "NY",
                "street": "123 Main St",
            },
            opt_in_process_description="Customers opt in at checkout by checking the SMS/RCS notifications box.",
            opt_in_screenshot_url=None,
            privacy_policy_url="https://example.com/privacy",
            sample_messages=["Your order #12345 has shipped and will arrive tomorrow."],
            sandbox=False,
            start_message="Welcome to Example Retail! Reply HELP for help or STOP to opt out.",
            stop_message="You have been unsubscribed from Example Retail notifications.",
            terms_and_conditions_url="https://example.com/terms",
            website_url="https://example.com",
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfRcsAgent, rc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Sent) -> None:
        response = client.channels.rcs.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rc = response.parse()
        assert_matches_type(APIResponseOfRcsAgent, rc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Sent) -> None:
        with client.channels.rcs.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rc = response.parse()
            assert_matches_type(APIResponseOfRcsAgent, rc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRcs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSent) -> None:
        rc = await async_client.channels.rcs.create()
        assert_matches_type(APIResponseOfRcsAgent, rc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSent) -> None:
        rc = await async_client.channels.rcs.create(
            agent_use_case="NOTIFICATIONS",
            banner_url="https://example.com/assets/banner-1440x448.png",
            brand_color="#1a73e8",
            brand_email="hello@example.com",
            brand_name="Example Retail",
            brand_phone_number="+12125550100",
            brief_company_description="Example Retail sells home goods across the US and ships to 48 states.",
            company_ein="12-3456789",
            contact_name_and_title="Jane Smith, Head of Marketing",
            customer_support_email="support@example.com",
            customer_support_phone_number="+18005550100",
            description="Order and delivery notifications for Example Retail customers.",
            display_name="Example Retail",
            entity_type="PRIVATE_PROFIT",
            help_message="For help, visit https://example.com/support or call 1-800-555-0100.",
            logo_url="https://example.com/assets/logo-224x224.png",
            official_address={
                "city": "New York",
                "country": "US",
                "postal_code": "10001",
                "state": "NY",
                "street": "123 Main St",
            },
            opt_in_process_description="Customers opt in at checkout by checking the SMS/RCS notifications box.",
            opt_in_screenshot_url=None,
            privacy_policy_url="https://example.com/privacy",
            sample_messages=["Your order #12345 has shipped and will arrive tomorrow."],
            sandbox=False,
            start_message="Welcome to Example Retail! Reply HELP for help or STOP to opt out.",
            stop_message="You have been unsubscribed from Example Retail notifications.",
            terms_and_conditions_url="https://example.com/terms",
            website_url="https://example.com",
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfRcsAgent, rc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.rcs.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rc = await response.parse()
        assert_matches_type(APIResponseOfRcsAgent, rc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSent) -> None:
        async with async_client.channels.rcs.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rc = await response.parse()
            assert_matches_type(APIResponseOfRcsAgent, rc, path=["response"])

        assert cast(Any, response.is_closed) is True
