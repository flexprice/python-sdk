# DtoIngestEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**event_id** | **str** |  | [optional] 
**event_name** | **str** |  | 
**external_customer_id** | **str** |  | 
**properties** | **Dict[str, str]** | Handled separately for dynamic columns | [optional] 
**source** | **str** |  | [optional] 
**timestamp** | **str** | Handled separately due to parsing | [optional] 

## Example

```python
from flexprice_client.models.dto_ingest_event_request import DtoIngestEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoIngestEventRequest from a JSON string
dto_ingest_event_request_instance = DtoIngestEventRequest.from_json(json)
# print the JSON string representation of the object
print(DtoIngestEventRequest.to_json())

# convert the object into a dict
dto_ingest_event_request_dict = dto_ingest_event_request_instance.to_dict()
# create an instance of DtoIngestEventRequest from a dict
dto_ingest_event_request_from_dict = DtoIngestEventRequest.from_dict(dto_ingest_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


