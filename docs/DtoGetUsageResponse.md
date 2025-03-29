# DtoGetUsageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_name** | **str** |  | [optional] 
**results** | [**List[DtoUsageResult]**](DtoUsageResult.md) |  | [optional] 
**type** | [**TypesAggregationType**](TypesAggregationType.md) |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_get_usage_response import DtoGetUsageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoGetUsageResponse from a JSON string
dto_get_usage_response_instance = DtoGetUsageResponse.from_json(json)
# print the JSON string representation of the object
print(DtoGetUsageResponse.to_json())

# convert the object into a dict
dto_get_usage_response_dict = dto_get_usage_response_instance.to_dict()
# create an instance of DtoGetUsageResponse from a dict
dto_get_usage_response_from_dict = DtoGetUsageResponse.from_dict(dto_get_usage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


