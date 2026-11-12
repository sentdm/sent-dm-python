# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .message_recipient import MessageRecipient

__all__ = ["MessageSendResult"]


class MessageSendResult(BaseModel):
    """
    The result of a multi-recipient send.

    Declared here rather than in the service layer. POST /v3/messages used to publish
    MessageSendResult — a type in Common.Services.Messaging.Contracts — so the public contract was
    whatever the send service happened to return, and changing that service for an internal reason changed the
    API. The service keeps its result; this is what a caller sees, and the mapping between them is a decision the
    endpoint makes.

    The shape of an immediate send: it never has a scheduled_at key. A send that carried
    scheduled_at is a ScheduledSendMessageResponse, and the endpoint decides which of the two to
    answer with. From always returns this type.
    """

    recipients: Optional[List[MessageRecipient]] = None

    status: Optional[str] = None
    """QUEUED: the batch is accepted.

    A request that carried scheduled_at is QUEUED here too; each message moves to
    SCHEDULED once it is held, as GET /v3/messages/{id} and the message.scheduled
    webhook report.
    """

    template_id: Optional[str] = None

    template_name: Optional[str] = None
