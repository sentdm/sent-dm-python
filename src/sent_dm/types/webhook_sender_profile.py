# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["WebhookSenderProfile"]


class WebhookSenderProfile(BaseModel):
    """
    The events a version 1 webhook's sender profile clones receive, as a response reports them.

    Its own type, field for field the same as the request's sender_profile. A response is not
    a request, whatever it carries.
    """

    event_filters: Optional[Dict[str, List[str]]] = None

    event_types: Optional[List[str]] = None
