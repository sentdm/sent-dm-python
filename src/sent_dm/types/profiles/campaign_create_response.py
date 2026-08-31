# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .messaging_use_case_us import MessagingUseCaseUs

__all__ = ["CampaignCreateResponse", "Data", "DataUseCase", "Error", "Meta"]


class DataUseCase(BaseModel):
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


class Data(BaseModel):
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

    use_cases: Optional[List[DataUseCase]] = FieldInfo(alias="useCases", default=None)

    volume: Optional[str] = None
    """
    Expected messaging volume for this campaign — customer-supplied on
    create/update, and the input to both the TCR usecase classification (LOW_VOLUME
    vs MIXED/specific) and the campaign fee tier. Surfaced so customers can read
    back the value they set.
    """


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
    """A 10DLC campaign registered for a brand."""

    error: Optional[Error] = None
    """Error information"""

    meta: Optional[Meta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
