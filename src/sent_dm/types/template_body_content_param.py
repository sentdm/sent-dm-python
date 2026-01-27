# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from .template_variable_param import TemplateVariableParam

__all__ = ["TemplateBodyContentParam"]


class TemplateBodyContentParam(TypedDict, total=False):
    template: str

    type: Optional[str]

    variables: Optional[Iterable[TemplateVariableParam]]
