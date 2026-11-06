# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .channels.rcs_address_param import RcsAddressParam

__all__ = ["SenderProfileRcsParam"]


class SenderProfileRcsParam(TypedDict, total=False):
    """
    Asks for an RCS agent of the profile's own, optionally with the full order form inline.

    Two modes, distinguished by whether any field is populated:
    "rcs": {} — intent only. Records that the profile wants its own agent; the order form is
    submitted separately through POST /v3/channels/rcs once the fields are ready.
    "rcs": { ...fields... } — full form. All required fields must be present; the agent is
    created alongside the profile in one call. Omitting opt_in_screenshot_url is allowed.
    """

    description: Required[str]

    agent_use_case: Optional[str]

    banner_url: Optional[str]

    billing_category: Optional[str]

    brand_color: Optional[str]

    brand_email: Optional[str]

    brand_name: Optional[str]

    brand_phone_number: Optional[str]

    brief_company_description: Optional[str]

    company_ein: Optional[str]

    contact_name_and_title: Optional[str]

    customer_support_email: Optional[str]

    customer_support_phone_number: Optional[str]

    display_name: Optional[str]

    entity_type: Optional[str]

    help_message: Optional[str]

    hosting_region: Optional[str]

    logo_url: Optional[str]

    official_address: Optional[RcsAddressParam]
    """The registered address of the company behind the agent."""

    opt_in_process_description: Optional[str]

    opt_in_screenshot_url: Optional[str]
    """Optional — uploaded separately and its URL may not be known at submission time."""

    privacy_policy_url: Optional[str]

    sample_messages: Optional[SequenceNotStr[str]]

    start_message: Optional[str]

    stop_message: Optional[str]

    terms_and_conditions_url: Optional[str]

    website_url: Optional[str]
