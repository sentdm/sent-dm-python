# Webhooks

Types:

```python
from sent_dm.types import (
    APIError,
    APIMeta,
    APIResponseWebhook,
    MutationRequest,
    PaginationMeta,
    WebhookResponse,
    WebhookListResponse,
    WebhookListEventTypesResponse,
    WebhookListEventsResponse,
    WebhookRotateSecretResponse,
    WebhookTestResponse,
)
```

Methods:

- <code title="post /v3/webhooks">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">create</a>(\*\*<a href="src/sent_dm/types/webhook_create_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_webhook.py">APIResponseWebhook</a></code>
- <code title="get /v3/webhooks/{id}">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">retrieve</a>(id) -> <a href="./src/sent_dm/types/api_response_webhook.py">APIResponseWebhook</a></code>
- <code title="put /v3/webhooks/{id}">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">update</a>(id, \*\*<a href="src/sent_dm/types/webhook_update_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_webhook.py">APIResponseWebhook</a></code>
- <code title="get /v3/webhooks">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">list</a>(\*\*<a href="src/sent_dm/types/webhook_list_params.py">params</a>) -> <a href="./src/sent_dm/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /v3/webhooks/{id}">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">delete</a>(id) -> None</code>
- <code title="get /v3/webhooks/event-types">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">list_event_types</a>() -> <a href="./src/sent_dm/types/webhook_list_event_types_response.py">WebhookListEventTypesResponse</a></code>
- <code title="get /v3/webhooks/{id}/events">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">list_events</a>(id, \*\*<a href="src/sent_dm/types/webhook_list_events_params.py">params</a>) -> <a href="./src/sent_dm/types/webhook_list_events_response.py">WebhookListEventsResponse</a></code>
- <code title="post /v3/webhooks/{id}/rotate-secret">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">rotate_secret</a>(id, \*\*<a href="src/sent_dm/types/webhook_rotate_secret_params.py">params</a>) -> <a href="./src/sent_dm/types/webhook_rotate_secret_response.py">WebhookRotateSecretResponse</a></code>
- <code title="post /v3/webhooks/{id}/test">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">test</a>(id, \*\*<a href="src/sent_dm/types/webhook_test_params.py">params</a>) -> <a href="./src/sent_dm/types/webhook_test_response.py">WebhookTestResponse</a></code>
- <code title="patch /v3/webhooks/{id}/toggle-status">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">toggle_status</a>(id, \*\*<a href="src/sent_dm/types/webhook_toggle_status_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_webhook.py">APIResponseWebhook</a></code>

# Users

Types:

```python
from sent_dm.types import APIResponseOfUser, UserResponse, UserListResponse
```

Methods:

