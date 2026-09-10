# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional, cast
from typing_extensions import override

from ._models import BaseModel, GenericModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "ContactsPageData",
    "ContactsPagePagination",
    "SyncContactsPage",
    "AsyncContactsPage",
    "ConversationsPageData",
    "ConversationsPagePagination",
    "SyncConversationsPage",
    "AsyncConversationsPage",
    "TemplatesPageData",
    "TemplatesPagePagination",
    "SyncTemplatesPage",
    "AsyncTemplatesPage",
    "WebhooksPageData",
    "WebhooksPagePagination",
    "SyncWebhooksPage",
    "AsyncWebhooksPage",
    "WebhookEventsPageData",
    "WebhookEventsPagePagination",
    "SyncWebhookEventsPage",
    "AsyncWebhookEventsPage",
]

_T = TypeVar("_T")


class ContactsPagePagination(BaseModel):
    has_more: Optional[bool] = None


class ContactsPageData(GenericModel, Generic[_T]):
    contacts: Optional[List[_T]] = None

    pagination: Optional[ContactsPagePagination] = None


class SyncContactsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[ContactsPageData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        contacts = None
        if self.data is not None:
            if self.data.contacts is not None:
                contacts = self.data.contacts
        if not contacts:
            return []
        return contacts

    @override
    def has_next_page(self) -> bool:
        has_more = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.has_more is not None:
                    has_more = self.data.pagination.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class AsyncContactsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[ContactsPageData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        contacts = None
        if self.data is not None:
            if self.data.contacts is not None:
                contacts = self.data.contacts
        if not contacts:
            return []
        return contacts

    @override
    def has_next_page(self) -> bool:
        has_more = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.has_more is not None:
                    has_more = self.data.pagination.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class ConversationsPagePagination(BaseModel):
    has_more: Optional[bool] = None


class ConversationsPageData(GenericModel, Generic[_T]):
    messages: Optional[List[_T]] = None

    pagination: Optional[ConversationsPagePagination] = None


class SyncConversationsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[ConversationsPageData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        messages = None
        if self.data is not None:
            if self.data.messages is not None:
                messages = self.data.messages
        if not messages:
            return []
        return messages

    @override
    def has_next_page(self) -> bool:
        has_more = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.has_more is not None:
                    has_more = self.data.pagination.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class AsyncConversationsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[ConversationsPageData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        messages = None
        if self.data is not None:
            if self.data.messages is not None:
                messages = self.data.messages
        if not messages:
            return []
        return messages

    @override
    def has_next_page(self) -> bool:
        has_more = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.has_more is not None:
                    has_more = self.data.pagination.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class TemplatesPagePagination(BaseModel):
    has_more: Optional[bool] = None


class TemplatesPageData(GenericModel, Generic[_T]):
    pagination: Optional[TemplatesPagePagination] = None

    templates: Optional[List[_T]] = None


class SyncTemplatesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[TemplatesPageData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        templates = None
        if self.data is not None:
            if self.data.templates is not None:
                templates = self.data.templates
        if not templates:
            return []
        return templates

    @override
    def has_next_page(self) -> bool:
        has_more = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.has_more is not None:
                    has_more = self.data.pagination.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class AsyncTemplatesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[TemplatesPageData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        templates = None
        if self.data is not None:
            if self.data.templates is not None:
                templates = self.data.templates
        if not templates:
            return []
        return templates

    @override
    def has_next_page(self) -> bool:
        has_more = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.has_more is not None:
                    has_more = self.data.pagination.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class WebhooksPagePagination(BaseModel):
    has_more: Optional[bool] = None


class WebhooksPageData(GenericModel, Generic[_T]):
    pagination: Optional[WebhooksPagePagination] = None

    webhooks: Optional[List[_T]] = None


class SyncWebhooksPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[WebhooksPageData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        webhooks = None
        if self.data is not None:
            if self.data.webhooks is not None:
                webhooks = self.data.webhooks
        if not webhooks:
            return []
        return webhooks

    @override
    def has_next_page(self) -> bool:
        has_more = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.has_more is not None:
                    has_more = self.data.pagination.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class AsyncWebhooksPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[WebhooksPageData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        webhooks = None
        if self.data is not None:
            if self.data.webhooks is not None:
                webhooks = self.data.webhooks
        if not webhooks:
            return []
        return webhooks

    @override
    def has_next_page(self) -> bool:
        has_more = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.has_more is not None:
                    has_more = self.data.pagination.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class WebhookEventsPagePagination(BaseModel):
    has_more: Optional[bool] = None


class WebhookEventsPageData(GenericModel, Generic[_T]):
    events: Optional[List[_T]] = None

    pagination: Optional[WebhookEventsPagePagination] = None


class SyncWebhookEventsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[WebhookEventsPageData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        events = None
        if self.data is not None:
            if self.data.events is not None:
                events = self.data.events
        if not events:
            return []
        return events

    @override
    def has_next_page(self) -> bool:
        has_more = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.has_more is not None:
                    has_more = self.data.pagination.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})


class AsyncWebhookEventsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: Optional[WebhookEventsPageData[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        events = None
        if self.data is not None:
            if self.data.events is not None:
                events = self.data.events
        if not events:
            return []
        return events

    @override
    def has_next_page(self) -> bool:
        has_more = None
        if self.data is not None:
            if self.data.pagination is not None:
                if self.data.pagination.has_more is not None:
                    has_more = self.data.pagination.has_more
        if has_more is not None and has_more is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        return PageInfo(params={"page": last_page + 1})
