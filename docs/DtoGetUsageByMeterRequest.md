# DtoGetUsageByMeterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**external_customer_id** | **str** |  | [optional] 
**filters** | **Dict[str, List[str]]** |  | [optional] 
**meter_id** | **str** |  | 
**start_time** | **str** |  | [optional] 
**window_size** | [**TypesWindowSize**](TypesWindowSize.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_get_usage_by_meter_request import DtoGetUsageByMeterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoGetUsageByMeterRequest from a JSON string
dto_get_usage_by_meter_request_instance = DtoGetUsageByMeterRequest.from_json(json)
# print the JSON string representation of the object
print(DtoGetUsageByMeterRequest.to_json())

# convert the object into a dict
dto_get_usage_by_meter_request_dict = dto_get_usage_by_meter_request_instance.to_dict()
# create an instance of DtoGetUsageByMeterRequest from a dict
dto_get_usage_by_meter_request_from_dict = DtoGetUsageByMeterRequest.from_dict(dto_get_usage_by_meter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


