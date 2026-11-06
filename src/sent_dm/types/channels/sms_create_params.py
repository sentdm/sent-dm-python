# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .market_compliance_param import MarketComplianceParam
from .sms_number_request_param import SMSNumberRequestParam

__all__ = ["SMSCreateParams"]


class SMSCreateParams(TypedDict, total=False):
    number_type: Required[Literal["LOCAL", "TOLL_FREE", "SHORT_CODE", "ALPHANUMERIC", "TEN_DLC", "MOBILE", "10DLC"]]
    """Sender type. Decides the provisioning flow and what compliance is asked for.

    [Required] so the published document says so. The validator has always demanded
    it, but requiredness reached the schema by matching a rule to a property name —
    which works for country, whose wire name is its camel-cased C# name, and
    silently does not for number_type. A client generating a request from our
    OpenAPI therefore sent what the document called sufficient and was answered 400.
    """

    area_codes: Optional[SequenceNotStr[str]]
    """The area codes to put this sender in, in your own order of preference, e.g.

    ["415", "628"] for the US or ["20"] for London. Omit it and a number is claimed
    anywhere in the country.

    Ordered, and the order is the request. The claim tries each code in turn and
    stops at the first that yields a number. Nothing sorts the list and a code
    listed twice is refused.

    One to fifty entries, each the area code as digits: 415, with the trunk prefix
    as 020, or with the country's dialing prefix as +1415 (all are stored as the
    bare code). A dialing prefix from a different country than country is refused.
    Each code is checked against the country's numbering plan: it must start real
    local or mobile numbers there, so toll-free and premium ranges, service codes
    and another country's codes are refused with a reason.

    LOCAL senders in any country, and US TEN_DLC senders. No other sender type has a
    geographic area code, and the list is refused with one rather than accepted and
    dropped.

    Honoured exactly or not at all. Ask for 415 and you get a 415 number or you get
    none, never a neighbouring code you did not name. A miss leaves the market with
    no sender yet and the codes recorded on it, so it is filled when stock appears
    rather than filled now from somewhere else. Many countries outside North America
    require address or business documents before a local number can be bought, which
    can delay or prevent the fill.
    """

    compliance: MarketComplianceParam
    """The compliance values a market registers with.

    `brand` and `campaign` apply to US `TEN_DLC`; other markets fill this map with
    the document keys their own requirements name.
    """

    country: str
    """ISO 3166-1 alpha-2 country the sender operates in."""

    numbers: Optional[Iterable[SMSNumberRequestParam]]
    """
    The numbers to assign, one entry per area code, e.g. [{"area_code": "212",
    "quantity": 2}, {"area_code": "415"}, {"quantity": 1}]: two numbers in 212, one
    in 415 and one in any area code. quantity defaults to 1, and an entry without
    area_code means any area code. Omit numbers for one number.

    Only with LOCAL or TEN_DLC, and not together with area_codes. Each area code is
    validated against country the same way area_codes is and may appear once, and at
    most one entry may leave area_code out. On a LOCAL market you already hold, this
    adds the numbers to it. US TEN_DLC numbers are assigned when the campaign is
    approved, not at request time. Not available when the profile inherits the
    organization's campaign.
    """

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    sender_value: Optional[str]
    """The sender's identity where the caller chooses it.

    Required when number_type is ALPHANUMERIC; optional for carrier-assigned types,
    which are procured afterwards.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
