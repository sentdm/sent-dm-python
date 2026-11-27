# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types.channels import APIResponseOfChannelMarket
from sent_dm.types.channels.sms import (
    TenDlcListCampaignsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTenDlc:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_campaign(self, client: Sent) -> None:
        ten_dlc = client.channels.sms.ten_dlc.add_campaign(
            description="Appointment reminders for patients who opted in when booking.",
            help_keywords="help_keywords",
            help_message="xxxxxxxxxxxxxxxxxxxx",
            message_flow="Patients opt in on the booking form by checking a consent box.",
            opt_in_keywords="opt_in_keywords",
            opt_in_message="xxxxxxxxxxxxxxxxxxxx",
            opt_out_keywords="opt_out_keywords",
            opt_out_message="xxxxxxxxxxxxxxxxxxxx",
            privacy_policy_link="privacy_policy_link",
            terms_and_conditions_link="terms_and_conditions_link",
            use_cases=[
                {
                    "sample_messages": ["Reminder: your appointment is tomorrow at 10:00. Reply STOP to opt out."],
                    "use_case": "ACCOUNT_NOTIFICATION",
                }
            ],
            volume="volume",
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_campaign_with_all_params(self, client: Sent) -> None:
        ten_dlc = client.channels.sms.ten_dlc.add_campaign(
            description="Appointment reminders for patients who opted in when booking.",
            help_keywords="help_keywords",
            help_message="xxxxxxxxxxxxxxxxxxxx",
            message_flow="Patients opt in on the booking form by checking a consent box.",
            opt_in_keywords="opt_in_keywords",
            opt_in_message="xxxxxxxxxxxxxxxxxxxx",
            opt_out_keywords="opt_out_keywords",
            opt_out_message="xxxxxxxxxxxxxxxxxxxx",
            privacy_policy_link="privacy_policy_link",
            terms_and_conditions_link="terms_and_conditions_link",
            use_cases=[
                {
                    "sample_messages": ["Reminder: your appointment is tomorrow at 10:00. Reply STOP to opt out."],
                    "use_case": "ACCOUNT_NOTIFICATION",
                }
            ],
            volume="volume",
            idempotency_key="req_abc123_retry1",
            sandbox=False,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_campaign(self, client: Sent) -> None:
        response = client.channels.sms.ten_dlc.with_raw_response.add_campaign(
            description="Appointment reminders for patients who opted in when booking.",
            help_keywords="help_keywords",
            help_message="xxxxxxxxxxxxxxxxxxxx",
            message_flow="Patients opt in on the booking form by checking a consent box.",
            opt_in_keywords="opt_in_keywords",
            opt_in_message="xxxxxxxxxxxxxxxxxxxx",
            opt_out_keywords="opt_out_keywords",
            opt_out_message="xxxxxxxxxxxxxxxxxxxx",
            privacy_policy_link="privacy_policy_link",
            terms_and_conditions_link="terms_and_conditions_link",
            use_cases=[
                {
                    "sample_messages": ["Reminder: your appointment is tomorrow at 10:00. Reply STOP to opt out."],
                    "use_case": "ACCOUNT_NOTIFICATION",
                }
            ],
            volume="volume",
            idempotency_key="req_abc123_retry1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ten_dlc = response.parse()
        assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_campaign(self, client: Sent) -> None:
        with client.channels.sms.ten_dlc.with_streaming_response.add_campaign(
            description="Appointment reminders for patients who opted in when booking.",
            help_keywords="help_keywords",
            help_message="xxxxxxxxxxxxxxxxxxxx",
            message_flow="Patients opt in on the booking form by checking a consent box.",
            opt_in_keywords="opt_in_keywords",
            opt_in_message="xxxxxxxxxxxxxxxxxxxx",
            opt_out_keywords="opt_out_keywords",
            opt_out_message="xxxxxxxxxxxxxxxxxxxx",
            privacy_policy_link="privacy_policy_link",
            terms_and_conditions_link="terms_and_conditions_link",
            use_cases=[
                {
                    "sample_messages": ["Reminder: your appointment is tomorrow at 10:00. Reply STOP to opt out."],
                    "use_case": "ACCOUNT_NOTIFICATION",
                }
            ],
            volume="volume",
            idempotency_key="req_abc123_retry1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ten_dlc = response.parse()
            assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_campaigns(self, client: Sent) -> None:
        ten_dlc = client.channels.sms.ten_dlc.list_campaigns()
        assert_matches_type(TenDlcListCampaignsResponse, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_campaigns_with_all_params(self, client: Sent) -> None:
        ten_dlc = client.channels.sms.ten_dlc.list_campaigns(
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TenDlcListCampaignsResponse, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_campaigns(self, client: Sent) -> None:
        response = client.channels.sms.ten_dlc.with_raw_response.list_campaigns()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ten_dlc = response.parse()
        assert_matches_type(TenDlcListCampaignsResponse, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_campaigns(self, client: Sent) -> None:
        with client.channels.sms.ten_dlc.with_streaming_response.list_campaigns() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ten_dlc = response.parse()
            assert_matches_type(TenDlcListCampaignsResponse, ten_dlc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_campaign(self, client: Sent) -> None:
        ten_dlc = client.channels.sms.ten_dlc.update_campaign(
            campaign_id="3f2a6c1e-8b4d-4e2a-9c7f-1d5b0a9e4c21",
        )
        assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_campaign_with_all_params(self, client: Sent) -> None:
        ten_dlc = client.channels.sms.ten_dlc.update_campaign(
            campaign_id="3f2a6c1e-8b4d-4e2a-9c7f-1d5b0a9e4c21",
            description="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            help_keywords="help_keywords",
            help_message="Example Clinic: for help call +1 212 555 0100. Reply STOP to opt out.",
            message_flow="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            opt_in_keywords="opt_in_keywords",
            opt_in_message="xxxxxxxxxxxxxxxxxxxx",
            opt_out_keywords="opt_out_keywords",
            opt_out_message="xxxxxxxxxxxxxxxxxxxx",
            privacy_policy_link="privacy_policy_link",
            sandbox=False,
            terms_and_conditions_link="terms_and_conditions_link",
            use_cases=[
                {
                    "sample_messages": [{}],
                    "use_case": "MARKETING",
                }
            ],
            volume="volume",
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_campaign(self, client: Sent) -> None:
        response = client.channels.sms.ten_dlc.with_raw_response.update_campaign(
            campaign_id="3f2a6c1e-8b4d-4e2a-9c7f-1d5b0a9e4c21",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ten_dlc = response.parse()
        assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_campaign(self, client: Sent) -> None:
        with client.channels.sms.ten_dlc.with_streaming_response.update_campaign(
            campaign_id="3f2a6c1e-8b4d-4e2a-9c7f-1d5b0a9e4c21",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ten_dlc = response.parse()
            assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_campaign(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            client.channels.sms.ten_dlc.with_raw_response.update_campaign(
                campaign_id="",
            )


class TestAsyncTenDlc:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_campaign(self, async_client: AsyncSent) -> None:
        ten_dlc = await async_client.channels.sms.ten_dlc.add_campaign(
            description="Appointment reminders for patients who opted in when booking.",
            help_keywords="help_keywords",
            help_message="xxxxxxxxxxxxxxxxxxxx",
            message_flow="Patients opt in on the booking form by checking a consent box.",
            opt_in_keywords="opt_in_keywords",
            opt_in_message="xxxxxxxxxxxxxxxxxxxx",
            opt_out_keywords="opt_out_keywords",
            opt_out_message="xxxxxxxxxxxxxxxxxxxx",
            privacy_policy_link="privacy_policy_link",
            terms_and_conditions_link="terms_and_conditions_link",
            use_cases=[
                {
                    "sample_messages": ["Reminder: your appointment is tomorrow at 10:00. Reply STOP to opt out."],
                    "use_case": "ACCOUNT_NOTIFICATION",
                }
            ],
            volume="volume",
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_campaign_with_all_params(self, async_client: AsyncSent) -> None:
        ten_dlc = await async_client.channels.sms.ten_dlc.add_campaign(
            description="Appointment reminders for patients who opted in when booking.",
            help_keywords="help_keywords",
            help_message="xxxxxxxxxxxxxxxxxxxx",
            message_flow="Patients opt in on the booking form by checking a consent box.",
            opt_in_keywords="opt_in_keywords",
            opt_in_message="xxxxxxxxxxxxxxxxxxxx",
            opt_out_keywords="opt_out_keywords",
            opt_out_message="xxxxxxxxxxxxxxxxxxxx",
            privacy_policy_link="privacy_policy_link",
            terms_and_conditions_link="terms_and_conditions_link",
            use_cases=[
                {
                    "sample_messages": ["Reminder: your appointment is tomorrow at 10:00. Reply STOP to opt out."],
                    "use_case": "ACCOUNT_NOTIFICATION",
                }
            ],
            volume="volume",
            idempotency_key="req_abc123_retry1",
            sandbox=False,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_campaign(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.sms.ten_dlc.with_raw_response.add_campaign(
            description="Appointment reminders for patients who opted in when booking.",
            help_keywords="help_keywords",
            help_message="xxxxxxxxxxxxxxxxxxxx",
            message_flow="Patients opt in on the booking form by checking a consent box.",
            opt_in_keywords="opt_in_keywords",
            opt_in_message="xxxxxxxxxxxxxxxxxxxx",
            opt_out_keywords="opt_out_keywords",
            opt_out_message="xxxxxxxxxxxxxxxxxxxx",
            privacy_policy_link="privacy_policy_link",
            terms_and_conditions_link="terms_and_conditions_link",
            use_cases=[
                {
                    "sample_messages": ["Reminder: your appointment is tomorrow at 10:00. Reply STOP to opt out."],
                    "use_case": "ACCOUNT_NOTIFICATION",
                }
            ],
            volume="volume",
            idempotency_key="req_abc123_retry1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ten_dlc = await response.parse()
        assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_campaign(self, async_client: AsyncSent) -> None:
        async with async_client.channels.sms.ten_dlc.with_streaming_response.add_campaign(
            description="Appointment reminders for patients who opted in when booking.",
            help_keywords="help_keywords",
            help_message="xxxxxxxxxxxxxxxxxxxx",
            message_flow="Patients opt in on the booking form by checking a consent box.",
            opt_in_keywords="opt_in_keywords",
            opt_in_message="xxxxxxxxxxxxxxxxxxxx",
            opt_out_keywords="opt_out_keywords",
            opt_out_message="xxxxxxxxxxxxxxxxxxxx",
            privacy_policy_link="privacy_policy_link",
            terms_and_conditions_link="terms_and_conditions_link",
            use_cases=[
                {
                    "sample_messages": ["Reminder: your appointment is tomorrow at 10:00. Reply STOP to opt out."],
                    "use_case": "ACCOUNT_NOTIFICATION",
                }
            ],
            volume="volume",
            idempotency_key="req_abc123_retry1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ten_dlc = await response.parse()
            assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_campaigns(self, async_client: AsyncSent) -> None:
        ten_dlc = await async_client.channels.sms.ten_dlc.list_campaigns()
        assert_matches_type(TenDlcListCampaignsResponse, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_campaigns_with_all_params(self, async_client: AsyncSent) -> None:
        ten_dlc = await async_client.channels.sms.ten_dlc.list_campaigns(
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TenDlcListCampaignsResponse, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_campaigns(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.sms.ten_dlc.with_raw_response.list_campaigns()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ten_dlc = await response.parse()
        assert_matches_type(TenDlcListCampaignsResponse, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_campaigns(self, async_client: AsyncSent) -> None:
        async with async_client.channels.sms.ten_dlc.with_streaming_response.list_campaigns() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ten_dlc = await response.parse()
            assert_matches_type(TenDlcListCampaignsResponse, ten_dlc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_campaign(self, async_client: AsyncSent) -> None:
        ten_dlc = await async_client.channels.sms.ten_dlc.update_campaign(
            campaign_id="3f2a6c1e-8b4d-4e2a-9c7f-1d5b0a9e4c21",
        )
        assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_campaign_with_all_params(self, async_client: AsyncSent) -> None:
        ten_dlc = await async_client.channels.sms.ten_dlc.update_campaign(
            campaign_id="3f2a6c1e-8b4d-4e2a-9c7f-1d5b0a9e4c21",
            description="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            help_keywords="help_keywords",
            help_message="Example Clinic: for help call +1 212 555 0100. Reply STOP to opt out.",
            message_flow="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            opt_in_keywords="opt_in_keywords",
            opt_in_message="xxxxxxxxxxxxxxxxxxxx",
            opt_out_keywords="opt_out_keywords",
            opt_out_message="xxxxxxxxxxxxxxxxxxxx",
            privacy_policy_link="privacy_policy_link",
            sandbox=False,
            terms_and_conditions_link="terms_and_conditions_link",
            use_cases=[
                {
                    "sample_messages": [{}],
                    "use_case": "MARKETING",
                }
            ],
            volume="volume",
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_campaign(self, async_client: AsyncSent) -> None:
        response = await async_client.channels.sms.ten_dlc.with_raw_response.update_campaign(
            campaign_id="3f2a6c1e-8b4d-4e2a-9c7f-1d5b0a9e4c21",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ten_dlc = await response.parse()
        assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_campaign(self, async_client: AsyncSent) -> None:
        async with async_client.channels.sms.ten_dlc.with_streaming_response.update_campaign(
            campaign_id="3f2a6c1e-8b4d-4e2a-9c7f-1d5b0a9e4c21",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ten_dlc = await response.parse()
            assert_matches_type(APIResponseOfChannelMarket, ten_dlc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_campaign(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `campaign_id` but received ''"):
            await async_client.channels.sms.ten_dlc.with_raw_response.update_campaign(
                campaign_id="",
            )
