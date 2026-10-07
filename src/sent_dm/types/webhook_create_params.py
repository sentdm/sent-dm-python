# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebhookCreateParams", "SenderProfile"]


class WebhookCreateParams(TypedDict, total=False):
    api_key: Annotated[str, PropertyInfo(alias="apiKey")]
    """
    API key from the x-api-key header, or empty when the caller sent it as
    Authorization: Bearer instead.

    Optional on purpose. CustomerV3AuthenticationHandler accepts the key in either
    header, and [FromHeader] is required by default, so a Bearer-only request would
    authenticate and then be refused with a 400 for a header it never needed.
    Endpoints read the customer from the CustomerId claim, not from this value.
    """

    display_name: str

    endpoint_url: str

    event_filters: Optional[Dict[str, SequenceNotStr[str]]]

    event_types: SequenceNotStr[str]

    retry_count: int

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    sender_profile: Optional[SenderProfile]
    """
    Request-only: the events an organization webhook's sender profile clones
    receive, one clone per existing and future profile. Responses never return it.
    """

    timeout_seconds: int

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]


class SenderProfile(TypedDict, total=False):
    """
    Request-only: the events an organization webhook's sender profile clones receive, one clone per existing
    and future profile. Responses never return it.
    """

    event_filters: Optional[Dict[str, SequenceNotStr[str]]]

    event_types: SequenceNotStr[str]
