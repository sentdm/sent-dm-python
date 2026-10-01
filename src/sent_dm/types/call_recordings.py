# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .call_recording import CallRecording

__all__ = ["CallRecordings"]


class CallRecordings(BaseModel):
    """The recordings of a call, each as a short-lived download link"""

    recordings: Optional[List[CallRecording]] = None
    """Every recording of the call, oldest first.

    Empty until the first call.recording_ready webhook has been sent, and for a call
    that was never recorded
    """
