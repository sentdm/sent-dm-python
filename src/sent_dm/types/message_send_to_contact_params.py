# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageSendToContactParams"]


class MessageSendToContactParams(TypedDict, total=False):
    contact_id: Required[Annotated[str, PropertyInfo(alias="contactId")]]
    """The unique identifier of the contact to send the message to"""

    template_id: Required[Annotated[str, PropertyInfo(alias="templateId")]]
    """The unique identifier of the template to use for the message"""

    template_variables: Annotated[Optional[Dict[str, str]], PropertyInfo(alias="templateVariables")]
    """Optional key-value pairs of template variables to replace in the template body.

    For example, if your template contains "Hello {{name}}", you would provide {
    "name": "John Doe" }
    """
