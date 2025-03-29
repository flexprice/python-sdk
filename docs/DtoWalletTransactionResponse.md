# DtoWalletTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**credit_amount** | **float** |  | [optional] 
**credit_balance_after** | **float** |  | [optional] 
**credit_balance_before** | **float** |  | [optional] 
**credits_available** | **float** |  | [optional] 
**description** | **str** |  | [optional] 
**expiry_date** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**reference_id** | **str** |  | [optional] 
**reference_type** | [**TypesWalletTxReferenceType**](TypesWalletTxReferenceType.md) |  | [optional] 
**transaction_reason** | [**TypesTransactionReason**](TypesTransactionReason.md) |  | [optional] 
**transaction_status** | [**TypesTransactionStatus**](TypesTransactionStatus.md) |  | [optional] 
**type** | **str** |  | [optional] 
**wallet_id** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_wallet_transaction_response import DtoWalletTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoWalletTransactionResponse from a JSON string
dto_wallet_transaction_response_instance = DtoWalletTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(DtoWalletTransactionResponse.to_json())

# convert the object into a dict
dto_wallet_transaction_response_dict = dto_wallet_transaction_response_instance.to_dict()
# create an instance of DtoWalletTransactionResponse from a dict
dto_wallet_transaction_response_from_dict = DtoWalletTransactionResponse.from_dict(dto_wallet_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


