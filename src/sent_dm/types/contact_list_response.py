# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .contact import Contact
from .._models import BaseModel
from .api_meta import APIMeta
from .api_error import APIError
from .pagination_meta import PaginationMeta

__all__ = ["ContactListResponse", "Data"]


class Data(BaseModel):
    """The response data (null if error)"""

    contacts: Optional[List[Contact]] = None
    """List of contacts"""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata"""


class ContactListResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """The response data (null if error)"""

    error: Optional[APIError] = None
    """Error details (null if successful)"""

    meta: Optional[APIMeta] = None
    """Metadata about the request and response"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
