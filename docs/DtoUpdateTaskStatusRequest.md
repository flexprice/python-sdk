# DtoUpdateTaskStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_status** | [**TypesTaskStatus**](TypesTaskStatus.md) |  | 

## Example

```python
from flexprice.models.dto_update_task_status_request import DtoUpdateTaskStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdateTaskStatusRequest from a JSON string
dto_update_task_status_request_instance = DtoUpdateTaskStatusRequest.from_json(json)
# print the JSON string representation of the object
print(DtoUpdateTaskStatusRequest.to_json())

# convert the object into a dict
dto_update_task_status_request_dict = dto_update_task_status_request_instance.to_dict()
# create an instance of DtoUpdateTaskStatusRequest from a dict
dto_update_task_status_request_from_dict = DtoUpdateTaskStatusRequest.from_dict(dto_update_task_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


