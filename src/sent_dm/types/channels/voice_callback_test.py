# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .voice_callback_test_error_info import VoiceCallbackTestErrorInfo
from .voice_callback_test_request_info import VoiceCallbackTestRequestInfo
from .voice_callback_test_response_info import VoiceCallbackTestResponseInfo

__all__ = ["VoiceCallbackTest"]


class VoiceCallbackTest(BaseModel):
    """The verdict of a test question sent to your callback URL"""

    answer: Optional[object] = None
    """
    Your answer as Sent read it, with numbers in E.164 and a missing caller id
    filled in. Set only when the outcome is ok.
    """

    call_id: Optional[str] = None
    """The call id the test question carried.

    It does not exist anywhere else and cannot be looked up.
    """

    error: Optional[VoiceCallbackTestErrorInfo] = None
    """Why the test did not end with ok"""

    outcome: Optional[str] = None
    """What happened: ok, timeout, connection_failed, http_error or invalid_answer"""

    request: Optional[VoiceCallbackTestRequestInfo] = None
    """The test question exactly as it was sent"""

    response: Optional[VoiceCallbackTestResponseInfo] = None
    """What your endpoint answered"""
