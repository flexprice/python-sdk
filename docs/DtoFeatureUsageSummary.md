# DtoFeatureUsageSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_usage** | **float** |  | [optional] 
**feature** | [**DtoFeatureResponse**](DtoFeatureResponse.md) |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**is_soft_limit** | **bool** |  | [optional] 
**sources** | [**List[DtoEntitlementSource]**](DtoEntitlementSource.md) |  | [optional] 
**total_limit** | **int** |  | [optional] 
**usage_percent** | **float** |  | [optional] 

## Example

```python
from flexprice.models.dto_feature_usage_summary import DtoFeatureUsageSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DtoFeatureUsageSummary from a JSON string
dto_feature_usage_summary_instance = DtoFeatureUsageSummary.from_json(json)
# print the JSON string representation of the object
print(DtoFeatureUsageSummary.to_json())

# convert the object into a dict
dto_feature_usage_summary_dict = dto_feature_usage_summary_instance.to_dict()
# create an instance of DtoFeatureUsageSummary from a dict
dto_feature_usage_summary_from_dict = DtoFeatureUsageSummary.from_dict(dto_feature_usage_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


