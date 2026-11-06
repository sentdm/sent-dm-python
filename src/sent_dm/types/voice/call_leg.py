# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CallLeg"]


class CallLeg(BaseModel):
    """One leg of a call the price covers"""

    billed_minutes: Optional[int] = None
    """The whole minutes the leg was billed for"""

    cost: Optional[float] = None
    """What the leg cost, in the same unit as the call's price"""

    currency: Optional[str] = None
    """The currency of the cost: USD"""

    direction: Optional[str] = None
    """
    inbound for the caller's leg to your number, outbound for a leg placed on your
    behalf
    """

    number: Optional[str] = None
    """
    The phone number the leg reached, in E.164 format: your number for the inbound
    leg, the number dialed for an outbound one. Null for a leg to one of your app
    users or a room
    """
