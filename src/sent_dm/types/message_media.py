# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessageMedia"]


class MessageMedia(BaseModel):
    """
    One attachment on a message, in either direction — and in both, a URL somebody else hosts.

    Outbound: the customer supplied a public URL and we handed it to the carrier.
    Inbound: the carrier hosts the file and we record where. sent.dm never holds the bytes, so
    there is no key, no expiry bookkeeping and nothing minted per read — what is stored is what is
    served.

    An inbound link expires on the carrier's own schedule and is unauthenticated. That is the
    customer's to manage, and it is documented where they will see it rather than only here — a
    recipient who needs an attachment to outlive that window copies it on receipt.

    Storing a presigned URL is the specific mistake this shape still avoids:
    M260826130000 and M260826140000 exist because RCS assets were stored as signed URLs
    and went stale. Nothing here is signed.
    """

    media_type: Optional[str] = FieldInfo(alias="mediaType", default=None)
    """One of MmsMediaTypes when the content type is known.

    Advisory — a reader should trust the fetched object's own Content-Type.
    """

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)
    """Content type as the provider declared it. Null when it declared none."""

    size_bytes: Optional[int] = FieldInfo(alias="sizeBytes", default=None)
    """Size as the provider declared it.

    Never measured here — nothing downloads the file.
    """

    source_hash_sha256: Optional[str] = FieldInfo(alias="sourceHashSha256", default=None)
    """
    Inbound only: the SHA-256 the provider declared alongside the attachment, when
    it declared one. Relayed to the customer so they can verify what they fetch
    matches what the carrier said it sent. It is the only integrity signal available
    on an attachment nobody here has read.
    """

    url: Optional[str] = None
    """Where the file lives.

    Outbound: the URL the customer gave us and the carrier fetched. Inbound: the URL
    the carrier hosts it at, relayed unchanged.
    """
