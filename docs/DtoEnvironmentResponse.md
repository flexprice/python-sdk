# DtoEnvironmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_environment_response import DtoEnvironmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoEnvironmentResponse from a JSON string
dto_environment_response_instance = DtoEnvironmentResponse.from_json(json)
# print the JSON string representation of the object
print(DtoEnvironmentResponse.to_json())

# convert the object into a dict
dto_environment_response_dict = dto_environment_response_instance.to_dict()
# create an instance of DtoEnvironmentResponse from a dict
dto_environment_response_from_dict = DtoEnvironmentResponse.from_dict(dto_environment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


