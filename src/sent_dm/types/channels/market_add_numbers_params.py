# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .sms_number_request_param import SMSNumberRequestParam

__all__ = ["MarketAddNumbersParams"]


class MarketAddNumbersParams(TypedDict, total=False):
    channel: Required[str]

    country: Required[str]

    numbers: Required[Iterable[Optional[SMSNumberRequestParam]]]
    """The numbers, one entry per area code, e.g.

    [{"area_code": "415", "quantity": 2}, {"quantity": 1}]. quantity defaults to 1,
    and an entry without area_code means any area code. Required.

    POST adds them to what the market or campaign already asks for; PATCH replaces
    that list with them, and has to cover every number already held, since none is
    ever released.
    """

    idempotency_key: Required[Annotated[str, PropertyInfo(alias="Idempotency-Key")]]

    campaign_id: Optional[str]
    """The campaign to add the numbers to, as campaigns[].id reports it.

    Required on SMS US TEN_DLC, where every number belongs to a campaign; refused on
    a market without campaigns.
    """

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
