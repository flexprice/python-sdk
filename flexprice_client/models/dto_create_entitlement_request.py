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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from flexprice_client.models.types_billing_period import TypesBillingPeriod
from flexprice_client.models.types_feature_type import TypesFeatureType
from typing import Optional, Set
from typing_extensions import Self

class DtoCreateEntitlementRequest(BaseModel):
    """
    DtoCreateEntitlementRequest
    """ # noqa: E501
    feature_id: StrictStr
    feature_type: TypesFeatureType
    is_enabled: Optional[StrictBool] = None
    is_soft_limit: Optional[StrictBool] = None
    plan_id: Optional[StrictStr] = None
    static_value: Optional[StrictStr] = None
    usage_limit: Optional[StrictInt] = None
    usage_reset_period: Optional[TypesBillingPeriod] = None
    __properties: ClassVar[List[str]] = ["feature_id", "feature_type", "is_enabled", "is_soft_limit", "plan_id", "static_value", "usage_limit", "usage_reset_period"]

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
        """Create an instance of DtoCreateEntitlementRequest from a JSON string"""
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
        """Create an instance of DtoCreateEntitlementRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "feature_id": obj.get("feature_id"),
            "feature_type": obj.get("feature_type"),
            "is_enabled": obj.get("is_enabled"),
            "is_soft_limit": obj.get("is_soft_limit"),
            "plan_id": obj.get("plan_id"),
            "static_value": obj.get("static_value"),
            "usage_limit": obj.get("usage_limit"),
            "usage_reset_period": obj.get("usage_reset_period")
        })
        return _obj


