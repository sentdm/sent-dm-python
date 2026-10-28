# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WebhookResponse", "SenderProfile"]


class SenderProfile(BaseModel):
    """
    The events a version 1 webhook's sender profile clones receive, as a response reports them.

    Its own type, field for field the same as the request's sender_profile. A response is not
    a request, whatever it carries.
    """

    event_filters: Optional[Dict[str, List[str]]] = None

    event_types: Optional[List[str]] = None


class WebhookResponse(BaseModel):
    id: Optional[str] = None

    consecutive_failures: Optional[int] = None
    """Failed attempts since the last success.

    Version 1 only: always 0 on a version 2 webhook, whose deliveries are in its
    events (GET /v3/webhooks/{id}/events).
    """

    created_at: Optional[datetime] = None

    customer_id: Optional[str] = None
    """Which customer owns this — the key's own, or the profile named in x-profile-id.

    Says whose resource this is, which the resource's own id does not.
    """

    display_name: Optional[str] = None

    endpoint_url: Optional[str] = None

    event_filters: Optional[Dict[str, List[str]]] = None

    event_types: Optional[List[str]] = None

    is_active: Optional[bool] = None

    is_inheritable: Optional[bool] = None
    """
    Whether the webhook also receives its organization's sender profiles' events,
    and each profile sees it and reads the events about itself. Always false on a
    version 1 webhook.
    """

    last_delivery_attempt_at: Optional[datetime] = None
    """When the webhook was last attempted.

    Version 1 only: always null on a version 2 webhook.
    """

    last_successful_delivery_at: Optional[datetime] = None
    """When the webhook last received an event.

    Version 1 only: always null on a version 2 webhook.
    """

    retry_count: Optional[int] = None

    sender_profile: Optional[SenderProfile] = None
    """
    The events a version 1 webhook's sender profile clones receive, as a response
    reports them.

    Its own type, field for field the same as the request's sender_profile. A
    response is not a request, whatever it carries.
    """

    signing_secret: Optional[str] = None

    timeout_seconds: Optional[int] = None

    updated_at: Optional[datetime] = None

    webhook_version: Optional[int] = None
    """Who delivers the webhook: 1 the older delivery, which will be retired, or 2
    Svix.

    A webhook is created as version 2 unless the request asks for 1.
    """
