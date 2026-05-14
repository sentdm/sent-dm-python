# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CampaignCreateParams", "Campaign", "CampaignUseCase"]


class CampaignCreateParams(TypedDict, total=False):
    campaign: Required[Campaign]
    """Campaign data for create or update operation"""

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]


class CampaignUseCase(TypedDict, total=False):
    """Campaign use case with sample messages"""

    messaging_use_case_us: Required[
        Annotated[
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
            ],
            PropertyInfo(alias="messagingUseCaseUs"),
        ]
    ]

    sample_messages: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="sampleMessages")]]
    """Sample messages for this use case (1-5 messages, max 1024 characters each)"""


class Campaign(TypedDict, total=False):
    """Campaign data for create or update operation"""

    description: Required[str]
    """Campaign description"""

    name: Required[str]
    """Campaign name"""

    type: Required[str]
    """Campaign type (e.g., "KYC", "App")"""

    use_cases: Required[Annotated[Iterable[CampaignUseCase], PropertyInfo(alias="useCases")]]
    """List of use cases with sample messages"""

    help_keywords: Annotated[Optional[str], PropertyInfo(alias="helpKeywords")]
    """
    Comma-separated keywords that trigger help message (e.g., "HELP, INFO, SUPPORT")
    """

    help_message: Annotated[Optional[str], PropertyInfo(alias="helpMessage")]
    """Message sent when user requests help"""

    message_flow: Annotated[Optional[str], PropertyInfo(alias="messageFlow")]
    """Description of how messages flow in the campaign"""

    optin_keywords: Annotated[Optional[str], PropertyInfo(alias="optinKeywords")]
    """Comma-separated keywords that trigger opt-in (e.g., "YES, START, SUBSCRIBE")"""

    optin_message: Annotated[Optional[str], PropertyInfo(alias="optinMessage")]
    """Message sent when user opts in"""

    optout_keywords: Annotated[Optional[str], PropertyInfo(alias="optoutKeywords")]
    """Comma-separated keywords that trigger opt-out (e.g., "STOP, UNSUBSCRIBE, END")"""

    optout_message: Annotated[Optional[str], PropertyInfo(alias="optoutMessage")]
    """Message sent when user opts out"""

    privacy_policy_link: Annotated[Optional[str], PropertyInfo(alias="privacyPolicyLink")]
    """URL to privacy policy"""

    terms_and_conditions_link: Annotated[Optional[str], PropertyInfo(alias="termsAndConditionsLink")]
    """URL to terms and conditions"""
