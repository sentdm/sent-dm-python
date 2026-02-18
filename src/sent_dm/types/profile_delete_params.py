# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProfileDeleteParams"]


class ProfileDeleteParams(TypedDict, total=False):
    body_profile_id: Annotated[str, PropertyInfo(alias="profile_id")]
    """Profile ID from route parameter"""

    test_mode: bool
    """
    Test mode flag - when true, the operation is simulated without side effects
    Useful for testing integrations without actual execution
    """
