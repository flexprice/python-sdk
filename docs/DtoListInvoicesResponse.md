# DtoListInvoicesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DtoInvoiceResponse]**](DtoInvoiceResponse.md) |  | [optional] 
**pagination** | [**TypesPaginationResponse**](TypesPaginationResponse.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_list_invoices_response import DtoListInvoicesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoListInvoicesResponse from a JSON string
dto_list_invoices_response_instance = DtoListInvoicesResponse.from_json(json)
# print the JSON string representation of the object
print(DtoListInvoicesResponse.to_json())

# convert the object into a dict
dto_list_invoices_response_dict = dto_list_invoices_response_instance.to_dict()
# create an instance of DtoListInvoicesResponse from a dict
dto_list_invoices_response_from_dict = DtoListInvoicesResponse.from_dict(dto_list_invoices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


