# DtoCreateWalletRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_topup_amount** | **float** |  | [optional] 
**auto_topup_min_balance** | **float** |  | [optional] 
**auto_topup_trigger** | [**TypesAutoTopupTrigger**](TypesAutoTopupTrigger.md) |  | [optional] 
**config** | [**TypesWalletConfig**](TypesWalletConfig.md) |  | [optional] 
**conversion_rate** | **float** |  | [optional] 
**currency** | **str** |  | 
**customer_id** | **str** |  | 
**description** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 
**wallet_type** | [**TypesWalletType**](TypesWalletType.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_create_wallet_request import DtoCreateWalletRequest

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


