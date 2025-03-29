# DtoEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**event_name** | **str** |  | [optional] 
**external_customer_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**properties** | **Dict[str, object]** |  | [optional] 
**source** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_event import DtoEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DtoEvent from a JSON string
dto_event_instance = DtoEvent.from_json(json)
# print the JSON string representation of the object
print(DtoEvent.to_json())

# convert the object into a dict
dto_event_dict = dto_event_instance.to_dict()
# create an instance of DtoEvent from a dict
dto_event_from_dict = DtoEvent.from_dict(dto_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


