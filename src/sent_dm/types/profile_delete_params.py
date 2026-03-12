# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .mutation_request_param import MutationRequestParam

__all__ = ["ProfileDeleteParams", "Body"]


class ProfileDeleteParams(TypedDict, total=False):
    body: Required[Body]
    """Request to delete a profile"""

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]


class Body(MutationRequestParam, total=False):
    """Request to delete a profile"""

    pass
