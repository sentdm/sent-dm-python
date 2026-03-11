# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["BillingContactInfoParam"]


class BillingContactInfoParam(TypedDict, total=False):
    """
    Billing contact information for a profile.
    Required when billing_model is "profile" or "profile_and_organization".
    """

    email: Required[str]
    """Email address where invoices will be sent (required)"""

    name: Required[str]
    """Full name of the billing contact or company (required)"""

    address: Optional[str]
    """Billing address (optional).

    Free-form text including street, city, state, postal code, and country.
    """

    phone: Optional[str]
    """Phone number for the billing contact (optional)"""
