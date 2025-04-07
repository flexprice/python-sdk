# DtoGetEventsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[DtoEvent]**](DtoEvent.md) |  | [optional] 
**has_more** | **bool** |  | [optional] 
**iter_first_key** | **str** |  | [optional] 
**iter_last_key** | **str** |  | [optional] 
**offset** | **int** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from flexprice.models.dto_get_events_response import DtoGetEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoGetEventsResponse from a JSON string
dto_get_events_response_instance = DtoGetEventsResponse.from_json(json)
# print the JSON string representation of the object
print(DtoGetEventsResponse.to_json())

# convert the object into a dict
dto_get_events_response_dict = dto_get_events_response_instance.to_dict()
# create an instance of DtoGetEventsResponse from a dict
dto_get_events_response_from_dict = DtoGetEventsResponse.from_dict(dto_get_events_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


