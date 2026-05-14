# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types.profiles import (
    CampaignListResponse,
    APIResponseOfTcrCampaignWithUseCases,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCampaigns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Sent) -> None:
        campaign = client.profiles.campaigns.create(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
        assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Sent) -> None:
        campaign = client.profiles.campaigns.create(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Sent) -> None:
        response = client.profiles.campaigns.with_raw_response.create(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
        assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Sent) -> None:
        with client.profiles.campaigns.with_streaming_response.create(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
            assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.campaigns.with_raw_response.create(
                profile_id="",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Sent) -> None:
        campaign = client.profiles.campaigns.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
        assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Sent) -> None:
        campaign = client.profiles.campaigns.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Sent) -> None:
        response = client.profiles.campaigns.with_raw_response.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
        assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Sent) -> None:
        with client.profiles.campaigns.with_streaming_response.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
            assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.campaigns.with_raw_response.update(
                campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
                profile_id="",
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
            client.profiles.campaigns.with_raw_response.update(
                campaign_id="",
                profile_id="770e8400-e29b-41d4-a716-446655440002",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Sent) -> None:
        campaign = client.profiles.campaigns.list(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
        )
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Sent) -> None:
        campaign = client.profiles.campaigns.list(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Sent) -> None:
        response = client.profiles.campaigns.with_raw_response.list(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Sent) -> None:
        with client.profiles.campaigns.with_streaming_response.list(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert_matches_type(CampaignListResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.campaigns.with_raw_response.list(
                profile_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Sent) -> None:
        campaign = client.profiles.campaigns.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
        )
        assert campaign is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Sent) -> None:
        campaign = client.profiles.campaigns.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
            sandbox=False,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert campaign is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Sent) -> None:
        response = client.profiles.campaigns.with_raw_response.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = response.parse()
        assert campaign is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Sent) -> None:
        with client.profiles.campaigns.with_streaming_response.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = response.parse()
            assert campaign is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.campaigns.with_raw_response.delete(
                campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
                profile_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.profiles.campaigns.with_raw_response.delete(
                campaign_id="",
                profile_id="770e8400-e29b-41d4-a716-446655440002",
            )


class TestAsyncCampaigns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSent) -> None:
        campaign = await async_client.profiles.campaigns.create(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
        assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSent) -> None:
        campaign = await async_client.profiles.campaigns.create(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSent) -> None:
        response = await async_client.profiles.campaigns.with_raw_response.create(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
        assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSent) -> None:
        async with async_client.profiles.campaigns.with_streaming_response.create(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
            assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.campaigns.with_raw_response.create(
                profile_id="",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSent) -> None:
        campaign = await async_client.profiles.campaigns.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
        assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSent) -> None:
        campaign = await async_client.profiles.campaigns.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSent) -> None:
        response = await async_client.profiles.campaigns.with_raw_response.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
        assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSent) -> None:
        async with async_client.profiles.campaigns.with_streaming_response.update(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
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
            assert_matches_type(APIResponseOfTcrCampaignWithUseCases, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.campaigns.with_raw_response.update(
                campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
                profile_id="",
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
            await async_client.profiles.campaigns.with_raw_response.update(
                campaign_id="",
                profile_id="770e8400-e29b-41d4-a716-446655440002",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSent) -> None:
        campaign = await async_client.profiles.campaigns.list(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
        )
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSent) -> None:
        campaign = await async_client.profiles.campaigns.list(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSent) -> None:
        response = await async_client.profiles.campaigns.with_raw_response.list(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert_matches_type(CampaignListResponse, campaign, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSent) -> None:
        async with async_client.profiles.campaigns.with_streaming_response.list(
            profile_id="770e8400-e29b-41d4-a716-446655440002",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert_matches_type(CampaignListResponse, campaign, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.campaigns.with_raw_response.list(
                profile_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncSent) -> None:
        campaign = await async_client.profiles.campaigns.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
        )
        assert campaign is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSent) -> None:
        campaign = await async_client.profiles.campaigns.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
            sandbox=False,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert campaign is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSent) -> None:
        response = await async_client.profiles.campaigns.with_raw_response.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        campaign = await response.parse()
        assert campaign is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSent) -> None:
        async with async_client.profiles.campaigns.with_streaming_response.delete(
            campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
            profile_id="770e8400-e29b-41d4-a716-446655440002",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            campaign = await response.parse()
            assert campaign is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.campaigns.with_raw_response.delete(
                campaign_id="b2c3d4e5-f6a7-8901-bcde-f12345678901",
                profile_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.profiles.campaigns.with_raw_response.delete(
                campaign_id="",
                profile_id="770e8400-e29b-41d4-a716-446655440002",
            )
