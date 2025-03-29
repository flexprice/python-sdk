# MeterFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key is the key for the filter from $event.properties Currently we support only first level keys in the properties and not nested keys | [optional] 
**values** | **List[str]** | Values are the possible values for the filter to be considered for the meter For ex \&quot;model_name\&quot; could have values \&quot;o1-mini\&quot;, \&quot;gpt-4o\&quot; etc | [optional] 

## Example

```python
from flexprice.models.meter_filter import MeterFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MeterFilter from a JSON string
meter_filter_instance = MeterFilter.from_json(json)
# print the JSON string representation of the object
print(MeterFilter.to_json())

# convert the object into a dict
meter_filter_dict = meter_filter_instance.to_dict()
# create an instance of MeterFilter from a dict
meter_filter_from_dict = MeterFilter.from_dict(meter_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


