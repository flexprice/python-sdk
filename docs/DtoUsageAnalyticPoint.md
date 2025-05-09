# DtoUsageAnalyticPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **float** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**usage** | **float** |  | [optional] 

## Example

```python
from flexprice.models.dto_usage_analytic_point import DtoUsageAnalyticPoint

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUsageAnalyticPoint from a JSON string
dto_usage_analytic_point_instance = DtoUsageAnalyticPoint.from_json(json)
# print the JSON string representation of the object
print(DtoUsageAnalyticPoint.to_json())

# convert the object into a dict
dto_usage_analytic_point_dict = dto_usage_analytic_point_instance.to_dict()
# create an instance of DtoUsageAnalyticPoint from a dict
dto_usage_analytic_point_from_dict = DtoUsageAnalyticPoint.from_dict(dto_usage_analytic_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


