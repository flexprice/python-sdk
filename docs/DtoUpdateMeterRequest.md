# DtoUpdateMeterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[MeterFilter]**](MeterFilter.md) |  | [optional] 

## Example

```python
from flexprice_client.models.dto_update_meter_request import DtoUpdateMeterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoUpdateMeterRequest from a JSON string
dto_update_meter_request_instance = DtoUpdateMeterRequest.from_json(json)
# print the JSON string representation of the object
print(DtoUpdateMeterRequest.to_json())

# convert the object into a dict
dto_update_meter_request_dict = dto_update_meter_request_instance.to_dict()
# create an instance of DtoUpdateMeterRequest from a dict
dto_update_meter_request_from_dict = DtoUpdateMeterRequest.from_dict(dto_update_meter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


