# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SentDmServicesCommonContractsPocOsAuthenticationConfigParam"]


class SentDmServicesCommonContractsPocOsAuthenticationConfigParam(TypedDict, total=False):
    """Configuration for AUTHENTICATION category templates"""

    add_security_recommendation: Annotated[bool, PropertyInfo(alias="addSecurityRecommendation")]
    """
    Whether to add the security recommendation text: "For your security, do not
    share this code."
    """

    code_expiration_minutes: Annotated[Optional[int], PropertyInfo(alias="codeExpirationMinutes")]
    """Code expiration time in minutes (1-90).

    If set, adds footer: "This code expires in X minutes."
    """
