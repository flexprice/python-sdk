# DtoTopUpWalletRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | amount is the amount in the currency of the wallet to be added NOTE: this is not the number of credits to add, but the amount in the currency amount &#x3D; credits_to_add * conversion_rate if both amount and credits_to_add are provided, amount will be ignored ex if the wallet has a conversion_rate of 2 then adding an amount of 10 USD in the wallet wil add 5 credits in the wallet | [optional] 
**credits_to_add** | **float** | credits_to_add is the number of credits to add to the wallet | [optional] 
**description** | **str** | description to add any specific details about the transaction | [optional] 
**expiry_date_utc** | **str** | expiry_date_utc is the expiry date in UTC timezone ex 2025-01-01 00:00:00 UTC | [optional] 
**idempotency_key** | **str** | idempotency_key is a unique key for the transaction | 
**metadata** | **Dict[str, str]** |  | [optional] 
**transaction_reason** | [**TypesTransactionReason**](TypesTransactionReason.md) |  | 

## Example

```python
from flexprice.models.dto_top_up_wallet_request import DtoTopUpWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoTopUpWalletRequest from a JSON string
dto_top_up_wallet_request_instance = DtoTopUpWalletRequest.from_json(json)
# print the JSON string representation of the object
print(DtoTopUpWalletRequest.to_json())

# convert the object into a dict
dto_top_up_wallet_request_dict = dto_top_up_wallet_request_instance.to_dict()
# create an instance of DtoTopUpWalletRequest from a dict
dto_top_up_wallet_request_from_dict = DtoTopUpWalletRequest.from_dict(dto_top_up_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


