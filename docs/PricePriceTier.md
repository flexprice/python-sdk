# PricePriceTier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flat_amount** | **float** | FlatAmount is the flat amount for the given tier and it is applied on top of the unit amount*quantity. It solves cases in banking like 2.7% + 5c | [optional] 
**unit_amount** | **float** | UnitAmount is the amount per unit for the given tier | [optional] 
**up_to** | **int** | Upto is the quantity up to which this tier applies. It is null for the last tier | [optional] 

## Example

```python
from flexprice_client.models.price_price_tier import PricePriceTier

# TODO update the JSON string below
json = "{}"
# create an instance of PricePriceTier from a JSON string
price_price_tier_instance = PricePriceTier.from_json(json)
# print the JSON string representation of the object
print(PricePriceTier.to_json())

# convert the object into a dict
price_price_tier_dict = price_price_tier_instance.to_dict()
# create an instance of PricePriceTier from a dict
price_price_tier_from_dict = PricePriceTier.from_dict(price_price_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


