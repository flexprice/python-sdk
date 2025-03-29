# PriceJSONBTransformQuantity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**divide_by** | **int** | Divide quantity by this number | [optional] 
**round** | **str** | up or down | [optional] 

## Example

```python
from flexprice.models.price_jsonb_transform_quantity import PriceJSONBTransformQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of PriceJSONBTransformQuantity from a JSON string
price_jsonb_transform_quantity_instance = PriceJSONBTransformQuantity.from_json(json)
# print the JSON string representation of the object
print(PriceJSONBTransformQuantity.to_json())

# convert the object into a dict
price_jsonb_transform_quantity_dict = price_jsonb_transform_quantity_instance.to_dict()
# create an instance of PriceJSONBTransformQuantity from a dict
price_jsonb_transform_quantity_from_dict = PriceJSONBTransformQuantity.from_dict(price_jsonb_transform_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


