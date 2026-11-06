# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .contact_response import ContactResponse

__all__ = ["ContactsList"]


class ContactsList(BaseModel):
    """A paginated list of contacts."""

    contacts: Optional[List[ContactResponse]] = None
    """The contacts on this page."""

    pagination: Optional[PaginationMeta] = None
    """Pagination metadata for list responses"""
