# DtoMeterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | [**MeterAggregation**](MeterAggregation.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**event_name** | **str** |  | [optional] 
**filters** | [**List[MeterFilter]**](MeterFilter.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**reset_usage** | [**TypesResetUsage**](TypesResetUsage.md) |  | [optional] 
**status** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_meter_response import DtoMeterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoMeterResponse from a JSON string
dto_meter_response_instance = DtoMeterResponse.from_json(json)
# print the JSON string representation of the object
print(DtoMeterResponse.to_json())

# convert the object into a dict
dto_meter_response_dict = dto_meter_response_instance.to_dict()
# create an instance of DtoMeterResponse from a dict
dto_meter_response_from_dict = DtoMeterResponse.from_dict(dto_meter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


