# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel
from .compliance_setup_step import ComplianceSetupStep

__all__ = ["ComplianceRequirements"]


class ComplianceRequirements(BaseModel):
    """
    Everything a market expects of a sender, for one channel, country and sender type.
    """

    channel: Optional[str] = None
    """Channel the requirements apply to — sms, whatsapp or rcs.

    Echoed so the document says which channel it describes. It always described one:
    setup's last step is a specific channel path, and every type is an SMS sender
    type — but a caller reading the payload had to infer that from the path to know
    it.
    """

    country: Optional[str] = None
    """ISO 3166-1 alpha-2 country the requirements apply to."""

    required: Optional[bool] = None
    """Whether this market demands anything before a sender can be registered.

    When false, the compliance array may be omitted entirely and the profile is
    ready once provisioned.
    """

    requirements: Optional[List["ComplianceRequirement"]] = None
    """Values to supply in compliance.

    Empty when the market demands nothing. Values Sent supplies on your behalf are
    never listed, and neither are ones it derives from what you send.
    """

    sender_id_pattern: Optional[str] = None
    """
    Pattern the sender's own value must match, where the market dictates one —
    alphanumeric sender ids and short codes. Null when the value is
    carrier-assigned.
    """

    setup: Optional[List[ComplianceSetupStep]] = None
    """
    The calls that set this market up, in the order they have to be made, each
    carrying a body that can be sent as it stands.

    This is the answer to "what do I actually do". Requirements describes each value
    the market wants; this assembles those descriptions into the requests that
    supply them, so a caller — or an agent acting for one — copies a body out and
    sends it rather than building one from a table.

    The last step is always the channel itself, and it is where the regime's own
    values are supplied. The one before it, where there is one, is the brand a
    registering market files against — so it is a step of its own and the channel
    call refuses until it exists. A market that registers with nobody has one step.
    """

    type: Optional[str] = None
    """Sender type the requirements apply to.

    Non-nullable while sms is the only channel answered here, because it is the only
    channel whose senders have a type — the day another one is answered, this
    becomes nullable along with it. Not nullable in advance: nothing can emit null
    today, and publishing a shape the API never sends is the same mistake as
    publishing a field it does not have.
    """


from .compliance_requirement import ComplianceRequirement
