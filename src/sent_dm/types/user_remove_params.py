# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .mutation_request_base_param import MutationRequestBaseParam

__all__ = ["UserRemoveParams", "Body"]


class UserRemoveParams(TypedDict, total=False):
    body: Required[Body]
    """Request to remove a user from an organization"""

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]


class Body(MutationRequestBaseParam, total=False):
    """Request to remove a user from an organization"""

    pass
