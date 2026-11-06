# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["MessageChannelOptionsParam"]

_MessageChannelOptionsParamReservedKeywords = TypedDict(
    "_MessageChannelOptionsParamReservedKeywords",
    {
        "from": Optional[SequenceNotStr[str]],
    },
    total=False,
)


class MessageChannelOptionsParam(_MessageChannelOptionsParamReservedKeywords, total=False):
    """
    One entry of a channel's list in Channels, e.g.
    {"country": "US", "from": ["+15559990002", "+15559990003"], "strategy": "sticky"}.
    """

    country: Optional[str]
    """Recipient country this entry is meant for (ISO 3166-1 alpha-2, e.g.

    US). Optional. Accepted and stored, not acted on yet.
    """

    strategy: Optional[str]
    """How to pick a number from From, e.g.

    sticky or geo. Optional. Accepted and stored, not acted on yet.
    """
