# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail
from .pagination_meta import PaginationMeta
from .contact_response import ContactResponse

__all__ = ["ContactListResponse", "Data"]


class Data(BaseModel):
    """A paginated list of contacts."""

    contacts: Optional[List[ContactResponse]] = None
    """The contacts on this page."""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""


class ContactListResponse(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[Data] = None
    """A paginated list of contacts."""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
