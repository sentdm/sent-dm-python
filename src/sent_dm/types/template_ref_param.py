# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["TemplateRefParam"]


class TemplateRefParam(TypedDict, total=False):
    """
    SDK-style template reference: resolve by ID or by name, with optional parameters.
    """

    id: Optional[str]
    """Template ID (mutually exclusive with name)"""

    name: Optional[str]
    """Template name (mutually exclusive with id)"""

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
