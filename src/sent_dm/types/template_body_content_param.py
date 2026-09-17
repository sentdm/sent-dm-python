# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .template_variable_param import TemplateVariableParam

__all__ = ["TemplateBodyContentParam"]


class TemplateBodyContentParam(TypedDict, total=False):
    template: Required[str]
    """The body copy, with variables written as {{index:variable}}.

    Length cap depends on which channel this body belongs to:
    TemplateContentLimits.MaxBodyLength (1024) for multiChannel, sms and whatsapp —
    Meta's BODY limit, which a multiChannel body may be delivered under — and
    TemplateContentLimits.MaxRcsBodyLength (3072) for an rcs body, which never
    reaches Meta. The maxLength advertised on this schema is the 1024 one, because
    all four channel bodies share this single schema — an rcs body between the two
    is accepted.

    Meta requires every variable to carry surrounding context, so a body is refused
    unless it also satisfies all of the following (enforced by
    TemplateDefinitionValidator): At least one letter before the first variable and
    after the last — trailing punctuation such as "... {{1:variable}}." does not
    count. At least (2 × variable count) + 1 words once the placeholders are
    removed. No two variables adjacent with only whitespace between them. No leading
    or trailing newline, no more than two consecutive line breaks, and no more than
    four consecutive spaces.

    Example: "Hello {{0:variable}}! Welcome to {{1:variable}}. We are glad to have
    you on board." — two variables, so at least five words are required, and the
    copy after the final variable contains letters.
    """

    type: Optional[str]
    """The type of body content — send "text".

    It is dropped from the stored definition when null, so a body posted without it
    is saved with no type key at all and the template editor has nothing to render
    the block from.
    """

    variables: Optional[Iterable[TemplateVariableParam]]
    """
    The variables referenced by the body copy, one entry per {{index:variable}}
    placeholder.
    """
