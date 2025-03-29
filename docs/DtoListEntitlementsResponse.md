# DtoListEntitlementsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DtoEntitlementResponse]**](DtoEntitlementResponse.md) |  | [optional] 
**pagination** | [**TypesPaginationResponse**](TypesPaginationResponse.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_list_entitlements_response import DtoListEntitlementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoListEntitlementsResponse from a JSON string
dto_list_entitlements_response_instance = DtoListEntitlementsResponse.from_json(json)
# print the JSON string representation of the object
print(DtoListEntitlementsResponse.to_json())

# convert the object into a dict
dto_list_entitlements_response_dict = dto_list_entitlements_response_instance.to_dict()
# create an instance of DtoListEntitlementsResponse from a dict
dto_list_entitlements_response_from_dict = DtoListEntitlementsResponse.from_dict(dto_list_entitlements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


