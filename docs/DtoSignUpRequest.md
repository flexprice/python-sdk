# DtoSignUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | [optional] 
**tenant_name** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_sign_up_request import DtoSignUpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoSignUpRequest from a JSON string
dto_sign_up_request_instance = DtoSignUpRequest.from_json(json)
# print the JSON string representation of the object
print(DtoSignUpRequest.to_json())

# convert the object into a dict
dto_sign_up_request_dict = dto_sign_up_request_instance.to_dict()
# create an instance of DtoSignUpRequest from a dict
dto_sign_up_request_from_dict = DtoSignUpRequest.from_dict(dto_sign_up_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


