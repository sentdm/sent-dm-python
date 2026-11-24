# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AuthenticationConfig"]


class AuthenticationConfig(BaseModel):
    """Configuration for AUTHENTICATION category templates"""

    add_security_recommendation: Optional[bool] = FieldInfo(alias="addSecurityRecommendation", default=None)
    """
    Whether to add the security recommendation text: "For your security, do not
    share this code."
    """

    code_expiration_minutes: Optional[int] = FieldInfo(alias="codeExpirationMinutes", default=None)
    """Code expiration time in minutes (1-90).

    If set, adds footer: "This code expires in X minutes."
    """
