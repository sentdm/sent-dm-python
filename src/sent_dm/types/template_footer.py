# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .template_variable import TemplateVariable

__all__ = ["TemplateFooter"]


class TemplateFooter(BaseModel):
    """Footer section of a message template"""

    template: str
    """The footer template text with optional variable placeholders"""

    type: Optional[str] = None
    """The type of footer (typically "text")"""

    variables: Optional[List[TemplateVariable]] = None
    """List of variables used in the footer template"""
