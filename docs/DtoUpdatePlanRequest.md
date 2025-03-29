# DtoUpdatePlanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**entitlements** | [**List[DtoUpdatePlanEntitlementRequest]**](DtoUpdatePlanEntitlementRequest.md) |  | [optional] 
**lookup_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**prices** | [**List[DtoUpdatePlanPriceRequest]**](DtoUpdatePlanPriceRequest.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_update_plan_request import DtoUpdatePlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdatePlanRequest from a JSON string
dto_update_plan_request_instance = DtoUpdatePlanRequest.from_json(json)
# print the JSON string representation of the object
print(DtoUpdatePlanRequest.to_json())

# convert the object into a dict
dto_update_plan_request_dict = dto_update_plan_request_instance.to_dict()
# create an instance of DtoUpdatePlanRequest from a dict
dto_update_plan_request_from_dict = DtoUpdatePlanRequest.from_dict(dto_update_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


