# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import profile_create_params, profile_delete_params, profile_update_params, profile_complete_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.profile_list_response import ProfileListResponse
from ..types.api_response_of_profile_detail import APIResponseOfProfileDetail

__all__ = ["ProfilesResource", "AsyncProfilesResource"]


class ProfilesResource(SyncAPIResource):
    """Manage organization profiles"""

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
        billing_model: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        inherit_contacts: Optional[bool] | Omit = omit,
        inherit_tcr_brand: Optional[bool] | Omit = omit,
        inherit_tcr_campaign: Optional[bool] | Omit = omit,
        inherit_templates: Optional[bool] | Omit = omit,
        name: str | Omit = omit,
        short_name: Optional[str] | Omit = omit,
        test_mode: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfProfileDetail:
        """Creates a new sender profile within an organization.

        Profiles represent
        different brands, departments, or use cases, each with their own messaging
        configuration and settings. Requires admin role in the organization.

        Args:
          allow_contact_sharing: Whether contacts are shared across profiles (default: false)

          allow_template_sharing: Whether templates are shared across profiles (default: false)

          billing_model:
              Billing model: profile, organization, or profile_and_organization (default:
              profile)

          description: Profile description (optional)

          icon: Profile icon URL (optional)

          inherit_contacts: Whether this profile inherits contacts from organization (default: true)

          inherit_tcr_brand: Whether this profile inherits TCR brand from organization (default: true)

          inherit_tcr_campaign: Whether this profile inherits TCR campaign from organization (default: true)

          inherit_templates: Whether this profile inherits templates from organization (default: true)

          name: Profile name (required)

          short_name: Profile short name/abbreviation (optional)

          test_mode: Test mode flag - when true, the operation is simulated without side effects
              Useful for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/v3/profiles",
            body=maybe_transform(
                {
                    "allow_contact_sharing": allow_contact_sharing,
                    "allow_template_sharing": allow_template_sharing,
                    "billing_model": billing_model,
                    "description": description,
                    "icon": icon,
                    "inherit_contacts": inherit_contacts,
                    "inherit_tcr_brand": inherit_tcr_brand,
                    "inherit_tcr_campaign": inherit_tcr_campaign,
                    "inherit_templates": inherit_templates,
                    "name": name,
                    "short_name": short_name,
                    "test_mode": test_mode,
                },
                profile_create_params.ProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfProfileDetail,
        )

    def retrieve(
        self,
        profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfProfileDetail:
        """
        Retrieves detailed information about a specific sender profile within an
        organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._get(
            f"/v3/profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfProfileDetail,
        )

    def update(
        self,
        path_profile_id: str,
        *,
        allow_contact_sharing: Optional[bool] | Omit = omit,
        allow_number_change_during_onboarding: Optional[bool] | Omit = omit,
        allow_template_sharing: Optional[bool] | Omit = omit,
        billing_model: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        inherit_contacts: Optional[bool] | Omit = omit,
        inherit_tcr_brand: Optional[bool] | Omit = omit,
        inherit_tcr_campaign: Optional[bool] | Omit = omit,
        inherit_templates: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        body_profile_id: str | Omit = omit,
        sending_phone_number: Optional[str] | Omit = omit,
        sending_phone_number_profile_id: Optional[str] | Omit = omit,
        sending_whatsapp_number_profile_id: Optional[str] | Omit = omit,
        short_name: Optional[str] | Omit = omit,
        test_mode: bool | Omit = omit,
        whatsapp_phone_number: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfProfileDetail:
        """Updates a profile's configuration and settings.

        Requires admin role in the
        organization. Only provided fields will be updated (partial update).

        Args:
          allow_contact_sharing: Whether contacts are shared across profiles (optional)

          allow_number_change_during_onboarding: Whether number changes are allowed during onboarding (optional)

          allow_template_sharing: Whether templates are shared across profiles (optional)

          billing_model: Billing model: profile, organization, or profile_and_organization (optional)

          description: Profile description (optional)

          icon: Profile icon URL (optional)

          inherit_contacts: Whether this profile inherits contacts from organization (optional)

          inherit_tcr_brand: Whether this profile inherits TCR brand from organization (optional)

          inherit_tcr_campaign: Whether this profile inherits TCR campaign from organization (optional)

          inherit_templates: Whether this profile inherits templates from organization (optional)

          name: Profile name (optional)

          body_profile_id: Profile ID from route parameter

          sending_phone_number: Direct phone number for SMS sending (optional)

          sending_phone_number_profile_id: Reference to another profile to use for SMS/Telnyx configuration (optional)

          sending_whatsapp_number_profile_id: Reference to another profile to use for WhatsApp configuration (optional)

          short_name: Profile short name/abbreviation (optional)

          test_mode: Test mode flag - when true, the operation is simulated without side effects
              Useful for testing integrations without actual execution

          whatsapp_phone_number: Direct phone number for WhatsApp sending (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_profile_id:
            raise ValueError(f"Expected a non-empty value for `path_profile_id` but received {path_profile_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._patch(
            f"/v3/profiles/{path_profile_id}",
            body=maybe_transform(
                {
                    "allow_contact_sharing": allow_contact_sharing,
                    "allow_number_change_during_onboarding": allow_number_change_during_onboarding,
                    "allow_template_sharing": allow_template_sharing,
                    "billing_model": billing_model,
                    "description": description,
                    "icon": icon,
                    "inherit_contacts": inherit_contacts,
                    "inherit_tcr_brand": inherit_tcr_brand,
                    "inherit_tcr_campaign": inherit_tcr_campaign,
                    "inherit_templates": inherit_templates,
                    "name": name,
                    "body_profile_id": body_profile_id,
                    "sending_phone_number": sending_phone_number,
                    "sending_phone_number_profile_id": sending_phone_number_profile_id,
                    "sending_whatsapp_number_profile_id": sending_whatsapp_number_profile_id,
                    "short_name": short_name,
                    "test_mode": test_mode,
                    "whatsapp_phone_number": whatsapp_phone_number,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfProfileDetail,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileListResponse:
        """Retrieves all sender profiles within an organization.

        Profiles represent
        different brands, departments, or use cases within an organization, each with
        their own messaging configuration.
        """
        return self._get(
            "/v3/profiles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileListResponse,
        )

    def delete(
        self,
        path_profile_id: str,
        *,
        body_profile_id: str | Omit = omit,
        test_mode: bool | Omit = omit,
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
          body_profile_id: Profile ID from route parameter

          test_mode: Test mode flag - when true, the operation is simulated without side effects
              Useful for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_profile_id:
            raise ValueError(f"Expected a non-empty value for `path_profile_id` but received {path_profile_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v3/profiles/{path_profile_id}",
            body=maybe_transform(
                {
                    "body_profile_id": body_profile_id,
                    "test_mode": test_mode,
                },
                profile_delete_params.ProfileDeleteParams,
            ),
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
        test_mode: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
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

          test_mode: Test mode flag - when true, the operation is simulated without side effects
              Useful for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            f"/v3/profiles/{profile_id}/complete",
            body=maybe_transform(
                {
                    "web_hook_url": web_hook_url,
                    "test_mode": test_mode,
                },
                profile_complete_params.ProfileCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncProfilesResource(AsyncAPIResource):
    """Manage organization profiles"""

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
        billing_model: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        inherit_contacts: Optional[bool] | Omit = omit,
        inherit_tcr_brand: Optional[bool] | Omit = omit,
        inherit_tcr_campaign: Optional[bool] | Omit = omit,
        inherit_templates: Optional[bool] | Omit = omit,
        name: str | Omit = omit,
        short_name: Optional[str] | Omit = omit,
        test_mode: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfProfileDetail:
        """Creates a new sender profile within an organization.

        Profiles represent
        different brands, departments, or use cases, each with their own messaging
        configuration and settings. Requires admin role in the organization.

        Args:
          allow_contact_sharing: Whether contacts are shared across profiles (default: false)

          allow_template_sharing: Whether templates are shared across profiles (default: false)

          billing_model:
              Billing model: profile, organization, or profile_and_organization (default:
              profile)

          description: Profile description (optional)

          icon: Profile icon URL (optional)

          inherit_contacts: Whether this profile inherits contacts from organization (default: true)

          inherit_tcr_brand: Whether this profile inherits TCR brand from organization (default: true)

          inherit_tcr_campaign: Whether this profile inherits TCR campaign from organization (default: true)

          inherit_templates: Whether this profile inherits templates from organization (default: true)

          name: Profile name (required)

          short_name: Profile short name/abbreviation (optional)

          test_mode: Test mode flag - when true, the operation is simulated without side effects
              Useful for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/v3/profiles",
            body=await async_maybe_transform(
                {
                    "allow_contact_sharing": allow_contact_sharing,
                    "allow_template_sharing": allow_template_sharing,
                    "billing_model": billing_model,
                    "description": description,
                    "icon": icon,
                    "inherit_contacts": inherit_contacts,
                    "inherit_tcr_brand": inherit_tcr_brand,
                    "inherit_tcr_campaign": inherit_tcr_campaign,
                    "inherit_templates": inherit_templates,
                    "name": name,
                    "short_name": short_name,
                    "test_mode": test_mode,
                },
                profile_create_params.ProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfProfileDetail,
        )

    async def retrieve(
        self,
        profile_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfProfileDetail:
        """
        Retrieves detailed information about a specific sender profile within an
        organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._get(
            f"/v3/profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfProfileDetail,
        )

    async def update(
        self,
        path_profile_id: str,
        *,
        allow_contact_sharing: Optional[bool] | Omit = omit,
        allow_number_change_during_onboarding: Optional[bool] | Omit = omit,
        allow_template_sharing: Optional[bool] | Omit = omit,
        billing_model: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        icon: Optional[str] | Omit = omit,
        inherit_contacts: Optional[bool] | Omit = omit,
        inherit_tcr_brand: Optional[bool] | Omit = omit,
        inherit_tcr_campaign: Optional[bool] | Omit = omit,
        inherit_templates: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        body_profile_id: str | Omit = omit,
        sending_phone_number: Optional[str] | Omit = omit,
        sending_phone_number_profile_id: Optional[str] | Omit = omit,
        sending_whatsapp_number_profile_id: Optional[str] | Omit = omit,
        short_name: Optional[str] | Omit = omit,
        test_mode: bool | Omit = omit,
        whatsapp_phone_number: Optional[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIResponseOfProfileDetail:
        """Updates a profile's configuration and settings.

        Requires admin role in the
        organization. Only provided fields will be updated (partial update).

        Args:
          allow_contact_sharing: Whether contacts are shared across profiles (optional)

          allow_number_change_during_onboarding: Whether number changes are allowed during onboarding (optional)

          allow_template_sharing: Whether templates are shared across profiles (optional)

          billing_model: Billing model: profile, organization, or profile_and_organization (optional)

          description: Profile description (optional)

          icon: Profile icon URL (optional)

          inherit_contacts: Whether this profile inherits contacts from organization (optional)

          inherit_tcr_brand: Whether this profile inherits TCR brand from organization (optional)

          inherit_tcr_campaign: Whether this profile inherits TCR campaign from organization (optional)

          inherit_templates: Whether this profile inherits templates from organization (optional)

          name: Profile name (optional)

          body_profile_id: Profile ID from route parameter

          sending_phone_number: Direct phone number for SMS sending (optional)

          sending_phone_number_profile_id: Reference to another profile to use for SMS/Telnyx configuration (optional)

          sending_whatsapp_number_profile_id: Reference to another profile to use for WhatsApp configuration (optional)

          short_name: Profile short name/abbreviation (optional)

          test_mode: Test mode flag - when true, the operation is simulated without side effects
              Useful for testing integrations without actual execution

          whatsapp_phone_number: Direct phone number for WhatsApp sending (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_profile_id:
            raise ValueError(f"Expected a non-empty value for `path_profile_id` but received {path_profile_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._patch(
            f"/v3/profiles/{path_profile_id}",
            body=await async_maybe_transform(
                {
                    "allow_contact_sharing": allow_contact_sharing,
                    "allow_number_change_during_onboarding": allow_number_change_during_onboarding,
                    "allow_template_sharing": allow_template_sharing,
                    "billing_model": billing_model,
                    "description": description,
                    "icon": icon,
                    "inherit_contacts": inherit_contacts,
                    "inherit_tcr_brand": inherit_tcr_brand,
                    "inherit_tcr_campaign": inherit_tcr_campaign,
                    "inherit_templates": inherit_templates,
                    "name": name,
                    "body_profile_id": body_profile_id,
                    "sending_phone_number": sending_phone_number,
                    "sending_phone_number_profile_id": sending_phone_number_profile_id,
                    "sending_whatsapp_number_profile_id": sending_whatsapp_number_profile_id,
                    "short_name": short_name,
                    "test_mode": test_mode,
                    "whatsapp_phone_number": whatsapp_phone_number,
                },
                profile_update_params.ProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIResponseOfProfileDetail,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileListResponse:
        """Retrieves all sender profiles within an organization.

        Profiles represent
        different brands, departments, or use cases within an organization, each with
        their own messaging configuration.
        """
        return await self._get(
            "/v3/profiles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfileListResponse,
        )

    async def delete(
        self,
        path_profile_id: str,
        *,
        body_profile_id: str | Omit = omit,
        test_mode: bool | Omit = omit,
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
          body_profile_id: Profile ID from route parameter

          test_mode: Test mode flag - when true, the operation is simulated without side effects
              Useful for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_profile_id:
            raise ValueError(f"Expected a non-empty value for `path_profile_id` but received {path_profile_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v3/profiles/{path_profile_id}",
            body=await async_maybe_transform(
                {
                    "body_profile_id": body_profile_id,
                    "test_mode": test_mode,
                },
                profile_delete_params.ProfileDeleteParams,
            ),
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
        test_mode: bool | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
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

          test_mode: Test mode flag - when true, the operation is simulated without side effects
              Useful for testing integrations without actual execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            f"/v3/profiles/{profile_id}/complete",
            body=await async_maybe_transform(
                {
                    "web_hook_url": web_hook_url,
                    "test_mode": test_mode,
                },
                profile_complete_params.ProfileCompleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
