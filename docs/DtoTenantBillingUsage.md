# DtoTenantBillingUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriptions** | [**List[DtoSubscriptionResponse]**](DtoSubscriptionResponse.md) |  | [optional] 
**usage** | [**DtoCustomerUsageSummaryResponse**](DtoCustomerUsageSummaryResponse.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_tenant_billing_usage import DtoTenantBillingUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DtoTenantBillingUsage from a JSON string
dto_tenant_billing_usage_instance = DtoTenantBillingUsage.from_json(json)
# print the JSON string representation of the object
print(DtoTenantBillingUsage.to_json())

# convert the object into a dict
dto_tenant_billing_usage_dict = dto_tenant_billing_usage_instance.to_dict()
# create an instance of DtoTenantBillingUsage from a dict
dto_tenant_billing_usage_from_dict = DtoTenantBillingUsage.from_dict(dto_tenant_billing_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


