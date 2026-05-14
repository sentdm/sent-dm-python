# Webhooks

Types:

```python
from sent_dm.types import (
    WebhookCreateResponse,
    WebhookRetrieveResponse,
    WebhookUpdateResponse,
    WebhookListResponse,
    WebhookListEventTypesResponse,
    WebhookListEventsResponse,
    WebhookRotateSecretResponse,
    WebhookTestResponse,
    WebhookToggleStatusResponse,
)
```

Methods:

- <code title="post /v3/webhooks">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">create</a>(\*\*<a href="src/sent_dm/types/webhook_create_params.py">params</a>) -> <a href="./src/sent_dm/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /v3/webhooks/{id}">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">retrieve</a>(id) -> <a href="./src/sent_dm/types/webhook_retrieve_response.py">WebhookRetrieveResponse</a></code>
- <code title="put /v3/webhooks/{id}">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">update</a>(id, \*\*<a href="src/sent_dm/types/webhook_update_params.py">params</a>) -> <a href="./src/sent_dm/types/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /v3/webhooks">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">list</a>(\*\*<a href="src/sent_dm/types/webhook_list_params.py">params</a>) -> <a href="./src/sent_dm/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /v3/webhooks/{id}">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">delete</a>(id) -> None</code>
- <code title="get /v3/webhooks/event-types">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">list_event_types</a>() -> <a href="./src/sent_dm/types/webhook_list_event_types_response.py">WebhookListEventTypesResponse</a></code>
- <code title="get /v3/webhooks/{id}/events">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">list_events</a>(id, \*\*<a href="src/sent_dm/types/webhook_list_events_params.py">params</a>) -> <a href="./src/sent_dm/types/webhook_list_events_response.py">WebhookListEventsResponse</a></code>
- <code title="post /v3/webhooks/{id}/rotate-secret">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">rotate_secret</a>(id, \*\*<a href="src/sent_dm/types/webhook_rotate_secret_params.py">params</a>) -> <a href="./src/sent_dm/types/webhook_rotate_secret_response.py">WebhookRotateSecretResponse</a></code>
- <code title="post /v3/webhooks/{id}/test">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">test</a>(id, \*\*<a href="src/sent_dm/types/webhook_test_params.py">params</a>) -> <a href="./src/sent_dm/types/webhook_test_response.py">WebhookTestResponse</a></code>
- <code title="patch /v3/webhooks/{id}/toggle-status">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">toggle_status</a>(id, \*\*<a href="src/sent_dm/types/webhook_toggle_status_params.py">params</a>) -> <a href="./src/sent_dm/types/webhook_toggle_status_response.py">WebhookToggleStatusResponse</a></code>

# Users

Types:

```python
from sent_dm.types import (
    UserRetrieveResponse,
    UserListResponse,
    UserInviteResponse,
    UserUpdateRoleResponse,
)
```

Methods:

- <code title="get /v3/users/{userId}">client.users.<a href="./src/sent_dm/resources/users.py">retrieve</a>(user_id) -> <a href="./src/sent_dm/types/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="get /v3/users">client.users.<a href="./src/sent_dm/resources/users.py">list</a>() -> <a href="./src/sent_dm/types/user_list_response.py">UserListResponse</a></code>
- <code title="post /v3/users">client.users.<a href="./src/sent_dm/resources/users.py">invite</a>(\*\*<a href="src/sent_dm/types/user_invite_params.py">params</a>) -> <a href="./src/sent_dm/types/user_invite_response.py">UserInviteResponse</a></code>
- <code title="delete /v3/users/{userId}">client.users.<a href="./src/sent_dm/resources/users.py">remove</a>(user_id, \*\*<a href="src/sent_dm/types/user_remove_params.py">params</a>) -> None</code>
- <code title="patch /v3/users/{userId}">client.users.<a href="./src/sent_dm/resources/users.py">update_role</a>(user_id, \*\*<a href="src/sent_dm/types/user_update_role_params.py">params</a>) -> <a href="./src/sent_dm/types/user_update_role_response.py">UserUpdateRoleResponse</a></code>

