# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .template import Template
from .pagination_meta import PaginationMeta

__all__ = ["TemplatesList"]


class TemplatesList(BaseModel):
    """A paginated list of templates."""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""

    templates: Optional[List[Template]] = None
    """The templates on this page."""
