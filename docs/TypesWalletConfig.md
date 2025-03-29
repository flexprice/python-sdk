# TypesWalletConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_price_types** | [**List[TypesWalletConfigPriceType]**](TypesWalletConfigPriceType.md) | AllowedPriceTypes is a list of price types that are allowed for the wallet nil means all price types are allowed | [optional] 

## Example

```python
from flexprice_client.models.types_wallet_config import TypesWalletConfig

# TODO update the JSON string below
json = "{}"
# create an instance of TypesWalletConfig from a JSON string
types_wallet_config_instance = TypesWalletConfig.from_json(json)
# print the JSON string representation of the object
print(TypesWalletConfig.to_json())

# convert the object into a dict
types_wallet_config_dict = types_wallet_config_instance.to_dict()
# create an instance of TypesWalletConfig from a dict
types_wallet_config_from_dict = TypesWalletConfig.from_dict(types_wallet_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


