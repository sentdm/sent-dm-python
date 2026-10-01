# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .voice_number import VoiceNumber

__all__ = ["VoiceNumberCreated"]


class VoiceNumberCreated(VoiceNumber):
    """One number the profile carries phone calls on."""

    callback_secret: Optional[str] = None
    """The whsec\\__ secret every question to callback_url is signed with.

    Shown here and by POST /v3/channels/voice/{number}/rotate-secret, nowhere else:
    store it now. Verify a question exactly as you verify a webhook, with
    X-Webhook-ID, X-Webhook-Timestamp and the body.
    """
