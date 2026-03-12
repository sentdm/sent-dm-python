# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .template_variable_param import TemplateVariableParam

__all__ = ["SentDmServicesCommonContractsPocOsTemplateFooterParam"]


class SentDmServicesCommonContractsPocOsTemplateFooterParam(TypedDict, total=False):
    """Footer section of a message template"""

    template: str
    """The footer template text with optional variable placeholders"""

    type: Optional[str]
    """The type of footer (typically "text")"""

    variables: Optional[Iterable[TemplateVariableParam]]
    """List of variables used in the footer template"""
