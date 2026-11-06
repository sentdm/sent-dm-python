# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .compliance_attachment_template import ComplianceAttachmentTemplate

__all__ = ["ComplianceSetupStep"]


class ComplianceSetupStep(BaseModel):
    """
    One call to make, with a body that can be sent as it stands.

    The steps are ordered and the order is load-bearing: a channel that registers with a regime is filed
    against a brand, so the brand call comes first and the channel call refuses until it has been made. Doing them
    in order is the whole of setting a market up.
    """

    attachments: Optional[List[ComplianceAttachmentTemplate]] = None
    """Files to attach as multipart, when this call takes any.

    Absent when it does not.
    """

    body: Optional[object] = None
    """
    The request body, with every key this market wants already present and the
    values left blank. Send it as it stands and the response names each blank that
    still has to be filled.
    """

    method: Optional[str] = None

    path: Optional[str] = None
    """Path to call.

    Add the x-profile-id header with an organization key to make the same call for
    one of your sender profiles — there is no separate path for that.
    """

    resource: Optional[str] = None
    """What this call sets up: brand or channel."""

    step: Optional[int] = None
    """Position in the sequence, from 1. Steps must be performed in this order."""

    why: Optional[str] = None
    """Why this market needs this call, in one sentence."""
