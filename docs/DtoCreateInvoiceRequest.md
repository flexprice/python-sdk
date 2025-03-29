# DtoCreateInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_due** | **float** |  | 
**amount_paid** | **float** |  | [optional] 
**billing_period** | **str** |  | [optional] 
**billing_reason** | [**TypesInvoiceBillingReason**](TypesInvoiceBillingReason.md) |  | [optional] 
**currency** | **str** |  | 
**customer_id** | **str** |  | 
**description** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**environment_id** | **str** |  | [optional] 
**idempotency_key** | **str** |  | [optional] 
**invoice_status** | [**TypesInvoiceStatus**](TypesInvoiceStatus.md) |  | [optional] 
**invoice_type** | [**TypesInvoiceType**](TypesInvoiceType.md) |  | [optional] 
**line_items** | [**List[DtoCreateInvoiceLineItemRequest]**](DtoCreateInvoiceLineItemRequest.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**payment_status** | [**TypesPaymentStatus**](TypesPaymentStatus.md) |  | [optional] 
**period_end** | **str** |  | [optional] 
**period_start** | **str** |  | [optional] 
**subscription_id** | **str** |  | [optional] 

## Example

```python
from flexprice_client.models.dto_create_invoice_request import DtoCreateInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DtoCreateInvoiceRequest from a JSON string
dto_create_invoice_request_instance = DtoCreateInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(DtoCreateInvoiceRequest.to_json())

# convert the object into a dict
dto_create_invoice_request_dict = dto_create_invoice_request_instance.to_dict()
# create an instance of DtoCreateInvoiceRequest from a dict
dto_create_invoice_request_from_dict = DtoCreateInvoiceRequest.from_dict(dto_create_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


