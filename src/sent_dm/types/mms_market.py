# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MmsMarket"]


class MmsMarket(BaseModel):
    """
    One market the profile can send MMS in.

    Deliberately not SmsMarketState: an MMS market carries no compliance of its own. It
    is the same number, carrier and registration as the SMS market on it in that country — MMS files nothing
    separately — so a compliance block here would always be null and would invite the question of
    what an MMS market owes. It owes what the SMS market owes, reported there.
    """

    country: Optional[str] = None
    """ISO-3166 alpha-2 of the market."""

    number_type: Optional[str] = None
    """The sender type the market sends from, mirroring the SMS sender."""

    sender_value: Optional[str] = None
    """The sending number. Null while the market is still being provisioned."""

    status: Optional[str] = None
    """Where this market's MMS sender stands. Read-only."""
