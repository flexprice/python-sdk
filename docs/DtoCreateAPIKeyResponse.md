# DtoCreateAPIKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**secret** | [**DtoSecretResponse**](DtoSecretResponse.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_create_api_key_response import DtoCreateAPIKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateAPIKeyResponse from a JSON string
dto_create_api_key_response_instance = DtoCreateAPIKeyResponse.from_json(json)
# print the JSON string representation of the object
print(DtoCreateAPIKeyResponse.to_json())

# convert the object into a dict
dto_create_api_key_response_dict = dto_create_api_key_response_instance.to_dict()
# create an instance of DtoCreateAPIKeyResponse from a dict
dto_create_api_key_response_from_dict = DtoCreateAPIKeyResponse.from_dict(dto_create_api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


