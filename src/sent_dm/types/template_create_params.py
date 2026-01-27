# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .template_definition_param import TemplateDefinitionParam

__all__ = ["TemplateCreateParams"]


class TemplateCreateParams(TypedDict, total=False):
    definition: Required[TemplateDefinitionParam]
    """Template definition containing header, body, footer, and buttons"""

    category: Optional[str]
    """The template category (e.g., MARKETING, UTILITY, AUTHENTICATION).

    Can only be set when creating a new template. If not provided, will be
    auto-generated using AI.
    """

    language: Optional[str]
    """The template language code (e.g., en_US, es_ES).

    Can only be set when creating a new template. If not provided, will be
    auto-detected using AI.
    """

    submit_for_review: Annotated[bool, PropertyInfo(alias="submitForReview")]
    """
    When false, the template will be saved as draft. When true, the template will be
    submitted for review.
    """
