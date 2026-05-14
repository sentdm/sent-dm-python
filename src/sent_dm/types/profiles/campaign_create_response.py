# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CampaignCreateResponse", "Data", "DataUseCase", "Error", "Meta"]


class DataUseCase(BaseModel):
    id: Optional[str] = None
    """Unique identifier"""

    campaign_id: Optional[str] = FieldInfo(alias="campaignId", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)

    messaging_use_case_us: Optional[
        Literal[
            "MARKETING",
            "ACCOUNT_NOTIFICATION",
            "CUSTOMER_CARE",
            "FRAUD_ALERT",
            "TWO_FA",
            "DELIVERY_NOTIFICATION",
            "SECURITY_ALERT",
            "M2M",
            "MIXED",
            "HIGHER_EDUCATION",
            "POLLING_VOTING",
            "PUBLIC_SERVICE_ANNOUNCEMENT",
            "LOW_VOLUME",
        ]
    ] = FieldInfo(alias="messagingUseCaseUs", default=None)

    sample_messages: Optional[List[str]] = FieldInfo(alias="sampleMessages", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)


class Data(BaseModel):
    """The response data (null if error)"""

    id: Optional[str] = None
    """Unique identifier"""

    billed_date: Optional[datetime] = FieldInfo(alias="billedDate", default=None)

    brand_id: Optional[str] = FieldInfo(alias="brandId", default=None)

    cost: Optional[float] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    csp_id: Optional[str] = FieldInfo(alias="cspId", default=None)

    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)

    dca_elections_complete: Optional[bool] = FieldInfo(alias="dcaElectionsComplete", default=None)

    dca_elections_completed_at: Optional[datetime] = FieldInfo(alias="dcaElectionsCompletedAt", default=None)

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

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    upstream_cnp_id: Optional[str] = FieldInfo(alias="upstreamCnpId", default=None)

    use_cases: Optional[List[DataUseCase]] = FieldInfo(alias="useCases", default=None)


class Error(BaseModel):
    """Error information"""

    code: Optional[str] = None
    """Machine-readable error code (e.g., "RESOURCE_001")"""

    details: Optional[Dict[str, List[str]]] = None
    """Additional validation error details (field-level errors)"""

    doc_url: Optional[str] = None
    """URL to documentation about this error"""

    message: Optional[str] = None
    """Human-readable error message"""


class Meta(BaseModel):
    """Request and response metadata"""

    request_id: Optional[str] = None
    """Unique identifier for this request (for tracing and support)"""

    timestamp: Optional[datetime] = None
    """Server timestamp when the response was generated"""

    version: Optional[str] = None
    """API version used for this request"""


class CampaignCreateResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The response data (null if error)"""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
