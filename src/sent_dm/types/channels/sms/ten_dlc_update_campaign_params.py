# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo
from ..market_compliance_param import MarketComplianceParam

__all__ = ["TenDlcUpdateCampaignParams"]


class TenDlcUpdateCampaignParams(TypedDict, total=False):
    compliance: MarketComplianceParam
    """The compliance values a market registers with.

    `brand` and `campaign` apply to US `TEN_DLC`; other markets fill this map with
    the document keys their own requirements name.
    """

    sandbox: bool

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
