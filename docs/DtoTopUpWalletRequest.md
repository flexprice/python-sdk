# DtoTopUpWalletRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | amount is the number of credits to add to the wallet | 
**description** | **str** | description to add any specific details about the transaction | [optional] 
**expiry_date** | **int** | expiry_date YYYYMMDD format in UTC timezone (optional to set nil means no expiry) for ex 20250101 means the credits will expire on 2025-01-01 00:00:00 UTC hence they will be available for use until 2024-12-31 23:59:59 UTC | [optional] 
**generate_invoice** | **bool** | generate_invoice when true, an invoice will be generated for the transaction | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**purchased_credits** | **bool** | purchased_credits when true, the credits are added as purchased credits | [optional] 
**reference_id** | **str** | reference_id is the ID of the reference ex payment ID, invoice ID, request ID | [optional] 
**reference_type** | **str** | reference_type is the type of the reference ex payment, invoice, request | [optional] 

## Example

```python
from flexprice_client.models.dto_top_up_wallet_request import DtoTopUpWalletRequest

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


