# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ComplianceRequirement"]


class ComplianceRequirement(BaseModel):
    """One value a market expects in a channel call's compliance map."""

    format: Optional[str] = None
    """Refinement of type where the market demands a specific shape, e.g.

    e164, url, email, iso3166_alpha2, csv_keywords.
    """

    item_fields: Optional[List["ComplianceRequirement"]] = None
    """
    Shape of each entry, when this requirement is a list of objects rather than of
    scalars.

    The compliance value stays null in the setup body like every other blank — a
    body that carries a half-filled object is one the endpoint refuses, which would
    break the promise that the published body can be sent as it stands. So the shape
    is described here instead, and each entry the caller composes has these keys.
    """

    key: Optional[str] = None
    """Key to use in the compliance map."""

    label: Optional[str] = None
    """Human label, suitable for a form field."""

    max_items: Optional[int] = None
    """Most entries this value accepts, where the market caps it."""

    min_length: Optional[int] = None
    """Shortest acceptable value, where the market sets one.

    TCR refuses a consent narrative under 40 characters, and finding that out at
    submission time is the round trip this exists to save.
    """

    notes: Optional[str] = None
    """Why the market asks for this."""

    options: Optional[List[str]] = None
    """Accepted values, when the type is an enum or a constrained array."""

    required: Optional[bool] = None
    """Whether the market always demands this value."""

    required_when: Optional[str] = None
    """
    Condition that makes this value required, when it is only required in some cases
    — e.g. brand.entity_type == PUBLIC_PROFIT. Evaluate it against your own payload
    to know whether to collect the field.
    """

    type: Optional[str] = None
    """Value type: string, number, boolean, date, enum, object, array or document."""
