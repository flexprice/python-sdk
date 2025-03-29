# DtoWalletBalanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_topup_amount** | **float** |  | [optional] 
**auto_topup_min_balance** | **float** |  | [optional] 
**auto_topup_trigger** | [**TypesAutoTopupTrigger**](TypesAutoTopupTrigger.md) |  | [optional] 
**balance** | **float** |  | [optional] 
**balance_updated_at** | **str** |  | [optional] 
**config** | [**TypesWalletConfig**](TypesWalletConfig.md) |  | [optional] 
**conversion_rate** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**credit_balance** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**current_period_usage** | **float** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**environment_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 
**real_time_balance** | **float** |  | [optional] 
**real_time_credit_balance** | **float** |  | [optional] 
**status** | [**TypesStatus**](TypesStatus.md) |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**unpaid_invoice_amount** | **float** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**wallet_status** | [**TypesWalletStatus**](TypesWalletStatus.md) |  | [optional] 
**wallet_type** | [**TypesWalletType**](TypesWalletType.md) |  | [optional] 

## Example

```python
from flexprice.models.dto_wallet_balance_response import DtoWalletBalanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoWalletBalanceResponse from a JSON string
dto_wallet_balance_response_instance = DtoWalletBalanceResponse.from_json(json)
# print the JSON string representation of the object
print(DtoWalletBalanceResponse.to_json())

# convert the object into a dict
dto_wallet_balance_response_dict = dto_wallet_balance_response_instance.to_dict()
# create an instance of DtoWalletBalanceResponse from a dict
dto_wallet_balance_response_from_dict = DtoWalletBalanceResponse.from_dict(dto_wallet_balance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


