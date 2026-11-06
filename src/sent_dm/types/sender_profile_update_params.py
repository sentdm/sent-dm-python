# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SenderProfileUpdateParams"]


class SenderProfileUpdateParams(TypedDict, total=False):
    description: Optional[str]

    name: str

    notifications: Optional[str]
    """
    Who is notified about this profile's events: ORGANIZATION, SENDER_PROFILE, or
    ORGANIZATION_AND_SENDER_PROFILE. Cannot be cleared — a supplied value must be
    one of those.
    """

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    short_name: Optional[str]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
