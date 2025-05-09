# DtoGetUsageAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**items** | [**List[DtoUsageAnalyticItem]**](DtoUsageAnalyticItem.md) |  | [optional] 
**total_cost** | **float** |  | [optional] 

## Example

```python
from flexprice.models.dto_get_usage_analytics_response import DtoGetUsageAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoGetUsageAnalyticsResponse from a JSON string
dto_get_usage_analytics_response_instance = DtoGetUsageAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(DtoGetUsageAnalyticsResponse.to_json())

# convert the object into a dict
dto_get_usage_analytics_response_dict = dto_get_usage_analytics_response_instance.to_dict()
# create an instance of DtoGetUsageAnalyticsResponse from a dict
dto_get_usage_analytics_response_from_dict = DtoGetUsageAnalyticsResponse.from_dict(dto_get_usage_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


