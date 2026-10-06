# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["VoiceToken"]


class VoiceToken(BaseModel):
    """A short-lived token your app passes to the voice client SDK to register"""

    token: Optional[str] = None
    """The signed token. Hand it to the client SDK unchanged."""

    expires_at: Optional[datetime] = None
    """When the token expires (UTC)"""

    identity: Optional[str] = None
    """The identity the token was minted for"""

    number: Optional[str] = None
    """The phone number this identity is now bound to, in E.164 format"""
