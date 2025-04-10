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
from flexprice.models.meter_aggregation import MeterAggregation
from flexprice.models.meter_filter import MeterFilter
from flexprice.models.types_reset_usage import TypesResetUsage
from typing import Optional, Set
from typing_extensions import Self

class DtoMeterResponse(BaseModel):
    """
    DtoMeterResponse
    """ # noqa: E501
    aggregation: Optional[MeterAggregation] = None
    created_at: Optional[StrictStr] = None
    event_name: Optional[StrictStr] = None
    filters: Optional[List[MeterFilter]] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    reset_usage: Optional[TypesResetUsage] = None
    status: Optional[StrictStr] = None
    tenant_id: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["aggregation", "created_at", "event_name", "filters", "id", "name", "reset_usage", "status", "tenant_id", "updated_at"]

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
        """Create an instance of DtoMeterResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aggregation
        if self.aggregation:
            _dict['aggregation'] = self.aggregation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item_filters in self.filters:
                if _item_filters:
                    _items.append(_item_filters.to_dict())
            _dict['filters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DtoMeterResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aggregation": MeterAggregation.from_dict(obj["aggregation"]) if obj.get("aggregation") is not None else None,
            "created_at": obj.get("created_at"),
            "event_name": obj.get("event_name"),
            "filters": [MeterFilter.from_dict(_item) for _item in obj["filters"]] if obj.get("filters") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "reset_usage": obj.get("reset_usage"),
            "status": obj.get("status"),
            "tenant_id": obj.get("tenant_id"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


