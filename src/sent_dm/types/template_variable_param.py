# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .template_variable_props_param import TemplateVariablePropsParam

__all__ = ["TemplateVariableParam"]


class TemplateVariableParam(TypedDict, total=False):
    name: Required[str]
    """
    The variable's name, and the key callers use for it in a send request's
    parameters object. Must start with a letter and hold only letters, digits and
    underscores.
    """

    props: Required[TemplateVariablePropsParam]

    type: Required[str]
    """One of variable, link or media. Decides which Props fields are required."""

    id: int
    """
    The variable's index, and the number its {{index:variable}} placeholder refers
    to.

    Omitting it is only safe for a section holding a single variable. The field is a
    non-nullable int, so every variable that leaves it out defaults to 0, and a
    section with two such variables is refused by the unique-id rule ("variables
    must have unique IDs"). Number them from 0 in the order they appear.
    """
