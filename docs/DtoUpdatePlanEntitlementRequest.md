# DtoUpdatePlanEntitlementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_id** | **str** |  | 
**feature_type** | [**TypesFeatureType**](TypesFeatureType.md) |  | 
**id** | **str** | The ID of the entitlement to update (present if the entitlement is being updated) | [optional] 
**is_enabled** | **bool** |  | [optional] 
**is_soft_limit** | **bool** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**static_value** | **str** |  | [optional] 
**usage_limit** | **int** |  | [optional] 
**usage_reset_period** | [**TypesBillingPeriod**](TypesBillingPeriod.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_update_plan_entitlement_request import DtoUpdatePlanEntitlementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdatePlanEntitlementRequest from a JSON string
dto_update_plan_entitlement_request_instance = DtoUpdatePlanEntitlementRequest.from_json(json)
# print the JSON string representation of the object
print(DtoUpdatePlanEntitlementRequest.to_json())

# convert the object into a dict
dto_update_plan_entitlement_request_dict = dto_update_plan_entitlement_request_instance.to_dict()
# create an instance of DtoUpdatePlanEntitlementRequest from a dict
dto_update_plan_entitlement_request_from_dict = DtoUpdatePlanEntitlementRequest.from_dict(dto_update_plan_entitlement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


