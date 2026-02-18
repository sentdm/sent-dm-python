# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProfileCompleteParams"]


class ProfileCompleteParams(TypedDict, total=False):
    web_hook_url: Required[Annotated[str, PropertyInfo(alias="webHookUrl")]]
    """Webhook URL to call when profile completion finishes (success or failure)"""

    test_mode: bool
    """
    Test mode flag - when true, the operation is simulated without side effects
    Useful for testing integrations without actual execution
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
