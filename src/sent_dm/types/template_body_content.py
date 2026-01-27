# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .template_variable import TemplateVariable

__all__ = ["TemplateBodyContent"]


class TemplateBodyContent(BaseModel):
    template: Optional[str] = None

    type: Optional[str] = None

    variables: Optional[List[TemplateVariable]] = None
