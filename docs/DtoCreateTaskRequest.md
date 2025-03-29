# DtoCreateTaskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | [**TypesEntityType**](TypesEntityType.md) |  | 
**file_name** | **str** |  | [optional] 
**file_type** | [**TypesFileType**](TypesFileType.md) |  | 
**file_url** | **str** |  | 
**metadata** | **Dict[str, object]** |  | [optional] 
**task_type** | [**TypesTaskType**](TypesTaskType.md) |  | 

## Example

```python
from flexprice_client.models.dto_create_task_request import DtoCreateTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateTaskRequest from a JSON string
dto_create_task_request_instance = DtoCreateTaskRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreateTaskRequest.to_json())

# convert the object into a dict
dto_create_task_request_dict = dto_create_task_request_instance.to_dict()
# create an instance of DtoCreateTaskRequest from a dict
dto_create_task_request_from_dict = DtoCreateTaskRequest.from_dict(dto_create_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


