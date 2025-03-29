# DtoCreateAPIKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **str** |  | [optional] 
**name** | **str** |  | 
**permissions** | **List[str]** |  | [optional] 
**type** | [**TypesSecretType**](TypesSecretType.md) |  | 

## Example

```python
from flexprice_client.models.dto_create_api_key_request import DtoCreateAPIKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateAPIKeyRequest from a JSON string
dto_create_api_key_request_instance = DtoCreateAPIKeyRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreateAPIKeyRequest.to_json())

# convert the object into a dict
dto_create_api_key_request_dict = dto_create_api_key_request_instance.to_dict()
# create an instance of DtoCreateAPIKeyRequest from a dict
dto_create_api_key_request_from_dict = DtoCreateAPIKeyRequest.from_dict(dto_create_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


