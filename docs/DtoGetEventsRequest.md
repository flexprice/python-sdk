# DtoGetEventsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_total** | **bool** |  | [optional] 
**end_time** | **str** |  | [optional] 
**event_id** | **str** |  | [optional] 
**event_name** | **str** |  | 
**external_customer_id** | **str** |  | [optional] 
**iter_first_key** | **str** |  | [optional] 
**iter_last_key** | **str** |  | [optional] 
**offset** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**property_filters** | **Dict[str, List[str]]** |  | [optional] 
**start_time** | **str** |  | [optional] 

## Example

```python
from flexprice.models.dto_get_events_request import DtoGetEventsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoGetEventsRequest from a JSON string
dto_get_events_request_instance = DtoGetEventsRequest.from_json(json)
# print the JSON string representation of the object
print(DtoGetEventsRequest.to_json())

# convert the object into a dict
dto_get_events_request_dict = dto_get_events_request_instance.to_dict()
# create an instance of DtoGetEventsRequest from a dict
dto_get_events_request_from_dict = DtoGetEventsRequest.from_dict(dto_get_events_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


