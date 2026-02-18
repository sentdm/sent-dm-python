# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .mutation_request_param import MutationRequestParam

__all__ = ["BrandDeleteParams", "Body"]


class BrandDeleteParams(TypedDict, total=False):
    body: Required[Body]
    """Request to delete a brand"""


class Body(MutationRequestParam, total=False):
    """Request to delete a brand"""

    pass
