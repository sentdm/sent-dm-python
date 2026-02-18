# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserRemoveParams"]


class UserRemoveParams(TypedDict, total=False):
    test_mode: bool
    """
    Test mode flag - when true, the operation is simulated without side effects
    Useful for testing integrations without actual execution
    """

    body_user_id: Annotated[str, PropertyInfo(alias="user_id")]
    """User ID from route parameter"""
