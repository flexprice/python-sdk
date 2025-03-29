# DtoTaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**entity_type** | [**TypesEntityType**](TypesEntityType.md) |  | [optional] 
**error_summary** | **str** |  | [optional] 
**failed_at** | **str** |  | [optional] 
**failed_records** | **int** |  | [optional] 
**file_name** | **str** |  | [optional] 
**file_type** | [**TypesFileType**](TypesFileType.md) |  | [optional] 
**file_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 
**processed_records** | **int** |  | [optional] 
**started_at** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**successful_records** | **int** |  | [optional] 
**task_status** | [**TypesTaskStatus**](TypesTaskStatus.md) |  | [optional] 
**task_type** | [**TypesTaskType**](TypesTaskType.md) |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**total_records** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_task_response import DtoTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoTaskResponse from a JSON string
dto_task_response_instance = DtoTaskResponse.from_json(json)
# print the JSON string representation of the object
print(DtoTaskResponse.to_json())

# convert the object into a dict
dto_task_response_dict = dto_task_response_instance.to_dict()
# create an instance of DtoTaskResponse from a dict
dto_task_response_from_dict = DtoTaskResponse.from_dict(dto_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


