# DtoAuthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_auth_response import DtoAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoAuthResponse from a JSON string
dto_auth_response_instance = DtoAuthResponse.from_json(json)
# print the JSON string representation of the object
print(DtoAuthResponse.to_json())

# convert the object into a dict
dto_auth_response_dict = dto_auth_response_instance.to_dict()
# create an instance of DtoAuthResponse from a dict
dto_auth_response_from_dict = DtoAuthResponse.from_dict(dto_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


