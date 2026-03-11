# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .sent_dm_services_common_contracts_poc_os_template_button_props_param import (
    SentDmServicesCommonContractsPocOsTemplateButtonPropsParam,
)

__all__ = ["SentDmServicesCommonContractsPocOsTemplateButtonParam"]


class SentDmServicesCommonContractsPocOsTemplateButtonParam(TypedDict, total=False):
    """Interactive button in a message template"""

    id: int
    """The unique identifier of the button (1-based index)"""

    props: SentDmServicesCommonContractsPocOsTemplateButtonPropsParam
    """Properties specific to the button type"""

    type: str
    """
    The type of button (e.g., QUICK_REPLY, URL, PHONE_NUMBER, VOICE_CALL, COPY_CODE)
    """
