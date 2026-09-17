# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Template"]


class Template(BaseModel):
    """Template response for v3 API"""

    customer_id: str
    """Which customer owns this — the key's own, or the profile named in x-profile-id.

    Says whose resource this is, which the resource's own id does not.
    """

    id: Optional[str] = None
    """Unique template identifier"""

    auto_reply_action: Optional[str] = None
    """
    Which consent keyword this template answers, when it is one of Sent's
    auto-replies: OPT_IN, OPT_OUT, HELP, or OTHER for a customer-defined keyword.
    Null for an ordinary template, and omitted from the response, so its presence is
    the answer to "is this an auto-reply".

    Deliberately not required, unlike CustomerId, even though the same "no single
    mapper" argument applies: NJsonSchema publishes a C# required member in the
    schema's required array, so the contract would have advertised a field this
    response omits for every ordinary template, and a generated client could refuse
    the common case. A compile-time guard is not worth a wrong published contract.
    Every mapping site sets it explicitly, and TemplateResponseSchemaTests pins the
    field as optional so it cannot be reintroduced.
    """

    category: Optional[str] = None
    """Template category: MARKETING, UTILITY, AUTHENTICATION"""

    channels: Optional[List[str]] = None
    """
    The channels this template's definition can render on, in canonical order: sms,
    whatsapp, rcs.

    Derived from the definition's body, mirroring each channel's send-time fallback
    chain, so a channel is listed only when a real body would be produced for it:
    SMS reads sms ?? multiChannel, WhatsApp reads whatsapp ?? multiChannel, and RCS
    reads rcs ?? multiChannel ?? sms. A multiChannel body therefore reports all
    three, and the extra SMS fallback on RCS is why an sms/whatsapp pair reports RCS
    too.

    This says what the content can render on, not what may be sent: sending also
    needs the template approved for that channel.
    """

    created_at: Optional[datetime] = None
    """When the template was created"""

    is_published: Optional[bool] = None
    """Whether the template is published and active"""

    language: Optional[str] = None
    """Template language code (e.g., en_US)"""

    name: Optional[str] = None
    """Template display name"""

    status: Optional[str] = None
    """Template status: DRAFT, PENDING, APPROVED, REJECTED.

    A template created with submit_for_review: false starts as DRAFT and stays there
    until it is submitted.
    """

    updated_at: Optional[datetime] = None
    """When the template was last updated"""

    variables: Optional[List[str]] = None
    """Template variables for personalization"""
