# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VoiceCreateTokenParams"]


class VoiceCreateTokenParams(TypedDict, total=False):
    identity: str
    """Your identifier for the app user, such as an agent or account id.

    Letters, digits, hyphens and underscores only, up to 200 characters.
    """

    number: Optional[str]
    """One of your voice-enabled phone numbers in E.164 format.

    Calls placed by this identity are routed through that number. Omit to use your
    default app-call number.
    """

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    ttl: Optional[int]
    """Token lifetime in seconds. Defaults to 600 and cannot exceed 3600."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
