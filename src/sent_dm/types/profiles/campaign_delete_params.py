# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..mutation_request_base_param import MutationRequestBaseParam

__all__ = ["CampaignDeleteParams", "Body"]


class CampaignDeleteParams(TypedDict, total=False):
    profile_id: Required[Annotated[str, PropertyInfo(alias="profileId")]]

    body: Required[Body]
    """Request to delete a campaign from a brand"""

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]


class Body(MutationRequestBaseParam, total=False):
    """Request to delete a campaign from a brand"""

    pass
