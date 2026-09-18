# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TemplateEventPayload"]


class TemplateEventPayload(BaseModel):
    """Body of a template status event.

    Delivered when a template's review outcome changes, so you can
    react without polling.
    """

    status: str
    """The review status the template just reached, for example APPROVED or REJECTED."""

    whatsapp_template_id: str
    """
    The template's identifier with Meta, assigned when the template is submitted for
    review.
    """

    account_id: Optional[str] = None
    """The account the template belongs to."""

    auto_reply_action: Optional[str] = None
    """
    Which consent keyword this template answers, when it is one of Sent's
    auto-replies: OPT_IN, OPT_OUT, HELP, or OTHER for a customer-defined keyword.

    Omitted for an ordinary template, so its presence is the answer to "is this an
    auto-reply". Sent creates the three compliance auto-replies at signup and they
    go through review like any other template, so their events arrive mixed in with
    the customer's own with nothing else to tell them apart.

    Named for the reader rather than after Template.OptAction, which it is mapped
    from. The MCP tool result deliberately keeps OptAction, OptKeywords and IsOpt:
    it mirrors the internal shape on purpose and publishes the keywords too, so
    renaming one of the three there would leave a surface half in each vocabulary.
    Two names for one concept, each consistent within its own surface, chosen over a
    rename that breaks MCP clients silently.
    """

    category: Optional[str] = None
    """The template's category, for example UTILITY, MARKETING, or AUTHENTICATION."""

    channel: Optional[str] = None
    """
    The channel leg this decision is about, for example whatsapp, sms, or rcs. A
    template is reviewed per channel and the legs come back independently, so each
    one reports separately.

    Omitted when the decision applies to the template as a whole rather than to one
    leg. That event is the broader news: a template-wide rejection blocks every
    channel, whatever the individual legs say.
    """

    language: Optional[str] = None
    """The template's language code, for example en_US."""

    reason: Optional[str] = None
    """Why the template reached Status, when a reason was given.

    Populated on a rejection.
    """

    template_id: Optional[str] = None
    """The template in Sent."""

    template_name: Optional[str] = None
    """The template's display name."""
