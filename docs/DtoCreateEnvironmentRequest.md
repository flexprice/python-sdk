# DtoCreateEnvironmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from flexprice_client.models.dto_create_environment_request import DtoCreateEnvironmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateEnvironmentRequest from a JSON string
dto_create_environment_request_instance = DtoCreateEnvironmentRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreateEnvironmentRequest.to_json())

# convert the object into a dict
dto_create_environment_request_dict = dto_create_environment_request_instance.to_dict()
# create an instance of DtoCreateEnvironmentRequest from a dict
dto_create_environment_request_from_dict = DtoCreateEnvironmentRequest.from_dict(dto_create_environment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


