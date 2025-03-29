# DtoListTasksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DtoTaskResponse]**](DtoTaskResponse.md) |  | [optional] 
**pagination** | [**TypesPaginationResponse**](TypesPaginationResponse.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_list_tasks_response import DtoListTasksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoListTasksResponse from a JSON string
dto_list_tasks_response_instance = DtoListTasksResponse.from_json(json)
# print the JSON string representation of the object
print(DtoListTasksResponse.to_json())

# convert the object into a dict
dto_list_tasks_response_dict = dto_list_tasks_response_instance.to_dict()
# create an instance of DtoListTasksResponse from a dict
dto_list_tasks_response_from_dict = DtoListTasksResponse.from_dict(dto_list_tasks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


