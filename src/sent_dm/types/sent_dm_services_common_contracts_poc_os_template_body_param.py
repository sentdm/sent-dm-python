# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .template_body_content_param import TemplateBodyContentParam

__all__ = ["SentDmServicesCommonContractsPocOsTemplateBodyParam"]


class SentDmServicesCommonContractsPocOsTemplateBodyParam(TypedDict, total=False):
    """Body section of a message template with channel-specific content"""

    multi_channel: Annotated[Optional[TemplateBodyContentParam], PropertyInfo(alias="multiChannel")]
    """
    Content that will be used for all channels (SMS and WhatsApp) unless
    channel-specific content is provided
    """

    rcs: Optional[TemplateBodyContentParam]
    """RCS-specific content that overrides multi-channel content for RCS messages"""

    sms: Optional[TemplateBodyContentParam]
    """SMS-specific content that overrides multi-channel content for SMS messages"""

    whatsapp: Optional[TemplateBodyContentParam]
    """
    WhatsApp-specific content that overrides multi-channel content for WhatsApp
    messages
    """
