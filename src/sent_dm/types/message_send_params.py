# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
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

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    template: Template
    """
    SDK-style template reference: resolve by ID or by name, with optional
    parameters.
    """

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
    """Template variable parameters for personalization"""
