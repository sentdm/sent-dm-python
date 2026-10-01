# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["VoiceSecret"]


class VoiceSecret(BaseModel):
    """A freshly rotated callback signing secret"""

    callback_secret: Optional[str] = None
    """The new whsec\\__ secret.

    The previous one stopped signing the moment this was returned, so update your
    backend before the next call reaches it. Shown once.
    """
