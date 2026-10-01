# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ParticipantRemoveParams"]


class ParticipantRemoveParams(TypedDict, total=False):
    id: Required[str]

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
