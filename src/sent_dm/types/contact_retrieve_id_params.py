# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContactRetrieveIDParams"]


class ContactRetrieveIDParams(TypedDict, total=False):
    id: Required[str]
    """The unique identifier (GUID) of the resource to retrieve"""
