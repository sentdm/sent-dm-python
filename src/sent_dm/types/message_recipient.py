# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MessageRecipient"]


class MessageRecipient(BaseModel):
    """What one recipient of a send got, as the API reports it."""

    body: Optional[str] = None
    """
    Resolved template body for this recipient's channel, or null when the channel is
    auto-detected.
    """

    channel: Optional[str] = None
    """Channel this message will be sent on — sms, whatsapp — or null to auto-detect."""

    message_id: Optional[str] = None
    """Identifier for tracking this recipient's message."""

    to: Optional[str] = None
    """Phone number in E.164 format."""
