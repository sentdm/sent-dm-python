# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .api_error import APIError
from .pagination_meta import PaginationMeta
from .contact_response import ContactResponse

__all__ = ["ContactListResponse", "Data"]


class Data(BaseModel):
    """Paginated list of contacts response"""

    contacts: Optional[List[ContactResponse]] = None
    """List of contacts"""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""


class ContactListResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """Paginated list of contacts response"""

    error: Optional[APIError] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
