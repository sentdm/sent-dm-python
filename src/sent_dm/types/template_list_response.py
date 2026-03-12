# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .template import Template
from .api_error import APIError
from .pagination_meta import PaginationMeta

__all__ = ["TemplateListResponse", "Data"]


class Data(BaseModel):
    """Paginated list of templates"""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""

    templates: Optional[List[Template]] = None
    """List of templates"""


class TemplateListResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """Paginated list of templates"""

    error: Optional[APIError] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
