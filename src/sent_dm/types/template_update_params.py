# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .template_definition_param import TemplateDefinitionParam

__all__ = ["TemplateUpdateParams"]


class TemplateUpdateParams(TypedDict, total=False):
    category: Optional[str]
    """Template category: MARKETING, UTILITY, AUTHENTICATION"""

    definition: Optional[TemplateDefinitionParam]
    """
    Complete definition of a message template including header, body, footer, and
    buttons
    """

    language: Optional[str]
    """Template language code (e.g., en_US)"""

    name: Optional[str]
    """Template display name"""

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    submit_for_review: bool
    """Whether to submit the template for review after updating (default: false)"""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
