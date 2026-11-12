# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .message_media import MessageMedia
from .message_button import MessageButton
from .message_header_media import MessageHeaderMedia

__all__ = ["MessageBody"]


class MessageBody(BaseModel):
    """
    Structured message body format for database storage.
    Preserves channel-specific components (header, header media, body, footer, buttons, MMS subject
    and media).

    Persisted as the messageBody jsonb column on Messages. Every write path goes
    through MessageUtils.MessageBodyJsonOptions, which writes nulls, so the envelope shape is
    stable regardless of channel or status. Anything that rebuilds this object field by field — the
    four IMessageBodyStrategy implementations and MessageUtils.BuildSegmentBody — has to
    carry every member, or that member is silently dropped on whichever path forgot it.
    """

    buttons: Optional[List[MessageButton]] = None

    content: Optional[str] = None

    footer: Optional[str] = None

    header: Optional[str] = None

    header_media: Optional[MessageHeaderMedia] = FieldInfo(alias="headerMedia", default=None)
    """The media asset that rode a message's header, recorded as sent."""

    media: Optional[List[MessageMedia]] = None
    """MMS attachments, as the publicly fetchable URLs handed to the carrier.

    Null on every other channel.

    Persisted rather than derived because a resend and a curfew release rebuild the
    send from the stored row — MessageReplayCommandBuilder reads templateId and
    templateVariables and nothing else — so media that lives only on the original
    request would silently turn a replayed MMS into a text message.
    """

    subject: Optional[str] = None
    """MMS subject line. Null on every other channel."""
