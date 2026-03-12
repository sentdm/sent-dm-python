# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .campaign_data_param import CampaignDataParam

__all__ = ["CampaignUpdateParams"]


class CampaignUpdateParams(TypedDict, total=False):
    profile_id: Required[Annotated[str, PropertyInfo(alias="profileId")]]

    campaign: Required[CampaignDataParam]
    """Campaign data for create or update operation"""

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
