# DtoAggregatedEntitlement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** |  | [optional] 
**is_soft_limit** | **bool** |  | [optional] 
**static_values** | **List[str]** | For static/SLA features | [optional] 
**usage_limit** | **int** |  | [optional] 
**usage_reset_period** | [**TypesBillingPeriod**](TypesBillingPeriod.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_aggregated_entitlement import DtoAggregatedEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of DtoAggregatedEntitlement from a JSON string
dto_aggregated_entitlement_instance = DtoAggregatedEntitlement.from_json(json)
# print the JSON string representation of the object
print(DtoAggregatedEntitlement.to_json())

# convert the object into a dict
dto_aggregated_entitlement_dict = dto_aggregated_entitlement_instance.to_dict()
# create an instance of DtoAggregatedEntitlement from a dict
dto_aggregated_entitlement_from_dict = DtoAggregatedEntitlement.from_dict(dto_aggregated_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


