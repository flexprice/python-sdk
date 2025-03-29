# DtoCreatePriceTier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flat_amount** | **str** |  | [optional] 
**unit_amount** | **str** |  | 
**up_to** | **int** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_create_price_tier import DtoCreatePriceTier

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreatePriceTier from a JSON string
dto_create_price_tier_instance = DtoCreatePriceTier.from_json(json)
# print the JSON string representation of the object
print(DtoCreatePriceTier.to_json())

# convert the object into a dict
dto_create_price_tier_dict = dto_create_price_tier_instance.to_dict()
# create an instance of DtoCreatePriceTier from a dict
dto_create_price_tier_from_dict = DtoCreatePriceTier.from_dict(dto_create_price_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


