# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["VoiceNumber"]


class VoiceNumber(BaseModel):
    """One number the profile carries phone calls on."""

    callback_url: Optional[str] = None
    """
    Where Sent asks what to do with each call on this number: a signed question is
    POSTed here when a call arrives or a caller presses a key, and the answer
    decides the call. The signing secret is not on this read; it is shown when voice
    is turned on and by the rotate endpoint.
    """

    created_at: Optional[datetime] = None

    default_for_app_calls: Optional[bool] = None
    """
    Whether this is the line app-originated calls are placed from when a voice token
    names no number. Exactly one active voice number carries it while the profile
    has any.
    """

    number: Optional[str] = None
    """The number, in E.164."""

    status: Optional[str] = None
    """ACTIVE while the number carries calls, INACTIVE once it was turned off.

    Nothing provisions: a number the customer holds can carry calls the moment voice
    is turned on for it.
    """

    updated_at: Optional[datetime] = None
