# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VoiceCreateParams"]


class VoiceCreateParams(TypedDict, total=False):
    callback_url: Required[str]
    """
    Where Sent asks what to do with each call on this number: an absolute HTTP or
    HTTPS URL on a public host. A signed question is POSTed here when a call arrives
    or a caller presses a key, and the answer decides the call. Every question is
    signed with the callback_secret the response returns, the same way your webhooks
    are signed. Turning the number on again with a different URL replaces it and
    keeps the secret.
    """

    area_code: Optional[str]
    """The US area code a new number should be in, as 212.

    Only for a request that leaves number out — sending both says two different
    things about which number to use, and is refused. Omit it too and the number
    comes from anywhere in the country.
    """

    default_for_app_calls: Optional[bool]
    """
    Make this the line app-originated calls are placed from when a voice token names
    no number. Omit it and your first voice number takes that role; a later one
    leaves it where it is.
    """

    number: Optional[str]
    """One of your phone numbers, in E.164 format.

    Leave the field out entirely to be given a new one instead; sending it empty is
    a refused request rather than a request for a new number.
    """

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
