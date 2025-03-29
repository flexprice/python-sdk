# DtoListEnvironmentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environments** | [**List[DtoEnvironmentResponse]**](DtoEnvironmentResponse.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_list_environments_response import DtoListEnvironmentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoListEnvironmentsResponse from a JSON string
dto_list_environments_response_instance = DtoListEnvironmentsResponse.from_json(json)
# print the JSON string representation of the object
print(DtoListEnvironmentsResponse.to_json())

# convert the object into a dict
dto_list_environments_response_dict = dto_list_environments_response_instance.to_dict()
# create an instance of DtoListEnvironmentsResponse from a dict
dto_list_environments_response_from_dict = DtoListEnvironmentsResponse.from_dict(dto_list_environments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


