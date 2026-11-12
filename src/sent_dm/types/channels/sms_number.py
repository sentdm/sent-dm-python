# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SMSNumber"]


class SMSNumber(BaseModel):
    """One number of an SMS market."""

    area_code: Optional[str] = None
    """The number's area code, e.g.

    212. While the number is still to be assigned, the area code it was asked for,
         or null when it was asked for in any area code.
    """

    campaign_id: Optional[str] = None
    """
    The campaign the number is on, or is owed for: the id of its entry in
    compliance.campaigns. Omitted for a market that registers no campaigns, and
    where the campaign is not known — a number recorded without one, or one owed on
    a campaign inherited from the organization.
    """

    sender_value: Optional[str] = None
    """The number, or null while it is still to be assigned."""

    status: Optional[str] = None
    """
    ACTIVE once the number can send; PROVISIONING while it is still to be assigned;
    INACTIVE once it could send and no longer can.
    """
