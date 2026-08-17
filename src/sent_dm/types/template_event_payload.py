# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TemplateEventPayload"]


class TemplateEventPayload(BaseModel):
    """Body of a template status event.

    Delivered when a template's review outcome changes, so you can
    react without polling.
    """

    account_id: Optional[str] = None
    """The account the template belongs to."""

    category: Optional[str] = None
    """The template's category, for example UTILITY, MARKETING, or AUTHENTICATION."""

    channel: Optional[str] = None
    """The channel the template applies to."""

    language: Optional[str] = None
    """The template's language code, for example en_US."""

    reason: Optional[str] = None
    """Why the template reached Status, when a reason was given.

    Populated on a rejection.
    """

    status: Optional[str] = None
    """The review status the template just reached, for example APPROVED or REJECTED."""

    template_id: Optional[str] = None
    """The template in Sent."""

    template_name: Optional[str] = None
    """The template's display name."""

    whatsapp_template_id: Optional[str] = None
    """
    The template's identifier with Meta, assigned when the template is submitted for
    review.
    """
