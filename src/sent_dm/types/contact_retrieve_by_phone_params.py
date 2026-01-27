# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactRetrieveByPhoneParams"]


class ContactRetrieveByPhoneParams(TypedDict, total=False):
    phone_number: Required[Annotated[str, PropertyInfo(alias="phoneNumber")]]
    """The phone number in international format (e.g., +1234567890)"""
