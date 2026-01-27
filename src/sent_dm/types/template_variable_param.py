# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TemplateVariableParam", "Props"]


class Props(TypedDict, total=False):
    alt: Optional[str]

    media_type: Annotated[Optional[str], PropertyInfo(alias="mediaType")]

    sample: Optional[str]

    short_url: Annotated[Optional[str], PropertyInfo(alias="shortUrl")]

    url: Optional[str]

    variable_type: Annotated[Optional[str], PropertyInfo(alias="variableType")]


class TemplateVariableParam(TypedDict, total=False):
    id: int

    name: str

    props: Props

    type: str
