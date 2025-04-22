# DtoCreateWalletRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_topup_amount** | **float** |  | [optional] 
**auto_topup_min_balance** | **float** |  | [optional] 
**auto_topup_trigger** | [**TypesAutoTopupTrigger**](TypesAutoTopupTrigger.md) |  | [optional] 
**config** | [**TypesWalletConfig**](TypesWalletConfig.md) |  | [optional] 
**conversion_rate** | **float** | amount in the currency &#x3D;  number of credits * conversion_rate ex if conversion_rate is 1, then 1 USD &#x3D; 1 credit ex if conversion_rate is 2, then 1 USD &#x3D; 0.5 credits ex if conversion_rate is 0.5, then 1 USD &#x3D; 2 credits | [optional] 
**currency** | **str** |  | 
**customer_id** | **str** |  | 
**description** | **str** |  | [optional] 
**initial_credits_to_load** | **float** | initial_credits_to_load is the number of credits to load to the wallet if not provided, the wallet will be created with 0 balance NOTE: this is not the amount in the currency, but the number of credits | [optional] 
**initial_credits_to_load_expiry_date** | **int** | initial_credits_to_load_expiry_date YYYYMMDD format in UTC timezone (optional to set nil means no expiry) for ex 20250101 means the credits will expire on 2025-01-01 00:00:00 UTC hence they will be available for use until 2024-12-31 23:59:59 UTC | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 
**wallet_type** | [**TypesWalletType**](TypesWalletType.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_create_wallet_request import DtoCreateWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateWalletRequest from a JSON string
dto_create_wallet_request_instance = DtoCreateWalletRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreateWalletRequest.to_json())

# convert the object into a dict
dto_create_wallet_request_dict = dto_create_wallet_request_instance.to_dict()
# create an instance of DtoCreateWalletRequest from a dict
dto_create_wallet_request_from_dict = DtoCreateWalletRequest.from_dict(dto_create_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


