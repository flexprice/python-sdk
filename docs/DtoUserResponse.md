# DtoUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**tenant** | [**DtoTenantResponse**](DtoTenantResponse.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_user_response import DtoUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUserResponse from a JSON string
dto_user_response_instance = DtoUserResponse.from_json(json)
# print the JSON string representation of the object
print(DtoUserResponse.to_json())

# convert the object into a dict
dto_user_response_dict = dto_user_response_instance.to_dict()
# create an instance of DtoUserResponse from a dict
dto_user_response_from_dict = DtoUserResponse.from_dict(dto_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


