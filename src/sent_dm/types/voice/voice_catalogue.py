# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .voice_catalogue_voice import VoiceCatalogueVoice

__all__ = ["VoiceCatalogue"]


class VoiceCatalogue(BaseModel):
    """
    The voices and languages a text-session agent may name in its speech settings: what
    GET /v3/voice/voices and the admin GET /voice/voices answer, in one shape.
    """

    languages: Optional[List[str]] = None
    """BCP 47 tags accepted as speech.language."""

    voices: Optional[List[VoiceCatalogueVoice]] = None
