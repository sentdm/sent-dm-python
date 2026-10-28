# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["VoiceAgentSecret"]


class VoiceAgentSecret(BaseModel):
    """A freshly rotated signing secret."""

    signing_secret: Optional[str] = None
    """The new whsec\\__ secret.

    The previous one stopped signing the moment this was returned. Shown once.
    """
