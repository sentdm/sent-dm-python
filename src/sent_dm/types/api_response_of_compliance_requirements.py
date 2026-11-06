# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .api_meta import APIMeta
from .error_detail import ErrorDetail

__all__ = ["APIResponseOfComplianceRequirements"]


class APIResponseOfComplianceRequirements(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional["ComplianceRequirements"] = None
    """
    Everything a market expects of a sender, for one channel, country and sender
    type.
    """

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""


from .compliance_requirements import ComplianceRequirements
