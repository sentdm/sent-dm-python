# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .template_definition import TemplateDefinition

__all__ = ["TemplateResponse"]


class TemplateResponse(BaseModel):
    """
    Represents a message template with comprehensive metadata including definition structure
    """

    id: Optional[str] = None
    """The unique identifier of the template"""

    category: Optional[str] = None
    """The template category (e.g., MARKETING, UTILITY, AUTHENTICATION)"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time when the template was created"""

    definition: Optional[TemplateDefinition] = None
    """The complete template definition including header, body, footer, and buttons"""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """The display name of the template (auto-generated if not provided)"""

    is_published: Optional[bool] = FieldInfo(alias="isPublished", default=None)
    """Indicates whether the template is published and available for use"""

    language: Optional[str] = None
    """The template language code (e.g., en_US, es_ES)"""

    status: Optional[str] = None
    """The approval status of the template (e.g., APPROVED, PENDING, REJECTED, DRAFT)"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The date and time when the template was last updated"""

    whatsapp_template_id: Optional[str] = FieldInfo(alias="whatsappTemplateId", default=None)
    """The WhatsApp Business API template ID from Meta"""

    whatsapp_template_name: Optional[str] = FieldInfo(alias="whatsappTemplateName", default=None)
    """The WhatsApp template name as registered with Meta"""
