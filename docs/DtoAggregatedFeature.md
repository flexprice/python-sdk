# DtoAggregatedFeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement** | [**DtoAggregatedEntitlement**](DtoAggregatedEntitlement.md) |  | [optional] 
**feature** | [**DtoFeatureResponse**](DtoFeatureResponse.md) |  | [optional] 
**sources** | [**List[DtoEntitlementSource]**](DtoEntitlementSource.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_aggregated_feature import DtoAggregatedFeature

# TODO update the JSON string below
json = "{}"
# create an instance of DtoAggregatedFeature from a JSON string
dto_aggregated_feature_instance = DtoAggregatedFeature.from_json(json)
# print the JSON string representation of the object
print(DtoAggregatedFeature.to_json())

# convert the object into a dict
dto_aggregated_feature_dict = dto_aggregated_feature_instance.to_dict()
# create an instance of DtoAggregatedFeature from a dict
dto_aggregated_feature_from_dict = DtoAggregatedFeature.from_dict(dto_aggregated_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


