# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .brand_data_param import BrandDataParam

__all__ = ["BrandCreateParams"]


class BrandCreateParams(TypedDict, total=False):
    brand: Required[BrandDataParam]
    """Brand and KYC information"""

    test_mode: bool
    """
    Test mode flag - when true, the operation is simulated without side effects
    Useful for testing integrations without actual execution
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
