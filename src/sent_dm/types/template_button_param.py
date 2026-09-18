# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .template_button_props_param import TemplateButtonPropsParam

__all__ = ["TemplateButtonParam"]


class TemplateButtonParam(TypedDict, total=False):
    """Interactive button in a message template"""

    props: Required[TemplateButtonPropsParam]
    """Properties specific to the button type"""

    type: Required[str]
    """
    The type of button (e.g., QUICK_REPLY, URL, PHONE_NUMBER, VOICE_CALL, COPY_CODE)
    """

    id: int
    """The button's identifier (1-based index), unique within the template.

    Omitting it is only safe for a template holding a single button. The field is a
    non-nullable int, so every button that leaves it out defaults to 0, and two such
    buttons are refused by the unique-id rule ("Button IDs must be unique"). Number
    them from 1 in the order they should appear — order matters on RCS, where only
    the first four buttons render.
    """
