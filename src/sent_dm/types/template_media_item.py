# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TemplateMediaItem"]


class TemplateMediaItem(BaseModel):
    """One attachment on an MMS template body."""

    media_type: Optional[str] = FieldInfo(alias="mediaType", default=None)
    """One of MmsMediaTypes.

    Advisory: the carrier reads the Content-Type off the fetched object, not this
    field. It exists so an authoring UI can render the right preview and so a
    reviewer can see what was intended.
    """

    url: Optional[str] = None
    """Publicly fetchable https URL.

    The carrier's MMSC fetches this at send time, so it has to stay reachable and
    unauthenticated for the life of the send — including retries and a DLQ replay —
    which is why a presigned URL is not a valid value here.
    """
