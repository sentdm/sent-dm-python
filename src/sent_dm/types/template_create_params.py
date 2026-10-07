# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .template_definition_param import TemplateDefinitionParam

__all__ = ["TemplateCreateParams"]


class TemplateCreateParams(TypedDict, total=False):
    api_key: Annotated[str, PropertyInfo(alias="apiKey")]
    """
    API key from the x-api-key header, or empty when the caller sent it as
    Authorization: Bearer instead.

    Optional on purpose. CustomerV3AuthenticationHandler accepts the key in either
    header, and [FromHeader] is required by default, so a Bearer-only request would
    authenticate and then be refused with a 400 for a header it never needed.
    Endpoints read the customer from the CustomerId claim, not from this value.
    """

    auto_create_for_sp: bool
    """
    Create this template automatically on every sender profile of the organization,
    now and in future (default: false). Accepted only from an organization that has
    been enabled for it, and only at creation — it cannot be changed afterwards.
    """

    category: Optional[str]
    """
    Template category: MARKETING, UTILITY, AUTHENTICATION (optional, auto-detected
    if not provided)
    """

    creation_source: Optional[str]
    """Source of template creation (default: from-api)"""

    definition: TemplateDefinitionParam
    """
    Complete definition of a message template including header, body, footer, and
    buttons
    """

    language: Optional[str]
    """Template language code (e.g., en_US) (optional, auto-detected if not provided)"""

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    submit_for_review: bool
    """Whether to submit the template for review after creation (default: false)"""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
