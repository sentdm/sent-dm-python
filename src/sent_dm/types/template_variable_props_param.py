# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TemplateVariablePropsParam"]


class TemplateVariablePropsParam(TypedDict, total=False):
    media_type: Required[Annotated[str, PropertyInfo(alias="mediaType")]]

    sample: Required[str]
    """
    Example value substituted into the template when previewing it and when
    submitting it to Meta for review. Free text by nature, so the converter accepts
    a JSON number or boolean here and normalizes it — see
    JsonScalarToStringConverter for why — and guarantees it is always serialized
    back out as a JSON string.
    """

    url: Required[str]

    variable_type: Required[Annotated[str, PropertyInfo(alias="variableType")]]

    alt: Optional[str]

    regex: Optional[str]

    short_url: Annotated[Optional[str], PropertyInfo(alias="shortUrl")]
