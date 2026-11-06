# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccountRcsChannel"]


class AccountRcsChannel(BaseModel):
    """RCS channel configuration. When configured, includes the RCS phone number."""

    configured: Optional[bool] = None
    """Whether RCS is configured for this account"""

    phone_number: Optional[str] = None
    """RCS-enabled phone number in E.164 format"""
