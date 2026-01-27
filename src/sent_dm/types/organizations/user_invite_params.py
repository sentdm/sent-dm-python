# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserInviteParams"]


class UserInviteParams(TypedDict, total=False):
    email: str

    invited_by: Annotated[Optional[str], PropertyInfo(alias="invitedBy")]

    name: str

    role: str
