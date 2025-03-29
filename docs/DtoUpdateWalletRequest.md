# DtoUpdateWalletRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_topup_amount** | **float** |  | [optional] 
**auto_topup_min_balance** | **float** |  | [optional] 
**auto_topup_trigger** | [**TypesAutoTopupTrigger**](TypesAutoTopupTrigger.md) |  | [optional] 
**config** | [**TypesWalletConfig**](TypesWalletConfig.md) |  | [optional] 
**description** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_update_wallet_request import DtoUpdateWalletRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdateWalletRequest from a JSON string
dto_update_wallet_request_instance = DtoUpdateWalletRequest.from_json(json)
# print the JSON string representation of the object
print(DtoUpdateWalletRequest.to_json())

# convert the object into a dict
dto_update_wallet_request_dict = dto_update_wallet_request_instance.to_dict()
# create an instance of DtoUpdateWalletRequest from a dict
dto_update_wallet_request_from_dict = DtoUpdateWalletRequest.from_dict(dto_update_wallet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


