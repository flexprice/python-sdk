# DtoBulkIngestEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[DtoIngestEventRequest]**](DtoIngestEventRequest.md) |  | 

## Example

```python
from flexprice.models.dto_bulk_ingest_event_request import DtoBulkIngestEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoBulkIngestEventRequest from a JSON string
dto_bulk_ingest_event_request_instance = DtoBulkIngestEventRequest.from_json(json)
# print the JSON string representation of the object
print(DtoBulkIngestEventRequest.to_json())

# convert the object into a dict
dto_bulk_ingest_event_request_dict = dto_bulk_ingest_event_request_instance.to_dict()
# create an instance of DtoBulkIngestEventRequest from a dict
dto_bulk_ingest_event_request_from_dict = DtoBulkIngestEventRequest.from_dict(dto_bulk_ingest_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


