# DtoCustomerEntitlementsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**features** | [**List[DtoAggregatedFeature]**](DtoAggregatedFeature.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_customer_entitlements_response import DtoCustomerEntitlementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCustomerEntitlementsResponse from a JSON string
dto_customer_entitlements_response_instance = DtoCustomerEntitlementsResponse.from_json(json)
# print the JSON string representation of the object
print(DtoCustomerEntitlementsResponse.to_json())

# convert the object into a dict
dto_customer_entitlements_response_dict = dto_customer_entitlements_response_instance.to_dict()
# create an instance of DtoCustomerEntitlementsResponse from a dict
dto_customer_entitlements_response_from_dict = DtoCustomerEntitlementsResponse.from_dict(dto_customer_entitlements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


