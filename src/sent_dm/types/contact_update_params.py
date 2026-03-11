# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactUpdateParams"]


class ContactUpdateParams(TypedDict, total=False):
    default_channel: Optional[str]
    """Default messaging channel: "sms" or "whatsapp" """

    opt_out: Optional[bool]
    """Whether the contact has opted out of messaging"""

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