# Templates

Types:

```python
from sent_dm.types import (
    TemplateCreateResponse,
    TemplateRetrieveResponse,
    TemplateUpdateResponse,
    TemplateListResponse,
)
```

Methods:

- <code title="post /v3/templates">client.templates.<a href="./src/sent_dm/resources/templates.py">create</a>(\*\*<a href="src/sent_dm/types/template_create_params.py">params</a>) -> <a href="./src/sent_dm/types/template_create_response.py">TemplateCreateResponse</a></code>
- <code title="get /v3/templates/{id}">client.templates.<a href="./src/sent_dm/resources/templates.py">retrieve</a>(id) -> <a href="./src/sent_dm/types/template_retrieve_response.py">TemplateRetrieveResponse</a></code>
- <code title="put /v3/templates/{id}">client.templates.<a href="./src/sent_dm/resources/templates.py">update</a>(id, \*\*<a href="src/sent_dm/types/template_update_params.py">params</a>) -> <a href="./src/sent_dm/types/template_update_response.py">TemplateUpdateResponse</a></code>
- <code title="get /v3/templates">client.templates.<a href="./src/sent_dm/resources/templates.py">list</a>(\*\*<a href="src/sent_dm/types/template_list_params.py">params</a>) -> <a href="./src/sent_dm/types/template_list_response.py">TemplateListResponse</a></code>
- <code title="delete /v3/templates/{id}">client.templates.<a href="./src/sent_dm/resources/templates.py">delete</a>(id, \*\*<a href="src/sent_dm/types/template_delete_params.py">params</a>) -> None</code>

# Profiles

Types:

```python
from sent_dm.types import (
    ProfileCreateResponse,
    ProfileRetrieveResponse,
    ProfileUpdateResponse,
    ProfileListResponse,
    ProfileCompleteResponse,
)
```

Methods:

- <code title="post /v3/profiles">client.profiles.<a href="./src/sent_dm/resources/profiles/profiles.py">create</a>(\*\*<a href="src/sent_dm/types/profile_create_params.py">params</a>) -> <a href="./src/sent_dm/types/profile_create_response.py">ProfileCreateResponse</a></code>
- <code title="get /v3/profiles/{profileId}">client.profiles.<a href="./src/sent_dm/resources/profiles/profiles.py">retrieve</a>(profile_id) -> <a href="./src/sent_dm/types/profile_retrieve_response.py">ProfileRetrieveResponse</a></code>
- <code title="patch /v3/profiles/{profileId}">client.profiles.<a href="./src/sent_dm/resources/profiles/profiles.py">update</a>(profile_id, \*\*<a href="src/sent_dm/types/profile_update_params.py">params</a>) -> <a href="./src/sent_dm/types/profile_update_response.py">ProfileUpdateResponse</a></code>
- <code title="get /v3/profiles">client.profiles.<a href="./src/sent_dm/resources/profiles/profiles.py">list</a>() -> <a href="./src/sent_dm/types/profile_list_response.py">ProfileListResponse</a></code>
- <code title="delete /v3/profiles/{profileId}">client.profiles.<a href="./src/sent_dm/resources/profiles/profiles.py">delete</a>(profile_id, \*\*<a href="src/sent_dm/types/profile_delete_params.py">params</a>) -> None</code>
- <code title="post /v3/profiles/{profileId}/complete">client.profiles.<a href="./src/sent_dm/resources/profiles/profiles.py">complete</a>(profile_id, \*\*<a href="src/sent_dm/types/profile_complete_params.py">params</a>) -> <a href="./src/sent_dm/types/profile_complete_response.py">ProfileCompleteResponse</a></code>

## Campaigns

Types:

