# DtoUpdateEntitlementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** |  | [optional] 
**is_soft_limit** | **bool** |  | [optional] 
**static_value** | **str** |  | [optional] 
**usage_limit** | **int** |  | [optional] 
**usage_reset_period** | [**TypesBillingPeriod**](TypesBillingPeriod.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_update_entitlement_request import DtoUpdateEntitlementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdateEntitlementRequest from a JSON string
dto_update_entitlement_request_instance = DtoUpdateEntitlementRequest.from_json(json)
# print the JSON string representation of the object
print(DtoUpdateEntitlementRequest.to_json())

# convert the object into a dict
dto_update_entitlement_request_dict = dto_update_entitlement_request_instance.to_dict()
# create an instance of DtoUpdateEntitlementRequest from a dict
dto_update_entitlement_request_from_dict = DtoUpdateEntitlementRequest.from_dict(dto_update_entitlement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


