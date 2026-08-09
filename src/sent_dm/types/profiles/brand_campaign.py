# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .campaign_use_case import CampaignUseCase

__all__ = ["BrandCampaign"]


class BrandCampaign(BaseModel):
    """A 10DLC campaign registered for a brand."""

    id: Optional[str] = None

    billed_date: Optional[datetime] = FieldInfo(alias="billedDate", default=None)

    brand_id: Optional[str] = FieldInfo(alias="brandId", default=None)

    cost: Optional[float] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)

    dca_elections_complete: Optional[bool] = FieldInfo(alias="dcaElectionsComplete", default=None)
    """
    True once every carrier has completed its DCA election and the campaign is
    operationally ready for traffic.
    """

    dca_elections_completed_at: Optional[datetime] = FieldInfo(alias="dcaElectionsCompletedAt", default=None)

    description: Optional[str] = None

    has_submission_transaction: Optional[bool] = FieldInfo(alias="hasSubmissionTransaction", default=None)
    """True when the one-time campaign submission fee has already been charged."""

    help_keywords: Optional[str] = FieldInfo(alias="helpKeywords", default=None)

    help_message: Optional[str] = FieldInfo(alias="helpMessage", default=None)

    message_flow: Optional[str] = FieldInfo(alias="messageFlow", default=None)

    name: Optional[str] = None

    optin_keywords: Optional[str] = FieldInfo(alias="optinKeywords", default=None)

    optin_message: Optional[str] = FieldInfo(alias="optinMessage", default=None)

    optout_keywords: Optional[str] = FieldInfo(alias="optoutKeywords", default=None)

    optout_message: Optional[str] = FieldInfo(alias="optoutMessage", default=None)

    privacy_policy_link: Optional[str] = FieldInfo(alias="privacyPolicyLink", default=None)

    status: Optional[Literal["SENT_CREATED", "ACTIVE", "EXPIRED"]] = None

    submitted_at: Optional[datetime] = FieldInfo(alias="submittedAt", default=None)

    submitted_to_tcr: Optional[bool] = FieldInfo(alias="submittedToTCR", default=None)

    tcr_campaign_id: Optional[str] = FieldInfo(alias="tcrCampaignId", default=None)
    """The Campaign Registry identifier, once the campaign has been accepted."""

    tcr_sync_error: Optional[str] = FieldInfo(alias="tcrSyncError", default=None)
    """Surfaced so customers can see why a submission did not reach the registry."""

    terms_and_conditions_link: Optional[str] = FieldInfo(alias="termsAndConditionsLink", default=None)

    type: Optional[str] = None
    """Campaign type (for example KYC or App)."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    use_cases: Optional[List[CampaignUseCase]] = FieldInfo(alias="useCases", default=None)

    volume: Optional[str] = None
    """
    Expected messaging volume for this campaign — customer-supplied on
    create/update, and the input to both the TCR usecase classification (LOW_VOLUME
    vs MIXED/specific) and the campaign fee tier. Surfaced so customers can read
    back the value they set.
    """
