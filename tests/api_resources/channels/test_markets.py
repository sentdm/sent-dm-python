# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types.channels import (
    APIResponseOfChannelMarket,
    APIResponseOfMarketNumbers,
    APIResponseOfListOfChannelMarket,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarkets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Sent) -> None:
        market = client.channels.markets.retrieve(
            type="ten_dlc",
            channel="sms",
            country="US",
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Sent) -> None:
        market = client.channels.markets.retrieve(
            type="ten_dlc",
            channel="sms",
            country="US",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Sent) -> None:
        response = client.channels.markets.with_raw_response.retrieve(
            type="ten_dlc",
            channel="sms",
            country="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Sent) -> None:
        with client.channels.markets.with_streaming_response.retrieve(
            type="ten_dlc",
            channel="sms",
            country="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel` but received ''"):
            client.channels.markets.with_raw_response.retrieve(
                type="ten_dlc",
                channel="",
                country="US",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country` but received ''"):
            client.channels.markets.with_raw_response.retrieve(
                type="ten_dlc",
                channel="sms",
                country="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            client.channels.markets.with_raw_response.retrieve(
                type="",
                channel="sms",
                country="US",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Sent) -> None:
        market = client.channels.markets.update(
            type="ten_dlc",
            channel="sms",
            country="US",
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Sent) -> None:
        market = client.channels.markets.update(
            type="ten_dlc",
            channel="sms",
            country="US",
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
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Sent) -> None:
        response = client.channels.markets.with_raw_response.update(
            type="ten_dlc",
            channel="sms",
            country="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Sent) -> None:
        with client.channels.markets.with_streaming_response.update(
            type="ten_dlc",
            channel="sms",
            country="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel` but received ''"):
            client.channels.markets.with_raw_response.update(
                type="ten_dlc",
                channel="",
                country="US",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country` but received ''"):
            client.channels.markets.with_raw_response.update(
                type="ten_dlc",
                channel="sms",
                country="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            client.channels.markets.with_raw_response.update(
                type="",
                channel="sms",
                country="US",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Sent) -> None:
        market = client.channels.markets.list(
            channel="channel",
        )
        assert_matches_type(APIResponseOfListOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Sent) -> None:
        market = client.channels.markets.list(
            channel="channel",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfListOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Sent) -> None:
        response = client.channels.markets.with_raw_response.list(
            channel="channel",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(APIResponseOfListOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Sent) -> None:
        with client.channels.markets.with_streaming_response.list(
            channel="channel",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(APIResponseOfListOfChannelMarket, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel` but received ''"):
            client.channels.markets.with_raw_response.list(
                channel="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_numbers(self, client: Sent) -> None:
        market = client.channels.markets.add_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[{}, {}],
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_numbers_with_all_params(self, client: Sent) -> None:
        market = client.channels.markets.add_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[
                {
                    "area_code": "415",
                    "quantity": 2,
                },
                {
                    "area_code": "212",
                    "quantity": 1,
                },
            ],
            idempotency_key="req_abc123_retry1",
            campaign_id="8f14e45f-ceea-467f-a8f0-7c2a3d1b9e01",
            sandbox=False,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_numbers(self, client: Sent) -> None:
        response = client.channels.markets.with_raw_response.add_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[{}, {}],
            idempotency_key="req_abc123_retry1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_numbers(self, client: Sent) -> None:
        with client.channels.markets.with_streaming_response.add_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[{}, {}],
            idempotency_key="req_abc123_retry1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_numbers(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel` but received ''"):
            client.channels.markets.with_raw_response.add_numbers(
                type="TEN_DLC",
                channel="",
                country="US",
                numbers=[{}, {}],
                idempotency_key="req_abc123_retry1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country` but received ''"):
            client.channels.markets.with_raw_response.add_numbers(
                type="TEN_DLC",
                channel="sms",
                country="",
                numbers=[{}, {}],
                idempotency_key="req_abc123_retry1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            client.channels.markets.with_raw_response.add_numbers(
                type="",
                channel="sms",
                country="US",
                numbers=[{}, {}],
                idempotency_key="req_abc123_retry1",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_numbers(self, client: Sent) -> None:
        market = client.channels.markets.list_numbers(
            type="type",
            channel="channel",
            country="country",
        )
        assert_matches_type(APIResponseOfMarketNumbers, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_numbers_with_all_params(self, client: Sent) -> None:
        market = client.channels.markets.list_numbers(
            type="type",
            channel="channel",
            country="country",
            campaign_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfMarketNumbers, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_numbers(self, client: Sent) -> None:
        response = client.channels.markets.with_raw_response.list_numbers(
            type="type",
            channel="channel",
            country="country",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(APIResponseOfMarketNumbers, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_numbers(self, client: Sent) -> None:
        with client.channels.markets.with_streaming_response.list_numbers(
            type="type",
            channel="channel",
            country="country",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(APIResponseOfMarketNumbers, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_numbers(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel` but received ''"):
            client.channels.markets.with_raw_response.list_numbers(
                type="type",
                channel="",
                country="country",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country` but received ''"):
            client.channels.markets.with_raw_response.list_numbers(
                type="type",
                channel="channel",
                country="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            client.channels.markets.with_raw_response.list_numbers(
                type="",
                channel="channel",
                country="country",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_numbers(self, client: Sent) -> None:
        market = client.channels.markets.replace_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[{}, {}],
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_numbers_with_all_params(self, client: Sent) -> None:
        market = client.channels.markets.replace_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[
                {
                    "area_code": "415",
                    "quantity": 2,
                },
                {
                    "area_code": "212",
                    "quantity": 1,
                },
            ],
            campaign_id="8f14e45f-ceea-467f-a8f0-7c2a3d1b9e01",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace_numbers(self, client: Sent) -> None:
        response = client.channels.markets.with_raw_response.replace_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = response.parse()
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace_numbers(self, client: Sent) -> None:
        with client.channels.markets.with_streaming_response.replace_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = response.parse()
            assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace_numbers(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel` but received ''"):
            client.channels.markets.with_raw_response.replace_numbers(
                type="TEN_DLC",
                channel="",
                country="US",
                numbers=[{}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country` but received ''"):
            client.channels.markets.with_raw_response.replace_numbers(
                type="TEN_DLC",
                channel="sms",
                country="",
                numbers=[{}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            client.channels.markets.with_raw_response.replace_numbers(
                type="",
                channel="sms",
                country="US",
                numbers=[{}, {}],
            )


class TestAsyncMarkets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSent) -> None:
        market = await async_client.channels.markets.retrieve(
            type="ten_dlc",
            channel="sms",
            country="US",
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSent) -> None:
        market = await async_client.channels.markets.retrieve(
            type="ten_dlc",
            channel="sms",
            country="US",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.markets.with_raw_response.retrieve(
            type="ten_dlc",
            channel="sms",
            country="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSent) -> None:
        async with async_client.channels.markets.with_streaming_response.retrieve(
            type="ten_dlc",
            channel="sms",
            country="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel` but received ''"):
            await async_client.channels.markets.with_raw_response.retrieve(
                type="ten_dlc",
                channel="",
                country="US",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country` but received ''"):
            await async_client.channels.markets.with_raw_response.retrieve(
                type="ten_dlc",
                channel="sms",
                country="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            await async_client.channels.markets.with_raw_response.retrieve(
                type="",
                channel="sms",
                country="US",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSent) -> None:
        market = await async_client.channels.markets.update(
            type="ten_dlc",
            channel="sms",
            country="US",
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSent) -> None:
        market = await async_client.channels.markets.update(
            type="ten_dlc",
            channel="sms",
            country="US",
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
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.markets.with_raw_response.update(
            type="ten_dlc",
            channel="sms",
            country="US",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSent) -> None:
        async with async_client.channels.markets.with_streaming_response.update(
            type="ten_dlc",
            channel="sms",
            country="US",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel` but received ''"):
            await async_client.channels.markets.with_raw_response.update(
                type="ten_dlc",
                channel="",
                country="US",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country` but received ''"):
            await async_client.channels.markets.with_raw_response.update(
                type="ten_dlc",
                channel="sms",
                country="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            await async_client.channels.markets.with_raw_response.update(
                type="",
                channel="sms",
                country="US",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSent) -> None:
        market = await async_client.channels.markets.list(
            channel="channel",
        )
        assert_matches_type(APIResponseOfListOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSent) -> None:
        market = await async_client.channels.markets.list(
            channel="channel",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfListOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.markets.with_raw_response.list(
            channel="channel",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(APIResponseOfListOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSent) -> None:
        async with async_client.channels.markets.with_streaming_response.list(
            channel="channel",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(APIResponseOfListOfChannelMarket, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel` but received ''"):
            await async_client.channels.markets.with_raw_response.list(
                channel="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_numbers(self, async_client: AsyncSent) -> None:
        market = await async_client.channels.markets.add_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[{}, {}],
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_numbers_with_all_params(self, async_client: AsyncSent) -> None:
        market = await async_client.channels.markets.add_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[
                {
                    "area_code": "415",
                    "quantity": 2,
                },
                {
                    "area_code": "212",
                    "quantity": 1,
                },
            ],
            idempotency_key="req_abc123_retry1",
            campaign_id="8f14e45f-ceea-467f-a8f0-7c2a3d1b9e01",
            sandbox=False,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_numbers(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.markets.with_raw_response.add_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[{}, {}],
            idempotency_key="req_abc123_retry1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_numbers(self, async_client: AsyncSent) -> None:
        async with async_client.channels.markets.with_streaming_response.add_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[{}, {}],
            idempotency_key="req_abc123_retry1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_numbers(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel` but received ''"):
            await async_client.channels.markets.with_raw_response.add_numbers(
                type="TEN_DLC",
                channel="",
                country="US",
                numbers=[{}, {}],
                idempotency_key="req_abc123_retry1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country` but received ''"):
            await async_client.channels.markets.with_raw_response.add_numbers(
                type="TEN_DLC",
                channel="sms",
                country="",
                numbers=[{}, {}],
                idempotency_key="req_abc123_retry1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            await async_client.channels.markets.with_raw_response.add_numbers(
                type="",
                channel="sms",
                country="US",
                numbers=[{}, {}],
                idempotency_key="req_abc123_retry1",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_numbers(self, async_client: AsyncSent) -> None:
        market = await async_client.channels.markets.list_numbers(
            type="type",
            channel="channel",
            country="country",
        )
        assert_matches_type(APIResponseOfMarketNumbers, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_numbers_with_all_params(self, async_client: AsyncSent) -> None:
        market = await async_client.channels.markets.list_numbers(
            type="type",
            channel="channel",
            country="country",
            campaign_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfMarketNumbers, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_numbers(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.markets.with_raw_response.list_numbers(
            type="type",
            channel="channel",
            country="country",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(APIResponseOfMarketNumbers, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_numbers(self, async_client: AsyncSent) -> None:
        async with async_client.channels.markets.with_streaming_response.list_numbers(
            type="type",
            channel="channel",
            country="country",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(APIResponseOfMarketNumbers, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_numbers(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel` but received ''"):
            await async_client.channels.markets.with_raw_response.list_numbers(
                type="type",
                channel="",
                country="country",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country` but received ''"):
            await async_client.channels.markets.with_raw_response.list_numbers(
                type="type",
                channel="channel",
                country="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            await async_client.channels.markets.with_raw_response.list_numbers(
                type="",
                channel="channel",
                country="country",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_numbers(self, async_client: AsyncSent) -> None:
        market = await async_client.channels.markets.replace_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[{}, {}],
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_numbers_with_all_params(self, async_client: AsyncSent) -> None:
        market = await async_client.channels.markets.replace_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[
                {
                    "area_code": "415",
                    "quantity": 2,
                },
                {
                    "area_code": "212",
                    "quantity": 1,
                },
            ],
            campaign_id="8f14e45f-ceea-467f-a8f0-7c2a3d1b9e01",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace_numbers(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.markets.with_raw_response.replace_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[{}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        market = await response.parse()
        assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace_numbers(self, async_client: AsyncSent) -> None:
        async with async_client.channels.markets.with_streaming_response.replace_numbers(
            type="TEN_DLC",
            channel="sms",
            country="US",
            numbers=[{}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            market = await response.parse()
            assert_matches_type(APIResponseOfChannelMarket, market, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace_numbers(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `channel` but received ''"):
            await async_client.channels.markets.with_raw_response.replace_numbers(
                type="TEN_DLC",
                channel="",
                country="US",
                numbers=[{}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `country` but received ''"):
            await async_client.channels.markets.with_raw_response.replace_numbers(
                type="TEN_DLC",
                channel="sms",
                country="",
                numbers=[{}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type` but received ''"):
            await async_client.channels.markets.with_raw_response.replace_numbers(
                type="",
                channel="sms",
                country="US",
                numbers=[{}, {}],
            )
