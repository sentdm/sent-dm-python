# Contacts

Types:

```python
from sent_dm.types import ContactListItem, ContactListResponse
```

Methods:

- <code title="get /v2/contacts">client.contacts.<a href="./src/sent_dm/resources/contacts.py">list</a>(\*\*<a href="src/sent_dm/types/contact_list_params.py">params</a>) -> <a href="./src/sent_dm/types/contact_list_response.py">ContactListResponse</a></code>
- <code title="get /v2/contacts/phone">client.contacts.<a href="./src/sent_dm/resources/contacts.py">retrieve_by_phone</a>(\*\*<a href="src/sent_dm/types/contact_retrieve_by_phone_params.py">params</a>) -> <a href="./src/sent_dm/types/contact_list_item.py">ContactListItem</a></code>
- <code title="get /v2/contacts/id">client.contacts.<a href="./src/sent_dm/resources/contacts.py">retrieve_id</a>(\*\*<a href="src/sent_dm/types/contact_retrieve_id_params.py">params</a>) -> <a href="./src/sent_dm/types/contact_list_item.py">ContactListItem</a></code>

# Messages

Types:

```python
from sent_dm.types import MessageRetrieveResponse
```

Methods:

- <code title="get /v2/messages/{id}">client.messages.<a href="./src/sent_dm/resources/messages.py">retrieve</a>(id) -> <a href="./src/sent_dm/types/message_retrieve_response.py">MessageRetrieveResponse</a></code>
- <code title="post /v2/messages/quick-message">client.messages.<a href="./src/sent_dm/resources/messages.py">send_quick_message</a>(\*\*<a href="src/sent_dm/types/message_send_quick_message_params.py">params</a>) -> None</code>
- <code title="post /v2/messages/contact">client.messages.<a href="./src/sent_dm/resources/messages.py">send_to_contact</a>(\*\*<a href="src/sent_dm/types/message_send_to_contact_params.py">params</a>) -> None</code>
- <code title="post /v2/messages/phone">client.messages.<a href="./src/sent_dm/resources/messages.py">send_to_phone</a>(\*\*<a href="src/sent_dm/types/message_send_to_phone_params.py">params</a>) -> None</code>

# Templates

Types:

```python
from sent_dm.types import (
    TemplateBodyContent,
    TemplateDefinition,
    TemplateResponseV2,
    TemplateVariable,
    TemplateListResponse,
)
```

Methods:

- <code title="post /v2/templates">client.templates.<a href="./src/sent_dm/resources/templates.py">create</a>(\*\*<a href="src/sent_dm/types/template_create_params.py">params</a>) -> <a href="./src/sent_dm/types/template_response_v2.py">TemplateResponseV2</a></code>
- <code title="get /v2/templates/{id}">client.templates.<a href="./src/sent_dm/resources/templates.py">retrieve</a>(id) -> <a href="./src/sent_dm/types/template_response_v2.py">TemplateResponseV2</a></code>
- <code title="get /v2/templates">client.templates.<a href="./src/sent_dm/resources/templates.py">list</a>(\*\*<a href="src/sent_dm/types/template_list_params.py">params</a>) -> <a href="./src/sent_dm/types/template_list_response.py">TemplateListResponse</a></code>
- <code title="delete /v2/templates/{id}">client.templates.<a href="./src/sent_dm/resources/templates.py">delete</a>(id) -> None</code>

# NumberLookup

Types:

```python
from sent_dm.types import NumberLookupRetrieveResponse
```

Methods:

- <code title="get /v2/number-lookup">client.number_lookup.<a href="./src/sent_dm/resources/number_lookup.py">retrieve</a>(\*\*<a href="src/sent_dm/types/number_lookup_retrieve_params.py">params</a>) -> <a href="./src/sent_dm/types/number_lookup_retrieve_response.py">NumberLookupRetrieveResponse</a></code>
