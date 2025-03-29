# DtoInvoiceLineItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**meter_display_name** | **str** |  | [optional] 
**meter_id** | **str** |  | [optional] 
**period_end** | **str** |  | [optional] 
**period_start** | **str** |  | [optional] 
**plan_display_name** | **str** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**price_id** | **str** |  | [optional] 
**price_type** | **str** |  | [optional] 
**quantity** | **float** |  | [optional] 
**status** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_invoice_line_item_response import DtoInvoiceLineItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DtoInvoiceLineItemResponse from a JSON string
dto_invoice_line_item_response_instance = DtoInvoiceLineItemResponse.from_json(json)
# print the JSON string representation of the object
print(DtoInvoiceLineItemResponse.to_json())

# convert the object into a dict
dto_invoice_line_item_response_dict = dto_invoice_line_item_response_instance.to_dict()
# create an instance of DtoInvoiceLineItemResponse from a dict
dto_invoice_line_item_response_from_dict = DtoInvoiceLineItemResponse.from_dict(dto_invoice_line_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


