# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MessageHeaderMedia"]


class MessageHeaderMedia(BaseModel):
    """The media asset that rode a message's header, recorded as sent."""

    type: Optional[str] = None
    """\"image", "video" or "document" — taken from the header's media variable."""

    url: Optional[str] = None
    """The https URL the caller supplied for this send.

    Never the template's stored props.sample, which is Meta's expiring header_handle
    rather than what was delivered.
    """
