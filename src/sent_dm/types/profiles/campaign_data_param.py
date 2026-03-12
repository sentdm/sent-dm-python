# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .sent_dm_services_endpoints_customer_ap_iv3_contracts_requests_campaigns_campaign_use_case_data_param import (
    SentDmServicesEndpointsCustomerApIv3ContractsRequestsCampaignsCampaignUseCaseDataParam,
)

__all__ = ["CampaignDataParam"]


class CampaignDataParam(TypedDict, total=False):
    """Campaign data for create or update operation"""

    description: Required[str]
    """Campaign description"""

    name: Required[str]
    """Campaign name"""

    type: Required[str]
    """Campaign type (e.g., "KYC", "App")"""

    use_cases: Required[
        Annotated[
            Iterable[SentDmServicesEndpointsCustomerApIv3ContractsRequestsCampaignsCampaignUseCaseDataParam],
            PropertyInfo(alias="useCases"),
        ]
    ]
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
