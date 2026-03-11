# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .messaging_use_case_us import MessagingUseCaseUs

__all__ = ["SentDmServicesEndpointsCustomerApIv3ContractsRequestsCampaignsCampaignUseCaseDataParam"]


class SentDmServicesEndpointsCustomerApIv3ContractsRequestsCampaignsCampaignUseCaseDataParam(TypedDict, total=False):
    """Campaign use case with sample messages"""

    messaging_use_case_us: Required[Annotated[MessagingUseCaseUs, PropertyInfo(alias="messagingUseCaseUs")]]
    """US messaging use case category"""

    sample_messages: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="sampleMessages")]]
    """Sample messages for this use case (1-5 messages, max 1024 characters each)"""
