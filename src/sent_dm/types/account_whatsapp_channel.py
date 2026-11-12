# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccountWhatsappChannel"]


class AccountWhatsappChannel(BaseModel):
    """WhatsApp Business channel configuration.

    When configured, includes the WhatsApp phone number
    and business name.
    """

    business_name: Optional[str] = None
    """WhatsApp Business display name"""

    configured: Optional[bool] = None
    """Whether WhatsApp is configured for this account"""

    phone_number: Optional[str] = None
    """WhatsApp phone number in E.164 format"""
