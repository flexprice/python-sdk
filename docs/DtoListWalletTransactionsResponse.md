# DtoListWalletTransactionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DtoWalletTransactionResponse]**](DtoWalletTransactionResponse.md) |  | [optional] 
**pagination** | [**TypesPaginationResponse**](TypesPaginationResponse.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_list_wallet_transactions_response import DtoListWalletTransactionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoListWalletTransactionsResponse from a JSON string
dto_list_wallet_transactions_response_instance = DtoListWalletTransactionsResponse.from_json(json)
# print the JSON string representation of the object
print(DtoListWalletTransactionsResponse.to_json())

# convert the object into a dict
dto_list_wallet_transactions_response_dict = dto_list_wallet_transactions_response_instance.to_dict()
# create an instance of DtoListWalletTransactionsResponse from a dict
dto_list_wallet_transactions_response_from_dict = DtoListWalletTransactionsResponse.from_dict(dto_list_wallet_transactions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


