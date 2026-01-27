# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProfileSummary"]


class ProfileSummary(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    icon: Optional[str] = None

    name: Optional[str] = None

    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)
