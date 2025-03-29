# MeterAggregation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Field is the key in $event.properties on which the aggregation is to be applied For ex if the aggregation type is sum for API usage, the field could be \&quot;duration_ms\&quot; | [optional] 
**type** | [**TypesAggregationType**](TypesAggregationType.md) |  | [optional] 

## Example

```python
from flexprice_client.models.meter_aggregation import MeterAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of MeterAggregation from a JSON string
meter_aggregation_instance = MeterAggregation.from_json(json)
# print the JSON string representation of the object
print(MeterAggregation.to_json())

# convert the object into a dict
meter_aggregation_dict = meter_aggregation_instance.to_dict()
# create an instance of MeterAggregation from a dict
meter_aggregation_from_dict = MeterAggregation.from_dict(meter_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