```python
from sent_dm.types.profiles import (
    CampaignCreateResponse,
    CampaignUpdateResponse,
    CampaignListResponse,
)
```

Methods:

- <code title="post /v3/profiles/{profileId}/campaigns">client.profiles.campaigns.<a href="./src/sent_dm/resources/profiles/campaigns.py">create</a>(profile_id, \*\*<a href="src/sent_dm/types/profiles/campaign_create_params.py">params</a>) -> <a href="./src/sent_dm/types/profiles/campaign_create_response.py">CampaignCreateResponse</a></code>
- <code title="put /v3/profiles/{profileId}/campaigns/{campaignId}">client.profiles.campaigns.<a href="./src/sent_dm/resources/profiles/campaigns.py">update</a>(campaign_id, \*, profile_id, \*\*<a href="src/sent_dm/types/profiles/campaign_update_params.py">params</a>) -> <a href="./src/sent_dm/types/profiles/campaign_update_response.py">CampaignUpdateResponse</a></code>
- <code title="get /v3/profiles/{profileId}/campaigns">client.profiles.campaigns.<a href="./src/sent_dm/resources/profiles/campaigns.py">list</a>(profile_id) -> <a href="./src/sent_dm/types/profiles/campaign_list_response.py">CampaignListResponse</a></code>
- <code title="delete /v3/profiles/{profileId}/campaigns/{campaignId}">client.profiles.campaigns.<a href="./src/sent_dm/resources/profiles/campaigns.py">delete</a>(campaign_id, \*, profile_id, \*\*<a href="src/sent_dm/types/profiles/campaign_delete_params.py">params</a>) -> None</code>

# Numbers

Types:

```python
from sent_dm.types import NumberLookupResponse
```

Methods:

- <code title="get /v3/numbers/lookup/{phoneNumber}">client.numbers.<a href="./src/sent_dm/resources/numbers.py">lookup</a>(phone_number) -> <a href="./src/sent_dm/types/number_lookup_response.py">NumberLookupResponse</a></code>

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

# Contacts

Types:

```python
from sent_dm.types import (
    ContactCreateResponse,
    ContactRetrieveResponse,
    ContactUpdateResponse,
    ContactListResponse,
)
```

Methods:

- <code title="post /v3/contacts">client.contacts.<a href="./src/sent_dm/resources/contacts.py">create</a>(\*\*<a href="src/sent_dm/types/contact_create_params.py">params</a>) -> <a href="./src/sent_dm/types/contact_create_response.py">ContactCreateResponse</a></code>
- <code title="get /v3/contacts/{id}">client.contacts.<a href="./src/sent_dm/resources/contacts.py">retrieve</a>(id) -> <a href="./src/sent_dm/types/contact_retrieve_response.py">ContactRetrieveResponse</a></code>
- <code title="patch /v3/contacts/{id}">client.contacts.<a href="./src/sent_dm/resources/contacts.py">update</a>(id, \*\*<a href="src/sent_dm/types/contact_update_params.py">params</a>) -> <a href="./src/sent_dm/types/contact_update_response.py">ContactUpdateResponse</a></code>
- <code title="get /v3/contacts">client.contacts.<a href="./src/sent_dm/resources/contacts.py">list</a>(\*\*<a href="src/sent_dm/types/contact_list_params.py">params</a>) -> <a href="./src/sent_dm/types/contact_list_response.py">ContactListResponse</a></code>
- <code title="delete /v3/contacts/{id}">client.contacts.<a href="./src/sent_dm/resources/contacts.py">delete</a>(id, \*\*<a href="src/sent_dm/types/contact_delete_params.py">params</a>) -> None</code>

# Me

Types:

```python
from sent_dm.types import MeRetrieveResponse
```

Methods:

- <code title="get /v3/me">client.me.<a href="./src/sent_dm/resources/me.py">retrieve</a>() -> <a href="./src/sent_dm/types/me_retrieve_response.py">MeRetrieveResponse</a></code>
