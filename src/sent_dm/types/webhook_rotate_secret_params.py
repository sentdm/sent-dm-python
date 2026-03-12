# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .mutation_request_param import MutationRequestParam

__all__ = ["WebhookRotateSecretParams", "Body"]


class WebhookRotateSecretParams(TypedDict, total=False):
    body: Required[Body]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]


class Body(MutationRequestParam, total=False):
    pass
