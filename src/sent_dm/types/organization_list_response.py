# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .profile_summary import ProfileSummary

__all__ = ["OrganizationListResponse", "Organization"]


class Organization(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    icon: Optional[str] = None

    name: Optional[str] = None

    profiles: Optional[List[ProfileSummary]] = None


class OrganizationListResponse(BaseModel):
    organizations: Optional[List[Organization]] = None
