# DtoCreateInvoiceLineItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | 
**display_name** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**meter_display_name** | **str** |  | [optional] 
**meter_id** | **str** |  | [optional] 
**period_end** | **str** |  | [optional] 
**period_start** | **str** |  | [optional] 
**plan_display_name** | **str** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**price_id** | **str** |  | 
**price_type** | **str** |  | [optional] 
**quantity** | **float** |  | 

## Example

```python
from flexprice_client.models.dto_create_invoice_line_item_request import DtoCreateInvoiceLineItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateInvoiceLineItemRequest from a JSON string
dto_create_invoice_line_item_request_instance = DtoCreateInvoiceLineItemRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreateInvoiceLineItemRequest.to_json())

# convert the object into a dict
dto_create_invoice_line_item_request_dict = dto_create_invoice_line_item_request_instance.to_dict()
# create an instance of DtoCreateInvoiceLineItemRequest from a dict
dto_create_invoice_line_item_request_from_dict = DtoCreateInvoiceLineItemRequest.from_dict(dto_create_invoice_line_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


