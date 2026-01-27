# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import SentDm, AsyncSentDm
from tests.utils import assert_matches_type
from sent_dm.types import (
    TemplateResponse,
    TemplateListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: SentDm) -> None:
        template = client.templates.create(
            definition={"body": {}},
        )
        assert_matches_type(TemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: SentDm) -> None:
        template = client.templates.create(
            definition={
                "body": {
                    "multi_channel": {
                        "template": "Hello {{1:variable}}, thank you for joining our service. We're excited to help you with your messaging needs!",
                        "type": None,
                        "variables": [
                            {
                                "id": 1,
                                "name": "customerName",
                                "props": {
                                    "alt": None,
                                    "media_type": None,
                                    "sample": "John Doe",
                                    "short_url": None,
                                    "url": None,
                                    "variable_type": "text",
                                },
                                "type": "variable",
                            }
                        ],
                    },
                    "sms": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "id": 0,
                                "name": "name",
                                "props": {
                                    "alt": "alt",
                                    "media_type": "mediaType",
                                    "sample": "sample",
                                    "short_url": "shortUrl",
                                    "url": "url",
                                    "variable_type": "variableType",
                                },
                                "type": "type",
                            }
                        ],
                    },
                    "whatsapp": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "id": 0,
                                "name": "name",
                                "props": {
                                    "alt": "alt",
                                    "media_type": "mediaType",
                                    "sample": "sample",
                                    "short_url": "shortUrl",
                                    "url": "url",
                                    "variable_type": "variableType",
                                },
                                "type": "type",
                            }
                        ],
                    },
                },
                "authentication_config": {
                    "add_security_recommendation": True,
                    "code_expiration_minutes": 0,
                },
                "buttons": [
                    {
                        "id": 0,
                        "props": {
                            "active_for": 0,
                            "autofill_text": "autofillText",
                            "country_code": "countryCode",
                            "offer_code": "offerCode",
                            "otp_type": "otpType",
                            "package_name": "packageName",
                            "phone_number": "phoneNumber",
                            "quick_reply_type": "quickReplyType",
                            "signature_hash": "signatureHash",
                            "text": "text",
                            "url": "url",
                            "url_type": "urlType",
                        },
                        "type": "type",
                    }
                ],
                "definition_version": "1.0",
                "footer": {
                    "template": "Best regards, The SentDM Team",
                    "type": "text",
                    "variables": [
                        {
                            "id": 0,
                            "name": "name",
                            "props": {
                                "alt": "alt",
                                "media_type": "mediaType",
                                "sample": "sample",
                                "short_url": "shortUrl",
                                "url": "url",
                                "variable_type": "variableType",
                            },
                            "type": "type",
                        }
                    ],
                },
                "header": {
                    "template": "Welcome to {{1:variable}}!",
                    "type": "text",
                    "variables": [
                        {
                            "id": 1,
                            "name": "companyName",
                            "props": {
                                "alt": None,
                                "media_type": None,
                                "sample": "SentDM",
                                "short_url": None,
                                "url": None,
                                "variable_type": "text",
                            },
                            "type": "variable",
                        }
                    ],
                },
            },
            category="MARKETING",
            language="en_US",
            submit_for_review=False,
        )
        assert_matches_type(TemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: SentDm) -> None:
        response = client.templates.with_raw_response.create(
            definition={"body": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: SentDm) -> None:
        with client.templates.with_streaming_response.create(
            definition={"body": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: SentDm) -> None:
        template = client.templates.retrieve(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert_matches_type(TemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: SentDm) -> None:
        response = client.templates.with_raw_response.retrieve(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: SentDm) -> None:
        with client.templates.with_streaming_response.retrieve(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.templates.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: SentDm) -> None:
        template = client.templates.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: SentDm) -> None:
        template = client.templates.list(
            page=0,
            page_size=0,
            category="category",
            search="search",
            status="status",
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: SentDm) -> None:
        response = client.templates.with_raw_response.list(
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: SentDm) -> None:
        with client.templates.with_streaming_response.list(
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: SentDm) -> None:
        template = client.templates.delete(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert template is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: SentDm) -> None:
        response = client.templates.with_raw_response.delete(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert template is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: SentDm) -> None:
        with client.templates.with_streaming_response.delete(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: SentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.templates.with_raw_response.delete(
                "",
            )


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSentDm) -> None:
        template = await async_client.templates.create(
            definition={"body": {}},
        )
        assert_matches_type(TemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSentDm) -> None:
        template = await async_client.templates.create(
            definition={
                "body": {
                    "multi_channel": {
                        "template": "Hello {{1:variable}}, thank you for joining our service. We're excited to help you with your messaging needs!",
                        "type": None,
                        "variables": [
                            {
                                "id": 1,
                                "name": "customerName",
                                "props": {
                                    "alt": None,
                                    "media_type": None,
                                    "sample": "John Doe",
                                    "short_url": None,
                                    "url": None,
                                    "variable_type": "text",
                                },
                                "type": "variable",
                            }
                        ],
                    },
                    "sms": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "id": 0,
                                "name": "name",
                                "props": {
                                    "alt": "alt",
                                    "media_type": "mediaType",
                                    "sample": "sample",
                                    "short_url": "shortUrl",
                                    "url": "url",
                                    "variable_type": "variableType",
                                },
                                "type": "type",
                            }
                        ],
                    },
                    "whatsapp": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "id": 0,
                                "name": "name",
                                "props": {
                                    "alt": "alt",
                                    "media_type": "mediaType",
                                    "sample": "sample",
                                    "short_url": "shortUrl",
                                    "url": "url",
                                    "variable_type": "variableType",
                                },
                                "type": "type",
                            }
                        ],
                    },
                },
                "authentication_config": {
                    "add_security_recommendation": True,
                    "code_expiration_minutes": 0,
                },
                "buttons": [
                    {
                        "id": 0,
                        "props": {
                            "active_for": 0,
                            "autofill_text": "autofillText",
                            "country_code": "countryCode",
                            "offer_code": "offerCode",
                            "otp_type": "otpType",
                            "package_name": "packageName",
                            "phone_number": "phoneNumber",
                            "quick_reply_type": "quickReplyType",
                            "signature_hash": "signatureHash",
                            "text": "text",
                            "url": "url",
                            "url_type": "urlType",
                        },
                        "type": "type",
                    }
                ],
                "definition_version": "1.0",
                "footer": {
                    "template": "Best regards, The SentDM Team",
                    "type": "text",
                    "variables": [
                        {
                            "id": 0,
                            "name": "name",
                            "props": {
                                "alt": "alt",
                                "media_type": "mediaType",
                                "sample": "sample",
                                "short_url": "shortUrl",
                                "url": "url",
                                "variable_type": "variableType",
                            },
                            "type": "type",
                        }
                    ],
                },
                "header": {
                    "template": "Welcome to {{1:variable}}!",
                    "type": "text",
                    "variables": [
                        {
                            "id": 1,
                            "name": "companyName",
                            "props": {
                                "alt": None,
                                "media_type": None,
                                "sample": "SentDM",
                                "short_url": None,
                                "url": None,
                                "variable_type": "text",
                            },
                            "type": "variable",
                        }
                    ],
                },
            },
            category="MARKETING",
            language="en_US",
            submit_for_review=False,
        )
        assert_matches_type(TemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSentDm) -> None:
        response = await async_client.templates.with_raw_response.create(
            definition={"body": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSentDm) -> None:
        async with async_client.templates.with_streaming_response.create(
            definition={"body": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSentDm) -> None:
        template = await async_client.templates.retrieve(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert_matches_type(TemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSentDm) -> None:
        response = await async_client.templates.with_raw_response.retrieve(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSentDm) -> None:
        async with async_client.templates.with_streaming_response.retrieve(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.templates.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSentDm) -> None:
        template = await async_client.templates.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSentDm) -> None:
        template = await async_client.templates.list(
            page=0,
            page_size=0,
            category="category",
            search="search",
            status="status",
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSentDm) -> None:
        response = await async_client.templates.with_raw_response.list(
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSentDm) -> None:
        async with async_client.templates.with_streaming_response.list(
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncSentDm) -> None:
        template = await async_client.templates.delete(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert template is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSentDm) -> None:
        response = await async_client.templates.with_raw_response.delete(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert template is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSentDm) -> None:
        async with async_client.templates.with_streaming_response.delete(
            "7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSentDm) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.templates.with_raw_response.delete(
                "",
            )
