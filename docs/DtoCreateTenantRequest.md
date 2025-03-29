# DtoCreateTenantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_details** | [**DtoTenantBillingDetails**](DtoTenantBillingDetails.md) |  | [optional] 
**name** | **str** |  | 

## Example

```python
from flexprice_client.models.dto_create_tenant_request import DtoCreateTenantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateTenantRequest from a JSON string
dto_create_tenant_request_instance = DtoCreateTenantRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreateTenantRequest.to_json())

# convert the object into a dict
dto_create_tenant_request_dict = dto_create_tenant_request_instance.to_dict()
# create an instance of DtoCreateTenantRequest from a dict
dto_create_tenant_request_from_dict = DtoCreateTenantRequest.from_dict(dto_create_tenant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


