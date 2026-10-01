# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CallTimelineEntry"]


class CallTimelineEntry(BaseModel):
    """When a call entered a status"""

    status: Optional[str] = None
    """initiated, ringing, answered, completed, failed, no_answer or rejected"""

    timestamp: Optional[datetime] = None
    """When the call entered this status (UTC)"""
