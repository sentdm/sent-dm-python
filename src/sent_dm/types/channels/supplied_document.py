# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SuppliedDocument"]


class SuppliedDocument(BaseModel):
    """A document a market asked for and has been given."""

    document_id: Optional[str] = None
    """Identifier of the upload, for fetching it back through the documents endpoints."""

    file_name: Optional[str] = None

    key: Optional[str] = None
    """The catalog's name for this document, matching the requirement it satisfies."""
