# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    display_name: str

    endpoint_url: str

    event_types: SequenceNotStr[str]

    retry_count: int

    test_mode: bool
    """
    Test mode flag - when true, the operation is simulated without side effects
    Useful for testing integrations without actual execution
    """

    timeout_seconds: int

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
