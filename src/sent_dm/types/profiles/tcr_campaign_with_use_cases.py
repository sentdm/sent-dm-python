# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .base_dto import BaseDto
from .messaging_use_case_us import MessagingUseCaseUs

__all__ = ["TcrCampaignWithUseCases", "TcrCampaignWithUseCasesUseCase"]


class TcrCampaignWithUseCasesUseCase(BaseDto):
    sample_messages: List[str] = FieldInfo(alias="sampleMessages")

    campaign_id: Optional[str] = FieldInfo(alias="campaignId", default=None)

    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)

    messaging_use_case_us: Optional[MessagingUseCaseUs] = FieldInfo(alias="messagingUseCaseUs", default=None)


class TcrCampaignWithUseCases(BaseDto):
    description: str

    name: str

    type: str

    billed_date: Optional[datetime] = FieldInfo(alias="billedDate", default=None)

    brand_id: Optional[str] = FieldInfo(alias="brandId", default=None)

    cost: Optional[float] = None

    csp_id: Optional[str] = FieldInfo(alias="cspId", default=None)

    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)

    dca_elections_complete: Optional[bool] = FieldInfo(alias="dcaElectionsComplete", default=None)

    dca_elections_completed_at: Optional[datetime] = FieldInfo(alias="dcaElectionsCompletedAt", default=None)

    has_submission_transaction: Optional[bool] = FieldInfo(alias="hasSubmissionTransaction", default=None)
    """
    True when this campaign already has a billing transaction of reference type
    TCR_CAMPAIGN_SUBMISSION (the one-time submission fee was charged). Populated
    only by the campaigns-list path; defaults false on other responses.
    """

    help_keywords: Optional[str] = FieldInfo(alias="helpKeywords", default=None)

    help_message: Optional[str] = FieldInfo(alias="helpMessage", default=None)

    kyc_submission_form_id: Optional[str] = FieldInfo(alias="kycSubmissionFormId", default=None)

    message_flow: Optional[str] = FieldInfo(alias="messageFlow", default=None)

    optin_keywords: Optional[str] = FieldInfo(alias="optinKeywords", default=None)

    optin_message: Optional[str] = FieldInfo(alias="optinMessage", default=None)

    optout_keywords: Optional[str] = FieldInfo(alias="optoutKeywords", default=None)

    optout_message: Optional[str] = FieldInfo(alias="optoutMessage", default=None)

    privacy_policy_link: Optional[str] = FieldInfo(alias="privacyPolicyLink", default=None)

    reseller_id: Optional[str] = FieldInfo(alias="resellerId", default=None)

    sharing_status: Optional[Literal["PENDING", "ACCEPTED", "DECLINED"]] = FieldInfo(
        alias="sharingStatus", default=None
    )

    status: Optional[Literal["SENT_CREATED", "ACTIVE", "EXPIRED"]] = None

    submitted_at: Optional[datetime] = FieldInfo(alias="submittedAt", default=None)

    submitted_to_tcr: Optional[bool] = FieldInfo(alias="submittedToTCR", default=None)

    tcr_campaign_id: Optional[str] = FieldInfo(alias="tcrCampaignId", default=None)

    tcr_sync_error: Optional[str] = FieldInfo(alias="tcrSyncError", default=None)

    telnyx_campaign_id: Optional[str] = FieldInfo(alias="telnyxCampaignId", default=None)

    terms_and_conditions_link: Optional[str] = FieldInfo(alias="termsAndConditionsLink", default=None)

    upstream_cnp_id: Optional[str] = FieldInfo(alias="upstreamCnpId", default=None)

    use_cases: Optional[List[TcrCampaignWithUseCasesUseCase]] = FieldInfo(alias="useCases", default=None)
