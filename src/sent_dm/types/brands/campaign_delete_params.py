# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..mutation_request_param import MutationRequestParam

__all__ = ["CampaignDeleteParams", "Body"]


class CampaignDeleteParams(TypedDict, total=False):
    brand_id: Required[Annotated[str, PropertyInfo(alias="brandId")]]

    body: Required[Body]
    """Request to delete a campaign from a brand"""


class Body(MutationRequestParam, total=False):
    """Request to delete a campaign from a brand"""

    pass
