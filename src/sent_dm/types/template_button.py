# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .template_button_props import TemplateButtonProps

__all__ = ["TemplateButton"]


class TemplateButton(BaseModel):
    """Interactive button in a message template"""

    props: TemplateButtonProps
    """Properties specific to the button type"""

    type: str
    """
    The type of button (e.g., QUICK_REPLY, URL, PHONE_NUMBER, VOICE_CALL, COPY_CODE)
    """

    id: Optional[int] = None
    """The button's identifier (1-based index), unique within the template.

    Omitting it is only safe for a template holding a single button. The field is a
    non-nullable int, so every button that leaves it out defaults to 0, and two such
    buttons are refused by the unique-id rule ("Button IDs must be unique"). Number
    them from 1 in the order they should appear — order matters on RCS, where only
    the first four buttons render.
    """
