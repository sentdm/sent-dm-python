# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CallRecording"]


class CallRecording(BaseModel):
    """A short-lived link to a call recording"""

    download_url: Optional[str] = None
    """A pre-signed link that downloads the recording as an MP3 file.

    Anyone holding it can download the recording until it expires
    """

    recording_id: Optional[str] = None
    """The recording's id, the one the call.recording_ready webhook announced it under"""

    url_expires_at: Optional[datetime] = None
    """When the link stops working (UTC).

    Request the recordings again for a fresh link
    """
