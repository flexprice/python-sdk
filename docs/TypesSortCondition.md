# TypesSortCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**TypesSortDirection**](TypesSortDirection.md) |  | [optional] 
**var_field** | **str** |  | [optional] 

## Example

```python
from flexprice.models.types_sort_condition import TypesSortCondition

# TODO update the JSON string below
json = "{}"
# create an instance of TypesSortCondition from a JSON string
types_sort_condition_instance = TypesSortCondition.from_json(json)
# print the JSON string representation of the object
print(TypesSortCondition.to_json())

# convert the object into a dict
types_sort_condition_dict = types_sort_condition_instance.to_dict()
# create an instance of TypesSortCondition from a dict
types_sort_condition_from_dict = TypesSortCondition.from_dict(types_sort_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


