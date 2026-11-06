# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RcsAddress"]


class RcsAddress(BaseModel):
    """The registered address of the company behind the agent."""

    city: Optional[str] = None

    country: Optional[str] = None

    postal_code: Optional[str] = None

    state: Optional[str] = None

    street: Optional[str] = None
