# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WebhookResponse"]


class WebhookResponse(BaseModel):
    id: Optional[str] = None

    consecutive_failures: Optional[int] = None

    created_at: Optional[datetime] = None

    display_name: Optional[str] = None

    endpoint_url: Optional[str] = None

    event_types: Optional[List[str]] = None

    is_active: Optional[bool] = None

    last_delivery_attempt_at: Optional[datetime] = None

    last_successful_delivery_at: Optional[datetime] = None

    retry_count: Optional[int] = None

    signing_secret: Optional[str] = None

    timeout_seconds: Optional[int] = None

    updated_at: Optional[datetime] = None
