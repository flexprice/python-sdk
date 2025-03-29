# DtoUsageResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **float** |  | [optional] 
**window_size** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_usage_result import DtoUsageResult

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUsageResult from a JSON string
dto_usage_result_instance = DtoUsageResult.from_json(json)
# print the JSON string representation of the object
print(DtoUsageResult.to_json())

# convert the object into a dict
dto_usage_result_dict = dto_usage_result_instance.to_dict()
# create an instance of DtoUsageResult from a dict
dto_usage_result_from_dict = DtoUsageResult.from_dict(dto_usage_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


