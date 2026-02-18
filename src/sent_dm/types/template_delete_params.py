# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["TemplateDeleteParams"]


class TemplateDeleteParams(TypedDict, total=False):
    delete_from_meta: Optional[bool]
    """
    Whether to also delete the template from WhatsApp/Meta (optional, defaults to
    false)
    """

    test_mode: bool
    """
    Test mode flag - when true, the operation is simulated without side effects
    Useful for testing integrations without actual execution
    """
