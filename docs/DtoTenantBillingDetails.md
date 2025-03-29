# DtoTenantBillingDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**DtoAddress**](DtoAddress.md) |  | [optional] 
**email** | **str** |  | [optional] 
**help_email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_tenant_billing_details import DtoTenantBillingDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DtoTenantBillingDetails from a JSON string
dto_tenant_billing_details_instance = DtoTenantBillingDetails.from_json(json)
# print the JSON string representation of the object
print(DtoTenantBillingDetails.to_json())

# convert the object into a dict
dto_tenant_billing_details_dict = dto_tenant_billing_details_instance.to_dict()
# create an instance of DtoTenantBillingDetails from a dict
dto_tenant_billing_details_from_dict = DtoTenantBillingDetails.from_dict(dto_tenant_billing_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


