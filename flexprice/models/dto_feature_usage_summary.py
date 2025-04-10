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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from flexprice.models.dto_entitlement_source import DtoEntitlementSource
from flexprice.models.dto_feature_response import DtoFeatureResponse
from typing import Optional, Set
from typing_extensions import Self

class DtoFeatureUsageSummary(BaseModel):
    """
    DtoFeatureUsageSummary
    """ # noqa: E501
    current_usage: Optional[Union[StrictFloat, StrictInt]] = None
    feature: Optional[DtoFeatureResponse] = None
    is_enabled: Optional[StrictBool] = None
    is_soft_limit: Optional[StrictBool] = None
    sources: Optional[List[DtoEntitlementSource]] = None
    total_limit: Optional[StrictInt] = None
    usage_percent: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["current_usage", "feature", "is_enabled", "is_soft_limit", "sources", "total_limit", "usage_percent"]

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
        """Create an instance of DtoFeatureUsageSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of feature
        if self.feature:
            _dict['feature'] = self.feature.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sources (list)
        _items = []
        if self.sources:
            for _item_sources in self.sources:
                if _item_sources:
                    _items.append(_item_sources.to_dict())
            _dict['sources'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DtoFeatureUsageSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "current_usage": obj.get("current_usage"),
            "feature": DtoFeatureResponse.from_dict(obj["feature"]) if obj.get("feature") is not None else None,
            "is_enabled": obj.get("is_enabled"),
            "is_soft_limit": obj.get("is_soft_limit"),
            "sources": [DtoEntitlementSource.from_dict(_item) for _item in obj["sources"]] if obj.get("sources") is not None else None,
            "total_limit": obj.get("total_limit"),
            "usage_percent": obj.get("usage_percent")
        })
        return _obj


