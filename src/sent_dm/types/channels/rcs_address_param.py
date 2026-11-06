# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["RcsAddressParam"]


class RcsAddressParam(TypedDict, total=False):
    """The registered address of the company behind the agent."""

    city: Optional[str]

    country: Optional[str]

    postal_code: Optional[str]

    state: Optional[str]

    street: Optional[str]
