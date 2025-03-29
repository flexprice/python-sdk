# DtoEntitlementSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_id** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**plan_name** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**static_value** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**usage_limit** | **int** |  | [optional] 

## Example

```python
from flexprice.models.dto_entitlement_source import DtoEntitlementSource

# TODO update the JSON string below
json = "{}"
# create an instance of DtoEntitlementSource from a JSON string
dto_entitlement_source_instance = DtoEntitlementSource.from_json(json)
# print the JSON string representation of the object
print(DtoEntitlementSource.to_json())

# convert the object into a dict
dto_entitlement_source_dict = dto_entitlement_source_instance.to_dict()
# create an instance of DtoEntitlementSource from a dict
dto_entitlement_source_from_dict = DtoEntitlementSource.from_dict(dto_entitlement_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


