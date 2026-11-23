# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["TemplateRefParam"]


class TemplateRefParam(TypedDict, total=False):
    """
    SDK-style template reference: resolve by id, by slug or by name (exactly one), with optional parameters.
    """

    id: Optional[str]
    """Template ID (mutually exclusive with slug and name)"""

    name: Optional[str]
    """Template name (mutually exclusive with id and slug)"""

    parameters: Optional[Dict[str, str]]
    """Template variable parameters for personalization, keyed by variable name.

    Every variable the template declares is required; GET /v3/templates/{id} lists
    them. Supplying a key the template does not declare is ignored.

    Media headers. A template whose header is an image (designed in WhatsApp Manager
    and imported into Sent) declares a reserved header_image key. Its value is a
    publicly reachable https URL that Meta fetches at send time — Sent does not host
    the asset, and the sample approved with the template is not reused. The key is
    derived from the header's media type, so header_video and header_document follow
    the same shape when those formats ship.

    "parameters": { "header_image": "https://cdn.example.com/banner.jpg", "name":
    "John Doe" }
    """

    slug: Optional[str]
    """
    Template slug (mutually exclusive with id and name): the stable name every
    template on this account carries (GET /v3/templates lists them). Compared
    case-insensitively.
    """
