# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BillingContact"]


class BillingContact(BaseModel):
    """Billing contact info returned in profile responses"""

    address: Optional[str] = None

    email: Optional[str] = None

    name: Optional[str] = None

    phone: Optional[str] = None
