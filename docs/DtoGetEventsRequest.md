# DtoGetEventsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **str** | End time of the events to be fetched in ISO 8601 format Defaults to now if not provided | [optional] 
**event_id** | **str** | Event ID is the idempotency key for the event | [optional] 
**event_name** | **str** | Event name / Unique identifier for the event in your system | [optional] 
**external_customer_id** | **str** | Customer ID in your system that was sent with the event | [optional] 
**iter_first_key** | **str** | First key to iterate over the events | [optional] 
**iter_last_key** | **str** | Last key to iterate over the events | [optional] 
**offset** | **int** | Offset to fetch the events and is set to 0 by default | [optional] 
**page_size** | **int** | Page size to fetch the events and is set to 50 by default | [optional] 
**property_filters** | **Dict[str, List[str]]** | Property filters to filter the events by the keys in &#x60;properties&#x60; field of the event | [optional] 
**source** | **str** | Source to filter the events by the source | [optional] 
**start_time** | **str** | Start time of the events to be fetched in ISO 8601 format Defaults to last 7 days from now if not provided | [optional] 

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


