# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TemplateDeleteParams"]


class TemplateDeleteParams(TypedDict, total=False):
    delete_from_meta: Optional[bool]
    """
    Whether to also delete the template from WhatsApp/Meta (optional, defaults to
    false)
    """

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
