# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CallParticipantTargetParam"]


class CallParticipantTargetParam(TypedDict, total=False):
    """A participant to add to a call"""

    kind: str
    """user for one of your app users, number for a phone number"""

    value: str
    """The app user's identity, or the phone number in E.164 format"""
