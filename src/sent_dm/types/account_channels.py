# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .account_rcs_channel import AccountRcsChannel
from .account_sms_channel import AccountSMSChannel
from .account_whatsapp_channel import AccountWhatsappChannel

__all__ = ["AccountChannels"]


class AccountChannels(BaseModel):
    """Messaging channel configuration.

    All three channels are always present.
    Each channel has a "configured" flag; configured channels expose additional details.
    """

    rcs: Optional[AccountRcsChannel] = None
    """RCS channel configuration. When configured, includes the RCS phone number."""

    sms: Optional[AccountSMSChannel] = None
    """SMS channel configuration. When configured, includes the sending phone number."""

    whatsapp: Optional[AccountWhatsappChannel] = None
    """WhatsApp Business channel configuration.

    When configured, includes the WhatsApp phone number and business name.
    """
