# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CustomerUser"]


class CustomerUser(BaseModel):
    id: Optional[str] = None
    """Unique identifier"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)

    email: Optional[str] = None

    invitation_sent_at: Optional[datetime] = FieldInfo(alias="invitationSentAt", default=None)

    invitation_token: Optional[str] = FieldInfo(alias="invitationToken", default=None)

    invitation_token_expires_at: Optional[datetime] = FieldInfo(alias="invitationTokenExpiresAt", default=None)

    last_login_at: Optional[datetime] = FieldInfo(alias="lastLoginAt", default=None)

    name: Optional[str] = None

    role: Optional[str] = None

    status: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
