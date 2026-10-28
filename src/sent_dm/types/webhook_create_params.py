# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebhookCreateParams", "SenderProfile"]


class WebhookCreateParams(TypedDict, total=False):
    display_name: str

    endpoint_url: str

    event_filters: Optional[Dict[str, SequenceNotStr[str]]]

    event_types: SequenceNotStr[str]

    is_inheritable: bool
    """
    Also delivers every sender profile's events to this webhook, at the same URL and
    with the same signing secret, and lets each profile see the webhook and read the
    events about itself. Off by default: the organization's own events only. Only an
    organization's version 2 webhook can set it.
    """

    retry_count: int
    """Delivery retries.

    Applies to version 1 only: Svix retries a version 2 webhook on its own schedule.
    """

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    sender_profile: Optional[SenderProfile]
    """
    Request-only: the events an organization webhook's sender profile clones
    receive, one clone per existing and future profile. A version 1 webhook's
    responses report it as WebhookSenderProfileV3Response.
    """

    timeout_seconds: int
    """Delivery timeout. Applies to version 1 only."""

    webhook_version: Optional[int]
    """
    Who delivers the webhook: 2, the default, is delivered by Svix and signed with
    the webhook-id, webhook-timestamp and webhook-signature headers; 1 is the older
    delivery, signed with the X-Webhook-\\** headers, which will be retired.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]


class SenderProfile(TypedDict, total=False):
    """
    Request-only: the events an organization webhook's sender profile clones receive, one clone per existing
    and future profile. A version 1 webhook's responses report it as WebhookSenderProfileV3Response.
    """

    event_filters: Optional[Dict[str, SequenceNotStr[str]]]

    event_types: SequenceNotStr[str]
