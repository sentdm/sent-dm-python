# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types import (
    APIResponseWebhook,
    WebhookListResponse,
    WebhookTestResponse,
    WebhookListEventsResponse,
    WebhookRotateSecretResponse,
    WebhookListEventTypesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Sent) -> None:
        webhook = client.webhooks.create()
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Sent) -> None:
        webhook = client.webhooks.create(
            display_name="Order Notifications",
            endpoint_url="https://example.com/webhooks/orders",
            event_filters={"message": ["delivered", "failed"]},
            event_types=["message", "templates"],
            retry_count=3,
            sandbox=False,
            timeout_seconds=30,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Sent) -> None:
        response = client.webhooks.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Sent) -> None:
        with client.webhooks.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(APIResponseWebhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Sent) -> None:
        webhook = client.webhooks.retrieve(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Sent) -> None:
        webhook = client.webhooks.retrieve(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Sent) -> None:
        response = client.webhooks.with_raw_response.retrieve(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Sent) -> None:
        with client.webhooks.with_streaming_response.retrieve(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(APIResponseWebhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Sent) -> None:
        webhook = client.webhooks.update(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Sent) -> None:
        webhook = client.webhooks.update(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            display_name="Updated Order Notifications",
            endpoint_url="https://example.com/webhooks/orders-v2",
            event_filters={"message": ["delivered", "failed"]},
            event_types=["message", "templates"],
            retry_count=5,
            sandbox=False,
            timeout_seconds=60,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Sent) -> None:
        response = client.webhooks.with_raw_response.update(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Sent) -> None:
        with client.webhooks.with_streaming_response.update(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(APIResponseWebhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Sent) -> None:
        webhook = client.webhooks.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Sent) -> None:
        webhook = client.webhooks.list(
            page=0,
            page_size=0,
            is_active=True,
            search="search",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Sent) -> None:
        response = client.webhooks.with_raw_response.list(
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Sent) -> None:
        with client.webhooks.with_streaming_response.list(
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Sent) -> None:
        webhook = client.webhooks.delete(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Sent) -> None:
        webhook = client.webhooks.delete(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Sent) -> None:
        response = client.webhooks.with_raw_response.delete(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Sent) -> None:
        with client.webhooks.with_streaming_response.delete(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_event_types(self, client: Sent) -> None:
        webhook = client.webhooks.list_event_types()
        assert_matches_type(WebhookListEventTypesResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_event_types_with_all_params(self, client: Sent) -> None:
        webhook = client.webhooks.list_event_types(
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookListEventTypesResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_event_types(self, client: Sent) -> None:
        response = client.webhooks.with_raw_response.list_event_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListEventTypesResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_event_types(self, client: Sent) -> None:
        with client.webhooks.with_streaming_response.list_event_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListEventTypesResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events(self, client: Sent) -> None:
        webhook = client.webhooks.list_events(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            page=0,
            page_size=0,
        )
        assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events_with_all_params(self, client: Sent) -> None:
        webhook = client.webhooks.list_events(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            page=0,
            page_size=0,
            search="search",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_events(self, client: Sent) -> None:
        response = client.webhooks.with_raw_response.list_events(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_events(self, client: Sent) -> None:
        with client.webhooks.with_streaming_response.list_events(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_events(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.list_events(
                id="",
                page=0,
                page_size=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rotate_secret(self, client: Sent) -> None:
        webhook = client.webhooks.rotate_secret(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            body={},
        )
        assert_matches_type(WebhookRotateSecretResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rotate_secret_with_all_params(self, client: Sent) -> None:
        webhook = client.webhooks.rotate_secret(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            body={"sandbox": False},
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookRotateSecretResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rotate_secret(self, client: Sent) -> None:
        response = client.webhooks.with_raw_response.rotate_secret(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookRotateSecretResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rotate_secret(self, client: Sent) -> None:
        with client.webhooks.with_streaming_response.rotate_secret(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookRotateSecretResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rotate_secret(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.rotate_secret(
                id="",
                body={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test(self, client: Sent) -> None:
        webhook = client.webhooks.test(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test_with_all_params(self, client: Sent) -> None:
        webhook = client.webhooks.test(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            event_type="message.sent",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test(self, client: Sent) -> None:
        response = client.webhooks.with_raw_response.test(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test(self, client: Sent) -> None:
        with client.webhooks.with_streaming_response.test(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookTestResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.test(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_toggle_status(self, client: Sent) -> None:
        webhook = client.webhooks.toggle_status(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_toggle_status_with_all_params(self, client: Sent) -> None:
        webhook = client.webhooks.toggle_status(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            is_active=False,
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_toggle_status(self, client: Sent) -> None:
        response = client.webhooks.with_raw_response.toggle_status(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_toggle_status(self, client: Sent) -> None:
        with client.webhooks.with_streaming_response.toggle_status(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(APIResponseWebhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_toggle_status(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.webhooks.with_raw_response.toggle_status(
                id="",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.create()
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.create(
            display_name="Order Notifications",
            endpoint_url="https://example.com/webhooks/orders",
            event_filters={"message": ["delivered", "failed"]},
            event_types=["message", "templates"],
            retry_count=3,
            sandbox=False,
            timeout_seconds=30,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSent) -> None:
        response = await async_client.webhooks.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSent) -> None:
        async with async_client.webhooks.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(APIResponseWebhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.retrieve(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.retrieve(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSent) -> None:
        response = await async_client.webhooks.with_raw_response.retrieve(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSent) -> None:
        async with async_client.webhooks.with_streaming_response.retrieve(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(APIResponseWebhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.update(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.update(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            display_name="Updated Order Notifications",
            endpoint_url="https://example.com/webhooks/orders-v2",
            event_filters={"message": ["delivered", "failed"]},
            event_types=["message", "templates"],
            retry_count=5,
            sandbox=False,
            timeout_seconds=60,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSent) -> None:
        response = await async_client.webhooks.with_raw_response.update(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSent) -> None:
        async with async_client.webhooks.with_streaming_response.update(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(APIResponseWebhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.list(
            page=0,
            page_size=0,
            is_active=True,
            search="search",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSent) -> None:
        response = await async_client.webhooks.with_raw_response.list(
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSent) -> None:
        async with async_client.webhooks.with_streaming_response.list(
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.delete(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.delete(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSent) -> None:
        response = await async_client.webhooks.with_raw_response.delete(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSent) -> None:
        async with async_client.webhooks.with_streaming_response.delete(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_event_types(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.list_event_types()
        assert_matches_type(WebhookListEventTypesResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_event_types_with_all_params(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.list_event_types(
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookListEventTypesResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_event_types(self, async_client: AsyncSent) -> None:
        response = await async_client.webhooks.with_raw_response.list_event_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListEventTypesResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_event_types(self, async_client: AsyncSent) -> None:
        async with async_client.webhooks.with_streaming_response.list_event_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListEventTypesResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.list_events(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            page=0,
            page_size=0,
        )
        assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events_with_all_params(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.list_events(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            page=0,
            page_size=0,
            search="search",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_events(self, async_client: AsyncSent) -> None:
        response = await async_client.webhooks.with_raw_response.list_events(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_events(self, async_client: AsyncSent) -> None:
        async with async_client.webhooks.with_streaming_response.list_events(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListEventsResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_events(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.list_events(
                id="",
                page=0,
                page_size=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rotate_secret(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.rotate_secret(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            body={},
        )
        assert_matches_type(WebhookRotateSecretResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rotate_secret_with_all_params(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.rotate_secret(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            body={"sandbox": False},
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookRotateSecretResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rotate_secret(self, async_client: AsyncSent) -> None:
        response = await async_client.webhooks.with_raw_response.rotate_secret(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookRotateSecretResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rotate_secret(self, async_client: AsyncSent) -> None:
        async with async_client.webhooks.with_streaming_response.rotate_secret(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookRotateSecretResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rotate_secret(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.rotate_secret(
                id="",
                body={},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.test(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test_with_all_params(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.test(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            event_type="message.sent",
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncSent) -> None:
        response = await async_client.webhooks.with_raw_response.test(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookTestResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncSent) -> None:
        async with async_client.webhooks.with_streaming_response.test(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookTestResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.test(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_toggle_status(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.toggle_status(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_toggle_status_with_all_params(self, async_client: AsyncSent) -> None:
        webhook = await async_client.webhooks.toggle_status(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
            is_active=False,
            sandbox=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_toggle_status(self, async_client: AsyncSent) -> None:
        response = await async_client.webhooks.with_raw_response.toggle_status(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(APIResponseWebhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_toggle_status(self, async_client: AsyncSent) -> None:
        async with async_client.webhooks.with_streaming_response.toggle_status(
            id="d4f5a6b7-c8d9-4e0f-a1b2-c3d4e5f6a7b8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(APIResponseWebhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_toggle_status(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.webhooks.with_raw_response.toggle_status(
                id="",
            )
