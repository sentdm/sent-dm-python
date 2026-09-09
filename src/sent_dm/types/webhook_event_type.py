# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WebhookEventType"]


class WebhookEventType(BaseModel):
    description: Optional[str] = None

    display_name: Optional[str] = None

    event_type: Optional[str] = None

    is_active: Optional[bool] = None

    name: Optional[str] = None

    sub_types: Optional[List["WebhookEventType"]] = None
