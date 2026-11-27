# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WhatsappChannel"]


class WhatsappChannel(BaseModel):
    """The profile's WhatsApp account. Its status is Meta's verification state."""

    owner_business_id: Optional[str] = None
    """Derived from the organization's shared-account listing, like SolutionId."""

    phone_number_id: Optional[str] = None
    """
    The Meta phone-number id the profile sends from, or null when the account is
    connected but no number has been named yet — which is what a provisioning status
    means here.
    """

    reason: Optional[str] = None
    """A sentence for reason_code, saying what to do where it is yours.

    Omitted while ACTIVE.
    """

    reason_code: Optional[str] = None
    """
    Why the account is not ACTIVE, as a stable code: an ErrorCodes CHANNEL_xxx value
    such as CHANNEL_001 (something you owe) or CHANNEL_009 (under review). Switch on
    this rather than on reason. Omitted while ACTIVE. Read-only; when nothing more
    specific is known it is the generic reason for the status.
    """

    solution_id: Optional[str] = None
    """Derived, not echoed.

    The request no longer accepts this — it is read off the organization's
    shared-account listing at connect time and reported back so a caller can see
    which partnership the account actually arrived through.
    """

    status: Optional[Literal["PROVISIONING", "ACTION_NEEDED", "PENDING_REVIEW", "ACTIVE", "INACTIVE"]] = None
    """Read-only.

    Never carries a token — the row holds that and it is not returned. ACTION_NEEDED
    when no account is connected or the account has no phone number: both are yours
    to do.
    """

    waba_id: Optional[str] = None
