# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .rcs_address_param import RcsAddressParam

__all__ = ["RcCreateParams"]


class RcCreateParams(TypedDict, total=False):
    agent_use_case: Literal["VERIFICATION", "NOTIFICATIONS", "MARKETING", "MULTI_USE"]
    """Which kind of traffic the agent carries.

    One of the accepted use cases; the error names the set.
    """

    banner_url: str

    brand_color: str
    """Primary brand colour, as #RRGGBB.

    Three-digit shorthand is refused: the value is submitted verbatim, so two
    spellings of one colour is only a way for the stored value to disagree with the
    form.
    """

    brand_email: str

    brand_name: str
    """The brand this agent presents over RCS.

    Not taken from your compliance.brand: a business may present a different brand
    on RCS than the one its 10DLC registration is filed against, and the carriers
    vet this one.
    """

    brand_phone_number: str
    """The brand's own number.

    Also becomes the agent's canonical sending number for routing, which is why it
    is normalised to E.164 rather than stored as sent.
    """

    brief_company_description: str

    company_ein: str

    contact_name_and_title: str

    customer_support_email: str

    customer_support_phone_number: str

    description: str
    """What the agent is for, shown to recipients. Capped by the carriers, not by us."""

    display_name: str
    """The name the agent shows in the messaging client."""

    entity_type: str

    help_message: str

    logo_url: str
    """Publicly reachable logo.

    It has to be fetchable without authentication at review time, so a URL behind a
    login passes this call and fails the review.
    """

    official_address: RcsAddressParam
    """The registered address of the company behind the agent."""

    opt_in_process_description: str
    """How recipients opt in, in prose. The carriers read this one."""

    opt_in_screenshot_url: Optional[str]
    """A screenshot of the opt-in, as a publicly fetchable URL."""

    privacy_policy_url: str
    """Required by US carriers. Must be an absolute http(s) URL they can fetch."""

    sample_messages: SequenceNotStr[str]
    """Examples of what the agent will send, for the review."""

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    start_message: str

    stop_message: str

    terms_and_conditions_url: str

    website_url: str
    """The brand's own site."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
