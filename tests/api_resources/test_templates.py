# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent_dm import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent_dm.types import (
    TemplateListResponse,
    TemplateCreateResponse,
    TemplateUpdateResponse,
    TemplateRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Sent) -> None:
        template = client.templates.create()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Sent) -> None:
        template = client.templates.create(
            category="MARKETING",
            creation_source=None,
            definition={
                "body": {
                    "multi_channel": {
                        "template": "Hello {{0:variable}}! Welcome to {{1:variable}}.",
                        "type": None,
                        "variables": [
                            {
                                "name": "name",
                                "props": {
                                    "media_type": "x",
                                    "sample": "John",
                                    "url": "x",
                                    "variable_type": "text",
                                    "alt": None,
                                    "regex": None,
                                    "short_url": None,
                                },
                                "type": "variable",
                                "id": 0,
                            },
                            {
                                "name": "company",
                                "props": {
                                    "media_type": "x",
                                    "sample": "SentDM",
                                    "url": "x",
                                    "variable_type": "text",
                                    "alt": None,
                                    "regex": None,
                                    "short_url": None,
                                },
                                "type": "variable",
                                "id": 1,
                            },
                        ],
                    },
                    "rcs": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "name": "x",
                                "props": {
                                    "media_type": "x",
                                    "sample": "x",
                                    "url": "x",
                                    "variable_type": "x",
                                    "alt": "alt",
                                    "regex": "regex",
                                    "short_url": "shortUrl",
                                },
                                "type": "x",
                                "id": 0,
                            }
                        ],
                    },
                    "sms": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "name": "x",
                                "props": {
                                    "media_type": "x",
                                    "sample": "x",
                                    "url": "x",
                                    "variable_type": "x",
                                    "alt": "alt",
                                    "regex": "regex",
                                    "short_url": "shortUrl",
                                },
                                "type": "x",
                                "id": 0,
                            }
                        ],
                    },
                    "whatsapp": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "name": "x",
                                "props": {
                                    "media_type": "x",
                                    "sample": "x",
                                    "url": "x",
                                    "variable_type": "x",
                                    "alt": "alt",
                                    "regex": "regex",
                                    "short_url": "shortUrl",
                                },
                                "type": "x",
                                "id": 0,
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
                        "props": {
                            "active_for": 1,
                            "country_code": "x",
                            "offer_code": "x",
                            "phone_number": "x",
                            "quick_reply_type": "x",
                            "text": "text",
                            "url": "x",
                            "url_type": "x",
                            "autofill_text": "autofillText",
                            "otp_type": "otpType",
                            "package_name": "packageName",
                            "signature_hash": "signatureHash",
                        },
                        "type": "x",
                        "id": 0,
                    }
                ],
                "definition_version": "1.0",
                "footer": {
                    "template": "template",
                    "type": "type",
                    "variables": [
                        {
                            "name": "x",
                            "props": {
                                "media_type": "x",
                                "sample": "x",
                                "url": "x",
                                "variable_type": "x",
                                "alt": "alt",
                                "regex": "regex",
                                "short_url": "shortUrl",
                            },
                            "type": "x",
                            "id": 0,
                        }
                    ],
                },
                "header": {
                    "template": "template",
                    "type": "type",
                    "variables": [
                        {
                            "name": "x",
                            "props": {
                                "media_type": "x",
                                "sample": "x",
                                "url": "x",
                                "variable_type": "x",
                                "alt": "alt",
                                "regex": "regex",
                                "short_url": "shortUrl",
                            },
                            "type": "x",
                            "id": 0,
                        }
                    ],
                },
            },
            language="en_US",
            sandbox=False,
            submit_for_review=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Sent) -> None:
        response = client.templates.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Sent) -> None:
        with client.templates.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateCreateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Sent) -> None:
        template = client.templates.retrieve(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Sent) -> None:
        template = client.templates.retrieve(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Sent) -> None:
        response = client.templates.with_raw_response.retrieve(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Sent) -> None:
        with client.templates.with_streaming_response.retrieve(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.templates.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Sent) -> None:
        template = client.templates.update(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Sent) -> None:
        template = client.templates.update(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
            category="MARKETING",
            definition={
                "body": {
                    "multi_channel": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "name": "x",
                                "props": {
                                    "media_type": "x",
                                    "sample": "x",
                                    "url": "x",
                                    "variable_type": "x",
                                    "alt": "alt",
                                    "regex": "regex",
                                    "short_url": "shortUrl",
                                },
                                "type": "x",
                                "id": 0,
                            }
                        ],
                    },
                    "rcs": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "name": "x",
                                "props": {
                                    "media_type": "x",
                                    "sample": "x",
                                    "url": "x",
                                    "variable_type": "x",
                                    "alt": "alt",
                                    "regex": "regex",
                                    "short_url": "shortUrl",
                                },
                                "type": "x",
                                "id": 0,
                            }
                        ],
                    },
                    "sms": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "name": "x",
                                "props": {
                                    "media_type": "x",
                                    "sample": "x",
                                    "url": "x",
                                    "variable_type": "x",
                                    "alt": "alt",
                                    "regex": "regex",
                                    "short_url": "shortUrl",
                                },
                                "type": "x",
                                "id": 0,
                            }
                        ],
                    },
                    "whatsapp": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "name": "x",
                                "props": {
                                    "media_type": "x",
                                    "sample": "x",
                                    "url": "x",
                                    "variable_type": "x",
                                    "alt": "alt",
                                    "regex": "regex",
                                    "short_url": "shortUrl",
                                },
                                "type": "x",
                                "id": 0,
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
                        "props": {
                            "active_for": 1,
                            "country_code": "x",
                            "offer_code": "x",
                            "phone_number": "x",
                            "quick_reply_type": "x",
                            "text": "text",
                            "url": "x",
                            "url_type": "x",
                            "autofill_text": "autofillText",
                            "otp_type": "otpType",
                            "package_name": "packageName",
                            "signature_hash": "signatureHash",
                        },
                        "type": "x",
                        "id": 0,
                    }
                ],
                "definition_version": "definitionVersion",
                "footer": {
                    "template": "template",
                    "type": "type",
                    "variables": [
                        {
                            "name": "x",
                            "props": {
                                "media_type": "x",
                                "sample": "x",
                                "url": "x",
                                "variable_type": "x",
                                "alt": "alt",
                                "regex": "regex",
                                "short_url": "shortUrl",
                            },
                            "type": "x",
                            "id": 0,
                        }
                    ],
                },
                "header": {
                    "template": "template",
                    "type": "type",
                    "variables": [
                        {
                            "name": "x",
                            "props": {
                                "media_type": "x",
                                "sample": "x",
                                "url": "x",
                                "variable_type": "x",
                                "alt": "alt",
                                "regex": "regex",
                                "short_url": "shortUrl",
                            },
                            "type": "x",
                            "id": 0,
                        }
                    ],
                },
            },
            language=None,
            name="Updated Welcome Message",
            sandbox=False,
            submit_for_review=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Sent) -> None:
        response = client.templates.with_raw_response.update(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Sent) -> None:
        with client.templates.with_streaming_response.update(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateUpdateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.templates.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Sent) -> None:
        template = client.templates.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Sent) -> None:
        template = client.templates.list(
            page=0,
            page_size=0,
            category="category",
            is_welcome_playground=True,
            search="search",
            status="status",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Sent) -> None:
        response = client.templates.with_raw_response.list(
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Sent) -> None:
        with client.templates.with_streaming_response.list(
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Sent) -> None:
        template = client.templates.delete(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Sent) -> None:
        template = client.templates.delete(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
            delete_from_meta=False,
            sandbox=False,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Sent) -> None:
        response = client.templates.with_raw_response.delete(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Sent) -> None:
        with client.templates.with_streaming_response.delete(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.templates.with_raw_response.delete(
                id="",
            )


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.create()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.create(
            category="MARKETING",
            creation_source=None,
            definition={
                "body": {
                    "multi_channel": {
                        "template": "Hello {{0:variable}}! Welcome to {{1:variable}}.",
                        "type": None,
                        "variables": [
                            {
                                "name": "name",
                                "props": {
                                    "media_type": "x",
                                    "sample": "John",
                                    "url": "x",
                                    "variable_type": "text",
                                    "alt": None,
                                    "regex": None,
                                    "short_url": None,
                                },
                                "type": "variable",
                                "id": 0,
                            },
                            {
                                "name": "company",
                                "props": {
                                    "media_type": "x",
                                    "sample": "SentDM",
                                    "url": "x",
                                    "variable_type": "text",
                                    "alt": None,
                                    "regex": None,
                                    "short_url": None,
                                },
                                "type": "variable",
                                "id": 1,
                            },
                        ],
                    },
                    "rcs": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "name": "x",
                                "props": {
                                    "media_type": "x",
                                    "sample": "x",
                                    "url": "x",
                                    "variable_type": "x",
                                    "alt": "alt",
                                    "regex": "regex",
                                    "short_url": "shortUrl",
                                },
                                "type": "x",
                                "id": 0,
                            }
                        ],
                    },
                    "sms": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "name": "x",
                                "props": {
                                    "media_type": "x",
                                    "sample": "x",
                                    "url": "x",
                                    "variable_type": "x",
                                    "alt": "alt",
                                    "regex": "regex",
                                    "short_url": "shortUrl",
                                },
                                "type": "x",
                                "id": 0,
                            }
                        ],
                    },
                    "whatsapp": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "name": "x",
                                "props": {
                                    "media_type": "x",
                                    "sample": "x",
                                    "url": "x",
                                    "variable_type": "x",
                                    "alt": "alt",
                                    "regex": "regex",
                                    "short_url": "shortUrl",
                                },
                                "type": "x",
                                "id": 0,
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
                        "props": {
                            "active_for": 1,
                            "country_code": "x",
                            "offer_code": "x",
                            "phone_number": "x",
                            "quick_reply_type": "x",
                            "text": "text",
                            "url": "x",
                            "url_type": "x",
                            "autofill_text": "autofillText",
                            "otp_type": "otpType",
                            "package_name": "packageName",
                            "signature_hash": "signatureHash",
                        },
                        "type": "x",
                        "id": 0,
                    }
                ],
                "definition_version": "1.0",
                "footer": {
                    "template": "template",
                    "type": "type",
                    "variables": [
                        {
                            "name": "x",
                            "props": {
                                "media_type": "x",
                                "sample": "x",
                                "url": "x",
                                "variable_type": "x",
                                "alt": "alt",
                                "regex": "regex",
                                "short_url": "shortUrl",
                            },
                            "type": "x",
                            "id": 0,
                        }
                    ],
                },
                "header": {
                    "template": "template",
                    "type": "type",
                    "variables": [
                        {
                            "name": "x",
                            "props": {
                                "media_type": "x",
                                "sample": "x",
                                "url": "x",
                                "variable_type": "x",
                                "alt": "alt",
                                "regex": "regex",
                                "short_url": "shortUrl",
                            },
                            "type": "x",
                            "id": 0,
                        }
                    ],
                },
            },
            language="en_US",
            sandbox=False,
            submit_for_review=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSent) -> None:
        response = await async_client.templates.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateCreateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSent) -> None:
        async with async_client.templates.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateCreateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.retrieve(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.retrieve(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSent) -> None:
        response = await async_client.templates.with_raw_response.retrieve(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSent) -> None:
        async with async_client.templates.with_streaming_response.retrieve(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateRetrieveResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.templates.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.update(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.update(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
            category="MARKETING",
            definition={
                "body": {
                    "multi_channel": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "name": "x",
                                "props": {
                                    "media_type": "x",
                                    "sample": "x",
                                    "url": "x",
                                    "variable_type": "x",
                                    "alt": "alt",
                                    "regex": "regex",
                                    "short_url": "shortUrl",
                                },
                                "type": "x",
                                "id": 0,
                            }
                        ],
                    },
                    "rcs": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "name": "x",
                                "props": {
                                    "media_type": "x",
                                    "sample": "x",
                                    "url": "x",
                                    "variable_type": "x",
                                    "alt": "alt",
                                    "regex": "regex",
                                    "short_url": "shortUrl",
                                },
                                "type": "x",
                                "id": 0,
                            }
                        ],
                    },
                    "sms": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "name": "x",
                                "props": {
                                    "media_type": "x",
                                    "sample": "x",
                                    "url": "x",
                                    "variable_type": "x",
                                    "alt": "alt",
                                    "regex": "regex",
                                    "short_url": "shortUrl",
                                },
                                "type": "x",
                                "id": 0,
                            }
                        ],
                    },
                    "whatsapp": {
                        "template": "template",
                        "type": "type",
                        "variables": [
                            {
                                "name": "x",
                                "props": {
                                    "media_type": "x",
                                    "sample": "x",
                                    "url": "x",
                                    "variable_type": "x",
                                    "alt": "alt",
                                    "regex": "regex",
                                    "short_url": "shortUrl",
                                },
                                "type": "x",
                                "id": 0,
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
                        "props": {
                            "active_for": 1,
                            "country_code": "x",
                            "offer_code": "x",
                            "phone_number": "x",
                            "quick_reply_type": "x",
                            "text": "text",
                            "url": "x",
                            "url_type": "x",
                            "autofill_text": "autofillText",
                            "otp_type": "otpType",
                            "package_name": "packageName",
                            "signature_hash": "signatureHash",
                        },
                        "type": "x",
                        "id": 0,
                    }
                ],
                "definition_version": "definitionVersion",
                "footer": {
                    "template": "template",
                    "type": "type",
                    "variables": [
                        {
                            "name": "x",
                            "props": {
                                "media_type": "x",
                                "sample": "x",
                                "url": "x",
                                "variable_type": "x",
                                "alt": "alt",
                                "regex": "regex",
                                "short_url": "shortUrl",
                            },
                            "type": "x",
                            "id": 0,
                        }
                    ],
                },
                "header": {
                    "template": "template",
                    "type": "type",
                    "variables": [
                        {
                            "name": "x",
                            "props": {
                                "media_type": "x",
                                "sample": "x",
                                "url": "x",
                                "variable_type": "x",
                                "alt": "alt",
                                "regex": "regex",
                                "short_url": "shortUrl",
                            },
                            "type": "x",
                            "id": 0,
                        }
                    ],
                },
            },
            language=None,
            name="Updated Welcome Message",
            sandbox=False,
            submit_for_review=False,
            idempotency_key="req_abc123_retry1",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSent) -> None:
        response = await async_client.templates.with_raw_response.update(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateUpdateResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSent) -> None:
        async with async_client.templates.with_streaming_response.update(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateUpdateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.templates.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.list(
            page=0,
            page_size=0,
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.list(
            page=0,
            page_size=0,
            category="category",
            is_welcome_playground=True,
            search="search",
            status="status",
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSent) -> None:
        response = await async_client.templates.with_raw_response.list(
            page=0,
            page_size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSent) -> None:
        async with async_client.templates.with_streaming_response.list(
            page=0,
            page_size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.delete(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.delete(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
            delete_from_meta=False,
            sandbox=False,
            x_profile_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSent) -> None:
        response = await async_client.templates.with_raw_response.delete(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert template is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSent) -> None:
        async with async_client.templates.with_streaming_response.delete(
            id="7ba7b820-9dad-11d1-80b4-00c04fd430c8",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert template is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.templates.with_raw_response.delete(
                id="",
            )
