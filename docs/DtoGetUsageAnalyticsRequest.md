# DtoGetUsageAnalyticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **str** |  | [optional] 
**external_customer_id** | **str** |  | 
**feature_ids** | **List[str]** |  | [optional] 
**group_by** | **List[str]** | allowed values: \&quot;source\&quot;, \&quot;feature_id\&quot; | [optional] 
**sources** | **List[str]** |  | [optional] 
**start_time** | **str** |  | [optional] 
**window_size** | [**TypesWindowSize**](TypesWindowSize.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_get_usage_analytics_request import DtoGetUsageAnalyticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoGetUsageAnalyticsRequest from a JSON string
dto_get_usage_analytics_request_instance = DtoGetUsageAnalyticsRequest.from_json(json)
# print the JSON string representation of the object
print(DtoGetUsageAnalyticsRequest.to_json())

# convert the object into a dict
dto_get_usage_analytics_request_dict = dto_get_usage_analytics_request_instance.to_dict()
# create an instance of DtoGetUsageAnalyticsRequest from a dict
dto_get_usage_analytics_request_from_dict = DtoGetUsageAnalyticsRequest.from_dict(dto_get_usage_analytics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


