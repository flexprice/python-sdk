# DtoCreateMeterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | [**MeterAggregation**](MeterAggregation.md) |  | 
**event_name** | **str** |  | 
**filters** | [**List[MeterFilter]**](MeterFilter.md) |  | [optional] 
**name** | **str** |  | 
**reset_usage** | [**TypesResetUsage**](TypesResetUsage.md) |  | 

## Example

```python
from flexprice_client.models.dto_create_meter_request import DtoCreateMeterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateMeterRequest from a JSON string
dto_create_meter_request_instance = DtoCreateMeterRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreateMeterRequest.to_json())

# convert the object into a dict
dto_create_meter_request_dict = dto_create_meter_request_instance.to_dict()
# create an instance of DtoCreateMeterRequest from a dict
dto_create_meter_request_from_dict = DtoCreateMeterRequest.from_dict(dto_create_meter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


