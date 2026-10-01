# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["VoiceCallbackTestRequestInfo"]


class VoiceCallbackTestRequestInfo(BaseModel):
    """The test question exactly as it was sent"""

    body: Optional[str] = None
    """The request body byte for byte. This is what the signature covers."""

    headers: Optional[Dict[str, str]] = None
    """
    Every header Sent added, the signature included, so you can compare against what
    your endpoint verified. The signing secret itself is never included.
    """

    url: Optional[str] = None
    """The callback URL that was called"""
