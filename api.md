# Webhooks

Types:

```python
from sent_dm.types import (
    APIMeta,
    APIResponseOfWebhookEventTypesList,
    APIResponseOfWebhookEventsList,
    APIResponseOfWebhookSecret,
    APIResponseOfWebhookTest,
    APIResponseOfWebhooksList,
    APIResponseWebhook,
    CallEvent,
    CallEventPayload,
    ChannelEvent,
    ChannelEventPayload,
    ContactEvent,
    ContactEventPayload,
    ErrorDetail,
    InboundMedia,
    InboundMessageEvent,
    InboundMessageEventPayload,
    LinkEvent,
    LinkEventPayload,
    MessageEvent,
    MessageEventPayload,
    MutationRequest,
    PaginationCursors,
    PaginationMeta,
    TemplateEvent,
    TemplateEventPayload,
    WebhookDelivery,
    WebhookEventType,
    WebhookEventTypesList,
    WebhookEventsList,
    WebhookResponse,
    WebhookSecret,
    WebhookSenderProfile,
    WebhookSenderProfileConfig,
    WebhookTest,
    WebhooksList,
)
```

Methods:

- <code title="post /v3/webhooks">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">create</a>(\*\*<a href="src/sent_dm/types/webhook_create_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_webhook.py">APIResponseWebhook</a></code>
- <code title="get /v3/webhooks/{id}">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">retrieve</a>(id) -> <a href="./src/sent_dm/types/api_response_webhook.py">APIResponseWebhook</a></code>
- <code title="put /v3/webhooks/{id}">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">update</a>(id, \*\*<a href="src/sent_dm/types/webhook_update_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_webhook.py">APIResponseWebhook</a></code>
- <code title="get /v3/webhooks">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">list</a>(\*\*<a href="src/sent_dm/types/webhook_list_params.py">params</a>) -> <a href="./src/sent_dm/types/webhook_response.py">SyncWebhooksPage[WebhookResponse]</a></code>
- <code title="delete /v3/webhooks/{id}">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">delete</a>(id) -> None</code>
- <code title="get /v3/webhooks/event-types">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">list_event_types</a>() -> <a href="./src/sent_dm/types/api_response_of_webhook_event_types_list.py">APIResponseOfWebhookEventTypesList</a></code>
- <code title="get /v3/webhooks/{id}/events">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">list_events</a>(id, \*\*<a href="src/sent_dm/types/webhook_list_events_params.py">params</a>) -> <a href="./src/sent_dm/types/webhook_delivery.py">SyncWebhookEventsPage[WebhookDelivery]</a></code>
- <code title="post /v3/webhooks/{id}/rotate-secret">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">rotate_secret</a>(id, \*\*<a href="src/sent_dm/types/webhook_rotate_secret_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_webhook_secret.py">APIResponseOfWebhookSecret</a></code>
- <code title="post /v3/webhooks/{id}/test">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">test</a>(id, \*\*<a href="src/sent_dm/types/webhook_test_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_webhook_test.py">APIResponseOfWebhookTest</a></code>
- <code title="patch /v3/webhooks/{id}/toggle-status">client.webhooks.<a href="./src/sent_dm/resources/webhooks.py">toggle_status</a>(id, \*\*<a href="src/sent_dm/types/webhook_toggle_status_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_webhook.py">APIResponseWebhook</a></code>

# Users

Types:

```python
from sent_dm.types import APIResponseOfUser, APIResponseOfUsersList, UserResponse, UsersList
```

Methods:

- <code title="get /v3/users/{userId}">client.users.<a href="./src/sent_dm/resources/users.py">retrieve</a>(user_id) -> <a href="./src/sent_dm/types/api_response_of_user.py">APIResponseOfUser</a></code>
- <code title="get /v3/users">client.users.<a href="./src/sent_dm/resources/users.py">list</a>() -> <a href="./src/sent_dm/types/api_response_of_users_list.py">APIResponseOfUsersList</a></code>
- <code title="post /v3/users">client.users.<a href="./src/sent_dm/resources/users.py">invite</a>(\*\*<a href="src/sent_dm/types/user_invite_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_user.py">APIResponseOfUser</a></code>
- <code title="delete /v3/users/{userId}">client.users.<a href="./src/sent_dm/resources/users.py">remove</a>(user_id, \*\*<a href="src/sent_dm/types/user_remove_params.py">params</a>) -> None</code>
- <code title="patch /v3/users/{userId}">client.users.<a href="./src/sent_dm/resources/users.py">update_role</a>(user_id, \*\*<a href="src/sent_dm/types/user_update_role_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_user.py">APIResponseOfUser</a></code>

# Templates

Types:

```python
from sent_dm.types import (
    APIResponseOfTemplatesList,
    APIResponseTemplate,
    AuthenticationConfig,
    Template,
    TemplateBody,
    TemplateBodyContent,
    TemplateButton,
    TemplateButtonProps,
    TemplateDefinition,
    TemplateFooter,
    TemplateHeader,
    TemplateHeaderLocation,
    TemplateMediaItem,
    TemplateMmsBodyContent,
    TemplateRef,
    TemplateVariable,
    TemplateVariableProps,
    TemplatesList,
)
```

Methods:

- <code title="post /v3/templates">client.templates.<a href="./src/sent_dm/resources/templates.py">create</a>(\*\*<a href="src/sent_dm/types/template_create_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_template.py">APIResponseTemplate</a></code>
- <code title="get /v3/templates/{id}">client.templates.<a href="./src/sent_dm/resources/templates.py">retrieve</a>(id) -> <a href="./src/sent_dm/types/api_response_template.py">APIResponseTemplate</a></code>
- <code title="put /v3/templates/{id}">client.templates.<a href="./src/sent_dm/resources/templates.py">update</a>(id, \*\*<a href="src/sent_dm/types/template_update_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_template.py">APIResponseTemplate</a></code>
- <code title="get /v3/templates">client.templates.<a href="./src/sent_dm/resources/templates.py">list</a>(\*\*<a href="src/sent_dm/types/template_list_params.py">params</a>) -> <a href="./src/sent_dm/types/template.py">SyncTemplatesPage[Template]</a></code>
- <code title="delete /v3/templates/{id}">client.templates.<a href="./src/sent_dm/resources/templates.py">delete</a>(id, \*\*<a href="src/sent_dm/types/template_delete_params.py">params</a>) -> None</code>

# Profiles

Types:

```python
from sent_dm.types import (
    APIResponseOfProfileCompletionAccepted,
    APIResponseOfProfileCompletionResult,
    APIResponseOfProfileDetail,
    APIResponseOfProfilesList,
    BillingContact,
    BillingContactInfo,
    BrandBusiness,
    BrandBusinessInfo,
    BrandCompliance,
    BrandComplianceInfo,
    BrandContact,
    BrandContactInfo,
    BrandWithKYC,
    BrandsBrandData,
    DestinationCountry,
    EntityType,
    PaymentDetails,
    ProfileCompletionAccepted,
    ProfileCompletionResult,
    ProfileDetail,
    ProfilesList,
    TcrBrandIdentityStatus,
    TcrBrandRelationship,
    TcrBrandStatus,
    TcrCampaignStatus,
    TcrVertical,
)
```

Methods:

- <code title="post /v3/profiles">client.profiles.<a href="./src/sent_dm/resources/profiles/profiles.py">create</a>(\*\*<a href="src/sent_dm/types/profile_create_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_profile_detail.py">APIResponseOfProfileDetail</a></code>
- <code title="get /v3/profiles/{profileId}">client.profiles.<a href="./src/sent_dm/resources/profiles/profiles.py">retrieve</a>(profile_id) -> <a href="./src/sent_dm/types/api_response_of_profile_detail.py">APIResponseOfProfileDetail</a></code>
- <code title="patch /v3/profiles/{profileId}">client.profiles.<a href="./src/sent_dm/resources/profiles/profiles.py">update</a>(profile_id, \*\*<a href="src/sent_dm/types/profile_update_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_profile_detail.py">APIResponseOfProfileDetail</a></code>
- <code title="get /v3/profiles">client.profiles.<a href="./src/sent_dm/resources/profiles/profiles.py">list</a>() -> <a href="./src/sent_dm/types/api_response_of_profiles_list.py">APIResponseOfProfilesList</a></code>
- <code title="delete /v3/profiles/{profileId}">client.profiles.<a href="./src/sent_dm/resources/profiles/profiles.py">delete</a>(profile_id, \*\*<a href="src/sent_dm/types/profile_delete_params.py">params</a>) -> None</code>
- <code title="post /v3/profiles/{profileId}/complete">client.profiles.<a href="./src/sent_dm/resources/profiles/profiles.py">complete</a>(profile_id, \*\*<a href="src/sent_dm/types/profile_complete_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_profile_completion_result.py">APIResponseOfProfileCompletionResult</a></code>

## Campaigns

Types:

```python
from sent_dm.types.profiles import (
    APIResponseOfBrandCampaign,
    APIResponseOfListOfBrandCampaign,
    BrandCampaign,
    CampaignData,
    CampaignUseCase,
    CampaignUseCaseData,
    MessagingUseCaseUs,
)
```

Methods:

- <code title="post /v3/profiles/{profileId}/campaigns">client.profiles.campaigns.<a href="./src/sent_dm/resources/profiles/campaigns.py">create</a>(profile_id, \*\*<a href="src/sent_dm/types/profiles/campaign_create_params.py">params</a>) -> <a href="./src/sent_dm/types/profiles/api_response_of_brand_campaign.py">APIResponseOfBrandCampaign</a></code>
- <code title="put /v3/profiles/{profileId}/campaigns/{campaignId}">client.profiles.campaigns.<a href="./src/sent_dm/resources/profiles/campaigns.py">update</a>(campaign_id, \*, profile_id, \*\*<a href="src/sent_dm/types/profiles/campaign_update_params.py">params</a>) -> <a href="./src/sent_dm/types/profiles/api_response_of_brand_campaign.py">APIResponseOfBrandCampaign</a></code>
- <code title="get /v3/profiles/{profileId}/campaigns">client.profiles.campaigns.<a href="./src/sent_dm/resources/profiles/campaigns.py">list</a>(profile_id) -> <a href="./src/sent_dm/types/profiles/api_response_of_list_of_brand_campaign.py">APIResponseOfListOfBrandCampaign</a></code>
- <code title="delete /v3/profiles/{profileId}/campaigns/{campaignId}">client.profiles.campaigns.<a href="./src/sent_dm/resources/profiles/campaigns.py">delete</a>(campaign_id, \*, profile_id, \*\*<a href="src/sent_dm/types/profiles/campaign_delete_params.py">params</a>) -> None</code>

# SenderProfiles

Types:

```python
from sent_dm.types import (
    APIResponseOfSenderProfile,
    APIResponseOfSenderProfilesList,
    SenderProfile,
    SenderProfileBilling,
    SenderProfileBillingRequest,
    SenderProfileChannels,
    SenderProfileRcs,
    SenderProfileSMS,
    SenderProfileWhatsapp,
    SenderProfilesList,
)
```

Methods:

- <code title="post /v3/sender-profiles">client.sender_profiles.<a href="./src/sent_dm/resources/sender_profiles.py">create</a>(\*\*<a href="src/sent_dm/types/sender_profile_create_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_sender_profile.py">APIResponseOfSenderProfile</a></code>
- <code title="get /v3/sender-profiles/{id}">client.sender_profiles.<a href="./src/sent_dm/resources/sender_profiles.py">retrieve</a>(id) -> <a href="./src/sent_dm/types/api_response_of_sender_profile.py">APIResponseOfSenderProfile</a></code>
- <code title="patch /v3/sender-profiles/{id}">client.sender_profiles.<a href="./src/sent_dm/resources/sender_profiles.py">update</a>(id, \*\*<a href="src/sent_dm/types/sender_profile_update_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_sender_profile.py">APIResponseOfSenderProfile</a></code>
- <code title="get /v3/sender-profiles">client.sender_profiles.<a href="./src/sent_dm/resources/sender_profiles.py">list</a>(\*\*<a href="src/sent_dm/types/sender_profile_list_params.py">params</a>) -> <a href="./src/sent_dm/types/sender_profile.py">SyncSenderProfilesPage[SenderProfile]</a></code>
- <code title="delete /v3/sender-profiles/{id}">client.sender_profiles.<a href="./src/sent_dm/resources/sender_profiles.py">delete</a>(id) -> None</code>

# Numbers

Types:

```python
from sent_dm.types import APIResponseOfNumberLookupResult, NumberLookupResult
```

Methods:

- <code title="get /v3/numbers/lookup/{phoneNumber}">client.numbers.<a href="./src/sent_dm/resources/numbers.py">lookup</a>(phone_number) -> <a href="./src/sent_dm/types/api_response_of_number_lookup_result.py">APIResponseOfNumberLookupResult</a></code>

# Messages

Types:

```python
from sent_dm.types import (
    APIResponseOfCancelledMessage,
    APIResponseOfMessage,
    APIResponseOfMessageActivities,
    CancelledMessage,
    Message,
    MessageActivities,
    MessageActivity,
    MessageBody,
    MessageButton,
    MessageChannelOptions,
    MessageHeaderMedia,
    MessageMedia,
    MessageRecipient,
    MessageSendResponse,
    MessageSendResult,
    MessageStatusEvent,
)
```

Methods:

- <code title="post /v3/messages/{id}/cancel">client.messages.<a href="./src/sent_dm/resources/messages.py">cancel</a>(id, \*\*<a href="src/sent_dm/types/message_cancel_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_cancelled_message.py">APIResponseOfCancelledMessage</a></code>
- <code title="post /v3/messages/{id}/resend">client.messages.<a href="./src/sent_dm/resources/messages.py">resend</a>(id, \*\*<a href="src/sent_dm/types/message_resend_params.py">params</a>) -> <a href="./src/sent_dm/types/message_send_response.py">MessageSendResponse</a></code>
- <code title="get /v3/messages/{id}/activities">client.messages.<a href="./src/sent_dm/resources/messages.py">retrieve_activities</a>(id) -> <a href="./src/sent_dm/types/api_response_of_message_activities.py">APIResponseOfMessageActivities</a></code>
- <code title="get /v3/messages/{id}">client.messages.<a href="./src/sent_dm/resources/messages.py">retrieve_status</a>(id) -> <a href="./src/sent_dm/types/api_response_of_message.py">APIResponseOfMessage</a></code>
- <code title="post /v3/messages">client.messages.<a href="./src/sent_dm/resources/messages.py">send</a>(\*\*<a href="src/sent_dm/types/message_send_params.py">params</a>) -> <a href="./src/sent_dm/types/message_send_response.py">MessageSendResponse</a></code>

# Contacts

Types:

```python
from sent_dm.types import (
    APIResponseOfContact,
    APIResponseOfContactMessageSummary,
    APIResponseOfContactsList,
    ChannelScore,
    ContactMessageSummary,
    ContactResponse,
    ContactsList,
)
```

Methods:

- <code title="post /v3/contacts">client.contacts.<a href="./src/sent_dm/resources/contacts.py">create</a>(\*\*<a href="src/sent_dm/types/contact_create_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_contact.py">APIResponseOfContact</a></code>
- <code title="get /v3/contacts/{id}">client.contacts.<a href="./src/sent_dm/resources/contacts.py">retrieve</a>(id) -> <a href="./src/sent_dm/types/api_response_of_contact.py">APIResponseOfContact</a></code>
- <code title="patch /v3/contacts/{id}">client.contacts.<a href="./src/sent_dm/resources/contacts.py">update</a>(id, \*\*<a href="src/sent_dm/types/contact_update_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_contact.py">APIResponseOfContact</a></code>
- <code title="get /v3/contacts">client.contacts.<a href="./src/sent_dm/resources/contacts.py">list</a>(\*\*<a href="src/sent_dm/types/contact_list_params.py">params</a>) -> <a href="./src/sent_dm/types/contact_response.py">SyncContactsPage[ContactResponse]</a></code>
- <code title="delete /v3/contacts/{id}">client.contacts.<a href="./src/sent_dm/resources/contacts.py">delete</a>(id, \*\*<a href="src/sent_dm/types/contact_delete_params.py">params</a>) -> None</code>
- <code title="get /v3/contacts/{contactId}/message-summary">client.contacts.<a href="./src/sent_dm/resources/contacts.py">retrieve_message_summary</a>(contact_id) -> <a href="./src/sent_dm/types/api_response_of_contact_message_summary.py">APIResponseOfContactMessageSummary</a></code>

# Conversations

Types:

```python
from sent_dm.types import APIResponseOfConversationMessagesList, ConversationMessagesList
```

Methods:

- <code title="get /v3/conversations">client.conversations.<a href="./src/sent_dm/resources/conversations.py">list</a>(\*\*<a href="src/sent_dm/types/conversation_list_params.py">params</a>) -> <a href="./src/sent_dm/types/message.py">SyncConversationsPage[Message]</a></code>
- <code title="get /v3/conversations/{id}">client.conversations.<a href="./src/sent_dm/resources/conversations.py">list_messages</a>(id, \*\*<a href="src/sent_dm/types/conversation_list_messages_params.py">params</a>) -> <a href="./src/sent_dm/types/message.py">SyncConversationsPage[Message]</a></code>

# Voice

## Calls

Types:

```python
from sent_dm.types.voice import (
    APIResponseOfCall,
    APIResponseOfCallRecordings,
    APIResponseOfCallsList,
    Call,
    CallLeg,
    CallParty,
    CallRecording,
    CallRecordings,
    CallTimelineEntry,
    CallsList,
)
```

Methods:

- <code title="get /v3/voice/calls/{id}">client.voice.calls.<a href="./src/sent_dm/resources/voice/calls/calls.py">retrieve</a>(id) -> <a href="./src/sent_dm/types/voice/api_response_of_call.py">APIResponseOfCall</a></code>
- <code title="get /v3/voice/calls">client.voice.calls.<a href="./src/sent_dm/resources/voice/calls/calls.py">list</a>(\*\*<a href="src/sent_dm/types/voice/call_list_params.py">params</a>) -> <a href="./src/sent_dm/types/voice/call.py">SyncCallsPage[Call]</a></code>
- <code title="post /v3/voice/calls/{id}/hangup">client.voice.calls.<a href="./src/sent_dm/resources/voice/calls/calls.py">hangup</a>(id, \*\*<a href="src/sent_dm/types/voice/call_hangup_params.py">params</a>) -> None</code>
- <code title="get /v3/voice/calls/{id}/recordings">client.voice.calls.<a href="./src/sent_dm/resources/voice/calls/calls.py">list_recordings</a>(id) -> <a href="./src/sent_dm/types/voice/api_response_of_call_recordings.py">APIResponseOfCallRecordings</a></code>
- <code title="post /v3/voice/calls/{id}/recordings">client.voice.calls.<a href="./src/sent_dm/resources/voice/calls/calls.py">record</a>(id, \*\*<a href="src/sent_dm/types/voice/call_record_params.py">params</a>) -> None</code>

### Participants

Types:

```python
from sent_dm.types.voice.calls import (
    APIResponseOfListOfCallParticipant,
    CallParticipant,
    CallParticipantTarget,
)
```

Methods:

- <code title="patch /v3/voice/calls/{id}/participants/{participantId}">client.voice.calls.participants.<a href="./src/sent_dm/resources/voice/calls/participants.py">update</a>(participant_id, \*, id, \*\*<a href="src/sent_dm/types/voice/calls/participant_update_params.py">params</a>) -> None</code>
- <code title="get /v3/voice/calls/{id}/participants">client.voice.calls.participants.<a href="./src/sent_dm/resources/voice/calls/participants.py">list</a>(id) -> <a href="./src/sent_dm/types/voice/calls/api_response_of_list_of_call_participant.py">APIResponseOfListOfCallParticipant</a></code>
- <code title="post /v3/voice/calls/{id}/participants">client.voice.calls.participants.<a href="./src/sent_dm/resources/voice/calls/participants.py">add</a>(id, \*\*<a href="src/sent_dm/types/voice/calls/participant_add_params.py">params</a>) -> <a href="./src/sent_dm/types/voice/api_response_of_call.py">APIResponseOfCall</a></code>
- <code title="delete /v3/voice/calls/{id}/participants/{participantId}">client.voice.calls.participants.<a href="./src/sent_dm/resources/voice/calls/participants.py">remove</a>(participant_id, \*, id, \*\*<a href="src/sent_dm/types/voice/calls/participant_remove_params.py">params</a>) -> None</code>
- <code title="delete /v3/voice/calls/{id}/participants">client.voice.calls.participants.<a href="./src/sent_dm/resources/voice/calls/participants.py">remove_all</a>(id, \*\*<a href="src/sent_dm/types/voice/calls/participant_remove_all_params.py">params</a>) -> None</code>

## Tokens

Types:

```python
from sent_dm.types.voice import APIResponseOfVoiceToken, VoiceToken
```

Methods:

- <code title="post /v3/voice/tokens">client.voice.tokens.<a href="./src/sent_dm/resources/voice/tokens.py">create</a>(\*\*<a href="src/sent_dm/types/voice/token_create_params.py">params</a>) -> <a href="./src/sent_dm/types/voice/api_response_of_voice_token.py">APIResponseOfVoiceToken</a></code>

## Agents

Types:

```python
from sent_dm.types.voice import (
    APIResponseOfVoiceAgent,
    APIResponseOfVoiceAgentSecret,
    APIResponseOfVoiceAgentsList,
    VoiceAgent,
    VoiceAgentAudio,
    VoiceAgentAudioSpec,
    VoiceAgentLimits,
    VoiceAgentLimitsSpec,
    VoiceAgentParty,
    VoiceAgentPartySpec,
    VoiceAgentSecret,
    VoiceAgentSpeech,
    VoiceAgentSpeechSpec,
    VoiceAgentTranscripts,
    VoiceAgentTranscriptsSpec,
    VoiceAgentsList,
)
```

Methods:

- <code title="post /v3/voice/agents">client.voice.agents.<a href="./src/sent_dm/resources/voice/agents.py">create</a>(\*\*<a href="src/sent_dm/types/voice/agent_create_params.py">params</a>) -> <a href="./src/sent_dm/types/voice/api_response_of_voice_agent.py">APIResponseOfVoiceAgent</a></code>
- <code title="get /v3/voice/agents/{id}">client.voice.agents.<a href="./src/sent_dm/resources/voice/agents.py">retrieve</a>(id) -> <a href="./src/sent_dm/types/voice/api_response_of_voice_agent.py">APIResponseOfVoiceAgent</a></code>
- <code title="patch /v3/voice/agents/{id}">client.voice.agents.<a href="./src/sent_dm/resources/voice/agents.py">update</a>(id, \*\*<a href="src/sent_dm/types/voice/agent_update_params.py">params</a>) -> <a href="./src/sent_dm/types/voice/api_response_of_voice_agent.py">APIResponseOfVoiceAgent</a></code>
- <code title="get /v3/voice/agents">client.voice.agents.<a href="./src/sent_dm/resources/voice/agents.py">list</a>(\*\*<a href="src/sent_dm/types/voice/agent_list_params.py">params</a>) -> <a href="./src/sent_dm/types/voice/voice_agent.py">SyncVoiceAgentsPage[VoiceAgent]</a></code>
- <code title="delete /v3/voice/agents/{id}">client.voice.agents.<a href="./src/sent_dm/resources/voice/agents.py">delete</a>(id, \*\*<a href="src/sent_dm/types/voice/agent_delete_params.py">params</a>) -> None</code>
- <code title="post /v3/voice/agents/{id}/rotate-secret">client.voice.agents.<a href="./src/sent_dm/resources/voice/agents.py">rotate_secret</a>(id, \*\*<a href="src/sent_dm/types/voice/agent_rotate_secret_params.py">params</a>) -> <a href="./src/sent_dm/types/voice/api_response_of_voice_agent_secret.py">APIResponseOfVoiceAgentSecret</a></code>

## Catalogue

Types:

```python
from sent_dm.types.voice import APIResponseOfVoiceCatalogue, VoiceCatalogue, VoiceCatalogueVoice
```

Methods:

- <code title="get /v3/voice/voices">client.voice.catalogue.<a href="./src/sent_dm/resources/voice/catalogue.py">list</a>() -> <a href="./src/sent_dm/types/voice/api_response_of_voice_catalogue.py">APIResponseOfVoiceCatalogue</a></code>

# Channels

Types:

```python
from sent_dm.types import APIResponseOfChannelsState, ChannelsState, MmsMarket
```

Methods:

- <code title="get /v3/channels">client.channels.<a href="./src/sent_dm/resources/channels/channels.py">list</a>() -> <a href="./src/sent_dm/types/api_response_of_channels_state.py">APIResponseOfChannelsState</a></code>

## SMS

Types:

```python
from sent_dm.types.channels import (
    APIResponseOfListOfSMSMarket,
    APIResponseOfSMSMarket,
    MarketCompliance,
    SMSMarket,
    SMSNumber,
    SMSNumberRequest,
    SuppliedCampaign,
    SuppliedCompliance,
    SuppliedDocument,
)
```

Methods:

- <code title="post /v3/channels/sms">client.channels.sms.<a href="./src/sent_dm/resources/channels/sms/sms.py">create</a>(\*\*<a href="src/sent_dm/types/channels/sms_create_params.py">params</a>) -> <a href="./src/sent_dm/types/channels/api_response_of_sms_market.py">APIResponseOfSMSMarket</a></code>
- <code title="get /v3/channels/sms/{country}/{type}">client.channels.sms.<a href="./src/sent_dm/resources/channels/sms/sms.py">retrieve</a>(type, \*, country) -> <a href="./src/sent_dm/types/channels/api_response_of_sms_market.py">APIResponseOfSMSMarket</a></code>
- <code title="patch /v3/channels/sms/{country}/{type}">client.channels.sms.<a href="./src/sent_dm/resources/channels/sms/sms.py">update</a>(type, \*, country, \*\*<a href="src/sent_dm/types/channels/sms_update_params.py">params</a>) -> <a href="./src/sent_dm/types/channels/api_response_of_sms_market.py">APIResponseOfSMSMarket</a></code>
- <code title="get /v3/channels/sms">client.channels.sms.<a href="./src/sent_dm/resources/channels/sms/sms.py">list</a>() -> <a href="./src/sent_dm/types/channels/api_response_of_list_of_sms_market.py">APIResponseOfListOfSMSMarket</a></code>

### TenDlc

Types:

```python
from sent_dm.types.channels.sms import APIResponseOfSuppliedCompliance
```

Methods:

- <code title="post /v3/channels/sms/compliances/US/TEN_DLC/campaigns">client.channels.sms.ten_dlc.<a href="./src/sent_dm/resources/channels/sms/ten_dlc.py">add_campaign</a>(\*\*<a href="src/sent_dm/types/channels/sms/ten_dlc_add_campaign_params.py">params</a>) -> <a href="./src/sent_dm/types/channels/api_response_of_sms_market.py">APIResponseOfSMSMarket</a></code>
- <code title="post /v3/channels/sms/numbers/US/TEN_DLC">client.channels.sms.ten_dlc.<a href="./src/sent_dm/resources/channels/sms/ten_dlc.py">add_numbers</a>(\*\*<a href="src/sent_dm/types/channels/sms/ten_dlc_add_numbers_params.py">params</a>) -> <a href="./src/sent_dm/types/channels/api_response_of_sms_market.py">APIResponseOfSMSMarket</a></code>
- <code title="get /v3/channels/sms/compliances/US/TEN_DLC">client.channels.sms.ten_dlc.<a href="./src/sent_dm/resources/channels/sms/ten_dlc.py">retrieve_compliance</a>() -> <a href="./src/sent_dm/types/channels/sms/api_response_of_supplied_compliance.py">APIResponseOfSuppliedCompliance</a></code>
- <code title="patch /v3/channels/sms/compliances/US/TEN_DLC/campaigns/{campaignId}">client.channels.sms.ten_dlc.<a href="./src/sent_dm/resources/channels/sms/ten_dlc.py">update_campaign</a>(campaign_id, \*\*<a href="src/sent_dm/types/channels/sms/ten_dlc_update_campaign_params.py">params</a>) -> <a href="./src/sent_dm/types/channels/api_response_of_sms_market.py">APIResponseOfSMSMarket</a></code>

## Rcs

Types:

```python
from sent_dm.types.channels import APIResponseOfRcsAgent, RcsAddress, RcsAgent
```

Methods:

- <code title="post /v3/channels/rcs">client.channels.rcs.<a href="./src/sent_dm/resources/channels/rcs.py">create</a>(\*\*<a href="src/sent_dm/types/channels/rc_create_params.py">params</a>) -> <a href="./src/sent_dm/types/channels/api_response_of_rcs_agent.py">APIResponseOfRcsAgent</a></code>

## Whatsapp

Types:

```python
from sent_dm.types.channels import APIResponseOfWhatsappChannel, WhatsappChannel
```

Methods:

- <code title="post /v3/channels/whatsapp">client.channels.whatsapp.<a href="./src/sent_dm/resources/channels/whatsapp.py">create</a>(\*\*<a href="src/sent_dm/types/channels/whatsapp_create_params.py">params</a>) -> <a href="./src/sent_dm/types/channels/api_response_of_whatsapp_channel.py">APIResponseOfWhatsappChannel</a></code>

## Voice

Types:

```python
from sent_dm.types.channels import (
    APIResponseOfListOfVoiceNumber,
    APIResponseOfVoiceCallbackTest,
    APIResponseOfVoiceNumber,
    APIResponseOfVoiceNumberCreated,
    APIResponseOfVoiceSecret,
    VoiceCallbackTest,
    VoiceCallbackTestErrorInfo,
    VoiceCallbackTestRequestInfo,
    VoiceCallbackTestResponseInfo,
    VoiceNumber,
    VoiceNumberCreated,
    VoiceSecret,
)
```

Methods:

- <code title="post /v3/channels/voice">client.channels.voice.<a href="./src/sent_dm/resources/channels/voice.py">create</a>(\*\*<a href="src/sent_dm/types/channels/voice_create_params.py">params</a>) -> <a href="./src/sent_dm/types/channels/api_response_of_voice_number_created.py">APIResponseOfVoiceNumberCreated</a></code>
- <code title="get /v3/channels/voice/{number}">client.channels.voice.<a href="./src/sent_dm/resources/channels/voice.py">retrieve</a>(number) -> <a href="./src/sent_dm/types/channels/api_response_of_voice_number.py">APIResponseOfVoiceNumber</a></code>
- <code title="patch /v3/channels/voice/{number}">client.channels.voice.<a href="./src/sent_dm/resources/channels/voice.py">update</a>(number, \*\*<a href="src/sent_dm/types/channels/voice_update_params.py">params</a>) -> <a href="./src/sent_dm/types/channels/api_response_of_voice_number.py">APIResponseOfVoiceNumber</a></code>
- <code title="get /v3/channels/voice">client.channels.voice.<a href="./src/sent_dm/resources/channels/voice.py">list</a>() -> <a href="./src/sent_dm/types/channels/api_response_of_list_of_voice_number.py">APIResponseOfListOfVoiceNumber</a></code>
- <code title="post /v3/channels/voice/{number}/rotate-secret">client.channels.voice.<a href="./src/sent_dm/resources/channels/voice.py">rotate_secret</a>(number, \*\*<a href="src/sent_dm/types/channels/voice_rotate_secret_params.py">params</a>) -> <a href="./src/sent_dm/types/channels/api_response_of_voice_secret.py">APIResponseOfVoiceSecret</a></code>
- <code title="post /v3/channels/voice/{number}/test">client.channels.voice.<a href="./src/sent_dm/resources/channels/voice.py">test</a>(number, \*\*<a href="src/sent_dm/types/channels/voice_test_params.py">params</a>) -> <a href="./src/sent_dm/types/channels/api_response_of_voice_callback_test.py">APIResponseOfVoiceCallbackTest</a></code>

# Compliance

Types:

```python
from sent_dm.types import (
    APIResponseOfComplianceRequirements,
    ComplianceAttachmentTemplate,
    ComplianceRequirement,
    ComplianceRequirements,
    ComplianceSetupStep,
)
```

Methods:

- <code title="get /v3/compliance/requirements">client.compliance.<a href="./src/sent_dm/resources/compliance.py">retrieve_requirements</a>(\*\*<a href="src/sent_dm/types/compliance_retrieve_requirements_params.py">params</a>) -> <a href="./src/sent_dm/types/api_response_of_compliance_requirements.py">APIResponseOfComplianceRequirements</a></code>

# Me

Types:

```python
from sent_dm.types import (
    Account,
    AccountChannels,
    AccountProfile,
    AccountRcsChannel,
    AccountSMSChannel,
    AccountWhatsappChannel,
    APIResponseOfAccount,
    ProfileSettings,
)
```

Methods:

- <code title="get /v3/me">client.me.<a href="./src/sent_dm/resources/me.py">retrieve</a>() -> <a href="./src/sent_dm/types/api_response_of_account.py">APIResponseOfAccount</a></code>
