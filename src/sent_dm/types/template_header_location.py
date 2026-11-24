# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["TemplateHeaderLocation"]


class TemplateHeaderLocation(BaseModel):
    """The map pin a location header drops.

    Meta wants none of this at creation — the component is just
    {"type":"header","format":"location"} — so these values exist for Sent: a preview, and the
    default a StaticResource header falls back to at send.
    """

    address: str

    latitude: str

    longitude: str

    name: str
