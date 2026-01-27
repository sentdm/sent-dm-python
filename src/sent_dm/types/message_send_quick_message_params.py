# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageSendQuickMessageParams"]


class MessageSendQuickMessageParams(TypedDict, total=False):
    custom_message: Required[Annotated[str, PropertyInfo(alias="customMessage")]]
    """The custom message content to include in the template"""

    phone_number: Required[Annotated[str, PropertyInfo(alias="phoneNumber")]]
    """
    The phone number to send the message to, in international format (e.g.,
    +1234567890)
    """
