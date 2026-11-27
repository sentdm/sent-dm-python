# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AgentEventPayload"]


class AgentEventPayload(BaseModel):
    """Body of an agent.* webhook (Sent Agents).

    The event is the agent service's own record,
    forwarded without renaming: EventId is its id, so a subscriber can dedupe a redelivery.
    """

    event_id: str
    """The agent service's event id. The same event is never delivered under two ids."""

    occurred_at: str
    """When the agent service recorded it, UTC, to the millisecond."""

    account_id: Optional[str] = None
    """The sender profile the agent runs on."""

    actor: Optional[str] = None
    """Who caused it: system, the agent service's customer, or an approver."""

    agent_id: Optional[str] = None
    """The agent."""

    agent_name: Optional[str] = None
    """The agent's name, as it is listed.

    Absent for an agent services no longer holds.
    """

    agent_version: Optional[int] = None
    """
    The version of the agent the event is of: the one its conversation runs, or the
    active one for an event of the agent itself. Absent when the agent service does
    not say it.
    """

    contact_id: Optional[str] = None
    """The contact of that conversation; absent on agent-level events."""

    contact_phone_number: Optional[str] = None
    """
    The contact's phone number, in E.164, so a receiver knows who the event is about
    without asking for the contact. Read from the account's contacts as the webhook
    is built: the agent service's own record names a contact by id only. Absent on
    agent-level events, and for a contact the account no longer holds.
    """

    data: Optional[object] = None
    """
    The event's own fields (outcome, reason, ...), exactly as the agent service
    recorded them.
    """

    instance_id: Optional[str] = None
    """
    The conversation (agent × contact) the event belongs to; absent on agent-level
    events.
    """

    sequence: Optional[int] = None
    """
    Where the event stands among the agent's events: a number that grows with each,
    so two events of the same second are put in order by it. Not a count: there are
    gaps between an agent's own. Absent from an agent service that does not say it.
    """
