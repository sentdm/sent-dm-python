# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .template_definition_param import TemplateDefinitionParam

__all__ = ["TemplateCreateParams"]


class TemplateCreateParams(TypedDict, total=False):
    category: Optional[str]
    """
    Template category: MARKETING, UTILITY, AUTHENTICATION (optional, auto-detected
    if not provided)
    """

    creation_source: Optional[str]
    """Source of template creation (default: from-api)"""

    definition: TemplateDefinitionParam
    """Template definition including header, body, footer, and buttons"""

    language: Optional[str]
    """Template language code (e.g., en_US) (optional, auto-detected if not provided)"""

    submit_for_review: bool
    """Whether to submit the template for review after creation (default: false)"""

    test_mode: bool
    """
    Test mode flag - when true, the operation is simulated without side effects
    Useful for testing integrations without actual execution
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
