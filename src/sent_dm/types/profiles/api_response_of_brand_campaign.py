# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..api_meta import APIMeta
from ..error_detail import ErrorDetail
from .brand_campaign import BrandCampaign

__all__ = ["APIResponseOfBrandCampaign"]


class APIResponseOfBrandCampaign(BaseModel):
    """Standard API response envelope for all v3 endpoints"""

    data: Optional[BrandCampaign] = None
    """A 10DLC campaign registered for a brand."""

    error: Optional[ErrorDetail] = None
    """Error information"""

    meta: Optional[APIMeta] = None
    """Request and response metadata"""

    success: Optional[bool] = None
    """Indicates whether the request was successful"""
