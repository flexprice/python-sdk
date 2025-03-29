# DtoEntitlementResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**environment_id** | **str** |  | [optional] 
**feature** | [**DtoFeatureResponse**](DtoFeatureResponse.md) |  | [optional] 
**feature_id** | **str** |  | [optional] 
**feature_type** | [**TypesFeatureType**](TypesFeatureType.md) |  | [optional] 
**id** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**is_soft_limit** | **bool** |  | [optional] 
**plan** | [**DtoPlanResponse**](DtoPlanResponse.md) |  | [optional] 
**plan_id** | **str** |  | [optional] 
**static_value** | **str** |  | [optional] 
**status** | [**TypesStatus**](TypesStatus.md) |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**usage_limit** | **int** |  | [optional] 
**usage_reset_period** | [**TypesBillingPeriod**](TypesBillingPeriod.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_entitlement_response import DtoEntitlementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoEntitlementResponse from a JSON string
dto_entitlement_response_instance = DtoEntitlementResponse.from_json(json)
# print the JSON string representation of the object
print(DtoEntitlementResponse.to_json())

# convert the object into a dict
dto_entitlement_response_dict = dto_entitlement_response_instance.to_dict()
# create an instance of DtoEntitlementResponse from a dict
dto_entitlement_response_from_dict = DtoEntitlementResponse.from_dict(dto_entitlement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


