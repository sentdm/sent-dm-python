# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CallParticipant"]


class CallParticipant(BaseModel):
    """A participant of a conference call"""

    id: Optional[str] = None
    """
    The participant's own call id: what the mute and remove endpoints take, and what
    GET /v3/calls/{id} accepts
    """

    duration_seconds: Optional[int] = None
    """How long the participant has been connected to the room, in seconds"""

    kind: Optional[str] = None
    """
    user for one of your app users, number for a phone number, anonymous for a
    caller who withheld their number
    """

    muted: Optional[bool] = None
    """True while the room mutes this participant"""

    value: Optional[str] = None
    """The app user's identity or the phone number in E.164 format.

    Null when the kind is anonymous
    """
