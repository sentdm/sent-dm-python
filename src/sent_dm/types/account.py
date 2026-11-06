# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .account_profile import AccountProfile
from .account_channels import AccountChannels
from .profile_settings import ProfileSettings

__all__ = ["Account"]


class Account(BaseModel):
    """
    Account response for GET /v3/me endpoint.
    Returns organization (with profiles), user (standalone), or profile (child of an organization)
    data depending on the API key type. Always includes messaging channel configuration.
    """

    id: Optional[str] = None
    """Customer ID (organization, account, or profile)"""

    channels: Optional[AccountChannels] = None
    """Messaging channel configuration.

    All three channels are always present. Each channel has a "configured" flag;
    configured channels expose additional details.
    """

    created_at: Optional[datetime] = None
    """When the account was created"""

    description: Optional[str] = None
    """Account description"""

    email: Optional[str] = None
    """Contact email address"""

    enable_template_auto_creation_for_sp: Optional[bool] = None
    """
    Whether this account may mark a template for automatic creation on its sender
    profiles. Granted by Sent per account and off by default, so it is what a
    template-create form reads to decide whether to offer the option at all —
    marking a template without it does nothing.

    Top-level rather than inside settings, which is written for type: "profile" only
    and so would never carry it to the account type that can act on it.

    This is the capability, not the stored flag: a profile reports false whatever
    its own row holds. A sender profile owns no sender profiles, so a template it
    marked would have nothing to be created on and the fan-out would never read the
    flag. The admin GET /customers/{id} reports the stored value instead, because
    that is the one an operator granted.
    """

    icon: Optional[str] = None
    """Account icon URL"""

    name: Optional[str] = None
    """Account name"""

    organization_id: Optional[str] = None
    """Organization ID (only for profile type — the parent organization)"""

    profiles: Optional[List[AccountProfile]] = None
    """
    List of profiles (populated for organization type, empty for user and profile
    types)
    """

    sending_phone_number: Optional[str] = None
    """The SMS sender this account sends from in the United States, in E.164 form.

    Null when the account has no US SMS sender.

    The same value as channels.sms.phone_number, published under both names on
    purpose: sending_phone_number is what this value is already called on GET
    /v3/profiles, so the same key answers the same question whichever of the two
    endpoints you ask. Neither name is preferred over the other and neither is
    deprecated.

    The same value, not the same presence: this key is always written, including as
    null, whereas channels.sms.phone_number is left out entirely when there is no
    sender.
    """

    sending_phone_number_profile_id: Optional[str] = None
    """
    The account that holds sending_phone_number in number inventory: normally this
    account itself, and a different account when the number is held elsewhere. Null
    when there is no US sender, or when the sender is not a number drawn from
    inventory — an alphanumeric sender ID or a short code.
    """

    settings: Optional[ProfileSettings] = None
    """Profile configuration settings"""

    short_name: Optional[str] = None
    """Short name / abbreviation (only for profile type)"""

    status: Optional[str] = None
    """
    Profile status (only for profile type): incomplete, pending_review, approved,
    etc.
    """

    type: Optional[str] = None
    """
    Account type: "organization" (has profiles), "user" (no profiles), or "profile"
    (child of an organization)
    """
