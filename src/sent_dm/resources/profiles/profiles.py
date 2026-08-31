# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
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
    """**Deprecated — use Sender Profiles.**

    The original profile resource, kept because it has live callers. It still works, and its replacement is `/v3/sender-profiles`, which takes the identity and the campaign in one call instead of across three.

    New integrations should not start here.
    """

    @cached_property
    def campaigns(self) -> CampaignsResource:
        """**Deprecated — use Sender Profiles.**

        The original profile resource, kept because it has live callers. It still works, and its replacement is `/v3/sender-profiles`, which takes the identity and the campaign in one call instead of across three.

        New integrations should not start here.
        """
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

    @typing_extensions.deprecated("deprecated")
    def create(
        self,
        *,
        allow_contact_sharing: Optional[bool] | Omit = omit,
        allow_template_sharing: Optional[bool] | Omit = omit,
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
        """
        **Deprecated.** This endpoint is replaced by `/v3/sender-profiles` and will be
        removed in a future release. It still behaves exactly as before, so nothing
        needs to change today — but new integrations should use `/v3/sender-profiles`,
        which models a profile's markets, compliance, brand, campaigns and billing
        explicitly.

        Creates a new sender profile within an organization. Profiles represent
        different brands, departments, or use cases, each with their own messaging
        configuration and settings. Requires admin role in the organization.

        ## WhatsApp Business Account

        Every profile owns its own WhatsApp Business Account — accounts are never shared
        between profiles or inherited from the organization. Provide a
        `whatsapp_business_account` object with `waba_id`, `phone_number_id`, and
        `access_token`. Obtain these from Meta Business Manager by creating a System
        User with `whatsapp_business_messaging` and `whatsapp_business_management`
        permissions.

        Omit the field and the profile is created without WhatsApp, staying incomplete
        until it has an account of its own.

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
          allow_contact_sharing: Deprecated. Accepted and ignored. Contact and template sharing between sender
              profiles is gone — a profile sees only what it owns, and the organization still
              sees all of its profiles' contacts and templates through read-time widening. The
              four columns behind these flags were dropped by M260720120000.

              Bound rather than dropped so the properties survive on the wire and in a
              generated client: an SDK that assigns them keeps compiling, which is the
              compatibility this exists for. Deliberately not refused either — a 400 would
              break an integration that is otherwise working, and the capability they ask for
              is gone either way. Same rule as SendingPhoneNumberProfileId.

              The read is what makes this survivable: every profile reports all four as false,
              so a caller that checks its own write can see it did not take. Requests carrying
              one are logged, so we can tell when nobody sends them any more and the fields
              can go for real.

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

          inherit_tcr_brand: Whether this profile inherits TCR brand from organization (default: false)

          inherit_tcr_campaign: Whether this profile inherits TCR campaign from organization (default: false)

          name: Profile name (required)

          payment_details: Payment card details for this profile (optional). Accepted when billing_model is
              "profile" or "profile_and_organization". Not persisted on our servers —
              forwarded to the payment processor.

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

    @typing_extensions.deprecated("deprecated")
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
        **Deprecated.** This endpoint is replaced by `/v3/sender-profiles` and will be
        removed in a future release. It still behaves exactly as before, so nothing
        needs to change today — but new integrations should use `/v3/sender-profiles`,
        which models a profile's markets, compliance, brand, campaigns and billing
        explicitly.

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

    @typing_extensions.deprecated("deprecated")
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
        """
        **Deprecated.** This endpoint is replaced by `/v3/sender-profiles` and will be
        removed in a future release. It still behaves exactly as before, so nothing
        needs to change today — but new integrations should use `/v3/sender-profiles`,
        which models a profile's markets, compliance, brand, campaigns and billing
        explicitly.

        Updates a profile's configuration and settings. Requires admin role in the
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

        ## Deprecated fields

        `sending_phone_number_profile_id` and `sending_whatsapp_number_profile_id` are
        **accepted and ignored**. Sender borrowing is gone: a profile cannot send from
        another profile's number, because two profiles behind one sender makes an
        inbound reply and a delivery receipt ambiguous about whose they are.

        Sending either **changes nothing and still returns `200`** — they are kept on
        the contract so an existing integration keeps working. Reads carry both keys too
        and always answer `null`, which is how you can confirm the value did not take.

        Give the profile a sender of its own instead — `POST /v3/channels/sms` or
        `POST /v3/channels/whatsapp`, sent with the `x-profile-id` header naming it.

        Args:
          allow_contact_sharing: Deprecated. Accepted and ignored. Contact and template sharing between sender
              profiles is gone — a profile sees only what it owns, and the organization still
              sees all of its profiles' contacts and templates through read-time widening. The
              four columns behind these flags were dropped by M260720120000.

              Retired the same way as SendingPhoneNumberProfileId, and for the same reason:
              the properties stay bound so an SDK that assigns them keeps compiling, and a 400
              would break a working integration over a capability that is gone regardless.
              Every profile reports all four as false, so a caller that checks its own write
              can see it did not take.

          allow_number_change_during_onboarding: Whether number changes are allowed during onboarding (optional)

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

          inherit_tcr_brand: Whether this profile inherits TCR brand from organization (optional)

          inherit_tcr_campaign: Whether this profile inherits TCR campaign from organization (optional)

          name: Profile name (optional)

          payment_details: Payment card details for this profile (optional). Accepted when billing_model is
              "profile" or "profile_and_organization". Not persisted on our servers —
              forwarded to the payment processor.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          sending_phone_number: Direct phone number for SMS sending (optional)

          sending_phone_number_profile_id: Deprecated. Accepted and ignored. Sender borrowing is gone: a profile cannot
              send from another profile's SMS number. Supplying this changes nothing and the
              request still succeeds.

              Bound rather than dropped so the property survives on the wire and in a
              generated client — an SDK that assigns it keeps compiling, which is the
              compatibility this exists for. It is deliberately not refused: a 400 here would
              break an integration that is otherwise working, and the capability it asks for
              is gone either way.

              The trade-off, stated plainly. A caller asking for borrowing is told it
              succeeded when nothing happened. What makes that survivable is the read:
              sending_phone_number_profile_id comes back null on every profile, so a caller
              that checks its own write can see it did not take. Every request that carries
              one is logged, so we can tell when nobody is sending it any more and the field
              can go for real.

              Give the profile a sender of its own instead: POST /v3/channels/sms with the
              x-profile-id header naming it.

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

    @typing_extensions.deprecated("deprecated")
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
        **Deprecated.** This endpoint is replaced by `/v3/sender-profiles` and will be
        removed in a future release. It still behaves exactly as before, so nothing
        needs to change today — but new integrations should use `/v3/sender-profiles`,
        which models a profile's markets, compliance, brand, campaigns and billing
        explicitly.

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

    @typing_extensions.deprecated("deprecated")
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
        """
        **Deprecated.** This endpoint is replaced by `/v3/sender-profiles` and will be
        removed in a future release. It still behaves exactly as before, so nothing
        needs to change today — but new integrations should use `/v3/sender-profiles`,
        which models a profile's markets, compliance, brand, campaigns and billing
        explicitly.

        Soft deletes a sender profile. The profile will be marked as deleted but data is
        retained. Anything it still held is released first: phone numbers return to our
        inventory and can go to whoever asks next, its own WhatsApp account is
        deregistered, and its routing rules stop being used. Requires admin role in the
        organization.

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

    @typing_extensions.deprecated("deprecated")
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
        """
        **Deprecated.** This endpoint is replaced by `/v3/sender-profiles` and will be
        removed in a future release. It still behaves exactly as before, so nothing
        needs to change today — but new integrations should use `/v3/sender-profiles`,
        which models a profile's markets, compliance, brand, campaigns and billing
        explicitly.

        Final step in the profile compliance workflow. Validates all prerequisites (KYC,
        brand, campaigns, required documents), connects the profile to the SMS and
        WhatsApp channels, and marks it onboarded. Prerequisites are always validated
        first: if any fail the call returns 400 naming every unmet one, and nothing is
        started. If they pass and the profile is already onboarded, the call returns 200
        and does nothing. Otherwise it returns 202 and calls the provided webhook URL
        when background processing finishes.

        Callable with the organization's API key or the profile's own key. The key's
        user must be an admin or owner of the profile, or of the organization it belongs
        to.

        Prerequisites (all but the last are checked before the already-onboarded
        short-circuit, matching the previous contract; the last is checked after it, so
        a profile that is already onboarded is never rejected by it):

        - Profile must have a name, short name, and description (short name max 50
          characters, description max 5000)
        - webHookUrl must be supplied on the request
        - A KYC form submission is required
        - A brand is required, either on the profile or inherited from the parent
          organization
        - TCR applications must have at least one campaign, own or inherited
        - Destination countries marked as main must have their required compliance
          documents uploaded
        - TCR applications must state whether they inherit the organization's TCR brand
          and campaign

        Outcome:

        - Once the prerequisites pass and background processing succeeds, the profile's
          conversionFlowStatus becomes ONBOARDED and its public status reads `approved`
        - A profile with no WhatsApp channel, or one still awaiting TCR registration or
          country documents, is onboarded like any other. Those are answered by the
          brand and campaign records, not by a status on the profile
        - If background processing fails, the profile keeps the status it already had
          and the webhook reports the reason

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
    """**Deprecated — use Sender Profiles.**

    The original profile resource, kept because it has live callers. It still works, and its replacement is `/v3/sender-profiles`, which takes the identity and the campaign in one call instead of across three.

    New integrations should not start here.
    """

    @cached_property
    def campaigns(self) -> AsyncCampaignsResource:
        """**Deprecated — use Sender Profiles.**

        The original profile resource, kept because it has live callers. It still works, and its replacement is `/v3/sender-profiles`, which takes the identity and the campaign in one call instead of across three.

        New integrations should not start here.
        """
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

    @typing_extensions.deprecated("deprecated")
    async def create(
        self,
        *,
        allow_contact_sharing: Optional[bool] | Omit = omit,
        allow_template_sharing: Optional[bool] | Omit = omit,
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
        """
        **Deprecated.** This endpoint is replaced by `/v3/sender-profiles` and will be
        removed in a future release. It still behaves exactly as before, so nothing
        needs to change today — but new integrations should use `/v3/sender-profiles`,
        which models a profile's markets, compliance, brand, campaigns and billing
        explicitly.

        Creates a new sender profile within an organization. Profiles represent
        different brands, departments, or use cases, each with their own messaging
        configuration and settings. Requires admin role in the organization.

        ## WhatsApp Business Account

        Every profile owns its own WhatsApp Business Account — accounts are never shared
        between profiles or inherited from the organization. Provide a
        `whatsapp_business_account` object with `waba_id`, `phone_number_id`, and
        `access_token`. Obtain these from Meta Business Manager by creating a System
        User with `whatsapp_business_messaging` and `whatsapp_business_management`
        permissions.

        Omit the field and the profile is created without WhatsApp, staying incomplete
        until it has an account of its own.

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
          allow_contact_sharing: Deprecated. Accepted and ignored. Contact and template sharing between sender
              profiles is gone — a profile sees only what it owns, and the organization still
              sees all of its profiles' contacts and templates through read-time widening. The
              four columns behind these flags were dropped by M260720120000.

              Bound rather than dropped so the properties survive on the wire and in a
              generated client: an SDK that assigns them keeps compiling, which is the
              compatibility this exists for. Deliberately not refused either — a 400 would
              break an integration that is otherwise working, and the capability they ask for
              is gone either way. Same rule as SendingPhoneNumberProfileId.

              The read is what makes this survivable: every profile reports all four as false,
              so a caller that checks its own write can see it did not take. Requests carrying
              one are logged, so we can tell when nobody sends them any more and the fields
              can go for real.

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

          inherit_tcr_brand: Whether this profile inherits TCR brand from organization (default: false)

          inherit_tcr_campaign: Whether this profile inherits TCR campaign from organization (default: false)

          name: Profile name (required)

          payment_details: Payment card details for this profile (optional). Accepted when billing_model is
              "profile" or "profile_and_organization". Not persisted on our servers —
              forwarded to the payment processor.

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

    @typing_extensions.deprecated("deprecated")
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
        **Deprecated.** This endpoint is replaced by `/v3/sender-profiles` and will be
        removed in a future release. It still behaves exactly as before, so nothing
        needs to change today — but new integrations should use `/v3/sender-profiles`,
        which models a profile's markets, compliance, brand, campaigns and billing
        explicitly.

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

    @typing_extensions.deprecated("deprecated")
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
        """
        **Deprecated.** This endpoint is replaced by `/v3/sender-profiles` and will be
        removed in a future release. It still behaves exactly as before, so nothing
        needs to change today — but new integrations should use `/v3/sender-profiles`,
        which models a profile's markets, compliance, brand, campaigns and billing
        explicitly.

        Updates a profile's configuration and settings. Requires admin role in the
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

        ## Deprecated fields

        `sending_phone_number_profile_id` and `sending_whatsapp_number_profile_id` are
        **accepted and ignored**. Sender borrowing is gone: a profile cannot send from
        another profile's number, because two profiles behind one sender makes an
        inbound reply and a delivery receipt ambiguous about whose they are.

        Sending either **changes nothing and still returns `200`** — they are kept on
        the contract so an existing integration keeps working. Reads carry both keys too
        and always answer `null`, which is how you can confirm the value did not take.

        Give the profile a sender of its own instead — `POST /v3/channels/sms` or
        `POST /v3/channels/whatsapp`, sent with the `x-profile-id` header naming it.

        Args:
          allow_contact_sharing: Deprecated. Accepted and ignored. Contact and template sharing between sender
              profiles is gone — a profile sees only what it owns, and the organization still
              sees all of its profiles' contacts and templates through read-time widening. The
              four columns behind these flags were dropped by M260720120000.

              Retired the same way as SendingPhoneNumberProfileId, and for the same reason:
              the properties stay bound so an SDK that assigns them keeps compiling, and a 400
              would break a working integration over a capability that is gone regardless.
              Every profile reports all four as false, so a caller that checks its own write
              can see it did not take.

          allow_number_change_during_onboarding: Whether number changes are allowed during onboarding (optional)

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

          inherit_tcr_brand: Whether this profile inherits TCR brand from organization (optional)

          inherit_tcr_campaign: Whether this profile inherits TCR campaign from organization (optional)

          name: Profile name (optional)

          payment_details: Payment card details for this profile (optional). Accepted when billing_model is
              "profile" or "profile_and_organization". Not persisted on our servers —
              forwarded to the payment processor.

          sandbox: Sandbox flag - when true, the operation is simulated without side effects Useful
              for testing integrations without actual execution

          sending_phone_number: Direct phone number for SMS sending (optional)

          sending_phone_number_profile_id: Deprecated. Accepted and ignored. Sender borrowing is gone: a profile cannot
              send from another profile's SMS number. Supplying this changes nothing and the
              request still succeeds.

              Bound rather than dropped so the property survives on the wire and in a
              generated client — an SDK that assigns it keeps compiling, which is the
              compatibility this exists for. It is deliberately not refused: a 400 here would
              break an integration that is otherwise working, and the capability it asks for
              is gone either way.

              The trade-off, stated plainly. A caller asking for borrowing is told it
              succeeded when nothing happened. What makes that survivable is the read:
              sending_phone_number_profile_id comes back null on every profile, so a caller
              that checks its own write can see it did not take. Every request that carries
              one is logged, so we can tell when nobody is sending it any more and the field
              can go for real.

              Give the profile a sender of its own instead: POST /v3/channels/sms with the
              x-profile-id header naming it.

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

    @typing_extensions.deprecated("deprecated")
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
        **Deprecated.** This endpoint is replaced by `/v3/sender-profiles` and will be
        removed in a future release. It still behaves exactly as before, so nothing
        needs to change today — but new integrations should use `/v3/sender-profiles`,
        which models a profile's markets, compliance, brand, campaigns and billing
        explicitly.

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

    @typing_extensions.deprecated("deprecated")
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
        """
        **Deprecated.** This endpoint is replaced by `/v3/sender-profiles` and will be
        removed in a future release. It still behaves exactly as before, so nothing
        needs to change today — but new integrations should use `/v3/sender-profiles`,
        which models a profile's markets, compliance, brand, campaigns and billing
        explicitly.

        Soft deletes a sender profile. The profile will be marked as deleted but data is
        retained. Anything it still held is released first: phone numbers return to our
        inventory and can go to whoever asks next, its own WhatsApp account is
        deregistered, and its routing rules stop being used. Requires admin role in the
        organization.

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

    @typing_extensions.deprecated("deprecated")
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
        """
        **Deprecated.** This endpoint is replaced by `/v3/sender-profiles` and will be
        removed in a future release. It still behaves exactly as before, so nothing
        needs to change today — but new integrations should use `/v3/sender-profiles`,
        which models a profile's markets, compliance, brand, campaigns and billing
        explicitly.

        Final step in the profile compliance workflow. Validates all prerequisites (KYC,
        brand, campaigns, required documents), connects the profile to the SMS and
        WhatsApp channels, and marks it onboarded. Prerequisites are always validated
        first: if any fail the call returns 400 naming every unmet one, and nothing is
        started. If they pass and the profile is already onboarded, the call returns 200
        and does nothing. Otherwise it returns 202 and calls the provided webhook URL
        when background processing finishes.

        Callable with the organization's API key or the profile's own key. The key's
        user must be an admin or owner of the profile, or of the organization it belongs
        to.

        Prerequisites (all but the last are checked before the already-onboarded
        short-circuit, matching the previous contract; the last is checked after it, so
        a profile that is already onboarded is never rejected by it):

        - Profile must have a name, short name, and description (short name max 50
          characters, description max 5000)
        - webHookUrl must be supplied on the request
        - A KYC form submission is required
        - A brand is required, either on the profile or inherited from the parent
          organization
        - TCR applications must have at least one campaign, own or inherited
        - Destination countries marked as main must have their required compliance
          documents uploaded
        - TCR applications must state whether they inherit the organization's TCR brand
          and campaign

        Outcome:

        - Once the prerequisites pass and background processing succeeds, the profile's
          conversionFlowStatus becomes ONBOARDED and its public status reads `approved`
        - A profile with no WhatsApp channel, or one still awaiting TCR registration or
          country documents, is onboarded like any other. Those are answered by the
          brand and campaign records, not by a status on the profile
        - If background processing fails, the profile keeps the status it already had
          and the webhook reports the reason

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

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                profiles.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                profiles.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                profiles.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                profiles.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                profiles.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.complete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                profiles.complete,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def campaigns(self) -> CampaignsResourceWithRawResponse:
        """**Deprecated — use Sender Profiles.**

        The original profile resource, kept because it has live callers. It still works, and its replacement is `/v3/sender-profiles`, which takes the identity and the campaign in one call instead of across three.

        New integrations should not start here.
        """
        return CampaignsResourceWithRawResponse(self._profiles.campaigns)


class AsyncProfilesResourceWithRawResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                profiles.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                profiles.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                profiles.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                profiles.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                profiles.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.complete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                profiles.complete,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithRawResponse:
        """**Deprecated — use Sender Profiles.**

        The original profile resource, kept because it has live callers. It still works, and its replacement is `/v3/sender-profiles`, which takes the identity and the campaign in one call instead of across three.

        New integrations should not start here.
        """
        return AsyncCampaignsResourceWithRawResponse(self._profiles.campaigns)


class ProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                profiles.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                profiles.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                profiles.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                profiles.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                profiles.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.complete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                profiles.complete,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def campaigns(self) -> CampaignsResourceWithStreamingResponse:
        """**Deprecated — use Sender Profiles.**

        The original profile resource, kept because it has live callers. It still works, and its replacement is `/v3/sender-profiles`, which takes the identity and the campaign in one call instead of across three.

        New integrations should not start here.
        """
        return CampaignsResourceWithStreamingResponse(self._profiles.campaigns)


class AsyncProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                profiles.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.retrieve = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                profiles.retrieve,  # pyright: ignore[reportDeprecated],
            )
        )
        self.update = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                profiles.update,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                profiles.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                profiles.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.complete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                profiles.complete,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def campaigns(self) -> AsyncCampaignsResourceWithStreamingResponse:
        """**Deprecated — use Sender Profiles.**

        The original profile resource, kept because it has live callers. It still works, and its replacement is `/v3/sender-profiles`, which takes the identity and the campaign in one call instead of across three.

        New integrations should not start here.
        """
        return AsyncCampaignsResourceWithStreamingResponse(self._profiles.campaigns)
