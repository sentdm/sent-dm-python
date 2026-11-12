# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TemplateHeaderLocationParam"]


class TemplateHeaderLocationParam(TypedDict, total=False):
    """The map pin a location header drops.

    Meta wants none of this at creation — the component is just
    {"type":"header","format":"location"} — so these values exist for Sent: a preview, and the
    default a StaticResource header falls back to at send.
    """

    address: Required[str]

    latitude: Required[str]

    longitude: Required[str]

    name: Required[str]
