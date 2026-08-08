# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .messaging_use_case_us import MessagingUseCaseUs

__all__ = ["CampaignUseCase"]


class CampaignUseCase(BaseModel):
    """
    Customer-facing use-case representation for the public v3 campaign contract.
    Exists for the same reason as BrandCampaignV3Response: nesting the
    TcrCampaignUseCase database entity in a public response means any column added to
    that table silently becomes part of the customer-facing contract. This DTO is an explicit
    allowlist, so a new column stays invisible until it is added here on purpose.
    This mirrors exactly the fields the entity already serialized, so it removes nothing from the
    current response shape. It only closes the future-leak path.
    """

    id: Optional[str] = None

    campaign_id: Optional[str] = FieldInfo(alias="campaignId", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)

    messaging_use_case_us: Optional[MessagingUseCaseUs] = FieldInfo(alias="messagingUseCaseUs", default=None)

    sample_messages: Optional[List[str]] = FieldInfo(alias="sampleMessages", default=None)
    """Sample messages submitted to the registry for this use case."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
