# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TemplateVariableParam", "Props"]


class Props(TypedDict, total=False):
    media_type: Required[Annotated[str, PropertyInfo(alias="mediaType")]]

    sample: Required[str]

    url: Required[str]

    variable_type: Required[Annotated[str, PropertyInfo(alias="variableType")]]

    alt: Optional[str]

    regex: Optional[str]

    short_url: Annotated[Optional[str], PropertyInfo(alias="shortUrl")]


class TemplateVariableParam(TypedDict, total=False):
    name: Required[str]

    props: Required[Props]

    type: Required[str]

    id: int
