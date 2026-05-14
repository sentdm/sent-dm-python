# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import profile_create_params, profile_delete_params, profile_update_params, profile_complete_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from .campaigns import (
    CampaignsResource,
    AsyncCampaignsResource,
    CampaignsResourceWithRawResponse,
    AsyncCampaignsResourceWithRawResponse,
    CampaignsResourceWithStreamingResponse,
    AsyncCampaignsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.profile_list_response import ProfileListResponse
from ...types.profile_create_response import ProfileCreateResponse
from ...types.profile_update_response import ProfileUpdateResponse
from ...types.profile_complete_response import ProfileCompleteResponse
from ...types.profile_retrieve_response import ProfileRetrieveResponse

__all__ = ["ProfilesResource", "AsyncProfilesResource"]


class ProfilesResource(SyncAPIResource):
    """Manage organization profiles"""

    @cached_property
    def campaigns(self) -> CampaignsResource:
        """Manage organization profiles"""
        return CampaignsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return ProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return ProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        allow_contact_sharing: bool | Omit = omit,
        allow_template_sharing: bool | Omit = omit,
        billing_contact: Optional[profile_create_params.BillingContact] | Omit = omit,
        billing_model: Optional[str] | Omit = omit,
        brand: Optional[profile_create_params.Brand] | Omit = omit,
        description: Optional[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        inherit_contacts: Optional[bool] | Omit = omit,
        inherit_tcr_brand: Optional[bool] | Omit = omit,
        inherit_tcr_campaign: Optional[bool] | Omit = omit,
        inherit_templates: Optional[bool] | Omit = omit,
        name: str | Omit = omit,
        payment_details: Optional[profile_create_params.PaymentDetails] | Omit = omit,
        sandbox: bool | Omit = omit,
        short_name: Optional[str] | Omit = omit,
        whatsapp_business_account: Optional[profile_create_params.WhatsappBusinessAccount] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileCreateResponse:
        """Creates a new sender profile within an organization.

        Profiles represent
        different brands, departments, or use cases, each with their own messaging
        configuration and settings. Requires admin role in the organization.

        ## WhatsApp Business Account

        Every profile must be linked to a WhatsApp Business Account. There are two ways
        to do this:

        **1. Inherit from organization (default)** — Omit the
        `whatsapp_business_account` field. The profile will share the organization's
        WhatsApp Business Account, which must have been set up via WhatsApp Embedded
        Signup. This is the recommended path for most use cases.

        **2. Direct credentials** — Provide a `whatsapp_business_account` object with
        `waba_id`, `phone_number_id`, and `access_token`. Use this when the profile
        needs its own independent WhatsApp Business Account. Obtain these from Meta
        Business Manager by creating a System User with `whatsapp_business_messaging`
        and `whatsapp_business_management` permissions.

        If the `whatsapp_business_account` field is omitted and the organization has no
        WhatsApp Business Account configured, the request will be rejected with
        HTTP 422.

        ## Brand

        Include the optional `brand` field to create the brand for this profile at the
        same time. Cannot be used when `inherit_tcr_brand` is `true`.

        ## Payment Details

        When `billing_model` is `"profile"` or `"profile_and_organization"` you may
        include a `payment_details` object containing the card number, expiry (MM/YY),
        CVC, and billing ZIP code. Payment details are **never stored** on our servers
        and are forwarded directly to the payment processor. Providing `payment_details`
        when `billing_model` is `"organization"` is not allowed.

        Args:
          allow_contact_sharing: Whether contacts are shared across profiles (default: false)

          allow_template_sharing: Whether templates are shared across profiles (default: false)

          billing_contact: Billing contact information for a profile. Required when billing_model is
              "profile" or "profile_and_organization".

          billing_model:
              Billing model: profile, organization, or profile_and_organization (default:
              profile).

              - "organization": the organization's billing details are used; no profile-level
                billing info needed.
              - "profile": the profile is billed independently; billing_contact is required.
              - "profile_and_organization": the profile is billed first with the organization
                as fallback; billing_contact is required.

          brand: Brand and KYC data grouped into contact, business, and compliance sections

          description: Profile description (optional)

          icon: Profile icon URL (optional)

          inherit_contacts: Whether this profile inherits contacts from organization (default: true)

          inherit_tcr_brand: Whether this profile inherits TCR brand from organization (default: true)

          inherit_tcr_campaign: Whether this profile inherits TCR campaign from organization (default: true)

          inherit_templates: Whether this profile inherits templates from organization (default: true)

          name: Profile name (required)

          payment_details: Payment card details for a profile. Accepted when billing_model is "profile" or
              "profile_and_organization". These details are not stored on our servers and will
              be forwarded to the payment processor.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          short_name: Profile short name/abbreviation (optional). Must be 3–11 characters, contain
              only letters, numbers, and spaces, and include at least one letter. Example:
              "SALES", "Mkt 2", "Support1".

          whatsapp_business_account: Direct WhatsApp Business Account credentials for a profile. Use this when the
              profile should have its own WhatsApp Business Account instead of inheriting from
              the organization. Credentials must be obtained from Meta Business Manager by
              creating a System User with whatsapp_business_messaging and
              whatsapp_business_management scopes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-profile-id": x_profile_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/v3/profiles",
            body=maybe_transform(
                {
                    "allow_contact_sharing": allow_contact_sharing,
                    "allow_template_sharing": allow_template_sharing,
                    "billing_contact": billing_contact,
                    "billing_model": billing_model,
                    "brand": brand,
                    "description": description,
                    "icon": icon,
                    "inherit_contacts": inherit_contacts,
                    "inherit_tcr_brand": inherit_tcr_brand,
                    "inherit_tcr_campaign": inherit_tcr_campaign,
                    "inherit_templates": inherit_templates,
                    "name": name,
                    "payment_details": payment_details,
                    "sandbox": sandbox,
                    "short_name": short_name,
                    "whatsapp_business_account": whatsapp_business_account,
                },
                profile_create_params.ProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileCreateResponse,
        )

    def retrieve(
        self,
        profile_id: str,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRetrieveResponse:
        """
        Retrieves detailed information about a specific sender profile within an
        organization, including brand and KYC information if a brand has been
        configured.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v3/profiles/{profile_id}", profile_id=profile_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveResponse,
        )

    def update(
        self,
        profile_id: str,
        *,
        allow_contact_sharing: Optional[bool] | Omit = omit,
        allow_number_change_during_onboarding: Optional[bool] | Omit = omit,
        allow_template_sharing: Optional[bool] | Omit = omit,
        billing_contact: Optional[profile_update_params.BillingContact] | Omit = omit,
        billing_model: Optional[str] | Omit = omit,
        brand: Optional[profile_update_params.Brand] | Omit = omit,
        description: Optional[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        inherit_contacts: Optional[bool] | Omit = omit,
        inherit_tcr_brand: Optional[bool] | Omit = omit,
        inherit_tcr_campaign: Optional[bool] | Omit = omit,
        inherit_templates: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        payment_details: Optional[profile_update_params.PaymentDetails] | Omit = omit,
        sandbox: bool | Omit = omit,
        sending_phone_number: Optional[str] | Omit = omit,
        sending_phone_number_profile_id: Optional[str] | Omit = omit,
        sending_whatsapp_number_profile_id: Optional[str] | Omit = omit,
        short_name: Optional[str] | Omit = omit,
        whatsapp_phone_number: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateResponse:
        """Updates a profile's configuration and settings.

        Requires admin role in the
        organization. Only provided fields will be updated (partial update).

        ## Brand Management

        Include the optional `brand` field to create or update the brand associated with
        this profile. The brand holds KYC and TCR compliance data (legal business info,
        contact details, messaging vertical). Once a brand has been submitted to TCR it
        cannot be modified. Setting `inherit_tcr_brand: true` and providing `brand` in
        the same request is not allowed.

        ## Payment Details

        When `billing_model` is `"profile"` or `"profile_and_organization"` you may
        include a `payment_details` object containing the card number, expiry (MM/YY),
        CVC, and billing ZIP code. Payment details are **never stored** on our servers
        and are forwarded directly to the payment processor. Providing `payment_details`
        when `billing_model` is `"organization"` is not allowed.

        Args:
          allow_contact_sharing: Whether contacts are shared across profiles (optional)

          allow_number_change_during_onboarding: Whether number changes are allowed during onboarding (optional)

          allow_template_sharing: Whether templates are shared across profiles (optional)

          billing_contact: Billing contact information for a profile. Required when billing_model is
              "profile" or "profile_and_organization".

          billing_model: Billing model: profile, organization, or profile_and_organization (optional).

              - "organization": the organization's billing details are used; no profile-level
                billing info needed.
              - "profile": the profile is billed independently; billing_contact is required.
              - "profile_and_organization": the profile is billed first with the organization
                as fallback; billing_contact is required.

          brand: Brand and KYC data grouped into contact, business, and compliance sections

          description: Profile description (optional)

          icon: Profile icon URL (optional)

          inherit_contacts: Whether this profile inherits contacts from organization (optional)

          inherit_tcr_brand: Whether this profile inherits TCR brand from organization (optional)

          inherit_tcr_campaign: Whether this profile inherits TCR campaign from organization (optional)

          inherit_templates: Whether this profile inherits templates from organization (optional)

          name: Profile name (optional)

          payment_details: Payment card details for a profile. Accepted when billing_model is "profile" or
              "profile_and_organization". These details are not stored on our servers and will
              be forwarded to the payment processor.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          sending_phone_number: Direct phone number for SMS sending (optional)

          sending_phone_number_profile_id: Reference to another profile to use for SMS/Telnyx configuration (optional)

          sending_whatsapp_number_profile_id: Reference to another profile to use for WhatsApp configuration (optional)

          short_name: Profile short name/abbreviation (optional). Must be 3–11 characters, contain
              only letters, numbers, and spaces, and include at least one letter. Example:
              "SALES", "Mkt 2", "Support1".

          whatsapp_phone_number: Direct phone number for WhatsApp sending (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-profile-id": x_profile_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._patch(
            path_template("/v3/profiles/{profile_id}", profile_id=profile_id),
            body=maybe_transform(
                {
                    "allow_contact_sharing": allow_contact_sharing,
                    "allow_number_change_during_onboarding": allow_number_change_during_onboarding,
                    "allow_template_sharing": allow_template_sharing,
                    "billing_contact": billing_contact,
                    "billing_model": billing_model,
                    "brand": brand,
                    "description": description,
                    "icon": icon,
                    "inherit_contacts": inherit_contacts,
                    "inherit_tcr_brand": inherit_tcr_brand,
                    "inherit_tcr_campaign": inherit_tcr_campaign,
                    "inherit_templates": inherit_templates,
                    "name": name,
                    "payment_details": payment_details,
                    "sandbox": sandbox,
                    "sending_phone_number": sending_phone_number,
                    "sending_phone_number_profile_id": sending_phone_number_profile_id,
                    "sending_whatsapp_number_profile_id": sending_whatsapp_number_profile_id,
                    "short_name": short_name,
                    "whatsapp_phone_number": whatsapp_phone_number,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
        )

    def list(
        self,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileListResponse:
        """
        Retrieves all sender profiles within an organization, including brand
        information for each profile. Profiles represent different brands, departments,
        or use cases within an organization, each with their own messaging
        configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._get(
            "/v3/profiles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileListResponse,
        )

    def delete(
        self,
        profile_id: str,
        *,
        sandbox: bool | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft deletes a sender profile.

        The profile will be marked as deleted but data is
        retained. Requires admin role in the organization.

        Args:
          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return self._delete(
            path_template("/v3/profiles/{profile_id}", profile_id=profile_id),
            body=maybe_transform({"sandbox": sandbox}, profile_delete_params.ProfileDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def complete(
        self,
        profile_id: str,
        *,
        web_hook_url: str,
        sandbox: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileCompleteResponse:
        """Final step in profile compliance workflow.

        Validates all prerequisites (general
        data, brand, campaigns), connects profile to Telnyx/WhatsApp, and sets status
        based on configuration. The process runs in the background and calls the
        provided webhook URL when finished.

                        Prerequisites:
                        - Profile must be completed
                        - If inheritTcrBrand=false: Profile must have existing brand
                        - If inheritTcrBrand=true: Parent must have existing brand
                        - If TCR application: Must have at least one campaign (own or inherited)
                        - If inheritTcrCampaign=false: Profile should have campaigns
                        - If inheritTcrCampaign=true: Parent must have campaigns

                        Status Logic:
                        - If both SMS and WhatsApp channels are missing → SUBMITTED
                        - If TCR application and not inheriting brand/campaigns → SUBMITTED
                        - If non-TCR with destination country (IsMain=true) → SUBMITTED
                        - Otherwise → COMPLETED

        Args:
          web_hook_url: Webhook URL to call when profile completion finishes (success or failure)

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-profile-id": x_profile_id,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/v3/profiles/{profile_id}/complete", profile_id=profile_id),
            body=maybe_transform(
                {
                    "web_hook_url": web_hook_url,
                    "sandbox": sandbox,
                },
                profile_complete_params.ProfileCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileCompleteResponse,
        )


class AsyncProfilesResource(AsyncAPIResource):
    """Manage organization profiles"""

    @cached_property
    def campaigns(self) -> AsyncCampaignsResource:
        """Manage organization profiles"""
        return AsyncCampaignsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-dm-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-dm-python#with_streaming_response
        """
        return AsyncProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        allow_contact_sharing: bool | Omit = omit,
        allow_template_sharing: bool | Omit = omit,
        billing_contact: Optional[profile_create_params.BillingContact] | Omit = omit,
        billing_model: Optional[str] | Omit = omit,
        brand: Optional[profile_create_params.Brand] | Omit = omit,
        description: Optional[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        inherit_contacts: Optional[bool] | Omit = omit,
        inherit_tcr_brand: Optional[bool] | Omit = omit,
        inherit_tcr_campaign: Optional[bool] | Omit = omit,
        inherit_templates: Optional[bool] | Omit = omit,
        name: str | Omit = omit,
        payment_details: Optional[profile_create_params.PaymentDetails] | Omit = omit,
        sandbox: bool | Omit = omit,
        short_name: Optional[str] | Omit = omit,
        whatsapp_business_account: Optional[profile_create_params.WhatsappBusinessAccount] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileCreateResponse:
        """Creates a new sender profile within an organization.

        Profiles represent
        different brands, departments, or use cases, each with their own messaging
        configuration and settings. Requires admin role in the organization.

        ## WhatsApp Business Account

        Every profile must be linked to a WhatsApp Business Account. There are two ways
        to do this:

        **1. Inherit from organization (default)** — Omit the
        `whatsapp_business_account` field. The profile will share the organization's
        WhatsApp Business Account, which must have been set up via WhatsApp Embedded
        Signup. This is the recommended path for most use cases.

        **2. Direct credentials** — Provide a `whatsapp_business_account` object with
        `waba_id`, `phone_number_id`, and `access_token`. Use this when the profile
        needs its own independent WhatsApp Business Account. Obtain these from Meta
        Business Manager by creating a System User with `whatsapp_business_messaging`
        and `whatsapp_business_management` permissions.

        If the `whatsapp_business_account` field is omitted and the organization has no
        WhatsApp Business Account configured, the request will be rejected with
        HTTP 422.

        ## Brand

        Include the optional `brand` field to create the brand for this profile at the
        same time. Cannot be used when `inherit_tcr_brand` is `true`.

        ## Payment Details

        When `billing_model` is `"profile"` or `"profile_and_organization"` you may
        include a `payment_details` object containing the card number, expiry (MM/YY),
        CVC, and billing ZIP code. Payment details are **never stored** on our servers
        and are forwarded directly to the payment processor. Providing `payment_details`
        when `billing_model` is `"organization"` is not allowed.

        Args:
          allow_contact_sharing: Whether contacts are shared across profiles (default: false)

          allow_template_sharing: Whether templates are shared across profiles (default: false)

          billing_contact: Billing contact information for a profile. Required when billing_model is
              "profile" or "profile_and_organization".

          billing_model:
              Billing model: profile, organization, or profile_and_organization (default:
              profile).

              - "organization": the organization's billing details are used; no profile-level
                billing info needed.
              - "profile": the profile is billed independently; billing_contact is required.
              - "profile_and_organization": the profile is billed first with the organization
                as fallback; billing_contact is required.

          brand: Brand and KYC data grouped into contact, business, and compliance sections

          description: Profile description (optional)

          icon: Profile icon URL (optional)

          inherit_contacts: Whether this profile inherits contacts from organization (default: true)

          inherit_tcr_brand: Whether this profile inherits TCR brand from organization (default: true)

          inherit_tcr_campaign: Whether this profile inherits TCR campaign from organization (default: true)

          inherit_templates: Whether this profile inherits templates from organization (default: true)

          name: Profile name (required)

          payment_details: Payment card details for a profile. Accepted when billing_model is "profile" or
              "profile_and_organization". These details are not stored on our servers and will
              be forwarded to the payment processor.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          short_name: Profile short name/abbreviation (optional). Must be 3–11 characters, contain
              only letters, numbers, and spaces, and include at least one letter. Example:
              "SALES", "Mkt 2", "Support1".

          whatsapp_business_account: Direct WhatsApp Business Account credentials for a profile. Use this when the
              profile should have its own WhatsApp Business Account instead of inheriting from
              the organization. Credentials must be obtained from Meta Business Manager by
              creating a System User with whatsapp_business_messaging and
              whatsapp_business_management scopes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-profile-id": x_profile_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/v3/profiles",
            body=await async_maybe_transform(
                {
                    "allow_contact_sharing": allow_contact_sharing,
                    "allow_template_sharing": allow_template_sharing,
                    "billing_contact": billing_contact,
                    "billing_model": billing_model,
                    "brand": brand,
                    "description": description,
                    "icon": icon,
                    "inherit_contacts": inherit_contacts,
                    "inherit_tcr_brand": inherit_tcr_brand,
                    "inherit_tcr_campaign": inherit_tcr_campaign,
                    "inherit_templates": inherit_templates,
                    "name": name,
                    "payment_details": payment_details,
                    "sandbox": sandbox,
                    "short_name": short_name,
                    "whatsapp_business_account": whatsapp_business_account,
                },
                profile_create_params.ProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileCreateResponse,
        )

    async def retrieve(
        self,
        profile_id: str,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileRetrieveResponse:
        """
        Retrieves detailed information about a specific sender profile within an
        organization, including brand and KYC information if a brand has been
        configured.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v3/profiles/{profile_id}", profile_id=profile_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileRetrieveResponse,
        )

    async def update(
        self,
        profile_id: str,
        *,
        allow_contact_sharing: Optional[bool] | Omit = omit,
        allow_number_change_during_onboarding: Optional[bool] | Omit = omit,
        allow_template_sharing: Optional[bool] | Omit = omit,
        billing_contact: Optional[profile_update_params.BillingContact] | Omit = omit,
        billing_model: Optional[str] | Omit = omit,
        brand: Optional[profile_update_params.Brand] | Omit = omit,
        description: Optional[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        inherit_contacts: Optional[bool] | Omit = omit,
        inherit_tcr_brand: Optional[bool] | Omit = omit,
        inherit_tcr_campaign: Optional[bool] | Omit = omit,
        inherit_templates: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        payment_details: Optional[profile_update_params.PaymentDetails] | Omit = omit,
        sandbox: bool | Omit = omit,
        sending_phone_number: Optional[str] | Omit = omit,
        sending_phone_number_profile_id: Optional[str] | Omit = omit,
        sending_whatsapp_number_profile_id: Optional[str] | Omit = omit,
        short_name: Optional[str] | Omit = omit,
        whatsapp_phone_number: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileUpdateResponse:
        """Updates a profile's configuration and settings.

        Requires admin role in the
        organization. Only provided fields will be updated (partial update).

        ## Brand Management

        Include the optional `brand` field to create or update the brand associated with
        this profile. The brand holds KYC and TCR compliance data (legal business info,
        contact details, messaging vertical). Once a brand has been submitted to TCR it
        cannot be modified. Setting `inherit_tcr_brand: true` and providing `brand` in
        the same request is not allowed.

        ## Payment Details

        When `billing_model` is `"profile"` or `"profile_and_organization"` you may
        include a `payment_details` object containing the card number, expiry (MM/YY),
        CVC, and billing ZIP code. Payment details are **never stored** on our servers
        and are forwarded directly to the payment processor. Providing `payment_details`
        when `billing_model` is `"organization"` is not allowed.

        Args:
          allow_contact_sharing: Whether contacts are shared across profiles (optional)

          allow_number_change_during_onboarding: Whether number changes are allowed during onboarding (optional)

          allow_template_sharing: Whether templates are shared across profiles (optional)

          billing_contact: Billing contact information for a profile. Required when billing_model is
              "profile" or "profile_and_organization".

          billing_model: Billing model: profile, organization, or profile_and_organization (optional).

              - "organization": the organization's billing details are used; no profile-level
                billing info needed.
              - "profile": the profile is billed independently; billing_contact is required.
              - "profile_and_organization": the profile is billed first with the organization
                as fallback; billing_contact is required.

          brand: Brand and KYC data grouped into contact, business, and compliance sections

          description: Profile description (optional)

          icon: Profile icon URL (optional)

          inherit_contacts: Whether this profile inherits contacts from organization (optional)

          inherit_tcr_brand: Whether this profile inherits TCR brand from organization (optional)

          inherit_tcr_campaign: Whether this profile inherits TCR campaign from organization (optional)

          inherit_templates: Whether this profile inherits templates from organization (optional)

          name: Profile name (optional)

          payment_details: Payment card details for a profile. Accepted when billing_model is "profile" or
              "profile_and_organization". These details are not stored on our servers and will
              be forwarded to the payment processor.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          sending_phone_number: Direct phone number for SMS sending (optional)

          sending_phone_number_profile_id: Reference to another profile to use for SMS/Telnyx configuration (optional)

          sending_whatsapp_number_profile_id: Reference to another profile to use for WhatsApp configuration (optional)

          short_name: Profile short name/abbreviation (optional). Must be 3–11 characters, contain
              only letters, numbers, and spaces, and include at least one letter. Example:
              "SALES", "Mkt 2", "Support1".

          whatsapp_phone_number: Direct phone number for WhatsApp sending (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-profile-id": x_profile_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._patch(
            path_template("/v3/profiles/{profile_id}", profile_id=profile_id),
            body=await async_maybe_transform(
                {
                    "allow_contact_sharing": allow_contact_sharing,
                    "allow_number_change_during_onboarding": allow_number_change_during_onboarding,
                    "allow_template_sharing": allow_template_sharing,
                    "billing_contact": billing_contact,
                    "billing_model": billing_model,
                    "brand": brand,
                    "description": description,
                    "icon": icon,
                    "inherit_contacts": inherit_contacts,
                    "inherit_tcr_brand": inherit_tcr_brand,
                    "inherit_tcr_campaign": inherit_tcr_campaign,
                    "inherit_templates": inherit_templates,
                    "name": name,
                    "payment_details": payment_details,
                    "sandbox": sandbox,
                    "sending_phone_number": sending_phone_number,
                    "sending_phone_number_profile_id": sending_phone_number_profile_id,
                    "sending_whatsapp_number_profile_id": sending_whatsapp_number_profile_id,
                    "short_name": short_name,
                    "whatsapp_phone_number": whatsapp_phone_number,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileUpdateResponse,
        )

    async def list(
        self,
        *,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileListResponse:
        """
        Retrieves all sender profiles within an organization, including brand
        information for each profile. Profiles represent different brands, departments,
        or use cases within an organization, each with their own messaging
        configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._get(
            "/v3/profiles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileListResponse,
        )

    async def delete(
        self,
        profile_id: str,
        *,
        sandbox: bool | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft deletes a sender profile.

        The profile will be marked as deleted but data is
        retained. Requires admin role in the organization.

        Args:
          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"x-profile-id": x_profile_id}), **(extra_headers or {})}
        return await self._delete(
            path_template("/v3/profiles/{profile_id}", profile_id=profile_id),
            body=await async_maybe_transform({"sandbox": sandbox}, profile_delete_params.ProfileDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def complete(
        self,
        profile_id: str,
        *,
        web_hook_url: str,
        sandbox: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        x_profile_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileCompleteResponse:
        """Final step in profile compliance workflow.

        Validates all prerequisites (general
        data, brand, campaigns), connects profile to Telnyx/WhatsApp, and sets status
        based on configuration. The process runs in the background and calls the
        provided webhook URL when finished.

                        Prerequisites:
                        - Profile must be completed
                        - If inheritTcrBrand=false: Profile must have existing brand
                        - If inheritTcrBrand=true: Parent must have existing brand
                        - If TCR application: Must have at least one campaign (own or inherited)
                        - If inheritTcrCampaign=false: Profile should have campaigns
                        - If inheritTcrCampaign=true: Parent must have campaigns

                        Status Logic:
                        - If both SMS and WhatsApp channels are missing → SUBMITTED
                        - If TCR application and not inheriting brand/campaigns → SUBMITTED
                        - If non-TCR with destination country (IsMain=true) → SUBMITTED
                        - Otherwise → COMPLETED

        Args:
          web_hook_url: Webhook URL to call when profile completion finishes (success or failure)

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "Idempotency-Key": idempotency_key,
                    "x-profile-id": x_profile_id,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/v3/profiles/{profile_id}/complete", profile_id=profile_id),
            body=await async_maybe_transform(
                {
                    "web_hook_url": web_hook_url,
                    "sandbox": sandbox,
                },
                profile_complete_params.ProfileCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileCompleteResponse,
        )


class ProfilesResourceWithRawResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.create = to_raw_response_wrapper(
            profiles.create,
        )
        self.retrieve = to_raw_response_wrapper(
            profiles.retrieve,
        )
        self.update = to_raw_response_wrapper(
            profiles.update,
        )
        self.list = to_raw_response_wrapper(
            profiles.list,
        )
        self.delete = to_raw_response_wrapper(
            profiles.delete,
        )
        self.complete = to_raw_response_wrapper(
            profiles.complete,
        )

    @cached_property
    def campaigns(self) -> CampaignsResourceWithRawResponse:
        """Manage organization profiles"""
        return CampaignsResourceWithRawResponse(self._profiles.campaigns)


class AsyncProfilesResourceWithRawResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.create = async_to_raw_response_wrapper(
            profiles.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            profiles.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            profiles.update,
        )
        self.list = async_to_raw_response_wrapper(
            profiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            profiles.delete,
        )
        self.complete = async_to_raw_response_wrapper(
            profiles.complete,
        )

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithRawResponse:
        """Manage organization profiles"""
        return AsyncCampaignsResourceWithRawResponse(self._profiles.campaigns)


class ProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.create = to_streamed_response_wrapper(
            profiles.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            profiles.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            profiles.update,
        )
        self.list = to_streamed_response_wrapper(
            profiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            profiles.delete,
        )
        self.complete = to_streamed_response_wrapper(
            profiles.complete,
        )

    @cached_property
    def campaigns(self) -> CampaignsResourceWithStreamingResponse:
        """Manage organization profiles"""
        return CampaignsResourceWithStreamingResponse(self._profiles.campaigns)


class AsyncProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.create = async_to_streamed_response_wrapper(
            profiles.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            profiles.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            profiles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            profiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            profiles.delete,
        )
        self.complete = async_to_streamed_response_wrapper(
            profiles.complete,
        )

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithStreamingResponse:
        """Manage organization profiles"""
        return AsyncCampaignsResourceWithStreamingResponse(self._profiles.campaigns)
