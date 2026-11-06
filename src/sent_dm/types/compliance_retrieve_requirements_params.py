# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ComplianceRetrieveRequirementsParams"]


class ComplianceRetrieveRequirementsParams(TypedDict, total=False):
    channel: Optional[str]
    """Channel the sender is for: sms, whatsapp or rcs.

    Defaults to sms, which is the only one answered today — the other two are 501
    until their requirements are declared.
    """

    country: Optional[str]
    """ISO 3166-1 alpha-2 country code, e.g. US, XK, IN"""

    type: Optional[str]
    """Sender type: LOCAL, MOBILE, TEN_DLC, TOLL_FREE, SHORT_CODE, ALPHANUMERIC.

    10DLC is accepted as a synonym of TEN_DLC, the same as on POST
    /v3/sender-profiles. Applies to channel=sms, the only channel whose senders have
    a type.
    """

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]
