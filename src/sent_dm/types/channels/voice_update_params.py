# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VoiceUpdateParams"]


class VoiceUpdateParams(TypedDict, total=False):
    api_key: Annotated[str, PropertyInfo(alias="apiKey")]
    """
    API key from the x-api-key header, or empty when the caller sent it as
    Authorization: Bearer instead.

    Optional on purpose. CustomerV3AuthenticationHandler accepts the key in either
    header, and [FromHeader] is required by default, so a Bearer-only request would
    authenticate and then be refused with a 400 for a header it never needed.
    Endpoints read the customer from the CustomerId claim, not from this value.
    """

    callback_url: Optional[str]
    """
    A new callback URL for the number, active or not: an absolute HTTP or HTTPS URL
    on a public host, where Sent asks what to do with each call. The signing secret
    is kept.
    """

    default_for_app_calls: Optional[bool]
    """
    true makes this the line app-originated calls are placed from when a voice token
    names no number. false is refused: an account with active voice numbers always
    has exactly one default, so the default moves by giving it to another number.
    """

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    status: Optional[Literal["ACTIVE", "INACTIVE"]]
    """ACTIVE turns calls on for the number again, INACTIVE turns them off.

    Matched ignoring case. Turning the default line off is refused while other
    active voice numbers remain.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
