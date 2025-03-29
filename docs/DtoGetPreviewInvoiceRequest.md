# DtoGetPreviewInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_end** | **str** |  | [optional] 
**period_start** | **str** |  | [optional] 
**subscription_id** | **str** |  | 

## Example

```python
from flexprice_client.models.dto_get_preview_invoice_request import DtoGetPreviewInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoGetPreviewInvoiceRequest from a JSON string
dto_get_preview_invoice_request_instance = DtoGetPreviewInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(DtoGetPreviewInvoiceRequest.to_json())

# convert the object into a dict
dto_get_preview_invoice_request_dict = dto_get_preview_invoice_request_instance.to_dict()
# create an instance of DtoGetPreviewInvoiceRequest from a dict
dto_get_preview_invoice_request_from_dict = DtoGetPreviewInvoiceRequest.from_dict(dto_get_preview_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


