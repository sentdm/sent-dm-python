# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MarketComplianceParam", "Brand", "Campaign", "CampaignUseCase"]


class Brand(TypedDict, total=False):
    """Business identity.

    The identity the registration is filed against. Omit to have none; { "inherit": true } to register under your organization's.
    """

    business_name: str
    """Public-facing name.

    TCR displayName — the name recipients would recognise. Named for what it holds
    rather than for TCR's field, which is why it is not `display_name`. Required
    when `compliance.brand.inherit != true`.
    """

    city: str
    """City. Required when `compliance.brand.inherit != true`."""

    contact_email: str
    """Contact email. TCR email. Required when `compliance.brand.inherit != true`."""

    contact_name: str
    """Responsible contact.

    Split into TCR's firstName/lastName on submission. BrandService refuses a blank
    one, so a missing name is reported here rather than thrown after the profile was
    written. Required when `compliance.brand.inherit != true`.
    """

    contact_phone: str
    """Contact phone.

    TCR sends it as both phone and mobilePhone, so it is asked for once. Named for
    the contact it belongs to rather than as a bare `phone` on a block that also
    carries an address. Required when `compliance.brand.inherit != true`.
    """

    country: str
    """Country of registration.

    Two letters — US. The country spelled out in full is accepted too and stored as
    its code, which is what a read answers with and what is filed. Required when
    `compliance.brand.inherit != true`.
    """

    ein_issuing_country: str
    """Country that issued the tax id.

    TCR einIssuingCountry — where the tax id was issued, which is not always where
    the business trades. Defaults to `country` when omitted, which is right for
    most. Takes the code or the country spelled out, as `country` does.
    """

    entity_type: Literal["PRIVATE_PROFIT", "PUBLIC_PROFIT", "NON_PROFIT", "SOLE_PROPRIETOR", "GOVERNMENT"]
    """Entity type.

    TCR entityType. Decides which vetting TCR applies and, for SOLE_PROPRIETOR,
    fixes the campaign fee regardless of volume. Also refused at submission if
    absent. Required when `compliance.brand.inherit != true`.
    """

    inherit: bool
    """Run on the organization's brand.

    True to register under the parent organization's identity rather than one of
    this profile's own; every field below is then neither asked for nor accepted.
    Omitted, the brand is the organization's unless this block supplies identity
    fields, which says plainly enough that it wants one of its own.
    """

    legal_name: str
    """Registered legal name.

    TCR companyName — the name on the incorporation documents, which is often not
    the name recipients would recognise. Required when
    `compliance.brand.inherit != true`.
    """

    postal_code: str
    """Postal code. Required when `compliance.brand.inherit != true`."""

    state: str
    """State or region.

    TCR state. Two letters for a US registration. Required when
    `compliance.brand.inherit != true`.
    """

    street: str
    """Street address. Required when `compliance.brand.inherit != true`."""

    tax_id: str
    """Tax identifier.

    TCR ein. TcrBrandSubmissionValidator refuses a submission without one, so it is
    wanted here rather than discovered at filing time. Required when
    `compliance.brand.inherit != true`.
    """

    tax_id_type: str
    """Kind of tax identifier.

    Which kind of identifier `tax_id` is, e.g. us_ein. Derived onto the brand form,
    and not itself sent to TCR. Required when `compliance.brand.inherit != true`.
    """

    website: str
    """Website.

    TCR website. Optional, and worth sending: carriers weigh it when vetting, so a
    brand that has one and omits it is vetted on less than it could be.
    """


class CampaignUseCase(TypedDict, total=False):
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


class Campaign(TypedDict, total=False):
    """Messaging campaign.

    What the programme sends and how recipients consented. Omit to run on your organization's; supplying it takes one of your own. { "inherit": true } says so outright. Required when `compliance.campaign.inherit != true`.
    """

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

    inherit: bool
    """Run on the organization's campaign.

    True to register under the parent organization's programme rather than one of
    this profile's own; every field below is then neither asked for nor accepted.
    Owning the identity and inheriting the campaign is refused — a campaign is filed
    against an identity registration, and chk_tcr_inheritance forbids that pairing
    outright.
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

    terms_and_conditions_link: str
    """Terms and conditions URL.

    TCR termsAndConditionsLink. Required when `compliance.campaign.inherit != true`.
    """

    use_cases: Iterable[CampaignUseCase]
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


class MarketComplianceParam(TypedDict, total=False):
    """The compliance values a market registers with.

    `brand` and `campaign` apply to US `TEN_DLC`; other markets fill this map with the document keys their own requirements name.
    """

    brand: Brand
    """Business identity.

    The identity the registration is filed against. Omit to have none; { "inherit":
    true } to register under your organization's.
    """

    campaign: Campaign
    """Messaging campaign.

    What the programme sends and how recipients consented. Omit to run on your
    organization's; supplying it takes one of your own. { "inherit": true } says so
    outright. Required when `compliance.campaign.inherit != true`.
    """
