# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MessageSendParams", "Template"]


class MessageSendParams(TypedDict, total=False):
    channel: Optional[SequenceNotStr[str]]
    """Channels to broadcast on, e.g.

    ["whatsapp", "sms"]. Each channel produces a separate message per recipient.
    "sent" = auto-detect. Defaults to ["sent"] (auto-detect) if omitted.
    """

    media_urls: Optional[SequenceNotStr[str]]
    """Attachments for this send, as publicly fetchable https URLs.

    Used by the MMS channel and ignored by every other one.

    Supplying these replaces the media on the template's mms body rather than adding
    to it, so a template can hold a default creative while a caller still sends
    something recipient-specific.

    Their presence is also what makes a message eligible for MMS on an auto-detect
    send: a message with nothing attached is delivered as SMS, because an MMS with
    no media is a more expensive text message.

    The recipient's carrier fetches each URL after the send is accepted, so it must
    stay publicly reachable — a link that expires, or one behind auth, arrives as a
    failed message.
    """

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    scheduled_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    Optional future send time as an ISO-8601 timestamp with an explicit UTC offset,
    e.g. 2026-10-01T09:00:00+02:00 or 2026-10-01T07:00:00Z. A value without an
    offset is rejected (400) rather than read in the server's zone. The offset only
    fixes the instant: it is stored and echoed in UTC as scheduled_at. Omit to send
    now. Must be at least one minute ahead and at most 30 days ahead. Accepted
    messages report SCHEDULED and are released for delivery at this time. Quiet
    hours, balance and template approval are evaluated at release, not at
    acceptance: a message whose time falls inside a recipient's protected
    quiet-hours window is moved to the next allowed time and a second
    message.scheduled webhook reports the new scheduled_at.
    """

    subject: Optional[str]
    """Subject line for this send, overriding the template's.

    MMS only; ignored on every other channel. Most handsets render it above the
    body, some ignore it entirely.
    """

    template: Optional[Template]
    """
    SDK-style template reference: resolve by ID or by name, with optional
    parameters.
    """

    text: Optional[str]
    """Plain-text (free-form) message body. Provide either Template or this."""

    to: SequenceNotStr[str]
    """List of recipient phone numbers in E.164 format (multi-recipient fan-out)"""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]


class Template(TypedDict, total=False):
    """
    SDK-style template reference: resolve by ID or by name, with optional parameters.
    """

    id: Optional[str]
    """Template ID (mutually exclusive with name)"""

    name: Optional[str]
    """Template name (mutually exclusive with id)"""

    parameters: Optional[Dict[str, str]]
    """Template variable parameters for personalization, keyed by variable name.

    Every variable the template declares is required; GET /v3/templates/{id} lists
    them. Supplying a key the template does not declare is ignored.

    Media headers. A template whose header is an image (designed in WhatsApp Manager
    and imported into Sent) declares a reserved header_image key. Its value is a
    publicly reachable https URL that Meta fetches at send time — Sent does not host
    the asset, and the sample approved with the template is not reused. The key is
    derived from the header's media type, so header_video and header_document follow
    the same shape when those formats ship.

    "parameters": { "header_image": "https://cdn.example.com/banner.jpg", "name":
    "John Doe" }
    """
