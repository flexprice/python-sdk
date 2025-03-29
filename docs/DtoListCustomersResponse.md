# DtoListCustomersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DtoCustomerResponse]**](DtoCustomerResponse.md) |  | [optional] 
**pagination** | [**TypesPaginationResponse**](TypesPaginationResponse.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_list_customers_response import DtoListCustomersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoListCustomersResponse from a JSON string
dto_list_customers_response_instance = DtoListCustomersResponse.from_json(json)
# print the JSON string representation of the object
print(DtoListCustomersResponse.to_json())

# convert the object into a dict
dto_list_customers_response_dict = dto_list_customers_response_instance.to_dict()
# create an instance of DtoListCustomersResponse from a dict
dto_list_customers_response_from_dict = DtoListCustomersResponse.from_dict(dto_list_customers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


