# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ComplianceAttachmentTemplate"]


class ComplianceAttachmentTemplate(BaseModel):
    """
    A file this market wants, and the multipart field to send it as.

    Separate from compliance because a file is not JSON: the channel call accepts multipart, and
    each file is named after the key it satisfies. Listing documents among the JSON entries would describe a
    request nobody could send.
    """

    field_name: Optional[str] = None
    """The multipart field name to attach the file under."""

    label: Optional[str] = None

    required: Optional[bool] = None
