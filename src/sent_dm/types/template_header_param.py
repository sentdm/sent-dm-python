# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .template_variable_param import TemplateVariableParam

__all__ = ["TemplateHeaderParam", "Location"]


class Location(TypedDict, total=False):
    """The map pin a location header drops.

    Meta wants none of this at creation — the component is just
    {"type":"header","format":"location"} — so these values exist for Sent: a preview, and the
    default a StaticResource header falls back to at send.
    """

    address: Required[str]

    latitude: Required[str]

    longitude: Required[str]

    name: Required[str]


class TemplateHeaderParam(TypedDict, total=False):
    """Header section of a message template"""

    template: Required[str]
    """
    The header template text with optional variable placeholders (e.g., "Welcome to
    {{0:variable}}")
    """

    example_url: Optional[str]
    """Request-only.

    The s.dm URL of the asset Meta's reviewers see — https://s.dm/s/{ID}, eight
    uppercase characters, uploaded to s.dm out of band. NormalizeRichHeader folds it
    into the synthesized media variable's Props.Sample and clears it, so it never
    persists and a stored definition is indistinguishable from an imported one.

    Stricter than the send path on purpose:
    TemplateUtils.ValidateMediaVariableValues accepts any absolute https URL for the
    per-send asset, because that one is the customer's and may live behind a signed
    CDN link. This one is the review sample, has to outlive every resubmission, and
    so must be ours. Do not "fix" one to match the other.
    """

    location: Optional[Location]
    """The map pin a location header drops.

    Meta wants none of this at creation — the component is just
    {"type":"header","format":"location"} — so these values exist for Sent: a
    preview, and the default a StaticResource header falls back to at send.
    """

    static_resource: bool
    """
    Whether the asset registered at creation is reused when a caller omits the
    header's variable at send time. Default false — the caller must supply it per
    message, which is the behaviour every existing template has. Written only when
    true, so a default-valued header serializes byte-identically to one imported
    from Meta.

    Stored and validated but not yet honoured at send: that lands with the Resumable
    Upload work, alongside the code that lets such a template be approved in the
    first place.
    """

    type: Optional[str]
    """The kind of header. One of:

    text — up to 60 characters, at most one variable. image — png, jpg or jpeg.
    Needs ExampleUrl. video — mp4. Needs ExampleUrl. gif — mp4, max 3.5MB. WhatsApp
    renders larger files as an ordinary video. Needs ExampleUrl. document — pdf or
    docx; only the first page is shown as a thumbnail, so pdf is the practical
    choice. Needs ExampleUrl. location — a map pin, supplied through Location.

    Kept lowercase because MetaToTemplateConverter writes Meta's format through
    ToLowerInvariant() into this field on import, and the two are compared directly.
    """

    variables: Optional[Iterable[TemplateVariableParam]]
    """List of variables used in the header template"""
