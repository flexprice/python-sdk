# DtoUpdateTenantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_details** | [**DtoTenantBillingDetails**](DtoTenantBillingDetails.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_update_tenant_request import DtoUpdateTenantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdateTenantRequest from a JSON string
dto_update_tenant_request_instance = DtoUpdateTenantRequest.from_json(json)
# print the JSON string representation of the object
print(DtoUpdateTenantRequest.to_json())

# convert the object into a dict
dto_update_tenant_request_dict = dto_update_tenant_request_instance.to_dict()
# create an instance of DtoUpdateTenantRequest from a dict
dto_update_tenant_request_from_dict = DtoUpdateTenantRequest.from_dict(dto_update_tenant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


