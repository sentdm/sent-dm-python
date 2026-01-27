# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .template_response import TemplateResponse

__all__ = ["TemplateListResponse"]


class TemplateListResponse(BaseModel):
    items: Optional[List[TemplateResponse]] = None

    page: Optional[int] = None

    page_size: Optional[int] = FieldInfo(alias="pageSize", default=None)

    total_count: Optional[int] = FieldInfo(alias="totalCount", default=None)

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
