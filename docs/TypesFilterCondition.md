# TypesFilterCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | [**TypesDataType**](TypesDataType.md) |  | [optional] 
**var_field** | **str** |  | [optional] 
**operator** | [**TypesFilterOperatorType**](TypesFilterOperatorType.md) |  | [optional] 
**value** | [**GithubComFlexpriceFlexpriceInternalTypesValue**](GithubComFlexpriceFlexpriceInternalTypesValue.md) |  | [optional] 

## Example

```python
from flexprice.models.types_filter_condition import TypesFilterCondition

# TODO update the JSON string below
json = "{}"
# create an instance of TypesFilterCondition from a JSON string
types_filter_condition_instance = TypesFilterCondition.from_json(json)
# print the JSON string representation of the object
print(TypesFilterCondition.to_json())

# convert the object into a dict
types_filter_condition_dict = types_filter_condition_instance.to_dict()
# create an instance of TypesFilterCondition from a dict
types_filter_condition_from_dict = TypesFilterCondition.from_dict(types_filter_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


