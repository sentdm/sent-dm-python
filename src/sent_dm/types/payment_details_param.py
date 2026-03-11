# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PaymentDetailsParam"]


class PaymentDetailsParam(TypedDict, total=False):
    """
    Payment card details for a profile.
    Accepted when billing_model is "profile" or "profile_and_organization".
    These details are not stored on our servers and will be forwarded to the payment processor.
    """

    card_number: Required[str]
    """Card number (digits only, 13–19 characters)"""

    cvc: Required[str]
    """Card security code (3–4 digits)"""

    expiry: Required[str]
    """Card expiry date in MM/YY format (e.g. "09/27")"""

    zip_code: Required[str]
    """Billing ZIP / postal code associated with the card"""
