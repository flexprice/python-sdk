# DtoUsageAnalyticItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_type** | [**TypesAggregationType**](TypesAggregationType.md) |  | [optional] 
**currency** | **str** |  | [optional] 
**event_name** | **str** |  | [optional] 
**feature_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**points** | [**List[DtoUsageAnalyticPoint]**](DtoUsageAnalyticPoint.md) |  | [optional] 
**source** | **str** |  | [optional] 
**total_cost** | **float** |  | [optional] 
**total_usage** | **float** |  | [optional] 
**unit** | **str** |  | [optional] 
**unit_plural** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_usage_analytic_item import DtoUsageAnalyticItem

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUsageAnalyticItem from a JSON string
dto_usage_analytic_item_instance = DtoUsageAnalyticItem.from_json(json)
# print the JSON string representation of the object
print(DtoUsageAnalyticItem.to_json())

# convert the object into a dict
dto_usage_analytic_item_dict = dto_usage_analytic_item_instance.to_dict()
# create an instance of DtoUsageAnalyticItem from a dict
dto_usage_analytic_item_from_dict = DtoUsageAnalyticItem.from_dict(dto_usage_analytic_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


