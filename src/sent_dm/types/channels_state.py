# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .mms_market import MmsMarket
from .channels.rcs_agent import RcsAgent
from .channels.sms_market import SMSMarket
from .channels.voice_number import VoiceNumber
from .channels.whatsapp_channel import WhatsappChannel

__all__ = ["ChannelsState"]


class ChannelsState(BaseModel):
    """The channels a profile sends on.

    SMS is a list because a profile can send in several markets; WhatsApp
    and RCS are single, because a profile has one business account and one agent.
    """

    customer_id: Optional[str] = None
    """
    Which customer these channels belong to — the key's own, or the profile named in
    x-profile-id.

    Same reason the brand carries one: as the response to /v3/channels there is no
    other id in the document, and under x-profile-id this is the profile the call
    resolved to rather than the caller. Absent when nested inside a sender profile,
    whose own id already says whose they are.
    """

    mms: Optional[List[MmsMarket]] = None
    """
    The markets this profile can send MMS in, one entry per country, or empty when
    none.

    Appears alongside sms rather than replacing an entry in it: the two are separate
    senders on the same number and a caller needs to see both — a market can be live
    for SMS while its MMS row is still provisioning, or MMS-incapable entirely
    because the market's sender-type SKU does not carry it.
    """

    rcs: Optional[RcsAgent] = None
    """
    An RCS agent as its owner sees it: the order form back, plus where the
    submission stands.

    Not RcsSenderResponse. That one is the admin projection and carries the pipeline
    we track about a customer's request — internalStatus, statusReason, isLaunched —
    and the S3 keys behind the assets. None of that is the customer's to read: an
    internal status is a note to ourselves, and an S3 key is a storage detail that
    would become a contract the moment it was published.

    What is here is what the caller sent, in the names it sent them under, plus the
    three things only we can answer: the record's id, its status, and the number it
    sends from. So a read after a write shows the form as stored rather than as
    echoed.
    """

    sms: Optional[List[SMSMarket]] = None

    voice: Optional[List[VoiceNumber]] = None
    """
    The numbers this profile carries phone calls on, one entry per number, or empty
    when none. Voice is per number like an SMS market is per country: each number is
    its own channel row, turned on and off on its own, and one of them is the line
    app-originated calls fall back to.
    """

    whatsapp: Optional[WhatsappChannel] = None
    """The profile's WhatsApp account. Its status is Meta's verification state."""
