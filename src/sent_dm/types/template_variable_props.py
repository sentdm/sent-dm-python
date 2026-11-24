# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TemplateVariableProps"]


class TemplateVariableProps(BaseModel):
    media_type: str = FieldInfo(alias="mediaType")

    sample: str
    """
    Example value substituted into the template when previewing it and when
    submitting it to Meta for review. Free text by nature, so the converter accepts
    a JSON number or boolean here and normalizes it — see
    JsonScalarToStringConverter for why — and guarantees it is always serialized
    back out as a JSON string.
    """

    url: str

    variable_type: str = FieldInfo(alias="variableType")

    alt: Optional[str] = None

    regex: Optional[str] = None

    short_url: Optional[str] = FieldInfo(alias="shortUrl", default=None)
