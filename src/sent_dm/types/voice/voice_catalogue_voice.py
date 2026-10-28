# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["VoiceCatalogueVoice"]


class VoiceCatalogueVoice(BaseModel):
    default: Optional[bool] = None
    """Whether this is the voice used when an agent names none."""

    description: Optional[str] = None

    language: Optional[str] = None
    """The language the voice speaks."""

    name: Optional[str] = None
    """The value to send as speech.voice."""
