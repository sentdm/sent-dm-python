# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["UserResponse"]


class UserResponse(BaseModel):
    """User response for v3 API"""

    id: Optional[str] = None
    """User unique identifier"""

    created_at: Optional[datetime] = None
    """When the user was added to the organization"""

    customer_id: Optional[str] = None
    """Which customer owns this — the key's own, or the profile named in x-profile-id.

    Says whose resource this is, which the resource's own id does not.
    """

    email: Optional[str] = None
    """User email address"""

    invited_at: Optional[datetime] = None
    """When the user was invited"""

    last_login_at: Optional[datetime] = None
    """When the user last logged in"""

    name: Optional[str] = None
    """User full name"""

    role: Optional[str] = None
    """User role in the organization: admin, billing, developer"""

    status: Optional[str] = None
    """User status: active, invited, suspended, rejected"""

    updated_at: Optional[datetime] = None
    """When the user record was last updated"""
