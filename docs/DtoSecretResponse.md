# DtoSecretResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**display_id** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_used_at** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 
**provider** | [**TypesSecretProvider**](TypesSecretProvider.md) |  | [optional] 
**status** | [**TypesStatus**](TypesStatus.md) |  | [optional] 
**type** | [**TypesSecretType**](TypesSecretType.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_secret_response import DtoSecretResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoSecretResponse from a JSON string
dto_secret_response_instance = DtoSecretResponse.from_json(json)
# print the JSON string representation of the object
print(DtoSecretResponse.to_json())

# convert the object into a dict
dto_secret_response_dict = dto_secret_response_instance.to_dict()
# create an instance of DtoSecretResponse from a dict
dto_secret_response_from_dict = DtoSecretResponse.from_dict(dto_secret_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


