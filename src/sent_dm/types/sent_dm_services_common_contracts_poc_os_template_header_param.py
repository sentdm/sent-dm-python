# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .template_variable_param import TemplateVariableParam

__all__ = ["SentDmServicesCommonContractsPocOsTemplateHeaderParam"]


class SentDmServicesCommonContractsPocOsTemplateHeaderParam(TypedDict, total=False):
    """Header section of a message template"""

    template: Required[str]
    """
    The header template text with optional variable placeholders (e.g., "Welcome to
    {{0:variable}}")
    """

    type: Optional[str]
    """The type of header (e.g., "text", "image", "video", "document")"""

    variables: Optional[Iterable[TemplateVariableParam]]
    """List of variables used in the header template"""
