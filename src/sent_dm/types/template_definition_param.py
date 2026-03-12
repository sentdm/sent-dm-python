# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .sent_dm_services_common_contracts_poc_os_template_body_param import (
    SentDmServicesCommonContractsPocOsTemplateBodyParam,
)
from .sent_dm_services_common_contracts_poc_os_template_button_param import (
    SentDmServicesCommonContractsPocOsTemplateButtonParam,
)
from .sent_dm_services_common_contracts_poc_os_template_footer_param import (
    SentDmServicesCommonContractsPocOsTemplateFooterParam,
)
from .sent_dm_services_common_contracts_poc_os_template_header_param import (
    SentDmServicesCommonContractsPocOsTemplateHeaderParam,
)
from .sent_dm_services_common_contracts_poc_os_authentication_config_param import (
    SentDmServicesCommonContractsPocOsAuthenticationConfigParam,
)

__all__ = ["TemplateDefinitionParam"]


class TemplateDefinitionParam(TypedDict, total=False):
    """
    Complete definition of a message template including header, body, footer, and buttons
    """

    body: Required[SentDmServicesCommonContractsPocOsTemplateBodyParam]
    """Body section of a message template with channel-specific content"""

    authentication_config: Annotated[
        Optional[SentDmServicesCommonContractsPocOsAuthenticationConfigParam],
        PropertyInfo(alias="authenticationConfig"),
    ]
    """Configuration for AUTHENTICATION category templates"""

    buttons: Optional[Iterable[SentDmServicesCommonContractsPocOsTemplateButtonParam]]
    """Optional list of interactive buttons (e.g., quick replies, URLs, phone numbers)"""

    definition_version: Annotated[Optional[str], PropertyInfo(alias="definitionVersion")]
    """The version of the template definition format"""

    footer: Optional[SentDmServicesCommonContractsPocOsTemplateFooterParam]
    """Footer section of a message template"""

    header: Optional[SentDmServicesCommonContractsPocOsTemplateHeaderParam]
    """Header section of a message template"""
