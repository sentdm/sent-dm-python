# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..shared.base_dto import BaseDto
from .messaging_use_case_us import MessagingUseCaseUs

__all__ = ["TcrCampaignWithUseCases", "TcrCampaignWithUseCasesUseCase"]


class TcrCampaignWithUseCasesUseCase(BaseDto):
    campaign_id: Optional[str] = FieldInfo(alias="campaignId", default=None)

    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)

    messaging_use_case_us: Optional[MessagingUseCaseUs] = FieldInfo(alias="messagingUseCaseUs", default=None)

    sample_messages: Optional[List[str]] = FieldInfo(alias="sampleMessages", default=None)


class TcrCampaignWithUseCases(BaseDto):
    billed_date: Optional[datetime] = FieldInfo(alias="billedDate", default=None)

    brand_id: Optional[str] = FieldInfo(alias="brandId", default=None)

    cost: Optional[float] = None

    csp_id: Optional[str] = FieldInfo(alias="cspId", default=None)

    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)

    description: Optional[str] = None

    help_keywords: Optional[str] = FieldInfo(alias="helpKeywords", default=None)

    help_message: Optional[str] = FieldInfo(alias="helpMessage", default=None)

    kyc_submission_form_id: Optional[str] = FieldInfo(alias="kycSubmissionFormId", default=None)

    message_flow: Optional[str] = FieldInfo(alias="messageFlow", default=None)

    name: Optional[str] = None

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

    type: Optional[str] = None

    upstream_cnp_id: Optional[str] = FieldInfo(alias="upstreamCnpId", default=None)

    use_cases: Optional[List[TcrCampaignWithUseCasesUseCase]] = FieldInfo(alias="useCases", default=None)
