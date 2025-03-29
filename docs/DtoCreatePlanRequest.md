# DtoCreatePlanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**entitlements** | [**List[DtoCreatePlanEntitlementRequest]**](DtoCreatePlanEntitlementRequest.md) |  | [optional] 
**lookup_key** | **str** |  | [optional] 
**name** | **str** |  | 
**prices** | [**List[DtoCreatePlanPriceRequest]**](DtoCreatePlanPriceRequest.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_create_plan_request import DtoCreatePlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreatePlanRequest from a JSON string
dto_create_plan_request_instance = DtoCreatePlanRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreatePlanRequest.to_json())

# convert the object into a dict
dto_create_plan_request_dict = dto_create_plan_request_instance.to_dict()
# create an instance of DtoCreatePlanRequest from a dict
dto_create_plan_request_from_dict = DtoCreatePlanRequest.from_dict(dto_create_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


