# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SMSNumberRequestParam"]


class SMSNumberRequestParam(TypedDict, total=False):
    """
    One entry of numbers: how many numbers to assign in one area code, or in any area code when
    AreaCode is omitted.
    """

    area_code: Optional[str]
    """The area code, e.g.

    212, validated against the request's country. Omit it for numbers in any area
    code.
    """

    quantity: Optional[int]
    """How many numbers. At least 1; omitted means 1."""
