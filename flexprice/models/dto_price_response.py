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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from flexprice.models.dto_meter_response import DtoMeterResponse
from flexprice.models.price_jsonb_transform_quantity import PriceJSONBTransformQuantity
from flexprice.models.price_price_tier import PricePriceTier
from flexprice.models.types_billing_cadence import TypesBillingCadence
from flexprice.models.types_billing_model import TypesBillingModel
from flexprice.models.types_billing_period import TypesBillingPeriod
from flexprice.models.types_billing_tier import TypesBillingTier
from flexprice.models.types_invoice_cadence import TypesInvoiceCadence
from flexprice.models.types_price_type import TypesPriceType
from flexprice.models.types_status import TypesStatus
from typing import Optional, Set
from typing_extensions import Self

class DtoPriceResponse(BaseModel):
    """
    DtoPriceResponse
    """ # noqa: E501
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Amount stored in main currency units (e.g., dollars, not cents) For USD: 12.50 means $12.50")
    billing_cadence: Optional[TypesBillingCadence] = None
    billing_model: Optional[TypesBillingModel] = None
    billing_period: Optional[TypesBillingPeriod] = None
    billing_period_count: Optional[StrictInt] = Field(default=None, description="BillingPeriodCount is the count of the billing period ex 1, 3, 6, 12")
    created_at: Optional[StrictStr] = None
    created_by: Optional[StrictStr] = None
    currency: Optional[StrictStr] = Field(default=None, description="Currency 3 digit ISO currency code in lowercase ex usd, eur, gbp")
    description: Optional[StrictStr] = Field(default=None, description="Description of the price")
    display_amount: Optional[StrictStr] = Field(default=None, description="DisplayAmount is the formatted amount with currency symbol For USD: $12.50")
    environment_id: Optional[StrictStr] = Field(default=None, description="EnvironmentID is the environment identifier for the price")
    id: Optional[StrictStr] = Field(default=None, description="ID uuid identifier for the price")
    invoice_cadence: Optional[TypesInvoiceCadence] = None
    lookup_key: Optional[StrictStr] = Field(default=None, description="LookupKey used for looking up the price in the database")
    metadata: Optional[Dict[str, StrictStr]] = None
    meter: Optional[DtoMeterResponse] = None
    meter_id: Optional[StrictStr] = Field(default=None, description="MeterID is the id of the meter for usage based pricing")
    plan_id: Optional[StrictStr] = Field(default=None, description="PlanID is the id of the plan for plan based pricing")
    status: Optional[TypesStatus] = None
    tenant_id: Optional[StrictStr] = None
    tier_mode: Optional[TypesBillingTier] = None
    tiers: Optional[List[PricePriceTier]] = None
    transform_quantity: Optional[PriceJSONBTransformQuantity] = None
    trial_period: Optional[StrictInt] = Field(default=None, description="TrialPeriod is the number of days for the trial period Note: This is only applicable for recurring prices (BILLING_CADENCE_RECURRING)")
    type: Optional[TypesPriceType] = None
    updated_at: Optional[StrictStr] = None
    updated_by: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["amount", "billing_cadence", "billing_model", "billing_period", "billing_period_count", "created_at", "created_by", "currency", "description", "display_amount", "environment_id", "id", "invoice_cadence", "lookup_key", "metadata", "meter", "meter_id", "plan_id", "status", "tenant_id", "tier_mode", "tiers", "transform_quantity", "trial_period", "type", "updated_at", "updated_by"]

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
        """Create an instance of DtoPriceResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of meter
        if self.meter:
            _dict['meter'] = self.meter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tiers (list)
        _items = []
        if self.tiers:
            for _item_tiers in self.tiers:
                if _item_tiers:
                    _items.append(_item_tiers.to_dict())
            _dict['tiers'] = _items
        # override the default output from pydantic by calling `to_dict()` of transform_quantity
        if self.transform_quantity:
            _dict['transform_quantity'] = self.transform_quantity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DtoPriceResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "billing_cadence": obj.get("billing_cadence"),
            "billing_model": obj.get("billing_model"),
            "billing_period": obj.get("billing_period"),
            "billing_period_count": obj.get("billing_period_count"),
            "created_at": obj.get("created_at"),
            "created_by": obj.get("created_by"),
            "currency": obj.get("currency"),
            "description": obj.get("description"),
            "display_amount": obj.get("display_amount"),
            "environment_id": obj.get("environment_id"),
            "id": obj.get("id"),
            "invoice_cadence": obj.get("invoice_cadence"),
            "lookup_key": obj.get("lookup_key"),
            "metadata": obj.get("metadata"),
            "meter": DtoMeterResponse.from_dict(obj["meter"]) if obj.get("meter") is not None else None,
            "meter_id": obj.get("meter_id"),
            "plan_id": obj.get("plan_id"),
            "status": obj.get("status"),
            "tenant_id": obj.get("tenant_id"),
            "tier_mode": obj.get("tier_mode"),
            "tiers": [PricePriceTier.from_dict(_item) for _item in obj["tiers"]] if obj.get("tiers") is not None else None,
            "transform_quantity": PriceJSONBTransformQuantity.from_dict(obj["transform_quantity"]) if obj.get("transform_quantity") is not None else None,
            "trial_period": obj.get("trial_period"),
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at"),
            "updated_by": obj.get("updated_by")
        })
        return _obj


