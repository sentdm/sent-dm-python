# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["InboundMedia"]


class InboundMedia(BaseModel):
    """One attachment on an inbound message."""

    hash_sha256: Optional[str] = None
    """SHA-256 of the file as the carrier declared it, when it declares one.

    Verify what you download against this — sent.dm never reads the bytes, so it is
    the only integrity signal available.
    """

    mime_type: Optional[str] = None
    """Content type as the carrier reported it, for example image/jpeg."""

    size_bytes: Optional[int] = None
    """Size in bytes as the carrier declared it. Absent when it declared none."""

    url: Optional[str] = None
    """Where the carrier hosts the attachment.

    This link expires and is not authenticated. sent.dm relays it rather than
    copying the file, so how long it stays fetchable is the carrier's decision and
    differs between them — assume days, not months. Anyone holding the URL can fetch
    it until it lapses. Copy the file on receipt if you need it to outlive that
    window; do not store this URL as a permanent reference.
    """
