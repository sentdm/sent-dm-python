# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["WebhookSenderProfileConfigParam"]


class WebhookSenderProfileConfigParam(TypedDict, total=False):
    """
    Request-only: the events an organization webhook's sender profile clones receive, one clone per existing
    and future profile. A version 1 webhook's responses report it as WebhookSenderProfileV3Response.
    """

    event_filters: Optional[Dict[str, SequenceNotStr[str]]]

    event_types: SequenceNotStr[str]
