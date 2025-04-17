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

from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from flexprice.models.dto_payment_attempt_response import DtoPaymentAttemptResponse
from flexprice.models.types_payment_destination_type import TypesPaymentDestinationType
from flexprice.models.types_payment_method_type import TypesPaymentMethodType
from flexprice.models.types_payment_status import TypesPaymentStatus
from typing import Optional, Set
from typing_extensions import Self

class DtoPaymentResponse(BaseModel):
    """
    DtoPaymentResponse
    """ # noqa: E501
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    attempts: Optional[List[DtoPaymentAttemptResponse]] = None
    created_at: Optional[StrictStr] = None
    created_by: Optional[StrictStr] = None
    currency: Optional[StrictStr] = None
    destination_id: Optional[StrictStr] = None
    destination_type: Optional[TypesPaymentDestinationType] = None
    error_message: Optional[StrictStr] = None
    failed_at: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    idempotency_key: Optional[StrictStr] = None
    invoice_number: Optional[StrictStr] = None
    metadata: Optional[Dict[str, StrictStr]] = None
    payment_method_id: Optional[StrictStr] = None
    payment_method_type: Optional[TypesPaymentMethodType] = None
    payment_status: Optional[TypesPaymentStatus] = None
    refunded_at: Optional[StrictStr] = None
    succeeded_at: Optional[StrictStr] = None
    tenant_id: Optional[StrictStr] = None
    track_attempts: Optional[StrictBool] = None
    updated_at: Optional[StrictStr] = None
    updated_by: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["amount", "attempts", "created_at", "created_by", "currency", "destination_id", "destination_type", "error_message", "failed_at", "id", "idempotency_key", "invoice_number", "metadata", "payment_method_id", "payment_method_type", "payment_status", "refunded_at", "succeeded_at", "tenant_id", "track_attempts", "updated_at", "updated_by"]

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
        """Create an instance of DtoPaymentResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attempts (list)
        _items = []
        if self.attempts:
            for _item_attempts in self.attempts:
                if _item_attempts:
                    _items.append(_item_attempts.to_dict())
            _dict['attempts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DtoPaymentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "attempts": [DtoPaymentAttemptResponse.from_dict(_item) for _item in obj["attempts"]] if obj.get("attempts") is not None else None,
            "created_at": obj.get("created_at"),
            "created_by": obj.get("created_by"),
            "currency": obj.get("currency"),
            "destination_id": obj.get("destination_id"),
            "destination_type": obj.get("destination_type"),
            "error_message": obj.get("error_message"),
            "failed_at": obj.get("failed_at"),
            "id": obj.get("id"),
            "idempotency_key": obj.get("idempotency_key"),
            "invoice_number": obj.get("invoice_number"),
            "metadata": obj.get("metadata"),
            "payment_method_id": obj.get("payment_method_id"),
            "payment_method_type": obj.get("payment_method_type"),
            "payment_status": obj.get("payment_status"),
            "refunded_at": obj.get("refunded_at"),
            "succeeded_at": obj.get("succeeded_at"),
            "tenant_id": obj.get("tenant_id"),
            "track_attempts": obj.get("track_attempts"),
            "updated_at": obj.get("updated_at"),
            "updated_by": obj.get("updated_by")
        })
        return _obj


