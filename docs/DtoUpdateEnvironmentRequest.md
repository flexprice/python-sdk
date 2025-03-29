# DtoUpdateEnvironmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_update_environment_request import DtoUpdateEnvironmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdateEnvironmentRequest from a JSON string
dto_update_environment_request_instance = DtoUpdateEnvironmentRequest.from_json(json)
# print the JSON string representation of the object
print(DtoUpdateEnvironmentRequest.to_json())

# convert the object into a dict
dto_update_environment_request_dict = dto_update_environment_request_instance.to_dict()
# create an instance of DtoUpdateEnvironmentRequest from a dict
dto_update_environment_request_from_dict = DtoUpdateEnvironmentRequest.from_dict(dto_update_environment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


