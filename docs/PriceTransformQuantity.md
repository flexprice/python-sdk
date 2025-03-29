# PriceTransformQuantity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**divide_by** | **int** | Divide quantity by this number | [optional] 
**round** | **str** | up or down | [optional] 

## Example

```python
from flexprice.models.price_transform_quantity import PriceTransformQuantity

# TODO update the JSON string below
json = "{}"
# create an instance of PriceTransformQuantity from a JSON string
price_transform_quantity_instance = PriceTransformQuantity.from_json(json)
# print the JSON string representation of the object
print(PriceTransformQuantity.to_json())

# convert the object into a dict
price_transform_quantity_dict = price_transform_quantity_instance.to_dict()
# create an instance of PriceTransformQuantity from a dict
price_transform_quantity_from_dict = PriceTransformQuantity.from_dict(price_transform_quantity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


