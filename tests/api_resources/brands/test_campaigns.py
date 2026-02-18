# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import SentDm, AsyncSentDm
from tests.utils import assert_matches_type
from sent_dm.types.brands import (
    CampaignListResponse,
    APIResponseTcrCampaignWithUseCases,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCampaigns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: SentDm) -> None:
        campaign = client.brands.campaigns.create(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Appointment reminders and account notifications",
                "name": "Customer Notifications",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
            },
        )
        assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: SentDm) -> None:
        campaign = client.brands.campaigns.create(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Appointment reminders and account notifications",
                "name": "Customer Notifications",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
                "help_keywords": "HELP, INFO, SUPPORT",
                "help_message": "Reply STOP to unsubscribe or contact support@acmecorp.com",
                "message_flow": "User signs up on website and opts in to receive SMS notifications",
                "optin_keywords": "YES, START, SUBSCRIBE",
                "optin_message": "You have opted in to Acme Corp notifications. Reply STOP to opt out.",
                "optout_keywords": "STOP, UNSUBSCRIBE, END",
                "optout_message": "You have been unsubscribed. Reply START to opt back in.",
                "privacy_policy_link": "https://acmecorp.com/privacy",
                "terms_and_conditions_link": "https://acmecorp.com/terms",
            },
            test_mode=False,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: SentDm) -> None:
        response = client.brands.campaigns.with_raw_response.create(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Appointment reminders and account notifications",
                "name": "Customer Notifications",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: SentDm) -> None:
        with client.brands.campaigns.with_streaming_response.create(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Appointment reminders and account notifications",
                "name": "Customer Notifications",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brands.campaigns.with_raw_response.create(
                brand_id="",
                campaign={
                    "description": "Appointment reminders and account notifications",
                    "name": "Customer Notifications",
                    "type": "App",
                    "use_cases": [
                        {
                            "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                            "sample_messages": [
                                "Hi {name}, your appointment is confirmed for {date} at {time}.",
                                "Your order #{order_id} has been shipped. Track at {url}",
                            ],
                        }
                    ],
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: SentDm) -> None:
        campaign = client.brands.campaigns.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Updated appointment reminders and account notifications",
                "name": "Customer Notifications Updated",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
            },
        )
        assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: SentDm) -> None:
        campaign = client.brands.campaigns.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Updated appointment reminders and account notifications",
                "name": "Customer Notifications Updated",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
                "help_keywords": None,
                "help_message": None,
                "message_flow": "User signs up on website and opts in to receive SMS notifications",
                "optin_keywords": None,
                "optin_message": None,
                "optout_keywords": None,
                "optout_message": None,
                "privacy_policy_link": None,
                "terms_and_conditions_link": None,
            },
            test_mode=False,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: SentDm) -> None:
        response = client.brands.campaigns.with_raw_response.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Updated appointment reminders and account notifications",
                "name": "Customer Notifications Updated",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: SentDm) -> None:
        with client.brands.campaigns.with_streaming_response.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Updated appointment reminders and account notifications",
                "name": "Customer Notifications Updated",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brands.campaigns.with_raw_response.update(
                campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
                brand_id="",
                campaign={
                    "description": "Updated appointment reminders and account notifications",
                    "name": "Customer Notifications Updated",
                    "type": "App",
                    "use_cases": [
                        {
                            "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                            "sample_messages": [
                                "Hi {name}, your appointment is confirmed for {date} at {time}.",
                                "Your order #{order_id} has been shipped. Track at {url}",
                            ],
                        }
                    ],
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.brands.campaigns.with_raw_response.update(
                campaign_id="",
                brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                campaign={
                    "description": "Updated appointment reminders and account notifications",
                    "name": "Customer Notifications Updated",
                    "type": "App",
                    "use_cases": [
                        {
                            "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                            "sample_messages": [
                                "Hi {name}, your appointment is confirmed for {date} at {time}.",
                                "Your order #{order_id} has been shipped. Track at {url}",
                            ],
                        }
                    ],
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: SentDm) -> None:
        campaign = client.brands.campaigns.list(
            "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: SentDm) -> None:
        response = client.brands.campaigns.with_raw_response.list(
            "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: SentDm) -> None:
        with client.brands.campaigns.with_streaming_response.list(
            "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignListResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brands.campaigns.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: SentDm) -> None:
        campaign = client.brands.campaigns.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={},
        )
        assert campaign is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: SentDm) -> None:
        campaign = client.brands.campaigns.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={"test_mode": False},
        )
        assert campaign is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: SentDm) -> None:
        response = client.brands.campaigns.with_raw_response.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert campaign is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: SentDm) -> None:
        with client.brands.campaigns.with_streaming_response.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert campaign is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brands.campaigns.with_raw_response.delete(
                campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
                brand_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.brands.campaigns.with_raw_response.delete(
                campaign_id="",
                brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                body={},
            )


class TestAsyncCampaigns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSentDm) -> None:
        campaign = await async_client.brands.campaigns.create(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Appointment reminders and account notifications",
                "name": "Customer Notifications",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
            },
        )
        assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSentDm) -> None:
        campaign = await async_client.brands.campaigns.create(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Appointment reminders and account notifications",
                "name": "Customer Notifications",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
                "help_keywords": "HELP, INFO, SUPPORT",
                "help_message": "Reply STOP to unsubscribe or contact support@acmecorp.com",
                "message_flow": "User signs up on website and opts in to receive SMS notifications",
                "optin_keywords": "YES, START, SUBSCRIBE",
                "optin_message": "You have opted in to Acme Corp notifications. Reply STOP to opt out.",
                "optout_keywords": "STOP, UNSUBSCRIBE, END",
                "optout_message": "You have been unsubscribed. Reply START to opt back in.",
                "privacy_policy_link": "https://acmecorp.com/privacy",
                "terms_and_conditions_link": "https://acmecorp.com/terms",
            },
            test_mode=False,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSentDm) -> None:
        response = await async_client.brands.campaigns.with_raw_response.create(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Appointment reminders and account notifications",
                "name": "Customer Notifications",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSentDm) -> None:
        async with async_client.brands.campaigns.with_streaming_response.create(
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Appointment reminders and account notifications",
                "name": "Customer Notifications",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brands.campaigns.with_raw_response.create(
                brand_id="",
                campaign={
                    "description": "Appointment reminders and account notifications",
                    "name": "Customer Notifications",
                    "type": "App",
                    "use_cases": [
                        {
                            "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                            "sample_messages": [
                                "Hi {name}, your appointment is confirmed for {date} at {time}.",
                                "Your order #{order_id} has been shipped. Track at {url}",
                            ],
                        }
                    ],
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSentDm) -> None:
        campaign = await async_client.brands.campaigns.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Updated appointment reminders and account notifications",
                "name": "Customer Notifications Updated",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
            },
        )
        assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSentDm) -> None:
        campaign = await async_client.brands.campaigns.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Updated appointment reminders and account notifications",
                "name": "Customer Notifications Updated",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
                "help_keywords": None,
                "help_message": None,
                "message_flow": "User signs up on website and opts in to receive SMS notifications",
                "optin_keywords": None,
                "optin_message": None,
                "optout_keywords": None,
                "optout_message": None,
                "privacy_policy_link": None,
                "terms_and_conditions_link": None,
            },
            test_mode=False,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSentDm) -> None:
        response = await async_client.brands.campaigns.with_raw_response.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Updated appointment reminders and account notifications",
                "name": "Customer Notifications Updated",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSentDm) -> None:
        async with async_client.brands.campaigns.with_streaming_response.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            campaign={
                "description": "Updated appointment reminders and account notifications",
                "name": "Customer Notifications Updated",
                "type": "App",
                "use_cases": [
                    {
                        "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                        "sample_messages": [
                            "Hi {name}, your appointment is confirmed for {date} at {time}.",
                            "Your order #{order_id} has been shipped. Track at {url}",
                        ],
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(APIResponseTcrCampaignWithUseCases, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brands.campaigns.with_raw_response.update(
                campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
                brand_id="",
                campaign={
                    "description": "Updated appointment reminders and account notifications",
                    "name": "Customer Notifications Updated",
                    "type": "App",
                    "use_cases": [
                        {
                            "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                            "sample_messages": [
                                "Hi {name}, your appointment is confirmed for {date} at {time}.",
                                "Your order #{order_id} has been shipped. Track at {url}",
                            ],
                        }
                    ],
                },
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.brands.campaigns.with_raw_response.update(
                campaign_id="",
                brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                campaign={
                    "description": "Updated appointment reminders and account notifications",
                    "name": "Customer Notifications Updated",
                    "type": "App",
                    "use_cases": [
                        {
                            "messaging_use_case_us": "ACCOUNT_NOTIFICATION",
                            "sample_messages": [
                                "Hi {name}, your appointment is confirmed for {date} at {time}.",
                                "Your order #{order_id} has been shipped. Track at {url}",
                            ],
                        }
                    ],
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSentDm) -> None:
        campaign = await async_client.brands.campaigns.list(
            "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSentDm) -> None:
        response = await async_client.brands.campaigns.with_raw_response.list(
            "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSentDm) -> None:
        async with async_client.brands.campaigns.with_streaming_response.list(
            "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignListResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brands.campaigns.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncSentDm) -> None:
        campaign = await async_client.brands.campaigns.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={},
        )
        assert campaign is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSentDm) -> None:
        campaign = await async_client.brands.campaigns.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={"test_mode": False},
        )
        assert campaign is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSentDm) -> None:
        response = await async_client.brands.campaigns.with_raw_response.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert campaign is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSentDm) -> None:
        async with async_client.brands.campaigns.with_streaming_response.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert campaign is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brands.campaigns.with_raw_response.delete(
                campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
                brand_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.brands.campaigns.with_raw_response.delete(
                campaign_id="",
                brand_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                body={},
            )