- <code title="get /v3/users/{userId}">client.users.<a href="./src/sent_dm/resources/users.py">retrieve</a>(user_id) -> <a href="./src/sent_dm/types/api_response_of_user.py">APIResponseOfUser</a></code>
- <code title="get /v3/users">client.users.<a href="./src/sent_dm/resources/users.py">list</a>() -> <a href="./src/sent_dm/types/user_list_response.py">UserListResponse</a></code>
- <code title="post /v3/users">client.users.<a href="./src/sent_dm/resources/users.py">invite</a>(\*\*<a href="src/sent_dm/types/user_invite_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_user.py">APIResponseOfUser</a></code>
- <code title="delete /v3/users/{userId}">client.users.<a href="./src/sent_dm/resources/users.py">remove</a>(path_user_id, \*\*<a href="src/sent_dm/types/user_remove_params.py">params</a>) -> None</code>
- <code title="patch /v3/users/{userId}">client.users.<a href="./src/sent_dm/resources/users.py">update_role</a>(path_user_id, \*\*<a href="src/sent_dm/types/user_update_role_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_user.py">APIResponseOfUser</a></code>

# Templates

Types:

```python
from sent_dm.types import (
    APIResponseTemplate,
    SentDmServicesCommonContractsPocOsAuthenticationConfig,
    SentDmServicesCommonContractsPocOsTemplateBody,
    SentDmServicesCommonContractsPocOsTemplateButton,
    SentDmServicesCommonContractsPocOsTemplateButtonProps,
    SentDmServicesCommonContractsPocOsTemplateFooter,
    SentDmServicesCommonContractsPocOsTemplateHeader,
    Template,
    TemplateBodyContent,
    TemplateDefinition,
    TemplateVariable,
    TemplateListResponse,
)
```

Methods:

- <code title="post /v3/templates">client.templates.<a href="./src/sent_dm/resources/templates.py">create</a>(\*\*<a href="src/sent_dm/types/template_create_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_template.py">APIResponseTemplate</a></code>
- <code title="get /v3/templates/{id}">client.templates.<a href="./src/sent_dm/resources/templates.py">retrieve</a>(id) -> <a href="./src/sent_dm/types/api_response_template.py">APIResponseTemplate</a></code>
- <code title="put /v3/templates/{id}">client.templates.<a href="./src/sent_dm/resources/templates.py">update</a>(id, \*\*<a href="src/sent_dm/types/template_update_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_template.py">APIResponseTemplate</a></code>
- <code title="get /v3/templates">client.templates.<a href="./src/sent_dm/resources/templates.py">list</a>(\*\*<a href="src/sent_dm/types/template_list_params.py">params</a>) -> <a href="./src/sent_dm/types/template_list_response.py">TemplateListResponse</a></code>
- <code title="delete /v3/templates/{id}">client.templates.<a href="./src/sent_dm/resources/templates.py">delete</a>(id, \*\*<a href="src/sent_dm/types/template_delete_params.py">params</a>) -> None</code>

# Profiles

Types:

```python
from sent_dm.types import APIResponseOfProfileDetail, ProfileDetail, ProfileListResponse
```

Methods:

- <code title="post /v3/profiles">client.profiles.<a href="./src/sent_dm/resources/profiles.py">create</a>(\*\*<a href="src/sent_dm/types/profile_create_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_profile_detail.py">APIResponseOfProfileDetail</a></code>
- <code title="get /v3/profiles/{profileId}">client.profiles.<a href="./src/sent_dm/resources/profiles.py">retrieve</a>(profile_id) -> <a href="./src/sent_dm/types/api_response_of_profile_detail.py">APIResponseOfProfileDetail</a></code>
- <code title="patch /v3/profiles/{profileId}">client.profiles.<a href="./src/sent_dm/resources/profiles.py">update</a>(path_profile_id, \*\*<a href="src/sent_dm/types/profile_update_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_profile_detail.py">APIResponseOfProfileDetail</a></code>
- <code title="get /v3/profiles">client.profiles.<a href="./src/sent_dm/resources/profiles.py">list</a>() -> <a href="./src/sent_dm/types/profile_list_response.py">ProfileListResponse</a></code>
- <code title="delete /v3/profiles/{profileId}">client.profiles.<a href="./src/sent_dm/resources/profiles.py">delete</a>(path_profile_id, \*\*<a href="src/sent_dm/types/profile_delete_params.py">params</a>) -> None</code>
- <code title="post /v3/profiles/{profileId}/complete">client.profiles.<a href="./src/sent_dm/resources/profiles.py">complete</a>(profile_id, \*\*<a href="src/sent_dm/types/profile_complete_params.py">params</a>) -> object</code>

# Messages

Types:

```python
from sent_dm.types import (
    MessageRetrieveActivitiesResponse,
    MessageRetrieveStatusResponse,
    MessageSendResponse,
)
```

Methods:

- <code title="get /v3/messages/{id}/activities">client.messages.<a href="./src/sent_dm/resources/messages.py">retrieve_activities</a>(id) -> <a href="./src/sent_dm/types/message_retrieve_activities_response.py">MessageRetrieveActivitiesResponse</a></code>
- <code title="get /v3/messages/{id}">client.messages.<a href="./src/sent_dm/resources/messages.py">retrieve_status</a>(id) -> <a href="./src/sent_dm/types/message_retrieve_status_response.py">MessageRetrieveStatusResponse</a></code>
- <code title="post /v3/messages">client.messages.<a href="./src/sent_dm/resources/messages.py">send</a>(\*\*<a href="src/sent_dm/types/message_send_params.py">params</a>) -> <a href="./src/sent_dm/types/message_send_response.py">MessageSendResponse</a></code>

# Lookup

Types:

```python
from sent_dm.types import LookupRetrievePhoneInfoResponse
```

Methods:

- <code title="get /v3/lookup/number/{phoneNumber}">client.lookup.<a href="./src/sent_dm/resources/lookup.py">retrieve_phone_info</a>(phone_number) -> <a href="./src/sent_dm/types/lookup_retrieve_phone_info_response.py">LookupRetrievePhoneInfoResponse</a></code>

# Contacts

Types:

```python
from sent_dm.types import APIResponseContact, Contact, ContactListResponse
```

Methods:

- <code title="post /v3/contacts">client.contacts.<a href="./src/sent_dm/resources/contacts.py">create</a>(\*\*<a href="src/sent_dm/types/contact_create_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_contact.py">APIResponseContact</a></code>
- <code title="get /v3/contacts/{id}">client.contacts.<a href="./src/sent_dm/resources/contacts.py">retrieve</a>(id) -> <a href="./src/sent_dm/types/api_response_contact.py">APIResponseContact</a></code>
- <code title="patch /v3/contacts/{id}">client.contacts.<a href="./src/sent_dm/resources/contacts.py">update</a>(id, \*\*<a href="src/sent_dm/types/contact_update_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_contact.py">APIResponseContact</a></code>
- <code title="get /v3/contacts">client.contacts.<a href="./src/sent_dm/resources/contacts.py">list</a>(\*\*<a href="src/sent_dm/types/contact_list_params.py">params</a>) -> <a href="./src/sent_dm/types/contact_list_response.py">ContactListResponse</a></code>
- <code title="delete /v3/contacts/{id}">client.contacts.<a href="./src/sent_dm/resources/contacts.py">delete</a>(id, \*\*<a href="src/sent_dm/types/contact_delete_params.py">params</a>) -> None</code>

# Brands

Types:

```python
from sent_dm.types import (
    APIResponseBrandWithKYC,
    BrandData,
    BrandWithKYC,
    DestinationCountry,
    TcrBrandRelationship,
    TcrVertical,
    BrandListResponse,
)
```

Methods:

- <code title="post /v3/brands">client.brands.<a href="./src/sent_dm/resources/brands/brands.py">create</a>(\*\*<a href="src/sent_dm/types/brand_create_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_brand_with_kyc.py">APIResponseBrandWithKYC</a></code>
- <code title="put /v3/brands/{brandId}">client.brands.<a href="./src/sent_dm/resources/brands/brands.py">update</a>(brand_id, \*\*<a href="src/sent_dm/types/brand_update_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_brand_with_kyc.py">APIResponseBrandWithKYC</a></code>
- <code title="get /v3/brands">client.brands.<a href="./src/sent_dm/resources/brands/brands.py">list</a>() -> <a href="./src/sent_dm/types/brand_list_response.py">BrandListResponse</a></code>
- <code title="delete /v3/brands/{brandId}">client.brands.<a href="./src/sent_dm/resources/brands/brands.py">delete</a>(brand_id, \*\*<a href="src/sent_dm/types/brand_delete_params.py">params</a>) -> None</code>

## Campaigns

Types:

```python
from sent_dm.types.brands import (
    APIResponseTcrCampaignWithUseCases,
    BaseDto,
    CampaignData,
    MessagingUseCaseUs,
    SentDmServicesEndpointsCustomerApIv3ContractsRequestsCampaignsCampaignUseCaseData,
    TcrCampaignWithUseCases,
    CampaignListResponse,
)
```

Methods:

- <code title="post /v3/brands/{brandId}/campaigns">client.brands.campaigns.<a href="./src/sent_dm/resources/brands/campaigns.py">create</a>(brand_id, \*\*<a href="src/sent_dm/types/brands/campaign_create_params.py">params</a>) -> <a href="./src/sent_dm/types/brands/api_response_tcr_campaign_with_use_cases.py">APIResponseTcrCampaignWithUseCases</a></code>
- <code title="put /v3/brands/{brandId}/campaigns/{campaignId}">client.brands.campaigns.<a href="./src/sent_dm/resources/brands/campaigns.py">update</a>(campaign_id, \*, brand_id, \*\*<a href="src/sent_dm/types/brands/campaign_update_params.py">params</a>) -> <a href="./src/sent_dm/types/brands/api_response_tcr_campaign_with_use_cases.py">APIResponseTcrCampaignWithUseCases</a></code>
- <code title="get /v3/brands/{brandId}/campaigns">client.brands.campaigns.<a href="./src/sent_dm/resources/brands/campaigns.py">list</a>(brand_id) -> <a href="./src/sent_dm/types/brands/campaign_list_response.py">CampaignListResponse</a></code>
- <code title="delete /v3/brands/{brandId}/campaigns/{campaignId}">client.brands.campaigns.<a href="./src/sent_dm/resources/brands/campaigns.py">delete</a>(campaign_id, \*, brand_id, \*\*<a href="src/sent_dm/types/brands/campaign_delete_params.py">params</a>) -> None</code>

# Me

Types:

```python
from sent_dm.types import ProfileSettings, MeRetrieveResponse
```

Methods:

- <code title="get /v3/me">client.me.<a href="./src/sent_dm/resources/me.py">retrieve</a>() -> <a href="./src/sent_dm/types/me_retrieve_response.py">MeRetrieveResponse</a></code>
