# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CallParty"]


class CallParty(BaseModel):
    """One end of a call"""

    kind: Optional[str] = None
    """
    user for one of your app users, number for a phone number, conference for a
    room, anonymous for a caller who withheld their number
    """

    value: Optional[str] = None
    """The app user's identity, the phone number in E.164 format, or the room name.

    Null when the kind is anonymous
    """
