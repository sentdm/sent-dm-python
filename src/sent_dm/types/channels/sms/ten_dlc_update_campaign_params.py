# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TenDlcUpdateCampaignParams", "UseCase"]


class TenDlcUpdateCampaignParams(TypedDict, total=False):
    description: str
    """What this programme sends.

    TCR description: what recipients will get and why, in a sentence. The only one
    of these TCR takes verbatim as a description of the programme, which is why it
    is asked for rather than derived from the customer's name. Required when
    `compliance.campaign.inherit != true`.
    """

    help_keywords: str
    """Help keywords.

    TCR helpKeywords, comma separated, e.g. HELP,INFO. Required when
    `compliance.campaign.inherit != true`.
    """

    help_message: str
    """Help reply.

    TCR helpMessage. Its presence is what sets subscriberHelp. Required when
    `compliance.campaign.inherit != true`.
    """

    message_flow: str
    """Consent narrative.

    TCR messageFlow: how recipients opt in, in prose. Under 40 characters is
    refused, and carriers reject vague descriptions — say where opt-in happens, that
    the box is unchecked by default, and that consent is not a condition of
    purchase. Required when `compliance.campaign.inherit != true`.
    """

    opt_in_keywords: str
    """Opt-in keywords.

    TCR optinKeywords, comma separated, e.g. START,YES. Required when
    `compliance.campaign.inherit != true`.
    """

    opt_in_message: str
    """Opt-in confirmation.

    TCR optinMessage. Should state message frequency and that rates may apply. Its
    presence is what sets subscriberOptin. Required when
    `compliance.campaign.inherit != true`.
    """

    opt_out_keywords: str
    """Opt-out keywords.

    TCR optoutKeywords, comma separated. STOP, END, CANCEL, UNSUBSCRIBE and QUIT are
    honoured regardless of what is declared. Required when
    `compliance.campaign.inherit != true`.
    """

    opt_out_message: str
    """Opt-out confirmation.

    TCR optoutMessage. Its presence is what sets subscriberOptout. Required when
    `compliance.campaign.inherit != true`.
    """

    privacy_policy_link: str
    """Privacy policy URL.

    TCR privacyPolicyLink. Required when `compliance.campaign.inherit != true`.
    """

    sandbox: bool
    """
    Sandbox flag - when true, the operation is simulated without side effects Useful
    for testing integrations without actual execution
    """

    terms_and_conditions_link: str
    """Terms and conditions URL.

    TCR termsAndConditionsLink. Required when `compliance.campaign.inherit != true`.
    """

    use_cases: Iterable[UseCase]
    """Use cases.

    What the campaign sends, and an example of each. One to five entries; how they
    register is decided by volume, never declared. Required when
    `compliance.campaign.inherit != true`.
    """

    volume: str
    """Expected monthly volume.

    Decides how the campaign registers and which fee tier applies: below the
    low-volume threshold it registers as LOW_VOLUME with sub-use-cases, above it as
    a single use case or MIXED. Omitting it registers the campaign at the higher-fee
    standard tier.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_profile_id: Annotated[str, PropertyInfo(alias="x-profile-id")]


class UseCase(TypedDict, total=False):
    sample_messages: Required[Iterable[object]]
    """Sample messages.

    TCR sample1..sample5 for this use case. One to five, each carrying the brand
    name and an opt-out instruction.
    """

    use_case: Required[
        Literal[
            "MARKETING",
            "ACCOUNT_NOTIFICATION",
            "CUSTOMER_CARE",
            "FRAUD_ALERT",
            "2FA",
            "DELIVERY_NOTIFICATION",
            "SECURITY_ALERT",
            "M2M",
            "HIGHER_EDUCATION",
            "POLLING_VOTING",
            "PUBLIC_SERVICE_ANNOUNCEMENT",
        ]
    ]
    """Use case.

    What this entry sends. MIXED and LOW_VOLUME are refused — volume decides those.
    """
