# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccountSMSChannel"]


class AccountSMSChannel(BaseModel):
    """SMS channel configuration. When configured, includes the sending phone number."""

    configured: Optional[bool] = None
    """Whether SMS is configured for this account"""

    phone_number: Optional[str] = None
    """Sending phone number in E.164 format"""
