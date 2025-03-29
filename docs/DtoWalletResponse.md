# DtoWalletResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_topup_amount** | **float** |  | [optional] 
**auto_topup_min_balance** | **float** |  | [optional] 
**auto_topup_trigger** | [**TypesAutoTopupTrigger**](TypesAutoTopupTrigger.md) |  | [optional] 
**balance** | **float** |  | [optional] 
**config** | [**TypesWalletConfig**](TypesWalletConfig.md) |  | [optional] 
**conversion_rate** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**credit_balance** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**wallet_status** | [**TypesWalletStatus**](TypesWalletStatus.md) |  | [optional] 
**wallet_type** | [**TypesWalletType**](TypesWalletType.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_wallet_response import DtoWalletResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoWalletResponse from a JSON string
dto_wallet_response_instance = DtoWalletResponse.from_json(json)
# print the JSON string representation of the object
print(DtoWalletResponse.to_json())

# convert the object into a dict
dto_wallet_response_dict = dto_wallet_response_instance.to_dict()
# create an instance of DtoWalletResponse from a dict
dto_wallet_response_from_dict = DtoWalletResponse.from_dict(dto_wallet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


