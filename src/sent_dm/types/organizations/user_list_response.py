# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .customer_user import CustomerUser

__all__ = ["UserListResponse"]


class UserListResponse(BaseModel):
    page: Optional[int] = None

    page_size: Optional[int] = FieldInfo(alias="pageSize", default=None)

    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)

    users: Optional[List[CustomerUser]] = None
