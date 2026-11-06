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

    - `PROVISIONING` - We are working on it and there is nothing for you to do — a
      number is being procured, or a registration is being assembled. Minutes to
      hours.
    - `ACTION_NEEDED` - **Waiting on you.** Something the market asks for has not
      been supplied, a regulator rejected what was, or we have asked you to correct
      and resubmit your identity data. Nothing progresses until you act. For an SMS
      market, `GET /v3/channels/sms/{country}/{type}` names what it wants and
      `PATCH` on the same path supplies it — compliance values, documents and
      numbers alike.
    - `PENDING_REVIEW` - With a regulator or carrier — filed, or assembled and
      queued for us to file — and their answer is what moves it, to `ACTIVE` or back
      to `ACTION_NEEDED`. Nothing on your side changes it. Days for SMS, weeks for
      RCS.
    - `ACTIVE` - Can carry traffic now. A channel a sender profile runs on its
      organization's reads `ACTIVE` too — it sends, which is what the field is
      about.
    - `INACTIVE` - **It had a working sender and no longer does** — the number was
      released, or the campaign it carried lapsed. Distinct from `PROVISIONING`,
      which means it has never sent yet: the same absence of a sender, opposite
      news. Sends will fail until it returns to `ACTIVE`.
    """

    waba_id: Optional[str] = None
