# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DestinationCountry"]


class DestinationCountry(BaseModel):
    id: Optional[str] = None

    is_main: Optional[bool] = FieldInfo(alias="isMain", default=None)
