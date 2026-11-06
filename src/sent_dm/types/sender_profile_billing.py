# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SenderProfileBilling"]


class SenderProfileBilling(BaseModel):
    """
    Who pays for a sender profile's traffic, as a read reports it.

    Its own type, field for field the same as
    BillingRequest. Same reason as the brand: a response is not
    a request, whatever it carries.
    """

    inherit: Optional[bool] = None
    """Whether the organization pays, rather than the profile."""
