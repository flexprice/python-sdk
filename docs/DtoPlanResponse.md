# DtoPlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**entitlements** | [**List[DtoEntitlementResponse]**](DtoEntitlementResponse.md) |  | [optional] 
**environment_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**lookup_key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**prices** | [**List[DtoPriceResponse]**](DtoPriceResponse.md) |  | [optional] 
**status** | [**TypesStatus**](TypesStatus.md) |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_plan_response import DtoPlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoPlanResponse from a JSON string
dto_plan_response_instance = DtoPlanResponse.from_json(json)
# print the JSON string representation of the object
print(DtoPlanResponse.to_json())

# convert the object into a dict
dto_plan_response_dict = dto_plan_response_instance.to_dict()
# create an instance of DtoPlanResponse from a dict
dto_plan_response_from_dict = DtoPlanResponse.from_dict(dto_plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


