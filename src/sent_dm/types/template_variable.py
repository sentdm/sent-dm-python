# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TemplateVariable", "Props"]


class Props(BaseModel):
    alt: Optional[str] = None

    media_type: Optional[str] = FieldInfo(alias="mediaType", default=None)

    sample: Optional[str] = None

    short_url: Optional[str] = FieldInfo(alias="shortUrl", default=None)

    url: Optional[str] = None

    variable_type: Optional[str] = FieldInfo(alias="variableType", default=None)


class TemplateVariable(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    props: Optional[Props] = None

    type: Optional[str] = None
