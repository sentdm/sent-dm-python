# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WhatsappCreateParams"]


class WhatsappCreateParams(TypedDict, total=False):
    phone_number_id: Optional[str]
    """
    The Meta phone-number id of the number on WabaId, which assigns it to this
    profile as the number it sends from. It is not checked against the account here,
    so name the account's number; it is refused if another profile already uses it.

    Optional: omit it to connect the account and settle the number later. Nothing
    picks one on your behalf.
    """

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    waba_id: str
    """WhatsApp Business Account id — one of the accounts shared into your
    organization.

    Required: the organization holds one per client, and nothing but the caller says
    which is meant here.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
