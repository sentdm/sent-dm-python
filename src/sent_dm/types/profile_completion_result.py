# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ProfileCompletionResult"]


class ProfileCompletionResult(BaseModel):
    """
    Response when a profile is already in the completed state and no further action is taken.
    """

    message: Optional[str] = None
    """Human-readable message describing the result."""

    status: Optional[str] = None
    """
    Current process status of the profile (e.g., "completed", "submitted",
    "in_progress").
    """
