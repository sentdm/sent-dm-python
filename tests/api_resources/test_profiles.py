# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import SentDm, AsyncSentDm
from tests.utils import assert_matches_type
from sent_dm.types import (
    ProfileListResponse,
    APIResponseOfProfileDetail,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: SentDm) -> None:
        profile = client.profiles.create()
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: SentDm) -> None:
        profile = client.profiles.create(
            allow_contact_sharing=True,
            allow_template_sharing=False,
            billing_model="profile",
            description="Sales department sender profile",
            icon="https://example.com/sales-icon.png",
            inherit_contacts=True,
            inherit_tcr_brand=True,
            inherit_tcr_campaign=True,
            inherit_templates=True,
            name="Sales Team",
            short_name="SALES",
            test_mode=False,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: SentDm) -> None:
        response = client.profiles.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: SentDm) -> None:
        with client.profiles.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: SentDm) -> None:
        profile = client.profiles.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: SentDm) -> None:
        response = client.profiles.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: SentDm) -> None:
        with client.profiles.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            client.profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: SentDm) -> None:
        profile = client.profiles.update(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: SentDm) -> None:
        profile = client.profiles.update(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allow_contact_sharing=True,
            allow_number_change_during_onboarding=None,
            allow_template_sharing=None,
            billing_model="organization",
            description="Updated sales department sender profile",
            icon=None,
            inherit_contacts=None,
            inherit_tcr_brand=None,
            inherit_tcr_campaign=None,
            inherit_templates=None,
            name="Sales Team - Updated",
            body_profile_id="770e8400-e29b-41d4-a716-446655440002",
            sending_phone_number=None,
            sending_phone_number_profile_id=None,
            sending_whatsapp_number_profile_id=None,
            short_name=None,
            test_mode=False,
            whatsapp_phone_number=None,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: SentDm) -> None:
        response = client.profiles.with_raw_response.update(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: SentDm) -> None:
        with client.profiles.with_streaming_response.update(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_profile_id` but received ''"):
            client.profiles.with_raw_response.update(
                path_profile_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: SentDm) -> None:
        profile = client.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: SentDm) -> None:
        response = client.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: SentDm) -> None:
        with client.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: SentDm) -> None:
        profile = client.profiles.delete(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: SentDm) -> None:
        profile = client.profiles.delete(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_profile_id="770e8400-e29b-41d4-a716-446655440002",
            test_mode=False,
        )
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: SentDm) -> None:
        response = client.profiles.with_raw_response.delete(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: SentDm) -> None:
        with client.profiles.with_streaming_response.delete(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_profile_id` but received ''"):
            client.profiles.with_raw_response.delete(
                path_profile_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete(self, client: SentDm) -> None:
        profile = client.profiles.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
        )
        assert_matches_type(object, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete_with_all_params(self, client: SentDm) -> None:
        profile = client.profiles.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
            test_mode=False,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(object, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_complete(self, client: SentDm) -> None:
        response = client.profiles.with_raw_response.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = response.parse()
        assert_matches_type(object, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_complete(self, client: SentDm) -> None:
        with client.profiles.with_streaming_response.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = response.parse()
            assert_matches_type(object, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_complete(self, client: SentDm) -> None:
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
    async def test_method_create(self, async_client: AsyncSentDm) -> None:
        profile = await async_client.profiles.create()
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSentDm) -> None:
        profile = await async_client.profiles.create(
            allow_contact_sharing=True,
            allow_template_sharing=False,
            billing_model="profile",
            description="Sales department sender profile",
            icon="https://example.com/sales-icon.png",
            inherit_contacts=True,
            inherit_tcr_brand=True,
            inherit_tcr_campaign=True,
            inherit_templates=True,
            name="Sales Team",
            short_name="SALES",
            test_mode=False,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSentDm) -> None:
        response = await async_client.profiles.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSentDm) -> None:
        async with async_client.profiles.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSentDm) -> None:
        profile = await async_client.profiles.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSentDm) -> None:
        response = await async_client.profiles.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSentDm) -> None:
        async with async_client.profiles.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSentDm) -> None:
        profile = await async_client.profiles.update(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSentDm) -> None:
        profile = await async_client.profiles.update(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allow_contact_sharing=True,
            allow_number_change_during_onboarding=None,
            allow_template_sharing=None,
            billing_model="organization",
            description="Updated sales department sender profile",
            icon=None,
            inherit_contacts=None,
            inherit_tcr_brand=None,
            inherit_tcr_campaign=None,
            inherit_templates=None,
            name="Sales Team - Updated",
            body_profile_id="770e8400-e29b-41d4-a716-446655440002",
            sending_phone_number=None,
            sending_phone_number_profile_id=None,
            sending_whatsapp_number_profile_id=None,
            short_name=None,
            test_mode=False,
            whatsapp_phone_number=None,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSentDm) -> None:
        response = await async_client.profiles.with_raw_response.update(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSentDm) -> None:
        async with async_client.profiles.with_streaming_response.update(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(APIResponseOfProfileDetail, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_profile_id` but received ''"):
            await async_client.profiles.with_raw_response.update(
                path_profile_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSentDm) -> None:
        profile = await async_client.profiles.list()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSentDm) -> None:
        response = await async_client.profiles.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(ProfileListResponse, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSentDm) -> None:
        async with async_client.profiles.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(ProfileListResponse, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncSentDm) -> None:
        profile = await async_client.profiles.delete(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSentDm) -> None:
        profile = await async_client.profiles.delete(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            body_profile_id="770e8400-e29b-41d4-a716-446655440002",
            test_mode=False,
        )
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSentDm) -> None:
        response = await async_client.profiles.with_raw_response.delete(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert profile is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSentDm) -> None:
        async with async_client.profiles.with_streaming_response.delete(
            path_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert profile is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_profile_id` but received ''"):
            await async_client.profiles.with_raw_response.delete(
                path_profile_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete(self, async_client: AsyncSentDm) -> None:
        profile = await async_client.profiles.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
        )
        assert_matches_type(object, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete_with_all_params(self, async_client: AsyncSentDm) -> None:
        profile = await async_client.profiles.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
            test_mode=False,
            idempotency_key="req_abc123_retry1",
        )
        assert_matches_type(object, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncSentDm) -> None:
        response = await async_client.profiles.with_raw_response.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profile = await response.parse()
        assert_matches_type(object, profile, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncSentDm) -> None:
        async with async_client.profiles.with_streaming_response.complete(
            profile_id="660e8400-e29b-41d4-a716-446655440000",
            web_hook_url="https://your-app.com/webhook/profile-complete",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profile = await response.parse()
            assert_matches_type(object, profile, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_complete(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `profile_id` but received ''"):
            await async_client.profiles.with_raw_response.complete(
                profile_id="",
                web_hook_url="https://your-app.com/webhook/profile-complete",
            )
