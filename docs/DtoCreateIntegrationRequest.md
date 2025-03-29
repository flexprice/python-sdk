# DtoCreateIntegrationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | **Dict[str, str]** |  | 
**name** | **str** |  | 
**provider** | [**TypesSecretProvider**](TypesSecretProvider.md) |  | 

## Example

```python
from flexprice_client.models.dto_create_integration_request import DtoCreateIntegrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateIntegrationRequest from a JSON string
dto_create_integration_request_instance = DtoCreateIntegrationRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreateIntegrationRequest.to_json())

# convert the object into a dict
dto_create_integration_request_dict = dto_create_integration_request_instance.to_dict()
# create an instance of DtoCreateIntegrationRequest from a dict
dto_create_integration_request_from_dict = DtoCreateIntegrationRequest.from_dict(dto_create_integration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


