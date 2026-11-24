# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MarketNumber"]


class MarketNumber(BaseModel):
    """One number the customer holds, or is still owed."""

    area_code: Optional[str] = None

    campaign_id: Optional[str] = None
    """The campaign the number belongs to (US TEN_DLC); null otherwise."""

    sender_value: Optional[str] = None
    """The number, or the sender id; null until it is assigned."""

    status: Optional[str] = None
    """ACTIVE, PROVISIONING or INACTIVE."""

    type: Optional[str] = None
    """The market's sender type, e.g. TEN_DLC, LOCAL."""
