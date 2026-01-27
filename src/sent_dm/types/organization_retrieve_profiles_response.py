# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .profile_summary import ProfileSummary

__all__ = ["OrganizationRetrieveProfilesResponse"]


class OrganizationRetrieveProfilesResponse(BaseModel):
    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)

    profiles: Optional[List[ProfileSummary]] = None
