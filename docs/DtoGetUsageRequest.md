# DtoGetUsageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_type** | [**TypesAggregationType**](TypesAggregationType.md) |  | 
**customer_id** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**event_name** | **str** |  | 
**external_customer_id** | **str** |  | [optional] 
**filters** | **Dict[str, List[str]]** |  | [optional] 
**property_name** | **str** | will be empty/ignored in case of COUNT | [optional] 
**start_time** | **str** |  | [optional] 
**window_size** | [**TypesWindowSize**](TypesWindowSize.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_get_usage_request import DtoGetUsageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoGetUsageRequest from a JSON string
dto_get_usage_request_instance = DtoGetUsageRequest.from_json(json)
# print the JSON string representation of the object
print(DtoGetUsageRequest.to_json())

# convert the object into a dict
dto_get_usage_request_dict = dto_get_usage_request_instance.to_dict()
# create an instance of DtoGetUsageRequest from a dict
dto_get_usage_request_from_dict = DtoGetUsageRequest.from_dict(dto_get_usage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


