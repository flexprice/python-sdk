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
from flexprice_client.models.dto_price_response import DtoPriceResponse
from flexprice_client.models.types_status import TypesStatus
from typing import Optional, Set
from typing_extensions import Self

class DtoPlanResponse(BaseModel):
    """
    DtoPlanResponse
    """ # noqa: E501
    created_at: Optional[StrictStr] = None
    created_by: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    entitlements: Optional[List[DtoEntitlementResponse]] = None
    environment_id: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    lookup_key: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    prices: Optional[List[DtoPriceResponse]] = None
    status: Optional[TypesStatus] = None
    tenant_id: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    updated_by: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["created_at", "created_by", "description", "entitlements", "environment_id", "id", "lookup_key", "name", "prices", "status", "tenant_id", "updated_at", "updated_by"]

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
        """Create an instance of DtoPlanResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in entitlements (list)
        _items = []
        if self.entitlements:
            for _item_entitlements in self.entitlements:
                if _item_entitlements:
                    _items.append(_item_entitlements.to_dict())
            _dict['entitlements'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in prices (list)
        _items = []
        if self.prices:
            for _item_prices in self.prices:
                if _item_prices:
                    _items.append(_item_prices.to_dict())
            _dict['prices'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DtoPlanResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "created_by": obj.get("created_by"),
            "description": obj.get("description"),
            "entitlements": [DtoEntitlementResponse.from_dict(_item) for _item in obj["entitlements"]] if obj.get("entitlements") is not None else None,
            "environment_id": obj.get("environment_id"),
            "id": obj.get("id"),
            "lookup_key": obj.get("lookup_key"),
            "name": obj.get("name"),
            "prices": [DtoPriceResponse.from_dict(_item) for _item in obj["prices"]] if obj.get("prices") is not None else None,
            "status": obj.get("status"),
            "tenant_id": obj.get("tenant_id"),
            "updated_at": obj.get("updated_at"),
            "updated_by": obj.get("updated_by")
        })
        return _obj

from flexprice_client.models.dto_entitlement_response import DtoEntitlementResponse
# TODO: Rewrite to not use raise_errors
DtoPlanResponse.model_rebuild(raise_errors=False)

