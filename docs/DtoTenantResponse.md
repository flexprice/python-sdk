# DtoTenantResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_details** | [**DtoTenantBillingDetails**](DtoTenantBillingDetails.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_tenant_response import DtoTenantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoTenantResponse from a JSON string
dto_tenant_response_instance = DtoTenantResponse.from_json(json)
# print the JSON string representation of the object
print(DtoTenantResponse.to_json())

# convert the object into a dict
dto_tenant_response_dict = dto_tenant_response_instance.to_dict()
# create an instance of DtoTenantResponse from a dict
dto_tenant_response_from_dict = DtoTenantResponse.from_dict(dto_tenant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


