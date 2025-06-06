# coding: utf-8

"""
    FlexPrice API

    FlexPrice API Service

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from flexprice.models.types_secret_provider import TypesSecretProvider
from flexprice.models.types_secret_type import TypesSecretType
from flexprice.models.types_status import TypesStatus
from typing import Optional, Set
from typing_extensions import Self

class DtoSecretResponse(BaseModel):
    """
    DtoSecretResponse
    """ # noqa: E501
    created_at: Optional[StrictStr] = None
    display_id: Optional[StrictStr] = None
    expires_at: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    last_used_at: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    permissions: Optional[List[StrictStr]] = None
    provider: Optional[TypesSecretProvider] = None
    status: Optional[TypesStatus] = None
    type: Optional[TypesSecretType] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["created_at", "display_id", "expires_at", "id", "last_used_at", "name", "permissions", "provider", "status", "type", "updated_at"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DtoSecretResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DtoSecretResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "display_id": obj.get("display_id"),
            "expires_at": obj.get("expires_at"),
            "id": obj.get("id"),
            "last_used_at": obj.get("last_used_at"),
            "name": obj.get("name"),
            "permissions": obj.get("permissions"),
            "provider": obj.get("provider"),
            "status": obj.get("status"),
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


