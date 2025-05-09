# TypesFeatureFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **str** |  | [optional] 
**expand** | **str** |  | [optional] 
**feature_ids** | **List[str]** | Feature specific filters | [optional] 
**filters** | [**List[TypesFilterCondition]**](TypesFilterCondition.md) | filters allows complex filtering based on multiple fields | [optional] 
**limit** | **int** |  | [optional] 
**lookup_key** | **str** |  | [optional] 
**meter_ids** | **List[str]** |  | [optional] 
**name_contains** | **str** |  | [optional] 
**offset** | **int** |  | [optional] 
**order** | **str** |  | [optional] 
**sort** | [**List[TypesSortCondition]**](TypesSortCondition.md) |  | [optional] 
**start_time** | **str** |  | [optional] 
**status** | [**TypesStatus**](TypesStatus.md) |  | [optional] 

## Example

```python
from flexprice.models.types_feature_filter import TypesFeatureFilter

# TODO update the JSON string below
json = "{}"
# create an instance of TypesFeatureFilter from a JSON string
types_feature_filter_instance = TypesFeatureFilter.from_json(json)
# print the JSON string representation of the object
print(TypesFeatureFilter.to_json())

# convert the object into a dict
types_feature_filter_dict = types_feature_filter_instance.to_dict()
# create an instance of TypesFeatureFilter from a dict
types_feature_filter_from_dict = TypesFeatureFilter.from_dict(types_feature_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


