# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .call_participant_target_param import CallParticipantTargetParam

__all__ = ["ParticipantAddParams"]


class ParticipantAddParams(TypedDict, total=False):
    api_key: Annotated[str, PropertyInfo(alias="apiKey")]
    """
    API key from the x-api-key header, or empty when the caller sent it as
    Authorization: Bearer instead.

    Optional on purpose. CustomerV3AuthenticationHandler accepts the key in either
    header, and [FromHeader] is required by default, so a Bearer-only request would
    authenticate and then be refused with a 400 for a header it never needed.
    Endpoints read the customer from the CustomerId claim, not from this value.
    """

    caller_id: Optional[str]
    """The number shown to a phone participant as the caller, in E.164 format.

    Must be one of your numbers. The call's owning number when omitted
    """

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    to: CallParticipantTargetParam
    """A participant to add to a call"""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
