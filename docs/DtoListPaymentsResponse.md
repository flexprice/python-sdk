# DtoListPaymentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DtoPaymentResponse]**](DtoPaymentResponse.md) |  | [optional] 
**pagination** | [**TypesPaginationResponse**](TypesPaginationResponse.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_list_payments_response import DtoListPaymentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoListPaymentsResponse from a JSON string
dto_list_payments_response_instance = DtoListPaymentsResponse.from_json(json)
# print the JSON string representation of the object
print(DtoListPaymentsResponse.to_json())

# convert the object into a dict
dto_list_payments_response_dict = dto_list_payments_response_instance.to_dict()
# create an instance of DtoListPaymentsResponse from a dict
dto_list_payments_response_from_dict = DtoListPaymentsResponse.from_dict(dto_list_payments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


