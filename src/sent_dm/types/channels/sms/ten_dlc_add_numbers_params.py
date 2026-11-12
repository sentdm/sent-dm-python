# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from ..sms_number_request_param import SMSNumberRequestParam

__all__ = ["TenDlcAddNumbersParams"]


class TenDlcAddNumbersParams(TypedDict, total=False):
    campaign_id: Required[str]
    """The campaign to add the numbers to, as compliance.campaigns[].id reports it.

    Required.
    """

    numbers: Required[Iterable[Optional[SMSNumberRequestParam]]]
    """The numbers to add, one entry per area code, e.g.

    [{"area_code": "415", "quantity": 2}, {"quantity": 1}]. quantity defaults to 1,
    and an entry without area_code means any area code. Required.

    Added to what the campaign already asks for, never replacing it.
    """

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
